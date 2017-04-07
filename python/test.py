#-*- coding: utf-8 -*-
import nltk, googlemaps
from nltk.tokenize import sent_tokenize, word_tokenize
#GOOGLE PROYECT: Tour App; Clave de API 3 tour app, AIzaSyB8xfxrwJAq-Iif3llruqe0mSkjeJ0bUiw
g = open('textoUP.txt')
s = []
n = []
w = []

#Funcion para calcular numero de lineas en el texto
def file_len(text):
	for i, l in enumerate(text):
		pass
	return i+1
k = file_len(g)
g.close()
g = open('textoUP.txt')

#Hash table de NNPs
for i in range(k):
	a = nltk.pos_tag(word_tokenize(g.readline().replace("á","a").replace('é','e').replace('ó','o').replace('ú','u').replace('í','i').replace('ü','u').replace('ä','a').replace('ö','o').replace('ï','i').replace('ë','e')))
	if len(a)>0:
		for j in range(len(a)): 
			if a[j][1] == 'NNP':
				s.append((a[j][0],i,j,len(a)))
	n.append(a)

#N-gramas
for j in range(len(s)-1):
	f = ''
	if (s[j+1][2] - s[j][2]<= 6):
		for i in range(s[j][2],s[j+1][2]):
			f+= n[s[j][1]][i][0]+ ' '
			print(j,i)
			print(f)
		w.append(f)

#Busqueda de candidatos en google maps
a = []
gmaps = googlemaps.Client(key = 'AIzaSyB8xfxrwJAq-Iif3llruqe0mSkjeJ0bUiw')
#For loop to process the hash table
for m in range(len(s)):
        geocoder = gmaps.geocode(s[m][0])
        if geocoder != []:
        	o = s[m][0].split()
        	weight = 0
            #For loop to identify if spacial entity is recognized by google maps
        	for d in range(len(o)):
        		if o[d] in geocoder[0]['formatted_address'] and ('Peru' in geocoder[0]['formatted_address']) :
        			weight += 1
        	a.append((s[m][0],weight/len(o)))

#For loop to process the n-gram array
for z in range(len(w)):
        if w[z] != "":
                geocoder = gmaps.geocode(w[z])
                if geocoder != []:
                	o = w[z].split()
                	weight = 0
                	for d in range(len(o)):
                		if o[d] in geocoder[0]['formatted_address']and ('Peru' in geocoder[0]['formatted_address']):
                			weight+=1
                            #Record longitute and latitute @ SE
                            #latlong = geocoder[0]['latitude']
                	a.append((w[z],weight/len(o)))
print(a)