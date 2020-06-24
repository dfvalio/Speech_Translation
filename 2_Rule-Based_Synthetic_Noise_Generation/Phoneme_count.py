import re
import codecs
from collections import Counter

diff_file = codecs.open("difflib_output_processed_original_lv_files_corr.txt","r","utf-8")
text=diff_file.readlines()

result=codecs.open("Close_phonemes_diff.txt","w","utf-8")

count_error=0
count_split=0
count_merge=0
count_special_split=0
count_special_merge=0

list_clean=[]
list_asr=[]

i=0
while (i<len(text)):
	token = text[i].split(" ")
	nb_tokens = len(text[i].split(" "))
	j=0
	while (j<nb_tokens):
		count_plus=0
		count_minus=0
		count_char=0
		count_space=0
		if (re.search('[a-z]*',token[j])):
			for char in token[j]:
				if (char=='+'):
					count_plus+=1
				if (char=='-'):
					count_minus+=1
				if (char!='-' and char !='+'):
					count_char+=1
				if (char=='S'):
					count_space+=1
		if (count_plus==1 and count_minus==1):
			if (re.search("\+.-.",token[j]) or re.search("-.\+.",token[j])):
				tok_len=len(token[j])
				z=0
				while(z<tok_len-1):
					if (token[j][z]=="-"):
						list_clean.append(token[j][z+1])
					if (token[j][z]=="+"):
						list_asr.append(token[j][z+1])
					z+=1
		j+=1
	i+=1

len_list_phon=len(list_clean)
z=0
while(z<len_list_phon):
	result.write(list_clean[z] + " " + list_asr[z] + "\n")
	z+=1



file=codecs.open("Close_phonemes_diff.txt","r","utf-8")
text=file.readlines()

result1=codecs.open("Count_Phonemes_Pairs.txt","w","utf-8")

for i in range(len(text)):
	text[i]=text[i].strip("\n")
	text[i]=text[i].strip("\r")

a=Counter(text)


for k,v in  a.most_common():
    result1.write("{} {}\n".format(k,v))



file1=codecs.open("Count_Phonemes_Pairs.txt","r","utf-8")
text1=file1.readlines()

result2=codecs.open("Close_Phonemes_stats.txt","w","utf-8")


list_pairs=["m n","n m","p b","b p","t d","d t","k g","g k","s z","z s","ž š","š ž","l ļ","ļ l","g ģ","ģ g","k ķ","ķ k","f v","v f", "n ņ","ņ n","a ā","ā a","e ē","ē e","i ī","ī i","u ū","ū u"]

for sentence in text1:
	for i in list_pairs:
		if (re.search(i, sentence)):
			result2.write(sentence)


#Missing: "c ts","ts dz","č dž"

