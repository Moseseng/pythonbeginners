import random
print("welcome to my first game")
name= input("what is your name?")
print('welcom to game  '+ name)
age =int(input("enter your age :"))

if age  >= 18:
  print("your old enough for play " +"\U0001F606")
  left_or_reght = input("first choice left or reght: ")
  if left_or_reght == "left":
    print('enter 3 number and will show you math eqution ')

    ans = int(input("first:"))
    ans2 = int(input("second:"))
    ans3 = int(input("third:"))


    a = "ans +ans2 +ans3"
    b = "ans +ans2 *ans3"
    c = "ans - ans2 + ans3"
    d = "ans **ans3"


    alist = [a ,b, c, d]
    x = random.choice(alist)
    print(x)


    answer = int(input("enter your anser"))

    if x == a:
        a=ans +ans2 +ans3
        if answer == a:
            print("good you are genius")
    elif x==b:
        b = ans +ans2 *ans3
        if answer == b:
            print("good you are genius")
    elif x==c:
        c = ans - ans2 + ans3
        if answer == c:
            print("good you are genius")
            
    elif x==d:
        d = ans **ans3
        if answer == d:
            print("good you are genius")
            
    else:
        print("yry again")
  if left_or_reght == "reght":
    print('I will tell you 5 advice')
    a ="Take time to know yourself"

    b ="A narrow focus brings big results"
    c ="Show up fully"
    d ="Don't make assumptions. "
    alist = [a ,b, c, d]
    print(random.choice(alist))





else:
  print("sory your old is not enough " +"\U0001F605")
