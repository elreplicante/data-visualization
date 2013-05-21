#!/usr/bin/py
# -*- coding: utf-8 -*-

import stats
import csv
import os

speeches_filenames = os.listdir('./data/speeches')
headlines_filenames = os.listdir('./data/headlines')

#Create comma separated values files
output = csv.writer(open("output_king.csv", "wb"))
output_headlines = csv.writer(open("output_headlines.csv", "wb"))


print speeches_filenames
print headlines_filenames

#Dictionary that holds the data to track
words = {	'españa': 0,
					'terrorismo': 0, 
					'patria': 0, 
					'familia': 0, 
					'paz': 0, 
					'libertad': 0,
					'crisis': 0,
					'amor': 0,
					'europa': 0,
					'paro': 0,
					'justicia': 0
		}


#List of rows
rows = ['año']

#Append dictionay keys to csv file rows
for key in words.iterkeys():
	rows.append(key)

print rows


output.writerow(rows)
output_headlines.writerow(rows)


#datafile = open('datos', 'w')

for filename in speeches_filenames:
	speech_file = open('./data/speeches/' + filename, 'r')
	data = speech_file.read().lower()
	values = [filename]
	for key in words.iterkeys():
		words[key] = data.count(key)
		values.append(words[key])
		
		#print key, words[key]
	output.writerow(values)
	print filename
	print words
	print values

for filename in headlines_filenames:
	headline_file = open('./data/headlines/' + filename, 'r')
	data = headline_file.read().lower()
	values = [filename]
	for key in words.iterkeys():
		words[key] = data.count(key)
		values.append(words[key])
		
		#print key, words[key]
	output_headlines.writerow(values)
	print filename
	print words
	print values



