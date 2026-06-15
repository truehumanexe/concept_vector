This is a project called "concept-vectors." It replaces the arbitrary latent dimensions of traditional word embeddings (e.g. Word2Vec, LLM embedding layers) with deterministic, human-defined semantic components that have been distilled from an LLM using a pre-defined scoring method. A need for restructuring of the model's tokenization or vocabulary alignment layers to accommodate this framework is understood and is explicitly outside the scope of this task.

This project has the following objectives:
1. Computational Efficiency & Memory Reduction: Restricting the core vector space density to a highly compressed footprint (< 1000).
2. Deterministic Controllability: Embedding explicit, isolated semantic components for areas of governance (e.g., Formality, Insult, Hedonics) to allow for predictable post-hoc filtering or scalar logit masking at the decoder layer.
3. Structural Explainability: Allowing for easier evaluation of how context shifts semantic baselines during attention execution.
    - Given the following vectors: [ Static ]; [ Dynamic || Trainable ] 
    - The static component is predefined during the distillation process, locked, and treated as a reference
    - The dynamic component is a copy of the static component that is combined with the trainable/undefined components and passed through attention/transformer layers
    - The trainable components allow an LLM to generate meaning that goes beyond the scope of concept-vectors
    - Changes between the static vector and dynamic vector components are measurable