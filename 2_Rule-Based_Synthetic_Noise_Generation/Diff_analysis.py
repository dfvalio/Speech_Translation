# Analysis of the output of difflib to count types of errors in asr

import re
import codecs

diff_file = codecs.open("difflib_output_processed_original_lv_files_corr.txt","r","utf-8")
text = diff_file.readlines()

count_error=0
count_split=0
count_merge=0
count_special_split=0
count_special_merge=0

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
		if(re.search("^\+$",token[j])):
			print(token[j-1] + " " + token[j+1])	
			count_split+=1
			break
		if(re.search("^-$",token[j])):
			count_merge+=1
		if (count_plus!=0 or count_minus!=0):
			if(count_char>count_plus and count_char>count_minus and count_space==0):
				count_error+=1
		if(re.search("[a-z]\+S[a-z]",token[j]) and count_space==count_plus and count_minus==0):
			count_special_split+=1
		if(re.search("[a-z]\-S[a-z]",token[j]) and count_space==count_minus and count_plus==0):	
			count_special_merge+=1
		j+=1
	i+=1


print("token error: " + str(count_error))
print("token split into more tokens: " + str(count_split))
print("tokens merged into one single token: " + str(count_merge))
print("token split into two tokens" + str(count_special_split))
print("two tokens merged into one token" str(count_special_merge))