import random
import Levenshtein

# read the dictionary text file into a list of words
with open('dizionario.txt') as f:
    words = f.read().splitlines()

# read the words from additional dictionary files
# with open('dizionario_2.txt') as f:
#    words.extend(f.read().splitlines())

# with open('dizionario_3.txt') as f:
#    words.extend(f.read().splitlines())

# prompt the user for a Levenshtein distance
while True:
    try:
        distance = int(input('Enter the Levenshtein distance: '))
        break
    except ValueError:
        print('Please enter a valid integer for the Levenshtein distance.')

# prompt the user for a preference on word length
while True:
    length_preference = input('Do the new words need to be the same length as the original ones? (y/n) ')
    if length_preference == 'y' or length_preference == 'n':
        break
    else:
        print('Please enter "y" or "n".')

# get the input sentence from the user
sentence = input('Enter the sentence: ')

# split the sentence into a list of words
sentence_words = sentence.split()

# create a new list to store the modified words
modified_words = []

# iterate over the words in the sentence
for word in sentence_words:
    # choose a random word from the dictionary with the specified Levenshtein distance
    # if no such word exists, use the original word instead
    if length_preference == 'y':
        # only consider words with the same length as the original word
        word_list = [w for w in words if Levenshtein.distance(word, w) == distance and len(w) == len(word)]
        if word_list:  # make sure the list is not empty
            modified_word = random.choice(word_list)
        else:
            modified_word = word
    else:
        # consider any words with the specified Levenshtein distance, regardless of length
        modified_word = random.choice([w for w in words if Levenshtein.distance(word, w) == distance]) or word
    
    # add the modified word to the list
    modified_words.append(modified_word)

# join the modified words into a sentence and print it
print(' '.join(modified_words))