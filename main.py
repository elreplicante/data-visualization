#!/usr/bin/py
# -*- coding: utf-8 -*-

import stats
import csv
import os

filenames = os.listdir('./data')
output = csv.writer(open("output.csv", "wb"))




print filenames
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
					'satisfacción': 0
					}

rows = ['año']
for key in words.iterkeys():
	rows.append(key)

print rows
output.writerow(rows)

datafile = open('datos', 'w')

for filename in filenames:
	file = open('./data/' + filename, 'r')	
	data = file.read().lower()
	values = [filename]
	for key in words.iterkeys():
		words[key] = data.count(key)
		values.append(words[key])
		
		#print key, words[key]
	output.writerow(values)
	print filename
	print words
	print values



