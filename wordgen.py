from collections import Counter
import nltk
from nltk.corpus import brown

# Download necessary NLTK datasets
# print("Downloading required corpora...")
# nltk.download("brown")
# nltk.download("universal_tagset")


def get_top_words_by_pos(target_count=100):
    # Retrieve all words with their Universal POS tags
    # The universal tagset simplifies tags into broad categories: NOUN, VERB, ADJ, ADV, etc.
    tagged_words = brown.tagged_words(tagset="universal")

    # Group words by their POS tags
    pos_buckets = {}
    for word, tag in tagged_words:
        # Lowercase to normalize frequencies (e.g., "The" vs "the")
        word_clean = word.lower()

        # Skip punctuation or pure numeric tokens
        if not word_clean.isalpha():
            continue

        if tag not in pos_buckets:
            pos_buckets[tag] = []
        pos_buckets[tag].append(word_clean)

    # Dictionary to hold the final top 100 lists
    top_words_by_pos = set()

    # Define the core parts of speech we want to target
    target_tags = {
        "NOUN": "Nouns",
        "VERB": "Verbs",
        "ADJ": "Adjectives",
        "ADV": "Adverbs",
        "PRON": "Pronouns",
        "ADP": "Prepositions",
        "CONJ": "Conjunctions",
        "DET": "Determiners",
    }

    # Extract the top N words for each targeted POS
    for tag, human_readable_name in target_tags.items():
        if tag in pos_buckets:
            counts = Counter(pos_buckets[tag])
            # Get the most common words and extract just the word string
            top_words = [word for word, count in counts.most_common(target_count)]
            # top_words_by_pos[human_readable_name] = top_words
            for w in top_words:
                top_words_by_pos.add(w)

    return top_words_by_pos


if __name__ == "__main__":
    pos_data = get_top_words_by_pos(100)

    # Print out a summary preview of the results
    print("\n--- Lexicon Extraction Complete ---\n")
    for pos_name, words in pos_data.items():
        print(f"### {pos_name} (Top 5 Examples): {', '.join(words[:5])}...")
        print(f"Total extracted: {len(words)}\n")

        # Optional: Save individual files if needed for pipeline digestion
        # with open(f"{pos_name.split()[0].lower()}_top100.txt", "w") as f:
        #     f.write("\n".join(words))