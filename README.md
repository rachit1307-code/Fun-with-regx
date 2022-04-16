# Fun_with_regx
Maximum string detection

The script regex.py utilises the re (regular expression) python module for matching and searching
string operations. 

Given two strings (str1 and str2), find the largest substring in str1 that contains str2 characters 
in the respective order. If there is no such a substring, return None.

For example,
str1 = "thisisaquestiontofindthelargestsubstring"
str2 = "test"

the output is
"thisisaquestiontofindthelargestsubst"

explanation: you can find the "test" as below
"t----------------------e----------st"
