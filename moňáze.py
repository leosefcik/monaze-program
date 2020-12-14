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
    yesno=input("Would you like to buy/sell anything? (y/n): ")
    print(" ")
    if yesno=="y":
        name=input("What are you buying/selling: ")
        cost=float(input("How much does it cost (positive for buying, negative for selling): "))
        if money-cost*1000<0:
            print("This costs more money than you have! Are you sure you want to proceed?")
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

#This is free and unencumbered software released into the public domain.
#
#Anyone is free to copy, modify, publish, use, compile, sell, or
#distribute this software, either in source code form or as a compiled
#binary, for any purpose, commercial or non-commercial, and by any
#means.
#
#In jurisdictions that recognize copyright laws, the author or authors
#of this software dedicate any and all copyright interest in the
#software to the public domain. We make this dedication for the benefit
#of the public at large and to the detriment of our heirs and
#successors. We intend this dedication to be an overt act of
#relinquishment in perpetuity of all present and future rights to this
#software under copyright law.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
#EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
#MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
#IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
#OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
#ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
#OTHER DEALINGS IN THE SOFTWARE.
#
#For more information, please refer to <https://unlicense.org>
