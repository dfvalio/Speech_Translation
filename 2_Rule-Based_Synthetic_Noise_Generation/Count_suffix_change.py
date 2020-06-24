import re
import codecs
from collections import Counter

file = codecs.open("List_pairs_suffix_change.txt","r","utf-8")
text=file.readlines()

result=codecs.open("Count_Suffix_Pairs.txt","w","utf-8")

for i in range(len(text)):
	text[i]=text[i].strip("\n")
	text[i]=text[i].strip("\r")

a=Counter(text)


for k,v in  a.most_common():
    result.write("{} {}\n".format(k,v))

