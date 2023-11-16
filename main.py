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

#tokenization is was of breaking a sentence into words
tokenized_word = clean_text.split()
# print(tokenized_word)
#stop words adds no meaning to the sentence
stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

#remove stop wordws
final_words = []
for word in tokenized_word:
    if word not in stop_words:
        final_words.append(word)
# print(final_words)
# nlp emotion algorithm
# 1. check if the word in the final word list is also present in emotion txt
#  - open the emotion file
#  - Loop through each line and clear it
#  - Extract the word and emotion using split
# 2) If word is present -> Add the emotion to emotion_list
# 3) Finally count each emotion in the emotion list
print(final_words)
with open('emotions.txt' , 'r') as file:
    for line in file:
        clear_line = line.replace("\n", '').replace(",",'').replace("'",'').strip()
        word, emotion = clear_line.split(':')
        print("word: "+word+" "+"emotion: "+emotion)



