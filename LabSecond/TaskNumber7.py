def is_anagram(word1, word2):
    return sorted(word1) == sorted(word2) #сортируем слова, если наборы букв одинаковые, значит true, else -> false

print(is_anagram("silent", "listen"))
print(is_anagram("list", "listen"))