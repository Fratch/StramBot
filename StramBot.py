import random
import Levenshtein

# read the dictionary text file into a list of words
with open('dizionario.txt') as f:
    words = f.read().splitlines()

# prompt the user for a Levenshtein distance
while True:
    try:
        distance = int(input('Enter the Levenshtein distance: '))
        break
    except ValueError:
        print('Please enter a valid integer for the Levenshtein distance.')

# get the input sentence from the user
sentence = input('Enter the sentence: ')

# split the sentence into a list of words
sentence_words = sentence.split()

# create a new list to store the modified words
modified_words = []

# iterate over the words in the sentence
for word in sentence_words:
    # choose a random word from the dictionary with the specified Levenshtein distance
    modified_word = random.choice([w for w in words if Levenshtein.distance(word, w) == distance])
    
    # add the modified word to the list
    modified_words.append(modified_word)

# join the modified words into a sentence and print it
print(' '.join(modified_words))
