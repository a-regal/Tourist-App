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

def isFirst(word, line):
	return word == line[0]

def getCountry(mapJSON):
	return mapJSON[0]['formatted_address'].split(',')[-1]
fileLines = lineCount('textoUP.txt')

file = open('textoUP.txt')

streetWords = ['Av.', 'Av', 'Avenida','avenida', 'av.','av', 'jr.','jr','jiron','Jiron', 'Calle', 'Ca.','ca.','ca',]
gmaps = googlemaps.Client(key = 'AIzaSyDl-LZjOPRm8XmG_waKx9mnVnD5pIDKdoo')

print(getCountry(gmaps.geocode("Calle Juan Norbeto Elespuru, San Isidro, Lima, Peru")))

#for i in range(fileLines):
#	line = nltk.pos_tag(word_tokenize(utfFix(file.readline())))
#	if len(line)>0:
#		for j in range(len(line)): 
#			if line[j][1] == 'NNP' and not isFirst(line[j]):
#				if line[j-1][0] in streetWords:
#					location = gmaps.geocode(line[j-1][0]+ line[j][0])
#					if location != '' and :

