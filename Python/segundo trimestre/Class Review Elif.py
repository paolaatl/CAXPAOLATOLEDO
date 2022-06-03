import datetime

dia = datetime.date.today()

print(dia)

w = dia.weekday()+1

if (w==0):
  print("es domingo")
elif(w==1):
  print("es lunes")
elif(w==2):
  print("es martes")
elif(w==3):
  print("es miercoles")
elif(w==4):
  print("es jueves")
elif(w==5):
  print("es viernes")

else:
  print("YAY, es sabado")
