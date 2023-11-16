# CLeaning Text steps
# 1. create a text file and take text from it
# 2. convert the letter into lowercase(apple is not equal to Apple)
# 3. remove punctuation
import string
text = open('read.txt' , encoding='utf-8').read()
#convert to lower text
lower_text = text.lower()
#remove punctuations
# maketrans what are the parameters
# str1 is list of characters we need to replace
# str2 is list of characters with which the characters need to be replaced
# str3 is list of characters that needed to be deleted
clean_text = lower_text.translate(str.maketrans('','',string.punctuation)) # makes a transition table
print(clean_text)


