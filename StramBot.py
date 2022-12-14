import sys
from Levenshtein import distance

# Read the dictionary from a file
with open('dizionario.txt') as f:
    words = f.read().splitlines()

# Read the sentence to be transformed from the command line arguments
sentence = ' '.join(sys.argv[1:])

# Split the sentence into individual words
words = sentence.split()

# Replace each word with another word in the dictionary that has the
# specified Levenshtein distance
output = []
levenshtein_distance = int(sys.argv[1])
for word in words:
    # Compute the Levenshtein distance between the word and each word
    # in the dictionary
    distances = [distance(word, w) for w in words]
    
    # Find the index of the closest word in the dictionary
    closest_index = min(range(len(distances)), key=distances.__getitem__)
    
    # Replace the word with the closest word in the dictionary
    output.append(words[closest_index])

# Join the words back into a sentence and print it
print(' '.join(output))