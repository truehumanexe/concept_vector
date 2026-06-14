This is a project called "concept-vectors." It replaces the arbitrary latent dimensions of traditional word embeddings (e.g., Word2Vec, LLM embedding layers) with deterministic, human-defined semantic components that have been distilled from an LLM using a pre-defined scoring method. Any downstream restructuring of the model's tokenization or vocabulary alignment layers to accommodate this framework is understood and is explicitly outside the scope of this task.

This project has the following objectives:
1. Computational Efficiency & Memory Reduction: Restricting the core vector space density to a highly compressed footprint (<< 1000).
2. Deterministic Controllability: Embedding explicit, isolated semantic components for areas of governance (e.g., Formality, Insult, Hedonics) to allow for predictable post-hoc filtering or scalar logit masking at the decoder layer.
3. Structural Explainability: Implementing a vector tracking pipeline [Static || Dynamic || Trainable] to isolate, quantify, and audit how context shifts semantic baselines during attention execution.
  - The static component is predefined during the distillation process
  - The dynamic component is a copy of the static component passed to an LLM with the undefined trainable components
  - the static component can be compared to the dynamic component to understand model behavior after attention updates

