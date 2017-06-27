# pmi

pmi.py-
This code calculates the pmi(pointwise mutual index) of the words present in the cleaned document with respect to sentence boundary. A cleaned document is a document that contains all the words separated by space. Note that any punctuation is considered as a separate word)

To run the code, use the following command- python pmi.py <input_file> <number of h> <number of j>

The output text files are in format: word  countJoint  countWord   pmi



normPMI.py-
This code calculates the pmi as well as normalised PMI of the words present in the cleaned document with respect to sentence boundary. A cleaned document is a document that contains all the words separated by space. Note that any punctuation is considered as a separate word)

To run the code, use the following command- python normPMI.py <input_file> <number of h> <number of j> <sortby>
<sortby> can take values: countJoint, countWord, pmi, normPMI

The output text files are in format: word  countJoint  countWord   pmi  normPMI
