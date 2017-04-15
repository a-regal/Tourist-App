from firebase import firebase
firebase = firebase.FirebaseApplication('https://tourist-b7db4.firebaseio.com/',authentication =None)
for i in range(2):
    firebase.put("/",str(i),{"key":"value"})
print(True)
