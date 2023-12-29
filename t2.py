# Task: Create a function that reverses the words in a given sentence

def reverse_words(sentence):
    words = sentence.split()
    # Use Copilot to complete the code to reverse the words in the sentence
    reversed_sentence = ' '.join(reversed(words[::-1]))
    return reversed_sentence


print(reverse_words("Hello World"))
