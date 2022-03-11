import random
start_game = 0
end_game = 40
you_win = False
computer_win = False
you = 0
computer = 0
your_position = 0
computer_position = 0
while not you_win or computer_win:
  start = input("if you want play t if you want end q ")
  if start == "q": break
  if start == "t":
    if  your_position < end_game:
      you = random.randint(1,6)
    
      your_position += you
      print("you get " + str(you) +"point " + " your position   " + str(your_position))
    else:
      print("you win ")
      break
    
    if computer_position < end_game:
      computer = random.randint(1,6)
      computer_position += computer
      print("you get " + str(computer) + " point  " + " your position " +str(computer_position))
    else:
      print('computer win')
      break  
