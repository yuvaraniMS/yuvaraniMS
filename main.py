
import csv
import re
import time
import psutil

# starting time for performance file creation
start = time.time()

# Reading the find_words.txt file
words_txt = open("find_words.txt", "r")
find_words = words_txt.read()
words_txt.close()
find_words_inlist = find_words.split()

# Reading the find_words.txt file and frequency of each word
frequency = {}
shakespeare_text = open("t8.shakespeare.txt", 'r')
text_string = shakespeare_text.read().lower()
match_pattern = re.findall(r'\b[a-z]{3,15}\b', text_string)

# Reading the dictionary.csv file as a dictionary using csv module
with open('french_dictionary.csv', mode='r') as data:
    reader = csv.reader(data)
    dict_from_csv = {rows[0]: rows[1] for rows in reader}

# creating an english list for all english words in find_words file
tot_eng = []
for word in match_pattern:
    if word in find_words_inlist:
        tot_eng.append(word)
eng = set(tot_eng)
eng = list(eng)

# creating an french list for all french words in find_words file
french = []
for x in eng:
    for key, value in dict_from_csv.items():
        if x in key:
            french.append(value)

# creating an frequency list for all words , their number of times the word was replaced
frequency = {}
for y in tot_eng:
    count = frequency.get(y, 0)
    frequency[y] = count + 1

frequency_list = frequency.keys()
f = []
for z in frequency_list:
    f.append(frequency[z])

# zipping to list of lists for english,french words and their corresponding frequency(join tuples together)
final = list(zip(eng, french, f))

# Creating frequency.csv having 3 columns, first “English Word”, second “French Word”
# and third “Frequency” and this should be the first line of the file
header = ['English Word', 'French Word', 'Frequency']
with open('frequency.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)

    # write the header(write the csv file)
    writer.writerow(header)

    for row in final:
        for x in row:
            f.write(str(x) + ',')
        f.write('\n')

# creating t8.shakespeare.translated.txt which is the processed output file that contains the words translated to French
test_str = text_string
print("The original string is : " + str(test_str))

#runs faster
lookp_dict = dict_from_csv

temp = test_str.split()
res = []
for wrd in temp:
    res.append(lookp_dict.get(wrd, wrd))

res = ' '.join(res)

f = open("t8.shakespeare.translated.txt", "w")
f.write(str(res))
f.close()

# creating performance.txt having the time taken for the script to complete and the second line should have the
# memory used by your script
time_taken = time.time() - start
memory_taken = psutil.cpu_percent(time_taken)
f = open("performance.txt", "w")
f.write(f'Time to process: 0 minutes {time_taken} seconds\nMemory used: {memory_taken} MB')
f.close()
