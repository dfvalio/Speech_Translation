# Treatment of difflib output to be used in further analysis 

import re
import codecs

diff_file = codecs.open("difflib_output_processed_original_lv_files.txt","r","utf-8")
result_file= codecs.open("difflib_output_processed_original_lv_files_corr.txt","w","utf-8")

text = diff_file.readlines()

for sentence in text:
    corr=re.sub('     ','X',sentence)
    corr1=re.sub('    ','S',corr)
    corr2=re.sub(' ','',corr1)
    corr3=re.sub('X', ' ', corr2)
    corr4=re.sub('--', ' - -',corr3)
    corr5=re.sub('\+\+', ' + +',corr4)
    result_file.write(corr5)