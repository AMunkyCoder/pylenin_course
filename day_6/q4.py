# Write a Python program to add first and last n characters in a string.

def add_n(sentence):
    n = int(input("Enter number:"))
    if n > len(sentence):
        word = ""
    else:
        word = sentence[:n] + sentence[-n:]
    return word


if __name__ == '__main__':
    sentence = input("Enter word:")
    print(add_n(sentence))