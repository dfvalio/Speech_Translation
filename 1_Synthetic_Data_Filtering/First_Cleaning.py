### First step: Identify size difference in terms of sentences between clean and asr 
### and remove punctuations

import codecs
import re
import string

# Open and read files
file=codecs.open("train.clean.lv","r","utf-8")
clean=file.readlines()

file=codecs.open("train.asr.clean.lv","r","utf-8")
clean_asr=file.readlines()


# Size comparison to check if files contain the same number of sentences
size_sent_clean=0
for sentence in clean:
    size_sent_clean+=1
print("Size of train.clean.lv: " + str(size_sent_clean) + " sentences")
size_sent_clean_asr=0
for sentence in clean_asr:
    size_sent_clean_asr+=1
print("Size of train.asr.clean.lv: " + str(size_sent_clean_asr) + " sentences")

#Delta: difference of size between files, it should be 0 (sentences aligned)
delta_sent=size_sent_clean - size_sent_clean_asr
print ("Number of sentences deleted in ASR file: " + str(delta_sent) + " sentences")


# Punctuation removal: using string.punctuation list
clean_wo_punct=[]
for element in clean:
    for c in string.punctuation:
        element=element.lower().replace(c,"")
    clean_wo_punct.append(element)


clean_asr_wo_punct=[]
for element in clean_asr:
    for c in string.punctuation:
        element=element.lower().replace(c,"")
    clean_asr_wo_punct.append(element)

# Writing output files with sentences without punctuation
result=codecs.open("clean_wo_punct.txt","w","utf-8")
result1=codecs.open("clean_asr_wo_punct.txt","w","utf-8")

for sentence in clean_wo_punct:
    result.write(sentence)

for sentence in clean_asr_wo_punct:
    result1.write(sentence)
