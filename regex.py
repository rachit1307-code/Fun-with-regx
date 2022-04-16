"""
Given two strings (str1 and str2), find the largest substring in str1 that contains str2 characters in the respective order. If there is no such a substring, return None.

For example,
str1 = "thisisaquestiontofindthelargestsubstring"
str2 = "test"

the output is
"thisisaquestiontofindthelargestsubst"

explanation: you can find the "test" as below
"t----------------------e----------st"
"""

import re

# input params
str1 = "thisisaquestiontofindthelargestsubstring"
str2 = "test"

# data processing for regular expression
str2_sample = [str2[-1]]*(len(str2))
for i in range(len(str2)-1):str2_sample[i] = str2[i] + ".*"
str2_sample = (''.join(str2_sample))

# find the larget substring in str1
x = re.findall(str2_sample, str1)
print (x)

if x:
  print("Yes, substring found")
else:
  raise Exception("Sorry, no substring found")
