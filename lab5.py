#1

import re

s1 = ["a", "ab", "abb", "ac", "b"]
for i in s1:
    if re.fullmatch(r'ab*', i):
        print(i)


#2

s2 = ["abb", "abbb", "abbbb", "a"]
for i in s2:
    if re.fullmatch(r'ab{2,3}', i):
        print(i)

#3

s3 = "abc_def ghi_jkl_mno PQ_rstu"
print(re.findall(r'[a-z]+_[a-z]+', s3))

#4

s4 = "Hello there Are you Ready For This"
print(re.findall(r'[A-Z][a-z]+', s4))

#5

s5 = ["a123b", "ab", "acb", "axb", "a-b", "a--"]
for i in s5:
    if re.fullmatch(r'a.*b', i):
        print(i)

 #6

s6 = "Python, is. hard language"
print(re.sub(r'[ ,.]', ':', s6))


#7

s7 = "this_is_snake_case_string"
print(''.join(x.capitalize() or '_' for x in s7.split('_')))


#8

s8 = "SplitAtUpperCaseLetters"
print(re.split(r'(?=[A-Z])', s8))


#9

s9 = "InsertSpacesBetweenWordsStartingWithCapitalLetters"
print(re.sub(r'([a-z])([A-Z])', r'\1 \2', s9))


#10

s10 = "ConvertCamelCaseToSnakeCase"
print(re.sub(r'(?<!^)(?=[A-Z])', '_', s10).lower())