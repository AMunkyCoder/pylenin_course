# Write a Python program to calculate character frequency in a string.

sentence = "hello, how are you this evening?"

def count_char_freq(sentence):
    char_dict = {}
    ctr = 0
    for char in sentence.lower():
        if char not in char_dict:
            char_dict[char] = 1
        elif char in char_dict.keys():
            char_dict[char] += 1
    return char_dict

if __name__ == '__main__':
    print(count_char_freq(sentence))