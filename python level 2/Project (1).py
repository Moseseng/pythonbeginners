adressDict = {'phony' : {'name' : 'Phony Phony', 'phone' : 'PhonyNum', 'adress' : 'Pony adress'}}
 
def addPerson():
    nickname = input('Type a nickname for the person\n - ')
    name = input('Type their full name\n - ')
    adress = input('Type their adress\n - ')
    phone = input('Type their phone number\n - ')
    add = False
    for i in adressDict:
        if i.lower() == name.lower():
            print('Name already there')
        elif adressDict[i]['name'].lower() == name.lower():
            print('Name already there')
        else:
            add = True         

    if add:
        adressDict.update({nickname : {'name' : name, 'phone' : phone, 'adress' : adress}})

def indexPerson():
    name = input('Type the person\'s name or nickname\n - ')
    for i in adressDict:
        if i.lower() == name.lower() or adressDict[i]['name'].lower() == name.lower():
            print('\nName: %s\nPhone Number: %s\nAdress: %s\n' %(adressDict[i]['name'], adressDict[i]['phone'], adressDict[i]['adress']))
        else:
            print('Name not found')

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



















        
