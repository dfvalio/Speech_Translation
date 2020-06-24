# Comparison of clean and asr tokenized and true cased using difflib to generate comparison file that will be used in further analysis

import codecs
import re
import string
import difflib
from difflib import SequenceMatcher
from difflib import Differ


# Open input and output files
file=codecs.open("train.clean.alg.lv.tok.tc.lv","r","utf-8")
clean=file.readlines()

file=codecs.open("train.asr.clean.lv.tok.tc.lv","r","utf-8")
clean_asr=file.readlines()

result=codecs.open("difflib_output_processed_original_lv_files.txt","w","utf-8")

print(len(clean))
print(len(clean_asr))

# i=0
# for sent_nb in range(len(clean)):
#     for line in difflib.context_diff(clean[sent_nb].split(" "), clean_asr[sent_nb].split(" "), fromfile='clean.txt', tofile='clean_asr.py', n=1000):
#         print (line)
#     i+=1
#     if(i>5):break


# Define comparison function and apply it generating output data
d = Differ()
list_result=[]

i=0
for sent_nb in range(len(clean)):
    #result.write(str(i)+"\n")
    result_diff = d.compare(clean[sent_nb], clean_asr[sent_nb])
    result.writelines(result_diff)
    i+=1




