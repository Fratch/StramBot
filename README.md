# StramBot

This Python script allows you to modify a given sentence by replacing each word with a random word from a set of dictionaries, considering Levenshtein distance and optionally maintaining the original word's length.

## Usage

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Fratch/StramBot
   cd StramBot
   ```

2. **Run the Script:**
   ```bash
    python strambot.py
    ```

3. **Follow the Prompts:**
    - Enter the Levenshtein distance (a non-negative integer).
    - Choose whether the new words need to be the same length as the original ones (yes/no).
    - Enter the sentence you want to modify.

4. **View the Result:**
    The script will output the modified sentence.

## Requirements
Python 3.x
The script relies on the Levenshtein module, which can be installed using:

```bash
pip install python-Levenshtein
```

## Folder Structure
The script expects a folder named "dictionaries" containing text files with lists of words. Each text file represents a dictionary.

## Example
Suppose you have dictionaries in the "dictionaries" folder, and you want to modify the sentence "The quick brown fox" with a Levenshtein distance of 1 and maintaining word length. The interaction would be:

```bash
Enter the Levenshtein distance: 1
Do the new words need to be the same length as the original ones? (y/n) y
Enter the sentence: The quick brown fox
```

The output might be something like:

```bash
Thy quiik broon fpx
```

## Notes
- If the "dictionaries" folder is not found or empty, the script will use a default list containing only the word "word."
- Invalid inputs will prompt error messages.
- The script is case-sensitive.
Feel free to customize the dictionaries or extend the functionality according to your needs.
