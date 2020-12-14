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
    money=int(money*1000)
else:
    import random
    money=int(random.randrange(50,100)*1000)
moneybeginning=money/1000
paid=0
items=[]
ceny=[]
clear()
while True:
    print("Your current balance is:",money/1000)
    if items==[]:
        print("You haven't bought/sold anything yet!")
    else:
        print("You have gained/lost",(paid-paid*2)/1000,"money for",', '.join(items))
    if money/1000<0:
        negativ=1
    else:
        negativ=0
    yesno=input("Would you like to buy/sell anything? (y/n): ")
    print(" ")
    if yesno=="y":
        name=input("What are you buying/selling: ")
        cost=float(input("How much does it cost (positive for buying, negative for selling): "))
        if (negativ==0)&(money-cost*1000<0):
            print("\nThis costs more money than you have! Are you sure you want to proceed?")
            yesno=input("Type y to confirm this item: ")
            if yesno=="y":
                paid=paid+cost*1000
                money=money-cost*1000
                items.append(name)
                ceny.append(cost-cost*2)
        else:
            paid=paid+cost*1000
            money=money-cost*1000
            items.append(name)
            ceny.append(cost-cost*2)
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
    print("Money now:",money/1000)
    print("You have gained/lost:",(paid-paid*2)/1000)
    print(" ")
    print("Your items (positive buy, negative sell):")
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
money=str(money/1000)
f.write("\nMoney now: ")
f.write(money)
paid=str((paid-paid*2)/1000)
f.write("\nYou have gained/lost: ")
f.write(paid)
f.write("\n\nYour items (positive buy, negative sell):")
for x in range(0,len(items)):
    f.write("\n- ")
    f.write(items[x])
    f.write(" | ")
    cena=str(ceny[x])
    f.write(cena)
    f.write(" money")
paus=input("Press Enter to close the program")

#wahat doses uncucumber d mean tho idk
