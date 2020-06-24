# Filtering sentences to remove main identified errors of ASR file by using Regex
# Selected sentences written in output files "stripped"

import codecs
import re
import string
import difflib
from difflib import SequenceMatcher

# Open and read files
file=codecs.open("clean_wo_punct_vf1.txt","r","utf-8")
clean=file.readlines()

file=codecs.open("clean_asr_wo_punct.txt","r","utf-8")
clean_asr=file.readlines()

file=codecs.open("train.asr.clean.en","r","utf-8")
clean_en=file.readlines()

# Open output files
result=codecs.open("clean_stripped.txt","w","utf-8")
result1=codecs.open("clean_asr_stripped.txt","w","utf-8")
result_en=codecs.open("clean_en_stripped.txt","w","utf-8")


print(len(clean))
print(len(clean_asr))
print(len(clean_en))

# For loop containing the Regex to identify sentences not to be written in output file.
i=0
for j in range(len(clean)):
        x = re.search("[0-9]", clean[j])
        y = re.search("http", clean[j])
        z = re.search("^[a-z]$", clean[j])
        k = re.search("^\n$",clean[j])
        l = re.search("www",clean[j])
        m = re.search("^[mdclxvi]+$",clean[j])
        n = re.search("^link$",clean[j])
        o = re.search("°",clean[j])
        p = re.search(" [mdclxvi]+$",clean[j])
        q = re.search("vidi", clean[j])

        if not x and not y and not z and not k and not l and not m and not n and not o and not p:
            result.write(clean[j])
            result1.write(clean_asr[j])
            result_en.write(clean_en[j])
            if (p) and (q):
                result.write(clean[j])
                result1.write(clean_asr[j])
                result_en.write(clean_en[j])
        if (similar(clean[j],clean_asr[j])<1):
            i+=1

print(i)


