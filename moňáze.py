import os
from datetime import datetime
def clear():
    os.system('cls' if os.name=='nt' else 'clear')
print(" /$$      /$$                                                  ")
print("| $$$    /$$$               ˇ          ´                       ")
print("| $$$$  /$$$$  /$$$$$$  /$$$$$$$   /$$$$$$  /$$$$$$$$  /$$$$$$ ")
print("| $$ $$/$$ $$ /$$__  $$| $$__  $$ |____  $$|____ /$$/ /$$__  $$")
print("| $$  $$$| $$| $$  \ $$| $$  \ $$  /$$$$$$$   /$$$$/ | $$$$$$$$")
print("| $$\  $ | $$| $$  | $$| $$  | $$ /$$__  $$  /$$__/  | $$_____/")
print("| $$ \/  | $$|  $$$$$$/| $$  | $$|  $$$$$$$ /$$$$$$$$|  $$$$$$$")
print("|__/     |__/ \______/ |__/  |__/ \_______/|________/ \_______/")
print(" ")
yesno=input("Would you like to input your own amount of money (type 1) or get a randomly generated amount (type anything else): ")
if yesno=="1":
    money=float(input("Enter the amount of money: "))
else:
    import random
    money=float(random.randrange(50,100))
moneybeginning=money
paid=0
items=[]
ceny=[]
clear()
while True:
    print("Your current balance is:",money)
    if items==[]:
        print("You haven't bought anything yet!")
    else:
        print("You have paid",paid,"money for",', '.join(items))
    yesno=input("Would you like to buy anything? (y/n): ")
    print(" ")
    if yesno=="y":
        name=input("What are you buying: ")
        cost=float(input("How much does it cost: "))
        paid=paid+cost
        money=money-cost
        items.append(name)
        ceny.append(cost)
        clear()
    elif yesno=="n":
        break
    else:
        print("Please type y or n!")
        input("Press enter to continue")
#        print(" \n ")
        clear()
clear()
if items==[]:
    print("Amazing! You haven't bought anything! Enjoy your",money,"money!")
else:
    print("Transactions done!")
    print(" ")
    print("Summary:")
    print("Money at the beginning:",moneybeginning)
    print("Money now:",money)
    print("You have paid:",paid)
    print(" ")
    print("Your items:")
    for x in range(0,len(items)):
        print("-",items[x],"|",ceny[x],"money")
        now=datetime.now().strftime("%Y-%m-%d %H-%M-%S")
print(" ")
#now=datetime.now().strftime("%Y-%m-%d %H-%M-%S")
#f=open(now+".txt","w")
now=datetime.now().strftime("%Y-%m-%d %H-%M-%S")
f=open(now+".txt","w")
f.write("Summary:\n")
moneybeginning=str(moneybeginning)
f.write("Money at the beginning: ")
f.write(moneybeginning)
money=str(money)
f.write("\nMoney now: ")
f.write(money)
paid=str(paid)
f.write("\nYou have paid: ")
f.write(paid)
f.write("\n\nYour items:")
for x in range(0,len(items)):
    f.write("\n- ")
    f.write(items[x])
    f.write(" | ")
    cena=str(ceny[x])
    f.write(cena)
    f.write(" money")
paus=input("Press Enter to close the program")