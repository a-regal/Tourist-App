from firebase import firebase
firebase = firebase.FirebaseApplication('https://tourist-b7db4.firebaseio.com/',authentication =None)
result = firebase.get('/a',None)
print(result)