# Comparison of sentences in clean and asr after first cleaning in terms of Levenshtein distance

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

file=codecs.open("clean_asr_stripped.txt","r","utf-8")
clean_asr=file.readlines()

# Open output file where the distance values for each pair of sentences will be saved. 
result=codecs.open("Distances.txt","w","utf-8")

print(len(clean))
print(len(clean_asr))

# Definition of function to calculate Levenshtein btw 2 sentences
def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

# Definition of the 5 different types to classify the sentences
equal=0
close=0
medium=0
low=0
different=0

normalized_levenshtein = NormalizedLevenshtein()
norm_dist=[]

# Loop to analyze each pair of sentences and count the number of occurences of each type
for sent_nb in range(len(clean)):
	Ratio = normalized_levenshtein.similarity(clean[sent_nb],clean_asr[sent_nb])
	norm_dist.append(Ratio)
	if (Ratio == 1):
		equal+=1
	if (Ratio > 0.9):
		close+=1
	if (Ratio <= 0.9 and Ratio > 0.7):
		medium+=1
	if (Ratio <= 0.7 and Ratio > 0.5):
		low+=1
	if (Ratio <= 0.5):
		different+=1

# Write the results of the comparisons in output file
for dist in norm_dist:
	result.write(str(dist) + "\n")

print(str(equal) + " " + str((equal/len(clean))))
print(str(close) + " " + str((close/len(clean))))
print(str(medium) + " " + str((medium/len(clean))))
print(str(low) + " " + str((low/len(clean))))
print(str(different) + " " + str((different/len(clean))))
