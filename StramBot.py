import os
import random
import Levenshtein

def read_dictionaries(folder):
    """Read all dictionaries in the given folder and return a list of words."""
    words = []
    for file in os.listdir(folder):
        # only consider files ending in .txt
        if file.endswith('.txt'):
            with open(os.path.join(folder, file)) as f:
                words.extend(f.read().splitlines())
    return words

def get_user_input(prompt, valid_inputs):
    """Prompt the user for input and return it if it is valid, otherwise repeat the prompt."""
    while True:
        user_input = input(prompt)
        if user_input in valid_inputs:
            return user_input
        else:
            print(f'Please enter one of the following: {", ".join(valid_inputs)}')

def modify_sentence(sentence, words, distance, length_preference):
    """Modify the sentence by replacing each word with a random word from the dictionary with the specified Levenshtein distance."""
    sentence_words = sentence.split()
    modified_words = []
    for word in sentence_words:
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
        modified_words.append(modified_word)
    return ' '.join(modified_words)

def main():
    # read the dictionary files
    words = read_dictionaries('dictionaries')

    # prompt the user for a Levenshtein distance
    distance = int(get_user_input('Enter the Levenshtein distance: ', map(str, range(100))))

    # prompt the user for a preference on word length
    length_preference = get_user_input('Do the new words need to be the same length as the original ones? (y/n) ', ['y', 'n'])

    # get the input sentence from the user
    sentence = input('Enter the sentence: ')

    # modify the sentence
    modified_sentence = modify_sentence(sentence, words, distance, length_preference)

    # print the modified sentence
    print(modified_sentence)

if __name__ == '__main__':
    main()
