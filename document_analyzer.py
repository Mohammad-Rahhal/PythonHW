my_file = open("document.txt", "r")
data = my_file.read()
data_into_list = data.split(" ")
from collections import Counter
x = Counter(data_into_list)
data_into_list.sort()
word_counter = {}
for word in data_into_list:
     if word in word_counter:
         word_counter[word] += 1
     else:
         word_counter[word] = 1
popular_words = sorted(word_counter, key = word_counter.get, reverse = True)
print(f'\n{popular_words[0]}: { x[popular_words[0]]}')
print(f'{popular_words[1]}: { x[popular_words[1]]}')
print(f'{popular_words[2]}: { x[popular_words[2]]}')
print(f'{popular_words[3]}: { x[popular_words[3]]}')
print(f'{popular_words[4]}: { x[popular_words[4]]}')

