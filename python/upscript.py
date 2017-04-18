# -*- coding: utf-8 -*-9

import nltk, googlemaps
from nltk.tokenize import sent_tokenize, word_tokenize

#GOOGLE PROYECT: Tour App; Clave de API 3 tour app, AIzaSyB8xfxrwJAq-Iif3llruqe0mSkjeJ0bUiw

#Functions for processing text
def process(arrayFrom, arrayTo, wordArray,index,nextIndex):
        string = ''
        if arrayFrom[index][1] == arrayFrom[nextIndex][1]:
                for w in range(arrayFrom[index][2], arrayFrom[nextIndex][2]+1):
                        string+= wordArray[arrayFrom[index][1]][w][0]+ ' '
                arrayTo.append(string)
        else:
                for m in range(arrayFrom[index][2], len(wordArray[arrayFrom[index][1]])):
                        string+= wordArray[arrayFrom[index][1]][m][0]+ ' '

                for n in range(0, arrayFrom[nextIndex][2]):
                        string+= wordArray[arrayFrom[nextIndex][1]][n][0]
                arrayTo.append(string)
def wordDif(w1,w2):
	return w2[3]-w1[3] <= 6

def lineDif(w1,w2):
	return w2[1]-w1[1] <= 1

def lastBatch(position, array):
	return len(array) - position

def isLast(word, array):
    return word == array[-1]
#File Line count function
def lineCount(file):
        with open(file,encoding = 'utf-8') as g:
                for i, l in enumerate(g):
                        pass
                return i+1

#Function for replacing non utf characters
def utfFix(line):
	return line.replace("á","a").replace('é','e').replace('ó','o').replace('ú','u').replace('í','i').replace('ü','u').replace('ä','a').replace('ö','o').replace('ï','i').replace('ë','e').replace('Á','A').replace('É','E').replace('Í','I').replace('Ó','O').replace('Ú','U')

#Function for maps
def getLocation(mapLocation):
        return mapLocation != [] and 'Peru' in mapLocation[0]['formatted_address']
fileLines = lineCount('textoUP.txt')

fileP = open('textoUP.txt',encoding = 'utf-8')

nnpArray = []
allWords = []

#line i, word j
for i in range(fileLines):
	line = nltk.pos_tag(word_tokenize(utfFix(fileP.readline())))
	if len(line)>0:
		for j in range(len(line)): 
			if line[j][1] == 'NNP':
				nnpArray.append((line[j][0],i,j,len(line[j][0])))
	allWords.append(line)



#N-grams
ngramArray = []

for i in range(len(nnpArray)):
        if lastBatch(i,nnpArray) <= 6:
                if isLast(nnpArray[i],nnpArray):
                        break
                nextW = i+1
                while len(nnpArray) > nextW:
                        if wordDif(nnpArray[i],nnpArray[nextW]) and lineDif(nnpArray[i],nnpArray[nextW]):
                                process(nnpArray,ngramArray,allWords,i,nextW)
                        nextW += 1
        else:
        	nextW = i+1
        	while wordDif(nnpArray[i],nnpArray[nextW]) and lineDif(nnpArray[i],nnpArray[nextW]):
                	process(nnpArray,ngramArray,allWords,i,nextW)
                	nextW += 1

#Busqueda de candidatos en google maps
mapsLocations = []
gmaps = googlemaps.Client(key = 'AIzaSyB8xfxrwJAq-Iif3llruqe0mSkjeJ0bUiw')
#For loop to process the hash table
for m in range(len(nnpArray)):
        geocoder = gmaps.geocode(nnpArray[m][0])
        if getLocation(geocoder):
                mapsLocations.append(nnpArray[m][0]) #missing latlng and description

#For loop to process the n-gram array
for z in range(len(ngramArray)):
        if ngramArray[z] != "":
                geocoder = gmaps.geocode(ngramArray[z])
                if getLocation(geocoder):
                	mapsLocations.append(ngramArray[z]) #missing latlng and description
