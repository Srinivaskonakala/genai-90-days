def word_frequency(text):
    words=text.split()
    for word in dict.fromkeys(words):
        print(word,words.count(word))
text=input()
word_frequency(text)