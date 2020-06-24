import re
import codecs

diff_file = codecs.open("difflib_output_processed_original_lv_files_corr.txt","r","utf-8")
text = diff_file.readlines()

file=codecs.open("lv_suffix.txt","r","utf-8")
suffixes=file.readlines()

for i in range(len(suffixes)):
	suffixes[i]=suffixes[i].strip("\n")
	suffixes[i]=suffixes[i].strip("\r")

result=codecs.open("Split_Merge_suffix_list.txt","w","utf-8")

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
		if(re.search("[a-z]\+S[a-z]",token[j]) and (count_space!=count_plus or count_minus!=0)):
			suf_clean=''
			suf_asr=''
			for k in range(len(token[j])-1):
				if (token[j][k] != '-' and token[j][k] != '+' and token[j][k-1] != '-' and token[j][k-1] != '+'):
					suf_asr=suf_asr+token[j][k]
					suf_clean=suf_clean+token[j][k]
				if(token[j][k] == '-'):
					suf_clean=suf_clean+token[j][k+1]
				if(token[j][k] == '+' and token[j][k+1] != "S"):
					suf_asr=suf_asr+token[j][k+1]
				if (token[j][k] == 'S'):
					suf_asr=suf_asr+" "
			list_clean.append(suf_clean)
			list_asr.append(suf_asr)
		
		if(re.search("[a-z]-S[a-z]",token[j]) and (count_space!=count_minus or count_plus!=0)):	
			suf_clean=''
			suf_asr=''
			for k in range(len(token[j])-1):
				if (token[j][k] != '-' and token[j][k] != '+' and token[j][k-1] != '-' and token[j][k-1] != '+'):
					suf_asr=suf_asr+token[j][k]
					suf_clean=suf_clean+token[j][k]
				if(token[j][k] == '-' and token[j][k+1] != "S"):
					suf_clean=suf_clean+token[j][k+1]
				if(token[j][k] == '+'):
					suf_asr=suf_asr+token[j][k+1]
				if (token[j][k] == 'S'):
					suf_clean=suf_clean+" "
			list_clean.append(suf_clean)
			list_asr.append(suf_asr)			
		j+=1
	i+=1


suffix_S=[]
for element in suffixes:
	suffix_S.append(element+" ")

suffix_F=[]
for element in suffixes:
	suffix_F.append(element+"\n")

list_clean_vf=[]
list_asr_vf=[]
for i in range(len(list_clean)):
	list_clean_vf.append(list_clean[i]+"\n")
	list_asr_vf.append(list_asr[i]+"\n")


for i in range(len(list_clean_vf)):
	for element in suffix_S:
		list_clean_vf[i]=re.sub(element, '', list_clean_vf[i])
	for element in suffix_F:
		list_clean_vf[i]=re.sub(element, '', list_clean_vf[i])

for i in range(len(list_asr_vf)):
	for element in suffix_S:
		list_asr_vf[i]=re.sub(element, '', list_asr_vf[i])
	for element in suffix_F:
		list_asr_vf[i]=re.sub(element, '', list_asr_vf[i])

k=0
count_merges_clean=0
count_splits_clean=0

for i in range(len(list_clean_vf)):
	if (list_clean_vf[i]==list_asr_vf[i]):
		k+=1
		result.write(list_clean[i] + " | " + list_asr[i] + "\n")
		if re.search(".* .*",list_clean[i]):
			count_merges_clean+=1
		else:
			count_splits_clean+=1

print(k)

print("count merges: " + str(count_merges_clean))
print("count splits: " + str(count_splits_clean))


