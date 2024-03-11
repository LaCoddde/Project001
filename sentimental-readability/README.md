A program that first asks the user to type in some text,
and then outputs the grade level for the text, according
to the Coleman-Liau formula,

Coleman-Liau index = 0.0588 * L - 0.296 * S - 15.8

where: L is the average number of letters per 100 words

S is the average number of sentences per 100 words in the text

- Get user input, and output answer


- Count the number of letters, words, and sentences in the text

  Letter = ascii__lowercase or ascii__uppercase

  Word = sequence of characters separated by spaces <---> .split()

  Sentence = indicated by the occurrence of a period, exclamation or question mark.


- Output "Grade X"

  where: X is the grade level computed by the Coleman-Liau formula, rounded to the nearest integer


- If the resulting index number is 16 or higher (>= a senior undergrad reading), output -> "Grade 16+" != "Grade 16"


- If index is less than 1, output -> "Before Grade 1"