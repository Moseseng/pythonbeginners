import random
play_game = 'y'
start =1
end = 100
direction = "N"
smallest = start
largest = end

while play_game == "y":

  smallest = start
  largest = end
  print("gues a number between 1 and 100")
  try_number = random.randint(start ,end)
  print(try_number)
  counter = "N"
  while direction != "C" :

    direction = input('is it to large (L) ,too small(S) , or correct(C)?')
    if direction == 'S':
      if try_number > smallest:
        smallest = try_number +1
      try_number = random.randint(smallest ,  largest)
      print (try_number)
    if direction == 'L':
      if try_number < largest:
        largest = largest -1
      try_number =  random.randint(smallest ,  largest)
      print(try_number)
  counter = counter +1
print("i got it tried" + str(counter + "times"))
play_agan = input("y")      
