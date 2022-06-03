
while True:
  x=int(input('GUESS THE NUMBER: '))

  if (x<10):
    print('COLD')
  if (x>20):
    print('HOT')
  if (x==21):
    print('YOU GOT IT!')
  