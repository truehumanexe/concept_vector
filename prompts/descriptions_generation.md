You are an automated data architecture parsing engine working on a project called "concept-vectors" that maps the English lexicon to human-defined semantic dimensions. 

Evaluate the raw concepts and descriptions provided at the end of this prompt, and rewrite them into precise, engineering-grade scoring rubrics. Your output must be a single, valid JSON object containing a dictionary of these concepts. Do not include any conversational preamble, markdown text, or explanations. Return only the raw JSON string.

For each concept, ensure your rewritten metadata adheres to these strict rules:
1. "scale_type": Must be exactly the string "unipolar" or "bipolar".
2. "axis_isolation": Ensure the definition focuses on a single, isolated semantic quality, explicitly eliminating conceptual bleeding or overlapping domains.
3. "definition": A cohesive instruction string defining what the dimension measures, explicitly defining what constitutes the baseline/neutral state (0.0) and what characterizes the absolute peaks or extremes of the scale (4.0 or +/-4.0).
4. Keys must be standard alphanumeric snake_case strings with no slashes or special characters.

Output Format Schema:
{
  "concept_name_snake_case": {
    "scale_type": "unipolar_or_bipolar",
    "definition": "The engineered prompt instruction string anchoring the boundaries."
  }
}

Here are the raw concepts and descriptions to evaluate and convert into the JSON schema:
[INSERT YOUR RAW DATA HERE]