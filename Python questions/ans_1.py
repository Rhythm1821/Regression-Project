inp = input()
lst = inp.split()
frequency = {}

for word in lst:
    frequency[word] = frequency.get(word, 0) + 1

max_freq = max(frequency.values())
longest_words = [word for word, freq in frequency.items() if freq == max_freq]
word_len = max(len(word) for word in longest_words)

print(word_len)
