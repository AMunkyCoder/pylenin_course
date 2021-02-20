# Write a Python program to replace all occurences of the first character in a string. 

sentence = "Hello World, How are you? Howdy!"

def first_letter(sentence):
    f_letter = sentence[0]
    new_sentence = sentence.replace(f_letter, "A")
    return new_sentence

if __name__ == '__main__':
    print(first_letter(sentence))