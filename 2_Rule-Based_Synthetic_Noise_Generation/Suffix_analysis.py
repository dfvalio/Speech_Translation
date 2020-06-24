import re
import codecs

diff_file = codecs.open("difflib_output_processed_original_lv_files_corr.txt","r","utf-8")
text=diff_file.readlines()

file=codecs.open("lv_suffix.txt","r","utf-8")
suffixes=file.readlines()

result=codecs.open("List_words_suffix_change.txt","w","utf-8")
result1=codecs.open("List_pairs_suffix_change.txt","w","utf-8")


for i in range(len(suffixes)):
	suffixes[i]=suffixes[i].strip("\n")
	suffixes[i]=suffixes[i].strip("\r")

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
		if(re.search("^\+$",token[j])):
			count_split+=1
		if(re.search("^-$",token[j])):
			count_merge+=1
		if (count_plus!=0 or count_minus!=0):
			if(count_char>count_plus and count_char>count_minus and count_space==0):
				a=re.search("\+",token[j])
				b=re.search("-",token[j])
				count_error+=1
				suf_clean=''
				suf_asr=''
				for k in range(len(token[j])-1):
					if (a and b):
						if (token[j][k] != '-' and token[j][k] != '+' and token[j][k-1] != '-' and token[j][k-1] != '+'):
							suf_asr=suf_asr+token[j][k]
							suf_clean=suf_clean+token[j][k]
						if(token[j][k] == '-'):
							suf_clean=suf_clean+token[j][k+1]
						if(token[j][k] == '+'):
							suf_asr=suf_asr+token[j][k+1]
				list_clean.append(suf_clean)
				list_asr.append(suf_asr)
		if(re.search("[a-z]\+S[a-z]",token[j]) and count_space==count_plus and count_minus==0):	
			count_special_split+=1
		if(re.search("[a-z]\-S[a-z]",token[j]) and count_space==count_minus and count_plus==0):	
			count_special_merge+=1
		j+=1
	i+=1
	# if(i>20):
	# 	break

print("Done1")

for i in range(len(list_clean)):
	if(re.search("\n", list_clean[i])):
		list_clean[i]=re.sub("\n","",list_clean[i])

for i in range(len(list_asr)):
	if(re.search("\n", list_asr[i])):
		list_asr[i]=re.sub("\n","",list_asr[i])

print("Done2")

# while("" in list_clean):
# 	list_clean.remove("") 

# while("" in list_asr):
# 	list_asr.remove("")

count_error_suffixes_in_list=0

for i in range(len(list_clean)):
	count_suff_clean=0
	count_suff_asr=0
	roots_clean=[]
	roots_asr=[]

	if(i%100000==0):
		print(i)

	for element in suffixes:
		if (list_clean[i].endswith(element)):
			count_suff_clean+=1
			roots_clean.append(re.sub(element + "$", "", list_clean[i]))

		if (list_asr[i].endswith(element)):
			count_suff_asr+=1
			roots_asr.append(re.sub(element + "$", "", list_asr[i]))
	
	if(count_suff_clean!=0 and count_suff_asr!=0):
		root_clean=min(roots_clean, key=len)
		root_asr= min(roots_asr, key=len)

		if (root_clean == root_asr):
				result.write(list_clean[i] + "\t" + list_asr[i] + "\t" + root_clean + "\t" + re.sub(root_clean, "", list_clean[i]) + "\t" +  re.sub(root_asr, "", list_asr[i]) + "\n")
				result1.write(re.sub(root_clean, "", list_clean[i]) + " " + re.sub(root_asr, "", list_asr[i]) + "\n")
				count_error_suffixes_in_list+=1	

print(count_error_suffixes_in_list)