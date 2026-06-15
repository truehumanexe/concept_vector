# Speculative use

- N-order thinking: concept-vectors focus on "first order concepts" i.e. those concepts that can be interpreted from a single word without additional linguistic context. Since the core vector components are interpretable, it may be possible to detect second or higher order concepts by tracking the relationship between defined component vectors and trainable component vectors. This relates to Facebook's research on Large Concept Models (LCMs) and mechanistic interpretability, but approaches it from a slightly different direction.
  - Alternatively, it may be possible to explicitly build higher order concepts by applying a mask to following layers. i.e. non-fully connected layers. Combining, modifier, insult, and formality, and maybe polarity concepts can potentially track offensiveness across sentences instead of only individual words.
  - This reminds me that I should probably add a negation concept explicitly. polarity might already generate overlap in which negative terms have negative polarity.
- Special purpose concepts: The concept-vector idea may be extendable to special purposes. For instance, programming concerns could potentially be embedded directly into the core vectors.
  - E.g:
    - concept: loop; Description: tokens that are associated with the beginning of a loop (while, for, etc.)
    - concept: conditional; Description: tokens that are assocaited with conditional logic (and, <, or, !, etc.)
  - extensions of these sort might provide easier training for special use cases.
  - Smaller spaces like this don't actually need model distillation. They can be specified manually and added into the vector-database or even joined directly with pre-existing distilled vectors where relevant via a vector component sum
  - Speech style should also be injectable directly into a model with a "speech_style" concept. 
    - Take all words that have likely usage from a particular speech archetype. 
    - Given them a value or 1
    - Do the inverse for words that shouldn't be used in a particular speech style
    - do a vector component sum against the database.
    - This could be thought of as a more general control over the explicit insult/formality concepts.
    - An analysis of word count could be done to the speech of desired individuals then used to nudge the model to a given word choice.