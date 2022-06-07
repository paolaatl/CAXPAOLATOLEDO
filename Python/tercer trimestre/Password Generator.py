import random
base ="abcdefghijklmnñopqrstuvwxyz"


passw=""

while True:
 j = int(input("de cuantos digitos quieres tu contraseña: " ))

 for i in range (j):
   passw=passw+random.choice(base)
 print("password:",passw)
 passw=""
 input()
  