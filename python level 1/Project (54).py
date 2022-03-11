def yesno():
    yesno = input("if you wanna add (y)or index (n) n / y")
    if yesno == "n":
        indexPerson()
        
    elif yesno == 'y':
        addPerson()
        
    else:
        print("invalid response")

def main():
    while True:
        
        Quit = input('Would you like to quit y/n \n - ')
        if Quit == 'n':
            yesno()
            pass
        elif Quit == 'y':
            break
        else:
            print('Invalid response')
 
print(main())
quit()
