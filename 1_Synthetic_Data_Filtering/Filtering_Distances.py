# Selecting sentences considered similar (Levenshtein distance > 0.9)

import codecs
import re
import string
import difflib
from difflib import SequenceMatcher
import numpy
import Levenshtein as lev
from similarity.normalized_levenshtein import NormalizedLevenshtein

# Open and read files
file=codecs.open("clean_stripped.txt","r","utf-8")
clean=file.readlines()

file=codecs.open("Clean_asr_stripped.txt","r","utf-8")
clean_asr=file.readlines()

file=codecs.open("clean_en_stripped.txt","r","utf-8")
clean_en=file.readlines()

file=codecs.open("Distances.txt","r","utf-8")
distances = file.readlines()

# Open output files
result=codecs.open("Clean_dist_filter.txt","w","utf-8")
result_asr=codecs.open("Clean_asr_dist_filter.txt","w","utf-8")
result_en=codecs.open("Clean_en_dist_filter.txt","w","utf-8")

print(len(clean))
print(len(clean_asr))
print(len(clean_en))
print(len(distances))

count=0
equal_nb_tokens=0

# Loop to identify similar sentences and write in output files
# Counting sentences with same number of tokens comparing clean and asr
for i in range(len(distances)):
	if (float(distances[i]) > 0.9):
		result.write(clean[i])
		result_asr.write(clean_asr[i])
		result_en.write(clean_en[i])
		count+=1
		if (len(clean[i].split(" "))==len(clean_asr[i].split(" "))):
			equal_nb_tokens+=1

print(str(count))
print(str(equal_nb_tokens))


