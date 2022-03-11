
import random
left_or_reght = input("first choice left or reght")
if left_or_reght == "left":
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
            
        
        
