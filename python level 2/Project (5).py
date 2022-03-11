import random
play_gane = "y"
while (play_gane == "y"):
  answer = random.randint(1 ,100)
  print ("dont enter (1) if you do you will out |\U0001F609")
  a =  int(input('enter any number "a" :'))
  b =  int(input('enter any number "b" :'))
  c = int(input('enter any number(c) :'))

  d = int(input('enter any number (d) :'))
  if a and b == 1: break
  else:
    x = ((a**b)+(b**c)+(c**d))*(d**answer)
    print("(a^b +b^c+c^a)d^answer = " + str(x))
  try_number = int(input("GUESS A NUMBER BETWEEN 1 AND 100 :  "))
  counter = 1
  while try_number != answer:
    if try_number >answer:
      print("your NUMBER is large \U0001F600")
    if try_number < answer:
      print("your NUMBER is small \U0001F612") 
    try_number = int(input("GUESS A NUMBER BETWEEN 1 AND 100 :  "))
    counter = counter + 1
    



  print('yes good you wine \U0001F601' + "you try " 
  + str(counter) + "times")
  play_gane =input('play agan ')

    
