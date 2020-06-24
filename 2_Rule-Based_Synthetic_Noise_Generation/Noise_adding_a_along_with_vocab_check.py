import codecs
import re
import string
import random

file=codecs.open("difflib_output_processed_original_lv_files_corr.txt","r","utf-8")
diff_file=file.readlines()

file=codecs.open("train.clean.alg.lv.tok.tc.lv","r","utf-8")
clean=file.readlines()

file=codecs.open("train.asr.clean.lv.tok.tc.lv","r","utf-8")
asr=file.readlines()

file=codecs.open("train.clean.en","r","utf-8")
clean_en=file.readlines()

file=codecs.open("POS_clean_alg_tok_tc_lv.txt","r","utf-8")
POS_clean=file.readlines()

# file=codecs.open("POS_clean_asr_tok_tc_lv.txt","r","utf-8")
# POS_asr=file.readlines()

file=codecs.open("vocab_final.txt","r","utf-8")
vocab_file=file.readlines()

print("Done charging files")


vocab=[]
for element in vocab_file:
	vocab.append(element.strip("\n").strip("\r"))
vocab_dic = dict.fromkeys(vocab, True)
print("Done dict vocab")


POS_clean_tok=[]
for sentence in POS_clean:
	sentence=sentence.split(" ")
	POS_clean_tok.append(sentence)

print("Done POS clean")

# POS_asr_tok=[]
# for sentence in POS_asr:
# 	sentence=sentence.split(" ")
# 	POS_asr_tok.append(sentence)

# print("Done")

sentence_clean_tok=[]
for sentence in clean:
	sentence=sentence.split(" ")
	sentence_clean_tok.append(sentence)

print("Done clean")

sentence_asr_tok=[]
for sentence in asr:
	sentence=sentence.split(" ")
	sentence_asr_tok.append(sentence)

print("Done ASR")
print("Begin of the loop")


list_POS=["A-msdp-y------------------l-","A-fsgp-n------------------l-","A-fsnc-n------------------l-","A-msdp-y------------------l-","P-msd-------m-------------l-","A-fpac-n------------------l-","A-msdc-y------------------l-","P-msn-------d-------------l-","A-msdp-y------------------l-","P-fsg-------g-------------l-","N-fsn---------n-----------l-","A-msgp-n------------------l-","P-msg-------i-------------l-","A-fsgp-n------------------l-","A-fsgp-n------------------l-","A-fsgp-n------------------l-","A-fpnp-n------------------l-","N-mpg---------n-----------l-","A-fsgp-n------------------l-","A-msgp-n------------------l-","N-fpa---------n-----------l-","N-fsg---------n-----------l-","----------------------------","Gpfpap-n---p--------------l-","P-fpa-------r-------------l-","A-fsgp-n--------y---------l-","N-fsn---------n-----------f-","A-msdc-n------------------l-","P-msg-------g-------------l-","Gsfpnp-n---p--------------l-","P-msg-------s-------------l-","A-fsgc-n------------------l-","A-fsgp-n--------y---------l-","P-msd-------g-------------l-","A-fsnc-n------------------l-","S----------------sap------l-","N-msg---------n-----------l-","N-fpn---------n-----------l-","A-fsnc-n------------------l-","P-msd-------r-------------l-","A-msdc-y------------------l-","A-msgp-n------------------l-","A-fsgp-n--------y---------l-","N-fsn---------n-y---------l-","N-fsd---------n-----------l-","P-msg-------i-------------l-","N-fsn---------n-----------l-","A-fsnp-n------------------l-","A-mpdc-y------------------l-","A-fsnc-n------------------l-","P-fpn-------i-------------l-","A-fsnp-n------------------l-","P-msg-------g-------------l-","P-msd-------d-------------l-","N-fsn---------y-----------l-","P-msg-------m-------------l-","N-msg---------n-----------l-","N-fsg---------n-----------l-","P-fpa-------i-------------l-","A-msdp-y------------------l-","A-fsgc-n------------------l-","N-fpn---------n-----------f-","N-msd---------y-----------l-","N-fsd---------n-----------f-","A-fsnc-n------------------l-","P-fsg-------s-------------l-","A-fpap-n--------y---------l-","A-msgp-n------------------l-","N-msd---------n-----------f-","P-msg-------g-------------l-","A-fsgc-n------------------l-","N-fpa---------n-----------l-","A-fsgc-n------------------l-","P-fsn-------g-------------l-","A-fpnp-n--------y---------l-","A-fsnp-n------------------l-","A-fsnc-n--------y---------l-","A-fsnc-n------------------l-","N-fsn---------n-----------l-","P-msd-------d-------------l-","A-fpnc-n------------------l-","A-msgp-n--------y---------l-","A-msgp-n------------------l-","A-msdc-n------------------l-","N-fpn---------n-----------l-","P-fsg-------g-------------l-","A-fpnp-n------------------l-","A-msdp-n------------------l-","A-fsgp-n------------------l-","A-msgc-n------------------l-","P-fsg-------s-------------l-","A-msdc-n------------------l-","A-fpap-n--------y---------l-","A-fpap-n--------y---------l-","A-fsnp-n------------------l-","A-msgp-n------------------l-","N-fsn---------n-----------l-","A-msgp-n------------------l-","A-msdp-n------------------l-","A-fpap-n--------y---------l-","A-fsgp-n------------------l-","A-msdp-y------------------l-","P-msn-------d-------------l-","N-msg---------y-----------l-","N-msg---------n-----------l-","A-fpnp-n--------y---------l-","A-fpnp-n------------------l-","Gpfpnp-n---p----y---------l-","P-msn-------d-------------l-","A-fpnp-n------------------l-","A-msdp-y------------------l-","P-msd-------s-------------l-","N-mpd---------n-----------l-","A-msgp-n------------------l-","P-fsg-------i-------------l-","A-fsgp-n------------------l-","A-msgc-n------------------l-","A-fsnc-n------------------l-","A-msdc-n------------------l-","A-fpap-n------------------l-","A-fpnp-n--------y---------l-","P-msg-------m-------------l-","A-fpap-n------------------l-","A-fpap-n------------------l-","N-fpn---------n-----------l-","P-fsg-------s-------------l-","P-fsn-------d-------------l-","N-msg---------n-----------l-","Q-------------------------l-","P-fpn-------d-------------l-","A-fsgc-n------------------l-","A-fsdp-n------------------l-","N-fsg---------n-----------l-","A-msgp-n------------------l-","N-fsg---------y-----------l-","A-fsgc-n------------------l-","P-msd-------d-------------l-","A-fpap-n------------------l-","A-fsgc-n------------------l-","N-msg---------n-----------f-","A-msdc-y------------------l-","P-fsn-------g-------------l-","M-msg---c-----------------l-","N-fsl---------y-----------l-","N-fpn---------n-----------l-","A-fpnp-n--------y---------l-","A-fpap-n------------------l-","A-msdp-n------------------l-","N-msn---------n-----------l-","A-msdp-y------------------l-","Gpfpap-n---a--------------l-","A-msgc-n------------------l-","N-fsn---------n-----------f-","A-msdp-y--------y---------l-","A-fpap-n------------------l-","N-fsl---------n-----------f-","N-fsg---------n-----------f-","A-fsgp-n------------------l-","A-fpnc-n------------------l-","A-fsgp-n--------y---------l-","M-msg---c-----------------l-","A-msdp-y------------------l-","N-fsg---------n-----------f-","A-fpnp-n------------------l-","P-msg-------i-------------l-","P-fsn-------g-------------l-","P-fpn-------r-------------l-","A-msdp-y------------------l-","N-fsn---------n-----------l-","A-fpap-n------------------l-","Gsfpdp-y---p--------------l-","N-msd---------n-----------l-","A-msdp-y------------------l-","N-fsg---------n-----------f-","Gpfsnp-n---a----y---------l-","A-fpnp-n------------------l-","A-fpnp-n------------------l-","A-msgp-n------------------l-","P-fpn-------i-------------l-","A-fsdp-y------------------l-","N-msg---------n-----------l-","A-fsgc-n------------------l-","A-msgc-n------------------l-","P-fsn-------r-------------l-","A-msdc-n------------------l-","P-fpa-------s-------------l-","A-fsgp-n------------------l-","A-fsgp-n--------y---------l-","P-fsd-------r-------------l-","Gsfpn--n---a--------------l-","A-msnc-y------------------l-","N-fpa---------n-----------l-","N-msg---------n-----------l-","N-msg---------n-----------l-","N-fpg---------n-----------l-","P-fpn-------i-------------l-","A-fsnp-n------------------l-","A-msgp-n------------------l-","A-msgp-n------------------l-","A-fpap-n------------------l-","A-fsgc-n------------------l-","A-fsgp-n------------------l-","N-msg---------n-----------l-","N-fsn---------n-y---------l-","P-fpn-------m-------------l-","A-msdp-y------------------l-","P-fpn-------r-------------l-","P-fsg-------d-------------l-","A-fsnp-n--------y---------l-","A-fsgc-n------------------l-","N-fpn---------n-----------l-","A-fsgp-n--------y---------l-","P-fsg-------i-------------l-","P-msg-------g-------------l-","A-fpap-n------------------l-","N-fsn---------n-----------f-","P-msg-------g-------------l-","N-msd---------n-----------l-","P-fsg-------d-------------l-","A-fplp-y------------------l-","N-msl---------n-----------l-","A-msgc-n------------------l-","A-fsgc-n------------------l-","P-msn-------d-------------l-","Gsfpnp-n---p----y---------l-","A-msdp-y------------------l-","A-fpnp-n------------------l-","A-fpap-n--------y---------l-","C-------------------------l-","P-msn-------d-------------l-","P-msd-------z-------------l-","P-fsn-------d-------------l-","A-fpac-n--------y---------l-","A-fsdp-y------------------l-","P-msg-------s-------------l-","N-msd---------n-----------f-","A-fpac-n------------------l-","A-fsnp-n--------y---------l-","N-msn---------n-----------l-","A-fpap-n------------------l-","P-fpn-------g-------------l-","S----------------pdp------l-","P-fpa-------s-------------l-","A-msnp-y------------------l-","P-fsn-------g-------------l-","A-fpap-n--------y---------l-","P-fsg-------s-------------l-","S----------------pdp------l-","A-msgp-n------------------l-","A-msdc-n------------------l-","A-fsgp-n------------------l-","A-fpac-n------------------l-","A-fsgc-n------------------l-","A-fsgp-n--------y---------l-","M-fpa---c-----------------l-","N-fsn---------n-----------l-","N-fpn---------n-----------l-","N-fpn---------n-----------l-","A-fpnc-n------------------l-","A-fsnp-n--------y---------l-","A-fpnc-n------------------l-","A-fpnc-n------------------l-","A-fpnc-n------------------l-","A-msgp-n--------y---------l-","A-fpac-n------------------l-","A-fpac-n------------------l-","N-fsl---------n-----------l-","A-fpap-n------------------l-","Gsfpap-n---p--------------l-","P-msg-------r-------------l-","N-fsg---------n-----------l-","N-fsg---------n-y---------l-","P-fpa-------s-------------l-","N-fpa---------n-----------l-","P-msn-------d-------------l-","A-fsgp-n--------y---------l-","A-fsnc-n------------------l-","P-msg-------m-------------l-","A-fsgp-n------------------l-","N-msd---------n-----------l-","P-msg-------i-------------l-","A-fsgp-n------------------l-","N-fsn---------n-----------l-","N-fsg---------n-----------l-","N-msd---------n-----------f-","N-fsg---------n-----------l-","A-fpnp-n--------y---------l-","A-fpnp-n------------------l-","A-msdp-n------------------l-","A-fsnp-n------------------l-","A-fsnc-n------------------l-","N-msg---------n-----------l-","A-fpdp-y------------------l-","P-msd-------r-------------l-","P-msn-------d-------------l-","A-fsnc-n------------------l-","A-msgp-n------------------l-","P-msg-------g-------------l-","A-fsgp-n------------------l-","A-fsnp-n------------------l-","P-fpn-------g-------------l-","A-msdc-n------------------l-","A-fpac-n------------------l-","A-fsnp-n------------------l-","A-msdp-y------------------l-","A-fsgc-n------------------l-","P-msd-------d-------------l-","A-fpnc-n------------------l-","N-fsg---------n-----------l-","P-fsn-------r-------------l-","P-fsn-------i-------------l-","N-fsn---------n-----------l-","N-fsn---------n-----------l-","A-fsnp-n--------y---------l-","N-fpa---------n-----------l-","S----------------sap------l-","Gsfsnp-n---p----y---------l-","P-msg-------d-------------l-","A-fsgp-n------------------l-","A-msdp-y------------------l-","A-msdp-y------------------l-","P-fpn-------d-------------l-","P-fpa-------s-------------l-","N-msg---------n-----------f-","A-fpap-n--------y---------l-","P-fpa-------g-------------l-","A-fpap-n------------------l-","P-fsn-------d-------------l-","P-fpa-------i-------------l-","A-fsnp-n--------y---------l-","P-fpn-------r-------------l-","A-fsnp-n------------------l-","A-fpac-n------------------l-","M-fsn---c-----------------l-","A-fsnp-n--------y---------l-","A-fpap-n--------y---------l-","N-fpn---------n-----------f-","A-msdp-n--------y---------l-","A-fpac-n------------------l-","P-msg-------r-------------l-","N-msg---------n-----------f-","N-msd---------n-----------f-","N-fpn---------n-----------l-","P-msd-------s-------------l-","A-fpnp-n------------------l-","P-msg-------g-------------l-","A-fpnp-n------------------l-","A-fsnc-n------------------l-","A-fpnp-n--------y---------l-","P-fsg-------s-------------l-","A-fsnp-n------------------l-","P-fpn-------i-------------l-","A-fpac-n--------y---------l-","A-msdp-y--------y---------l-","A-fsnc-n------------------l-","N-fsn---------n-----------l-","A-fsdp-n------------------l-","P-fpa-------d-------------l-","N-fsa---------n-----------l-","N-fsn---------n-----------f-","A-fsnp-n--------y---------l-","P-fpn-------d-------------l-","N-fsg---------n-y---------l-","A-mpdp-y------------------l-","N-fsn---------n-----------l-","P-fsg-------d-------------l-","A-fpap-n------------------l-","A-fsgp-n------------------l-","N-fsg---------n-----------f-","N-fsd---------n-----------f-","N-fsn---------n-----------f-","A-fpnp-n--------y---------l-","Gpfpnp-n---p--------------l-","N-msd---------n-----------f-","P-msd-------d-------------l-","P-fpn-------i-------------l-","A-fsgp-n--------y---------l-","P-fsn-------i-------------l-","P-fpn-------i-------------l-","A-fsnp-n--------y---------l-","A-fpnp-n------------------l-","A-fsnc-n------------------l-","P-fpn-------i-------------l-","A-fpap-n------------------l-","A-fpdp-y------------------l-","N-msd---------n-----------l-","M-msd---o-----------------l-","N-fsg---------n-----------l-","A-msds-y------------------l-","A-fsnp-n--------y---------l-","A-fpap-n------------------l-","A-msdp-y------------------l-","A-msgp-n------------------l-","A-fpnp-n--------y---------l-","N-fsl---------n-----------l-","A-msgp-n--------y---------l-","N-fsg---------n-----------l-","A-msgp-n--------y---------l-","A-fpnp-n------------------l-","A-msdc-y------------------l-","A-fsnc-n------------------l-","A-fsgp-n------------------l-","A-msgc-n------------------l-","N-fsn---------n-----------f-","A-fsnp-n------------------l-","N-msg---------n-----------f-","A-fsgp-n------------------l-","N-msg---------n-----------l-","N-fsg---------n-----------l-","N-fsn---------n-----------l-","P---n-------r-------------l-","N-fpn---------n-----------l-","A-fpap-n------------------l-","P-fpa-------s-------------l-","N-fpa---------n-----------l-","A-fpnp-n------------------l-","A-fsgp-n------------------l-","A-fsgp-n------------------l-","A-fsgp-n------------------l-","Gpfpnp-n---p--------------l-","Gpfpnp-n---p--------------l-","A-msgp-n------------------l-","N-fsg---------n-----------f-","A-msnc-y------------------l-","N-fsg---------n-----------l-","P-fsn-------s-------------l-","A-msdp-y------------------l-","A-fsgc-n------------------l-","A-msdp-n------------------l-","P-fpn-------d-------------l-","A-fpap-n------------------l-","A-fsnp-n------------------l-","P-msd-------g-------------l-","N-fsg---------n-----------l-","A-fsgp-n------------------l-","A-msgp-n--------y---------l-","P-msd-------d-------------l-","A-msgc-n------------------l-","A-fsnp-n------------------l-","P-msd-------r-------------l-","A-msdp-y------------------l-","N-fsa---------n-----------l-","N-fsn---------n-----------l-","N-fsn---------n-----------f-","N-fsg---------n-----------l-","N-msg---------n-----------l-","A-mslp-n------------------f-","A-msgp-n------------------l-","P-fsn-------r-------------l-","A-msgp-n------------------l-","A-fpnp-n--------y---------l-","A-msdp-y------------------l-","A-fsgc-n------------------l-","A-fsgp-n------------------l-","A-fsgp-n------------------l-","P-fsn-------g-------------l-","P-msd-------r-------------l-","A-fsnp-n------------------l-","P-fpn-------s-------------l-","N-fsn---------n-----------f-","A-fpap-n------------------l-","N-fsd---------n-----------f-","N-fsd---------n-----------f-","Vp-------c----------------l-","M-fsn---c-----------------l-","N-msg---------n-----------l-","P-msg-------d-------------l-","A-fsgp-n------------------l-","A-fsnp-n------------------l-","A-fsdp-n------------------l-","P-fsn-------z-------------l-","A-fpap-n------------------l-","P-msd-------i-------------l-","A-msgp-n------------------l-","A-fpnp-n------------------l-","N-msd---------n-----------f-","A-fsnp-n------------------l-","P-fpn-------d-------------l-","P-fpn-------d-------------l-","A-fpap-n------------------l-","A-fsdp-n------------------l-","N-fsg---------n-----------l-","A-fsgc-n------------------l-","A-fpnc-n------------------l-","N-fpn---------n-----------l-","M-fsg---c-----------------l-","A-fsgp-n------------------l-","N-msg---------n-----------l-","A-fsgp-n--------y---------l-","A-msdp-n------------------l-","N-fsg---------n-----------f-","N-msn---------n-----------l-","A-fpnc-n------------------l-","N-fsn---------n-----------l-","A-fpnp-n--------y---------l-","A-fsgp-n--------y---------l-","A-msgp-n------------------l-","A-msnc-y------------------l-","P-fsg-------r-------------l-","A-msgp-n------------------l-","A-fslp-y------------------l-","A-fsnp-n------------------l-","P-fsn-------i-------------l-","N-fsn---------n-----------l-","N-mpn---------n-----------l-","A-fpap-n------------------l-","A-msgc-n------------------l-","N-fsd---------n-----------l-","N-mpd---------n-----------l-","A-fsnp-n------------------l-","N-fsn---------n-----------l-","A-msgp-n------------------l-","Gpfsnc-n---a--------------l-","A-msdc-y------------------l-","P-fpn-------r-------------l-","A-fsnp-n------------------l-","A-msnp-y------------------l-","A-fsnc-n------------------l-","N-msg---------n-----------l-","P-msg-------m-------------l-","A-fpnp-n------------------l-","A-msnp-y------------------l-","A-msdc-y------------------l-","A-msns-y------------------l-","N-fpa---------n-----------l-","P-msd-------g-------------l-","N-msn---------n-----------l-","Gpfsnp-n---a--------------l-","Gpmsgp-n---a--------------l-","A-msgp-n--------y---------l-","Gsmsgp-n---p--------------l-","P-msn-------d-------------l-","A-msgp-n------------------l-","A-fsnp-n------------------l-","N-fsg---------n-----------l-","A-msdp-y------------------l-","N-fsn---------n-----------l-","N-fpn---------y-----------l-","P-fsg-------r-------------l-","A-fsnc-n------------------l-","N-msg---------n-----------l-","A-fsgc-n------------------l-","A-msgp-n------------------l-","A-fpnc-n------------------l-","A-fsnp-n--------y---------l-","N-fsg---------n-----------l-","A-fsnp-n--------y---------l-","N-msg---------n-----------f-","P-msg-------g-------------l-","A-fsnc-n------------------l-","N-fpn---------y-----------l-","N-msd---------n-----------l-","A-msgp-n------------------l-","A-fpap-n------------------l-","Vp----3--i----------------l-","N-fpa---------n-----------l-","A-fpac-n--------y---------l-","A-fpnp-n------------------l-","A-fsnc-n------------------l-","N-fpv---------n-----------l-","A-fpnc-n------------------l-","A-msdc-y------------------l-","A-fsnc-n------------------l-","A-msdp-y------------------l-","N-fsg---------n-----------l-","P-msg-------g-------------l-","P-msg-------g-------------l-","A-fsnc-n------------------l-","N-fsn---------n-----------l-","A-fpac-n------------------l-","A-fpnp-n------------------l-","A-fpnp-n------------------l-","P-msn-------d-------------l-","N-fsn---------n-----------f-","P-msd-------s-------------l-","N-msl---------n-----------l-","P-fpn-------i-------------l-","A-msgp-n--------y---------l-","N-fsn---------n-----------f-","A-fsgc-n------------------l-","Gsfsnp-n---p--------------l-","N-msg---------n-----------l-","N-fpg---------n-----------l-","A-msgp-n------------------l-","N-fpa---------n-----------l-","A-fsnp-n--------y---------l-","A-msnp-y------------------l-","A-fpap-n--------y---------l-","Vp----3--i-----y----------l-","N-fsn---------n-----------l-","N-msn---------n-----------f-","Gsfsgp-n---p--------------l-","A-fpnc-n------------------l-","A-fpap-n------------------l-","A-fpnc-n------------------l-","N-fsg---------n-----------f-","N-msd---------n-----------l-","N-fpa---------n-----------l-","R----p--------------------l-","A-msdp-n------------------l-","A-msdp-y--------y---------l-","A-fsnp-n------------------l-","N-msg---------n-----------l-","N-fsd---------n-----------l-","N-fsg---------n-----------l-","N-fsd---------n-----------l-","Gpfsnp-n---p--------------l-","N-msg---------n-----------l-","A-fpac-n------------------l-","A-msdp-n------------------l-","N-msa---------n-----------l-","A-fpnp-n------------------l-","N-msg---------n-----------l-","A-fpnp-n--------y---------l-","A-fsnp-n------------------l-","A-fpap-n--------y---------l-","A-fpnc-n------------------l-","P-fpn-------i-------------l-","P-fsn-------g-------------l-","P-fpa-------g-------------l-","Gsmsg--n---a--------------l-","N-mpa---------n-----------l-","N-fsg---------n-----------l-","Gpfsnp-n---a--------------l-","A-fpap-n------------------l-","A-msnp-y------------------l-","N-fpn---------n-----------l-","Gpfpap-n---a--------------l-","N-fsn---------n-----------l-","N-fsl---------n-----------l-","M-fsg---c-----------------l-","Vp-p--1--i----------------l-","N-msg---------n-----------l-","A-fpnp-n------------------l-","M-fpn---c-----------------l-","N-fpn---------n-----------l-","P-msn-------d-------------l-","N-msg---------n-----------f-","N-fpa---------n-----------l-","A-fsnc-n------------------l-","P-msg-------m-------------l-","A-fsgc-n------------------l-","A-fsnp-n------------------l-","N-fsa---------n-----------l-","A-fpdp-y------------------l-","A-fpnp-n------------------l-","A-msdp-n------------------l-","Gpfsgp-n---a--------------l-","A-fsgp-n------------------l-","A-fpnp-n--------y---------l-","N-msd---------n-----------l-","N-msg---------n-y---------l-","A-fsgp-n--------y---------l-","A-fpnp-n------------------l-","A-fpnp-n------------------l-","P-fsg-------s-------------l-","A-msnp-y------------------l-","N-fsg---------n-y---------l-","N-msg---------n-----------l-","A-msgp-n--------y---------l-","N-fsg---------n-----------f-","A-msgp-n------------------l-","N-fpn---------y-----------l-","P-msg-------r-------------l-","P-fpn-------g-------------l-","N-fsn---------n-----------f-","N-msl---------n-----------l-","A-msdp-y--------y---------l-","A-fpac-n------------------l-","A-msdp-n------------------l-","P-fpa-------d-------------l-","N-fpa---------n-----------l-","P-fpa-------r-------------l-","A-msdc-y------------------l-","A-fpnc-n------------------l-","P-msd-------d-------------l-","P-fpn-------r-------------l-","N-fsn---------n-----------f-","P-fpa-------i-------------l-","A-fsgp-n--------y---------l-","A-mslp-y------------------l-","A-fpap-n--------y---------l-","Gpfpnp-n---a--------------l-","A-fpdp-y------------------l-","A-fpnc-n------------------l-","P-fsn-------d-------------l-","A-fsgp-n------------------l-","A-msdp-n------------------l-","Vp----3--i-----y----------l-","A-fsnp-n------------------l-","P-fpn-------g-------------l-","A-fpap-n------------------l-","P-fsn-------g-------------l-","A-msdp-n------------------l-","A-fsgp-n------------------l-","N-fsd---------n-----------l-","P-fsn-------i-------------l-","A-fsnc-n------------------l-","A-fsdc-n------------------l-","A-fpnp-n------------------l-","A-fpap-n------------------l-","N-msg---------n-----------l-","N-fsg---------n-----------l-"]


noise_sentences=[]
noise_sentences_en=[]
nb_changes_each_sentence=[]

count_changes=0
count_tot=0

z=0
while (z<len(clean)):
	nb_changes_each_sentence.append(0)
	z+=1


i=0
while (i<len(clean)):
	for index_tok_clean,token in enumerate(sentence_clean_tok[i]):
		if token.endswith("a"):
			if POS_clean_tok[i][index_tok_clean].split("|")[2] in list_POS:
				nb_changes_each_sentence[i]=nb_changes_each_sentence[i]+1
	i+=1
	if(i%100000==0):
		print(i)

count_in_dic=0
count_out_dic=0

i=0
while (i<len(clean)):
	change=False
	for index_tok_clean,token in enumerate(sentence_clean_tok[i]):
		if token.endswith("a"):
			if POS_clean_tok[i][index_tok_clean].split("|")[2] in list_POS:
				noise_tok=re.sub("a$","ā",token)
				count_tot+=1
				rand=random.uniform(0,1)
				if(noise_tok in vocab_dic):
					if(rand < 1/nb_changes_each_sentence[i]):
						count_in_dic+=1
						noise_sentence=re.sub(token,noise_tok,clean[i])
						change=True
						count_changes=count_changes+1
				else:
					count_out_dic+=1
	if change:
		noise_sentences.append(noise_sentence)
		noise_sentences_en.append(clean_en[i])
	i+=1
	if(i%100000==0):
		print(i)

print(count_tot)
print(count_changes)
print(len(noise_sentences))
print(len(noise_sentences_en))


sentences_noise_file=codecs.open("sentences_noise_a_along_allchangesonesentence_randomfilter_proportional_withdic_final.txt","w","utf-8")
sentences_noise_file_en=codecs.open("sentences_noise_a_along_allchangesonesentence_randomfilter_proportional_withdic_final_en.txt","w","utf-8")


noise_sentences_final=[]
noise_sentences_en_final=[]

for i,sent in enumerate(noise_sentences):
	new_rand=random.uniform(0,1)
	if (new_rand < 0.15):
		noise_sentences_final.append(sent)
		noise_sentences_en_final.append(noise_sentences_en[i])


print(len(noise_sentences_final))
print(len(noise_sentences_en_final))

noise_sentences_final_set=[]
noise_sentences_en_final_set=[]

i=0
while i<len(noise_sentences_final):
	if(noise_sentences_final[i] not in noise_sentences_final_set):
		noise_sentences_final_set.append(noise_sentences_final[i])
		noise_sentences_en_final_set.append(noise_sentences_en_final[i])
	i+=1
	if(i%100000==0):
		print(i)

print(len(noise_sentences_final_set))
print(len(noise_sentences_en_final_set))


i=0
while i<len(noise_sentences_final_set):
	sentences_noise_file.write(noise_sentences_final_set[i])
	sentences_noise_file_en.write(noise_sentences_en_final_set[i])
	i+=1