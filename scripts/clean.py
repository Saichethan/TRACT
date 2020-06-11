import re
import csv
import string
import os

def strip_links(text):
    link_regex    = re.compile('((https?):((//)|(\\\\))+([\w\d:#@%/;$()~_?\+-=\\\.&](#!)?)*)', re.DOTALL)
    links         = re.findall(link_regex, text)
    for link in links:
        text = text.replace(link[0], ', ')    
    return text

def strip_all_entities(text):
    entity_prefixes = ['@', '#']

    for separator in  string.punctuation:
        if separator not in entity_prefixes :
            text = text.replace(separator,' ')
    words = []
    for word in text.split():
        word = word.strip()
        if word:
            if word[0] not in entity_prefixes :
                words.append(word)
    sentence = ' '.join(words)
    return sentence


raw_file = open("raw.tsv", "w+")
clean_file = open("clean.tsv", "w+") 
raw_writer = csv.writer(raw_file, delimiter='\t')
clean_writer = csv.writer(clean_file, delimiter='\t')


raw_writer.writerow(["tweet_id", "tweet", "label"])
clean_writer.writerow(["tweet_id", "tweet", "label"])

data_dir = "/home/reddy/TRACT/data/"
for item in os.listdir(data_dir):

	name = str(item.replace(".csv", ""))
	fil = open(data_dir + item, "r")
	reader = csv.reader(fil, delimiter=",")



	for line in reader:
		tweet = line[1]
		clean = strip_all_entities(strip_links(tweet.lower()))
		raw_writer.writerow([line[0], tweet])
		clean_writer.writerow([line[0], clean, line[-1]])

	fil.close()

#re.sub('[^A-Za-z0-9]+', '', mystring)
