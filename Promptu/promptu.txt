lexicon_file = 'lexicon.txt'
lex_stats_file = 'lexstats.txt'
max_prons_file = 'maxprons.txt'

# dictionary to store word counts in lexicon
word_dict = {}

'''
 reading lexicon file
 strip and split each line with \t 
 store first index into word
 incremet the count if it already exists in word_dict 
'''
with open(lexicon_file, 'r') as file:
    for line in file:
        line = line.strip().split('\t')
        word = line[0]
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1

# sort words in alphabetical order with the dictionary keys {word/key, count/value}
sorted_words = sorted(word_dict.keys())

# write into lex_stats_file with {word and numbers of pronunciation}
with open(lex_stats_file, 'w') as stats_file:
    for word in sorted_words:
        stats_file.write(f"{word}\t{word_dict[word]}\n")

# calculating the total words and pronunciations
total_word_count = len(word_dict)
total_pronun_count = sum(word_dict.values())

# calculating the average by using the previous total pronunciations and words
pronun_avg = total_pronun_count / total_word_count

# calculating the max pronunciations of each word
max_pronun = max(word_dict.values())

'''
 writing to max_prons with {words and their maximum pronunciations}
 extracts word from key/value pairs in word_dict if count is equal to max_pronun
 write the word with max pronunciation into max_prons
'''
max_pronunciation_words = [word for word, count in word_dict.items() if count == max_pronun]
with open(max_prons_file, 'w') as max_prons:
    for word in max_pronunciation_words:
        max_prons.write(f"{word}\n")

print('Number of words: ' + str(total_word_count))
print('Number of pronunciations: ' + str(total_pronun_count))
print('Average number of pronunciations per word: ' + str(pronun_avg))
print('Maximum number of pronunciations per word: ' + str(max_pronun))
