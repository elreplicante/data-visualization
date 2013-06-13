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

#Dictionary that holds the data to track
words = {			'economía': 0,
					'crisis': 0
		}
#List of rows
rows = ['año']

#Append dictionay keys to csv file rows
for key in words.iterkeys():
	rows.append(key)

output.writerow(rows)
output_headlines.writerow(rows)

for filename in speeches_filenames:
	speech_file = open('./data/speeches/' + filename, 'r')
	data = speech_file.read().lower().split(' ')

	values = [filename]
	for key in words.iterkeys():
		words[key] = data.count(key)
		values.append(words[key])
	output.writerow(values)

for filename in headlines_filenames:
	headline_file = open('./data/headlines/' + filename, 'r')
	data = headline_file.read().lower().split(' ')
	values = [filename]
	for key in words.iterkeys():
		words[key] = data.count(key)
		values.append(words[key])
	output_headlines.writerow(values)