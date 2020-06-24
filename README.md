# Speech_Translation

Synthetic Data Filtering:
Apply the following scripts in the order presented here.
  1.	Punctuation removal (Latvian files): First_cleaning.py
  2.	Removal of sentences containing typical ASR errors: ASR_Mistakes.py
  3.	Calculating Levenshtein distance for each pair of sentences: Diff_Lev.py
  4.	Filtering according the Levenshtein distance (>0.9): Filtering_Distances.py


Rule-Based Synthetic Noise Generation:
Apply the following scripts in the order presented here.
  1.	Comparison between files using difflib Python library: Comparison_difflib.py
  2.	Pre-processing results from difflib analysis: Difflib_post_treatment.py
  3.	Analysing types of errors (token error, split and merge): Diff_analysis.py
  4.	Identification of suffix changes (using a list of possible suffixes in Latvian): Suffix_analysis.py
  5.	Counting number of each type of suffix change: Count_suffix_change.py
  6.	Identification of cases where split or merge of tokens occurred with a suffix change: Split_Merge_Suffix_analysis.py 
  7.	Identification of cases where the difference was linked to a close phoneme change (ex: s changed into z): Phoneme_count.py
  8.	For each pair of suffix change identified in step 5, use the following scripts to generate noise (here the scrips concern the change a  ā):
    
    a.	Analysis of Part-of-Speech changes when suffix change happens in ASR: POS_noise_analysis_a_along.py
    
    b.	Generation of sentences containing noise (without vocabulary check): Noise_adding_a_along.py
    
      i.	In list_POS, there must be the list of allowed POS identified in step 8.a (first column of the file Result_same_POS1_a_along.txt)
    
      ii.	For new_rand, the value for the condition (line 135) is defined by the ratio of the number of occurrences of this suffix changes and the total number of suffix changes. 
    
    c.	Generation of sentences containing noise (with vocabulary check): Noise_adding_a_along_with_vocab_check.py
    
      i.	In list_POS, there must be the list of allowed POS identified in step 8.a (first column of the file Result_same_POS1_a_along.txt)
      
      ii.	For new_rand, the value for the condition (line 135) is defined by the ratio of the number of occurrences of this suffix changes and the total number of suffix changes.
