"""
In a file called twttr.py, reimplement Setting up my twttr from Problem Set 2, r
estructuring your code per the below, wherein shorten expects a str as input and
returns that same str but with all vowels (A, E, I, O, and U) omitted,
whether inputted in uppercase or lowercase.
"""

def main():
    my_input = input()
    print(shorten(my_input))

def shorten(word):
    new_sentence = ''
    for l in word:
        if l in 'AEIOUaeiou':
            continue
        else:
            new_sentence = new_sentence + l
    return new_sentence

if __name__ == "__main__":
    main()

