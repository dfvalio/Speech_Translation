import codecs
import re
import string

file=codecs.open("difflib_output_processed_original_lv_files_corr.txt","r","utf-8")
diff_file=file.readlines()

file=codecs.open("train.clean.alg.lv.tok.tc.lv","r","utf-8")
clean=file.readlines()

# file=codecs.open("train.asr.clean.lv.tok.tc.lv","r","utf-8")
# asr=file.readlines()

file=codecs.open("POS_clean_alg_tok_tc_lv.txt","r","utf-8")
POS_clean=file.readlines()

file=codecs.open("POS_clean_asr_tok_tc_lv.txt","r","utf-8")
POS_asr=file.readlines()


list_clean=[]
list_asr=[]
list_POS_clean=[]
list_POS_asr=[]
list_POS_clean_complete=[]
list_POS_asr_complete=[]
sent_index=[]

counter=0
count_suf_clean=0
count_suf_asr=0
for sentence_diff,sentence_POS_clean,sentence_POS_asr in zip(diff_file,POS_clean,POS_asr):
	token = sentence_diff.split(" ")
	nb_tokens = len(sentence_diff.split(" "))
	sentence_POS_clean = sentence_POS_clean.split(" ")
	sentence_POS_asr = sentence_POS_asr.split(" ")
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
		if (count_plus!=0 or count_minus!=0):
			if(count_char>count_plus and count_char>count_minus and count_space==0):
				a=re.search("\+",token[j])
				b=re.search("-",token[j])
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
				if (suf_clean.endswith("a") and suf_asr.endswith("ā")):
					sent_index.append(counter)
					suf_ver_clean=re.sub("a$","",suf_clean)
					suf_ver_asr=re.sub("ā$","",suf_asr)
					if(suf_ver_clean==suf_ver_asr):
						count_suf_clean+=1
						count_suf_asr+=1
						for word in sentence_POS_clean:
							word=word.split("|")
							if (suf_clean in word[0]):
								list_clean.append(suf_clean)
								list_POS_clean_complete.append(word[2].strip("\n"))
								word2=word[2].split("-")
								list_POS_clean.append(word2[0])
								break
						for word in sentence_POS_asr:
							word=word.split("|")
							if (suf_asr in word[0]):
								list_asr.append(suf_asr)
								list_POS_asr_complete.append(word[2].strip("\n"))
								word2=word[2].split("-")
								list_POS_asr.append(word2[0])
								break
		j+=1	
	counter+=1
	# if (counter>10):
	# 	break
	if (counter%100000 == 0):
		print(counter)


print(count_suf_clean)
print(count_suf_asr)

# for index,element in enumerate(list_clean):
# 	print(str(sent_index[index]) + " " + list_clean[index] + " " + list_POS_clean[index] + " " + list_POS_clean_complete[index] + " " + list_asr[index] + " " + list_POS_asr[index] + " " + list_POS_asr_complete[index])

list_comb_POS=[]
list_comb_same_POS1=[]
for element_clean,element_asr,tok_clean,tok_asr in zip(list_POS_clean_complete,list_POS_asr_complete,list_clean,list_asr):
	comb=element_clean + "\t" + element_asr
	list_comb_POS.append(comb)
	element_clean=element_clean.split("-")
	element_asr=element_asr.split("-")
	if element_clean[0] == element_asr[0]:
		list_comb_same_POS1.append(comb)


set_comb_POS=set(list_comb_POS)
print(len(set_comb_POS))
result_POS=codecs.open("Result_POS_a_along.txt","w","utf-8")
for comb in set_comb_POS:
	result_POS.write(comb + "\n")


set_comb_same_POS1=set(list_comb_same_POS1)
print(len(set_comb_same_POS1))
result_POS1=codecs.open("Result_same_POS1_a_along.txt","w","utf-8")
for comb in set_comb_same_POS1:
	result_POS1.write(comb + "\n")


list_comb_POS=[]
list_comb_same_POS1=[]

print(len(list_clean))
print(len(list_asr))
print(len(list_POS_clean_complete))
print(len(list_POS_asr_complete))

for element_clean,element_asr,tok_clean,tok_asr in zip(list_POS_clean_complete,list_POS_asr_complete,list_clean,list_asr):
	comb=element_clean + "\t" + tok_clean + "\t" + element_asr + "\t" + tok_asr	
	list_comb_POS.append(comb)


result_POS2=codecs.open("Result_POS_a_along_with_tok.txt","w","utf-8")
for comb in list_comb_POS:
	result_POS2.write(comb + "\n")