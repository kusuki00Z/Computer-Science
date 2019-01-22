'''
Shengnan Zhou
CSCI 305, Assignment 1
Jan. 18, 2019
'''



money = int(input("Enter the amount between 1-99: "))



# do calculation
def conversion(money):
        # Declare and initialize variables
        quarter = 0
        dime = 0
        nickel = 0
        penny = 0

        qstring = ""
        dstring = ""
        nstring = ""
        pstring = ""
        
        if money == 0:
                print("Error: Out of range.")


        while money != 0:
                if money > 99:
                        print("Error: Out of range.")
                        break
                elif money >= 25:
                        quarter = money // 25
                        money = money % 25
                elif money >= 10:
                        dime = money // 10
                        money = money % 10
                elif money >= 5:
                        nickel = money // 5
                        money = money % 5
                elif money >= 1:
                        penny = money // 1
                        money = money % 1
                else:
                	print("Error: Out of range.")
                	break


        if quarter > 0:
        	qstring = str(quarter) + " quarter "

        if dime > 0:
        	dstring = str(dime) + " dime "

        if nickel > 0:
        	nstring = str(nickel) + " nickel "

        if penny > 0:
        	pstring = str(penny) + " penny "


        print(qstring+dstring+nstring+pstring)


conversion(money)


