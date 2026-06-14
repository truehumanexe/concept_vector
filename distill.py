import pandas as pd
import requests
import json
import os

MODULE_DIR = os.path.dirname(os.path.abspath(__file__))

CONCEPT_PATH = os.path.join(MODULE_DIR,'data','concepts.csv')
PROMPT_PATH = os.path.join(MODULE_DIR,'prompts')
WORD_PATH = os.path.join(MODULE_DIR,'data','words.csv')
DATA_PATH = os.path.join(MODULE_DIR,'data')
SCORE_PATH = os.path.join(MODULE_DIR,'data','scores')

def get_prompt_templates(prompt_path=PROMPT_PATH):
    intro_file = "rank_intro_statement.md"
    rank_files = {
        "unipolar": "unipolar_rank.md",
        "bipolar": "bipolar_rank.md",
        "unipolar_normalized": "unipolar_normalized_rank.md"  
    }
    end_rules_file = "rank_final_rules.md"
    
    def read_file(file_name):
        full_path = os.path.join(prompt_path, file_name)
        with open(full_path, "r", encoding="utf-8") as f:
            return f.read()
            

    intro_text = read_file(intro_file)
    end_rules_text = read_file(end_rules_file)
    
    prompts = {}
    
    for key, rank_filename in rank_files.items():
        rank_text = read_file(rank_filename)
        
        prompts[key] = f"{intro_text}\n{rank_text}\n{end_rules_text}"
        
    return prompts

def get_system_prompts(concept, mapping, description, prompt_ref):

    M = mapping
    D = description
    C = concept
    prompt = prompt_ref[M]
    prompt = prompt.replace("{M}", M)
    prompt = prompt.replace("{D}", D)
    prompt = prompt.replace("{C}", C)
    return prompt

def get_system_prompt(concept, concept_path=CONCEPT_PATH, prompt_path = PROMPT_PATH ):
    concepts = pd.read_csv(concept_path)
        
    prompt_ref = get_prompt_templates(prompt_path)
    row = concepts.loc[concepts['concept'] == concept,:]

    if len(row) == 1:
        c = row['concept'].values[0]
        m = row['mapping'].values[0]
        d = row['description'].values[0]
        print(get_system_prompts(c,m,d, prompt_ref))
    else:
        print(f'Could not find {concept}')


def distill(model, word = None, start=0, end = None, concept_path=CONCEPT_PATH, prompt_path = PROMPT_PATH, word_path = WORD_PATH, out_path = DATA_PATH):
    """
    Write word:score pairs as .csv to the currrent directory location using the lmdstudio OpenAI stateless API with a pre-existing server.
    Sends a local model a description of how to score a word's relationship to a given concept as well as a single word to evaluate without context drift
    
    model: lmstudio model name
    start: the starting index to begin the distillation process from the concept list
    end: the ending index to complete the distillation process or the length of the concept list
    """

    chat_url = "http://127.0.0.1:1234/v1/chat/completions"

    concepts = pd.read_csv(concept_path)

    end = len(concepts) if end is None else end
    
    prompt_ref = get_prompt_templates(prompt_path)

    words = [word]
    if word is None:
        words = pd.read_csv(word_path)['WORDS'].tolist()

    for index,row in concepts[start:end].iterrows():
        results = []
        system_prompt = get_system_prompts(row['concept'], row['mapping'], row['description'],prompt_ref)
        print(row['concept'])
        for i, word in enumerate(words):

            payload = {
                "model": model,
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": word}
                ],
                "temperature":0.0,
            }
            response = requests.post(chat_url, json=payload)
            
            if response.status_code ==200:
                r = json.loads(response.text)
                results.append(r['choices'][0]['message']['content'])
            print(i, end="\r", flush=True)
            # break
        results = '\n'.join(results)

        with open(os.path.join(out_path,f'{row['concept']}'), 'w') as f:
            try:
                # Intentionally going with minimal processing here
                # I experienced odd outputs that broke the pipeline,
                # Dropping raw text for manual cleaning seems preferred to assuming consistency
                f.write(results)
            except Exception as e:
                print('failed ', row['concept'])
        # break


def process_scores():
    path = SCORE_PATH
    files = os.listdir(path)
    scores = {}
    for name in files:

        with open(os.path.join(path,name), 'r') as f:
            scores[name] = f.readlines()
    
    for k, l in scores.items():
        l = list(map(lambda x: x.replace('\"',''), l))
        l = list(map(lambda x: x.replace('\n',''), l))
        l = list(map(lambda x: x.split(':'), l))
        l = list(filter(lambda x: len(x) == 2, l))
        scores[k] = l
    return scores

def get_vectors(scores):

    dfs = {}

    for k, l in scores.items():
        dfs[k] = pd.DataFrame(data = l, columns = 'word,score'.split(','))

    processed_dfs = []
    for k, df in dfs.items():

        df['score'] = pd.to_numeric(df['score'], errors='coerce').fillna(0)
        df = df.drop_duplicates(subset=['word'], keep='first')
        indexed_df = df.set_index('word')[['score']].rename(columns={'score': k})
        processed_dfs.append(indexed_df)

    vectors = pd.concat(processed_dfs, axis=1)

    # 4. Fill missing values with 0 for words that didn't exist in a specific dataframe
    vectors = vectors.fillna(0)

    concepts = pd.read_csv(CONCEPT_PATH)

    vectors = vectors[list(concepts['concept'].values)]

    return vectors
    
    