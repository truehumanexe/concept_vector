# Statistic Vectors and Tokenization Methods

Below is an incomplete idea for an extension of concept-vectors. The core concern is handling typos, but it may extend to other areas.

Consider the two following functions:
func Concept(s:String) -> Concept-Vector
- Concept-Vector: N dimensional normalized vector that measures the intensity of a token's relationship to a given concept.
- It has multiple concepts including unknown (i.e. is this token in the vector database)
func Char(s:String) -> Character-Vector
- Character-Vector: M dimensional normalized vector that measures the count of discrete ascii characters that a token contains as well as the length of the token.

Split all strings such that they contain discrete white space characters, continuous alpha sequences, continuous digit sequences, or discrete remaining glyphs.

Concept(s) behavior:
 - tokens return an unknown vector (unknown concept set to 1 with all other concepts set to 0) if they aren't in the database, otherwise they return a defined vector

Char(s) behavior:
 - discrete tokens get vector components set to # occurrences and the length component is set to the total length of the sequence


outputs are concatenated together along with an undefined working space for the model
 - concept-vector || character- vector || ones-vector

Example:
- Concept('the') -> known vector with flags for 'determiner', 'absoluteness' and other relevant concepts
- Char('the') -> values of 1 for t, h, and e, with length 3

- Concept('teh') -> unknown vector
- Char('teh') -> values of 1 for t, h, and e, with length 3

Expected behavior: 
- Down stream model understanding that 'the' and 'teh' are related based on common locations in text and actual character statistics.
- More accurate answer for questions like ",how many {letters} are in {word}?"
- Hopefully no need for addtional tokenization process for handling unknown words

## Quantization

If character-vectors are useful, then it will be necessary to ensure that quantization doesn't corrupt them, since they will have a specific meaning at their original scale instead of a simple connection to a "threshold" or "intensity". An appropriate transformation would need to be done before quantization.