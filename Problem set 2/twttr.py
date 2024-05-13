"""
When texting or tweeting, it’s not uncommon to shorten words to save time or space, as by omitting vowels,
much like Twitter was originally called twttr.
In a file called twttr.py, implement a program that prompts the user for a str of text and then outputs that same text but
with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.
"""

def remove_vowels(sentence):
    new_sentence = ''
    for l in sentence:
        if l in 'AEIOUaeiou':
            continue
        else:
            new_sentence = new_sentence + l
    return new_sentence

message = input("Type your message: ")
ANSWER = remove_vowels(message)
print(ANSWER)

