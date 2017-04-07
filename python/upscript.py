#-*- coding: utf-8 -*-

import nltk, googlemaps
from nltk.tokenize import sent_tokenize, word_tokenize

#GOOGLE PROYECT: Tour App; Clave de API 3 tour app, AIzaSyB8xfxrwJAq-Iif3llruqe0mSkjeJ0bUiw

#File Line count function
def lineCount(file):
	with open(file) as g:
		return sum(1 for _ in g)

#Function for replacing non utf characters
def utfFix(line):
	return line.replace("á","a").replace('é','e').replace('ó','o').replace('ú','u').replace('í','i').replace('ü','u').replace('ä','a').replace('ö','o').replace('ï','i').replace('ë','e').replace('ñ','n')
fileLines = lineCount('textoUP.txt')

file = open('textoUP.txt')

nnpArray = []
allWords = []
#line i, word j
for i in range(fileLines):
	line = nltk.pos_tag(word_tokenize(utfFix(file.readline())))
	if len(line)>0:
		for j in range(len(line)): 
			if line[j][1] == 'NNP':
				nnpArray.append((line[j][0],i,j,len(line[j][0])))
	allWords.append(line)

#N-grams
ngramArray = []

for k in range(len(nnpArray)-1):
	string = ''
	if (nnpArray[k+1][2] - nnpArray[k][2] <= 6):
		if nnpArray[k][1] == nnpArray[k+1][1]:
			for w in range(nnpArray[k][2], nnpArray[k+1][2]+1):
				string+= allWords[nnpArray[k][1]][w][0]+ ' '
			ngramArray.append(string)
		else:
			for m in range(nnpArray[k][2], len(allWords[nnpArray[k][1]])):
				string+= allWords[nnpArray[k][1]][m][0]+ ' '

			for n in range(0, nnpArray[k+1][2]):
				string+= allWords[nnpArray[k+1][1]][n][0]
			ngramArray.append(string)

mapLocations = []
gmaps = googlemaps.Client(key = 'AIzaSyDl-LZjOPRm8XmG_waKx9mnVnD5pIDKdoo')
#For loop to process the hash table
for m in range(len(s)):
        geocoder = gmaps.geocode(s[m][0])
        if geocoder != []:
        	o = nnpArray[m][0].split()
        	weight = 0
            #For loop to identify if spacial entity is recognized by google maps
        	for d in range(len(o)):
        		if o[d] in geocoder[0]['formatted_address'] and ('Peru' in geocoder[0]['formatted_address']) :
        			weight += 1
        	mapLocations.append((nnpArray[m][0],weight/len(o)))

#For loop to process the n-gram array
for z in range(len(w)):
        if w[z] != "":
                geocoder = gmaps.geocode(w[z])
                if geocoder != []:
                	o = ngramArray[z].split()
                	weight = 0
                	for d in range(len(o)):
                		if o[d] in geocoder[0]['formatted_address']and ('Peru' in geocoder[0]['formatted_address']):
                			weight+=1
                            #Record longitute and latitute @ SE
                            #latlong = geocoder[0]['latitude']
                	mapLocations.append((ngramArray[z],weight/len(o)))