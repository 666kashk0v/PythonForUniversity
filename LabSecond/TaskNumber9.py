#dictionary { key:value }
words_dict = {
    "hello everyone": len("hello everyone"),
    "hello stupid python": len("hello stupid python"),
    "world": len("hello stupid python")
}
print(words_dict)

#или

word1 = "hello everyone"
word2 = "hello stupid python"
word3 = "world"

word_list2 = {
    word1: len(word1),
    word2: len(word2),
    word3: len(word3)
}
print(word_list2)