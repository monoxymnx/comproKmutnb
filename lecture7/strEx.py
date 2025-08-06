def sort_word_in_sentence(sentence):
    word = sentence.split()
    print(word)
    word.sort(key=str.lower)
    sorted_sentence = ' '.join(word)
    print(word)
    return sorted_sentence

sentence = "This is a man world"
sorted_result = sort_word_in_sentence(sentence)
print("sorted sentence",sorted_result)
