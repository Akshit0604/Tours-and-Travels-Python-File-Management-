from tkinter import*
import random
print("\t\tWelcome to BlueStar Tours and Travels\n")
print("Fill in the registration details to get started\n")
print("Here is a display of sample registration")
print("\tFull Name: Ram B")
print("\tDate of Birth: 12/11/19** ") 
print("\tPhone Number: 99******12")
print("\tEmail: abc123@gmail.com\n")
print("Kindly adhere to the sample registration order for convenience")
root = Tk()
root.geometry('500x500')
root.title("WELCOME TO BLUESTAR TRAVELS")
root.configure(background="yellow")

#using GUI(tkinter)for the registration
label = Label(root, text="REGISTRATION ",width=20,bg="black",fg="white",font=("calibri", 20))
label.place(x=90,y=50)

label1 = Label(root, text="Full Name",width=20,font=("arial", 10))#creating labels
label1.place(x=80,y=130)
entry1 =Entry(root)
entry1.place(x=250,y=130)

label2 = Label(root, text="Date of Birth",width=20,font=("arial", 10))
label2.place(x=80,y=180)
entry2 = Entry(root)
entry2.place(x=250,y=180)

label3 = Label(root, text="Phone Number",width=20,font=("arial", 10))
label3.place(x=80,y=230)
entry3=Entry(root)
entry3.place(x=250,y=230)

label4 = Label(root, text="Email",width=20,font=("arial", 10))
label4.place(x=80,y=280)
entry4 = Entry(root)
entry4.place(x=250,y=280)

Button(root, text='Proceed',width=20,bg='grey',fg='white').place(x=180,y=350)#creating a button
root.mainloop()
print("\nYou have successfully registered with BlueStar travels !!!\n")
print("The available places for tour are:")


bill=0
discount=0

#using Data Structure(Stacks)to display the available places 
def stk():
        
        stack=[]
        stack.append("1.Ooty")
        stack.append("2.Goa")
        stack.append("3.Wayanad")
        stack.append("4.Hyderabad")
        stack.append("5.Pune")
        print(stack)
        i=int(input("enter the index number correspoding to the place you would like to go"))
        for j in range(1,6):
                if j==i:
                        print("The destination you have choosen is")
                        print(stack.pop(j-1)) #using pop to display the destination choosen
        print("the following places are also available")
        print(stack)

stk()

while True:          #using conditional statements(while loop)
    ch=int(input("\nEnter the corresponding serial number to know more information about the tour: "))
    if ch==1:
        import tkinter as tk   #using tkinter to display ooty itinerary in the tkinter window
        root1=tk.Tk()
        root1.geometry("1500x2500")
        root1.title("ooty itinerary")
        root1.configure(background="grey")
        T = tk.Text(root1, height=80, width=150,bg="black",fg="white",font=("calibri", 14))
        T.place(x=0,y=0)
        quote = """OOTY:
        *Overview:
         Udagamandalam or ootacamund pr ooty is located in the heart of Nilgiris and often
         known as 'Queen of hill stations'.It is a popular hill station in South India.
         It ahs been a hideouy from scorching summer from the British days,infact it was the summer capital of the British.

        *Highlights
        -Botanical Garden
        -Doddabetta Park
        -tea Museum and Tea factory
        -Rose Garden
        -Ooty Lake
        -Avalanche Lake
        -Pykara Lake and Waterfall
        -Toy train."""
        
        T.insert(tk.END, quote)
        tk.mainloop()

        OOTY=open("Ootypro.txt","r") #using file handling to import and display daywise itinerary for ooty
        OP=OOTY.read()
        print(OP)

        import numpy as np  #using pyplot to display stats of ooty tourism 
        import matplotlib.pyplot as pl
        x=['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
        y=[1200,1321,1434,2422,2511,2532,1145,1254,1811,1743,1533,1211]
        pl.xlabel("months")
        pl.ylabel("average visitors")
        pl.bar(x,y,width=0.3,color='b')
        pl.show()
        print("\nThese are the different categories avalable") 
        

        print("\nChoose your preferred category by entering the respective serial number")
        cp=int(input("1.Basic\n2.Semi-Deluxe\n3.Deluxe\n"))
        while True:
            if cp==1:
                print("NOTE 1:Price per head is the price only for 1 day including tax")
                print("NOTE 2:Price for passengers of age below 12 will be charged only half of the original price")
                print("\nPrice per head for age 12 and above:Rs. 1900")
                print("Price per head for age below 12:Rs. 950")
                maj1=int(input("\nNumber of people aged 12 and above:"))
                min1=int(input("Number of people aged below 12:"))
                bill=4*((maj1*1900)+(min1*950))
                print("\n\nWe offer a lucky lottery type of discount for our customers")
                print("The program would generate a random number from 10 to 20 and if you guess it right, there would be a discount of 10% on the final amount")
                lottery=int(input("Choose a number from 10 to 20:"))
                d=random.randint(10,20) #using random module
                print("The number generated by the program is:",d) 
                print("Price for one day(inc tax):",bill/4)         
                print("Price for all dyas(inc ta)",bill)
                if d==lottery:   #calculating bill
                    discount=0.1*bill
                    bill=0.9*bill
                print("Discount:",discount)
                print("Final amount to be paid:",bill)                   
                break
            

            elif cp==2:
                print("NOTE 1:Price per head is the price only for 1 day including tax")
                print("NOTE 2:Price for passengers of age below 12 will be charged only half of the original price")
                print("\nPrice per head for age 12 and above:Rs. 2100")
                print("Price per head for age below 12:Rs. 1050")
                maj1=int(input("\nNumber of people aged 12 and above:"))
                min1=int(input("Number of people aged below 12:"))
                bill=4*((maj1*2100)+(min1*1050))
                print("\n\nWe offer a lucky lottery type of discount for our customers")
                print("The program would generate a random number from 10 to 20 and if you guess it right, there would be a discount of 10% on the final amount")
                lottery=int(input("Choose a number from 10 to 20:"))
                d=random.randint(10,20)
                print("The number generated by the program is:",d) 
                print("Price for one day(inc tax):",bill/4)         
                print("Price for all days(inc tax)",bill)
                if d==lottery:
                    discount=0.1*bill
                    bill=0.9*bill
                print("Discount:",discount)
                print("Final amount to be paid:",bill)                   
                break
            

            elif cp==3: 
                print("NOTE 1:Price per head is the price only for 1 day including tax")
                print("NOTE 2:Price for passengers of age below 12 will be charged only half of the original price")
                print("\nPrice per head for age 12 and above:Rs. 2500")
                print("Price per head for age below 12:Rs. 1250")
                maj1=int(input("\nNumber of people aged 12 and above:"))
                min1=int(input("Number of people aged below 12:"))
                bill=4*((maj1*2500)+(min1*1250))
                print("\n\nWe offer a lucky lottery type of discount for our customers")
                print("The program would generate a random number from 10 to 20 and if you guess it right, there would be a discount of 10% on the final amount")
                lottery=int(input("Choose a number from 10 to 20:"))
                d=random.randint(10,20)
                print("The number generated by the program is:",d) 
                print("Price for one day(inc tax):",bill/4)         
                print("Price for all days(inc tax)",bill)
                if d==lottery:
                    discount=0.1*bill
                    bill=0.9*bill
                print("Discount:",discount)
                print("Final amount to be paid:",bill)                   
                break
                       
        break

    elif ch==2:
        import tkinter as tk #using tkinter to display goa itinerary in the tkinter window
        root1=tk.Tk()
        root1.geometry('1500x2500')
        root1.title("goa itinerary")
        root1.configure(background="grey")
        T = tk.Text(root1, height=80, width=150,bg="black",fg="white",font=("calibri", 14))
        T.place(x=0,y=0)
        quote = """GOA:
        *Overview
        Vacation is refreshment, a way to rejuvenate your senses. Goa is a must visit destination for this purpose.
        This Indian state is a platform of utmost fun and an exciting vacation. Goa beaches are known for awesome scenic beauty and safe night life.
        The luxurious villas at the beaches offer soothing Ayurveda massages, which have always been known for their extensive health benefits.
        The Portuguese influence can still be found in the life style of the locals.
        Some of the oldest churches of the country can be seen here, which are known for their invaluable inscriptions and unique architecture.
        A land of spices and sea food, you can satisfy your taste buds with spicy prawn fries, quality wine and more.
        Hence, plan 4 Days Goa Beaches Tour with us to make this vacation memorable.

        *Highlights
        -Basilica of BOM Jesus, Se-Cathedral
        -Stroll Around Miramar Beach
        -Enjoy Swimming at Baga Beach
        -Take a Sun Bath at Colva Beach
        -Enjoy boating on speedboats at Dona Paula."""
        T.insert(tk.END, quote)
        tk.mainloop()

            
        GOA=open("Goapro.txt","r") #using file handling to import and display daywise itinerary for goa
        GP=GOA.read()
        print(GP)
        import numpy as np #using pyplot to display stats of goa tourism 
        import matplotlib.pyplot as pl
        x=['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
        y=[1214,3012,1432,412,512,554,676,754,1813,1624,2554,1332]
        pl.xlabel("months")
        pl.ylabel("average visitors")
        pl.bar(x,y,width=0.3,color='g')
        pl.show()

        print("\nThese are the different categories avalable")

        

        print("Choose your preferred category by entering the respective serial number")
        cp=int(input("1.Basic\n2.Semi-Deluxe\n3.Deluxe\n"))
        while True:
            if cp==1:
                print("NOTE 1:Price per head is the price only for 1 day including tax")
                print("NOTE 2:Price for passengers of age below 12 will be charged only half of the original price")
                print("\nPrice per head for age 12 and above:Rs. 2100")
                print("Price per head for age below 12:Rs. 1050")
                maj1=int(input("\nNumber of people aged 12 and above:"))
                min1=int(input("Number of people aged below 12:"))
                bill=4*((maj1*2100)+(min1*1050))
                print("\nWe offer a lucky lottery type of discount for our customers")
                print("The program would generate a random number from 10 to 20 and if you guess it right, there would be a discount of 10% on the final amount")
                lottery=int(input("Choose a number from 10 to 20"))
                d=random.randint(10,20)
                print("The number generated by the program is:",d) 
                print("Price for one day(inc tax):",bill/4)         
                print("Price for all dyas(inc ta)",bill)
                if d==lottery:
                    discount=0.1*bill
                    bill=0.9*bill
                print("Discount:",discount)
                print("Final amount to be paid:",bill)                   
                break
            

            elif cp==2:
                print("NOTE 1:Price per head is the price only for 1 day including tax")
                print("NOTE 2:Price for passengers of age below 12 will be charged only half of the original price")
                print("\nPrice per head for age 12 and above:Rs. 2300")
                print("Price per head for age below 12:Rs. 1150")
                maj1=int(input("\nNumber of people aged 12 and above:"))
                min1=int(input("Number of people aged below 12:"))
                bill=4*((maj1*2300)+(min1*1150))
                print("\nWe offer a lucky lottery type of discount for our customers")
                print("The program would generate a random number from 10 to 20 and if you guess it right, there would be a discount of 10% on the final amount")
                lottery=int(input("Choose a number from 10 to 20"))
                d=random.randint(10,20)
                print("The number generated by the program is:",d) 
                print("Price for one day(inc tax):",bill/4)         
                print("Price for all dyas(inc ta)",bill)
                if d==lottery:
                    discount=0.1*bill
                    bill=0.9*bill
                print("Discount:",discount)
                print("Final amount to be paid:",bill)                   
                break
            

            elif cp==3: 
                print("NOTE 1:Price per head is the price only for 1 day including tax")
                print("NOTE 2:Price for passengers of age below 12 will be charged only half of the original price")
                print("\nPrice per head for age 12 and above:Rs. 2700")
                print("Price per head for age below 12:Rs. 1350")
                maj1=int(input("\nNumber of people aged 12 and above:"))
                min1=int(input("Number of people aged below 12:"))
                bill=4*((maj1*2700)+(min1*1350))
                print("\nWe offer a lucky lottery type of discount for our customers")
                print("The program would generate a random number from 10 to 20 and if you guess it right, there would be a discount of 10% on the final amount")
                lottery=int(input("Choose a number from 10 to 20"))
                d=random.randint(10,20)
                print("The number generated by the program is:",d) 
                print("Price for one day(inc tax):",bill/4)         
                print("Price for all dyas(inc ta)",bill)
                if d==lottery:
                    discount=0.1*bill
                    bill=0.9*bill
                print("Discount:",discount)
                print("Final amount to be paid:",bill)                   
                break
        
        break

    elif ch==3:
        import tkinter as tk #using tkinter to display wayanad itinerary in the tkinter window
        root1=tk.Tk()
        root1.geometry('1500x2500')
        root1.title("Wayanad itinerary")
        root1.configure(background="grey")
        T = tk.Text(root1, height=80, width=150,bg="black",fg="white",font=("calibri", 14))
        T.place(x=0,y=0)
        quote = """ WAYANAD:

        *Overview:
        Wayanad is a fascinating place, not just for nature-lovers but also for history-buffs.
        Archeologists found traces of human civilization that have existed here for over 6000 years.
        The Edakkal caves are the glowing evidence of the claim. However, there is not much of documented history of this region before the 18th century.
        Wayanad has the largest tribal community in Kerala. Many of these tribal groups were treated as slaves by the landlords for a long time.
        The historic Bonded Labor Act of 1976 made this unconstitutional. Now, most of these tribes make a living from their skills in agriculture,
        carpentry, and craftsmanship. You can learn a lot about the tribes of Wayanad and their life in the Wayanad Heritage Museum.
        Wayanad is surrounded by the Bandipur, Nagarhole and Mudumalai forests in the east. These three together with the eastern forests of Wayanad has
        the largest tiger population in the whole world. While the whole district is covered in green,
        if you love jungle safaris you should stay towards the east near the Muthanga hills.
        The region Sultan Bathery in the interiors of Wayanad is famous for the Edakkal Caves and other heritage sites.

        *Highlights:
        -Banasura Sagara Dam
        -Chembra Peak
        -Sailing to Kuruva Island on a Bamboo Raft
        -Kalpetta tea estate
        -Phantom Rock
        -Edakkal Caves
        -Wayanad Heritage Museum
        -Soochipara Falls
        -Lakkidi viewpoint
        -Wildlife tour in Wayanad."""
        T.insert(tk.END, quote)
        tk.mainloop()
        WAY=open("Waypro.txt","r")#using file handling to import and display daywise itinerary for wayanad
        WP=WAY.read()
        print(WP)
       
        import numpy as np #using pyplot to display stats of wayanad tourism 
        import matplotlib.pyplot as pl
        x=['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
        y=[1234,1332,1232,2412,1754,1033,621,732,1842,2665,2523,1365]
        pl.xlabel("months")
        pl.ylabel("average visitors")
        pl.bar(x,y,width=0.3,color='y')
        pl.show()

        print("\nThese are the different categories avalable")

        

        print("Choose your preferred category by entering the respective serial number")
        cp=int(input("1.Basic\n2.Semi-Deluxe\n3.Deluxe\n"))
        while True:
            if cp==1:
                print("NOTE 1:Price per head is the price only for 1 day including tax")
                print("NOTE 2:Price for passengers of age below 12 will be charged only half of the original price")
                print("\nPrice per head for age 12 and above:Rs. 1800")
                print("Price per head for age below 12:Rs. 900")
                maj1=int(input("\nNumber of people aged 12 and above:"))
                min1=int(input("Number of people aged below 12:"))
                bill=4*((maj1*1800)+(min1*900))
                print("\nWe offer a lucky lottery type of discount for our customers")
                print("The program would generate a random number from 10 to 20 and if you guess it right, there would be a discount of 10% on the final amount")
                lottery=int(input("Choose a number from 10 to 20"))
                d=random.randint(10,20)
                print("The number generated by the program is:",d) 
                print("Price for one day(inc tax):",bill/4)         
                print("Price for all dyas(inc ta)",bill)
                if d==lottery:
                    discount=0.1*bill
                    bill=0.9*bill
                print("Discount:",discount)
                print("Final amount to be paid:",bill)                   
                break
            

            elif cp==2:
                print("NOTE 1:Price per head is the price only for 1 day including tax")
                print("NOTE 2:Price for passengers of age below 12 will be charged only half of the original price")
                print("\nPrice per head for age 12 and above:Rs. 2200")
                print("Price per head for age below 12:Rs. 1100")
                maj1=int(input("\nNumber of people aged 12 and above:"))
                min1=int(input("Number of people aged below 12:"))
                bill=4*((maj1*2200)+(min1*1100))
                print("\nWe offer a lucky lottery type of discount for our customers")
                print("The program would generate a random number from 10 to 20 and if you guess it right, there would be a discount of 10% on the final amount")
                lottery=int(input("Choose a number from 10 to 20"))
                d=random.randint(10,20)
                print("The number generated by the program is:",d) 
                print("Price for one day(inc tax):",bill/4)         
                print("Price for all dyas(inc ta)",bill)
                if d==lottery:
                    discount=0.1*bill
                    bill=0.9*bill
                print("Discount:",discount)
                print("Final amount to be paid:",bill)                   
                break
            

            elif cp==3: 
                print("NOTE 1:Price per head is the price only for 1 day including tax")
                print("NOTE 2:Price for passengers of age below 12 will be charged only half of the original price")
                print("\nPrice per head for age 12 and above:Rs. 2500")
                print("Price per head for age below 12:Rs. 1250")
                maj1=int(input("\nNumber of people aged 12 and above:"))
                min1=int(input("Number of people aged below 12:"))
                bill=4*((maj1*2500)+(min1*1250))
                print("\nWe offer a lucky lottery type of discount for our customers")
                print("The program would generate a random number from 10 to 20 and if you guess it right, there would be a discount of 10% on the final amount")
                lottery=int(input("Choose a number from 10 to 20"))
                d=random.randint(10,20)
                print("The number generated by the program is:",d) 
                print("Price for one day(inc tax):",bill/4)         
                print("Price for all dyas(inc ta)",bill)
                if d==lottery:
                    discount=0.1*bill
                    bill=0.9*bill
                print("Discount:",discount)
                print("Final amount to be paid:",bill)                   
                break
        
        break

    elif ch==4:
        import tkinter as tk #using tkinter to display hyderabad itinerary in the tkinter window
        root1=tk.Tk()
        root1.geometry('1500x2500')
        root1.title("Hyderabad itinerary")
        root1.configure(background="grey")
        T = tk.Text(root1, height=80, width=150,bg="black",fg="white",font=("calibri", 14))
        T.place(x=0,y=0)
        quote = """HYDERABAD:

        *Overview:
        Hyderabad is the capital of southern India's Telangana state. A major center for the technology industry,
        it's home to many upscale restaurants and shops. Its historic sites include Golconda Fort,
        a former diamond-trading center that was once the Qutb Shahi dynastic capital.
        The Charminar, a 16th-century mosque whose 4 arches support towering minarets, is an old city landmark near the long-standing Laad Bazaar.

        *Highlights:
        -Archival Museum.
        -Birla Mandir.
        -Birla Planetarium.
        -Golconda Fort.
        -Hyderabad Race Club.
        -Lumbini Park.
        -Mecca Masjid.
        -Necklace Road. """
        T.insert(tk.END, quote)
        tk.mainloop()
        HYD=open("Hydpro.txt","r")#using file handling to import and display daywise itinerary for hyderabad
        HP=HYD.read()
        print(HP)
        
        import numpy as np #using pyplot to display stats of hyderabad tourism 
        import matplotlib.pyplot as pl
        x=['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
        y=[1123,1233,1455,2434,2254,521,654,987,1876,2666,2545,1022]
        pl.xlabel("months")
        pl.ylabel("average visitors")
        pl.bar(x,y,width=0.3,color='r')
        pl.show()

        print("\nThese are the different categories avalable")
        
       

        print("Choose your preferred category by entering the respective serial number")
        cp=int(input("1.Basic\n2.Semi-Deluxe\n3.Deluxe\n"))
        while True:
            if cp==1:
                print("NOTE 1:Price per head is the price only for 1 day including tax")
                print("NOTE 2:Price for passengers of age below 12 will be charged only half of the original price")
                print("\nPrice per head for age 12 and above:Rs. 2000")
                print("Price per head for age below 12:Rs. 1000")
                maj1=int(input("\nNumber of people aged 12 and above:"))
                min1=int(input("Number of people aged below 12:"))
                bill=4*((maj1*2000)+(min1*1000))
                print("\nWe offer a lucky lottery type of discount for our customers")
                print("The program would generate a random number from 10 to 20 and if you guess it right, there would be a discount of 10% on the final amount")
                lottery=int(input("Choose a number from 10 to 20"))
                d=random.randint(10,20)
                print("The number generated by the program is:",d) 
                print("Price for one day(inc tax):",bill/4)         
                print("Price for all dyas(inc ta)",bill)
                if d==lottery:
                    discount=0.1*bill
                    bill=0.9*bill
                print("Discount:",discount)
                print("Final amount to be paid:",bill)                   
                break
            

            elif cp==2:
                print("NOTE 1:Price per head is the price only for 1 day including tax")
                print("NOTE 2:Price for passengers of age below 12 will be charged only half of the original price")
                print("\nPrice per head for age 12 and above:Rs. 2300")
                print("Price per head for age below 12:Rs. 1150")
                maj1=int(input("\nNumber of people aged 12 and above:"))
                min1=int(input("Number of people aged below 12:"))
                bill=4*((maj1*2300)+(min1*1150))
                print("\nWe offer a lucky lottery type of discount for our customers")
                print("The program would generate a random number from 10 to 20 and if you guess it right, there would be a discount of 10% on the final amount")
                lottery=int(input("Choose a number from 10 to 20"))
                d=random.randint(10,20)
                print("The number generated by the program is:",d) 
                print("Price for one day(inc tax):",bill/4)         
                print("Price for all dyas(inc ta)",bill)
                if d==lottery:
                    discount=0.1*bill
                    bill=0.9*bill
                print("Discount:",discount)
                print("Final amount to be paid:",bill)                   
                break
            

            elif cp==3: 
                print("NOTE 1:Price per head is the price only for 1 day including tax")
                print("NOTE 2:Price for passengers of age below 12 will be charged only half of the original price")
                print("\nPrice per head for age 12 and above:Rs. 2800")
                print("Price per head for age below 12:Rs. 1400")
                maj1=int(input("\nNumber of people aged 12 and above:"))
                min1=int(input("Number of people aged below 12:"))
                bill=4*((maj1*2800)+(min1*1400))
                print("\nWe offer a lucky lottery type of discount for our customers")
                print("The program would generate a random number from 10 to 20 and if you guess it right, there would be a discount of 10% on the final amount")
                lottery=int(input("Choose a number from 10 to 20"))
                d=random.randint(10,20)
                print("The number generated by the program is:",d) 
                print("Price for one day(inc tax):",bill/4)         
                print("Price for all dyas(inc ta)",bill)
                if d==lottery:
                    discount=0.1*bill
                    bill=0.9*bill
                print("Discount:",discount)
                print("Final amount to be paid:",bill)                   
                break
        
        break

    elif ch==5:
        import tkinter as tk #using tkinter to display pune itinerary in the tkinter window
        root1=tk.Tk()
        root1.geometry('1500x2500')
        root1.title("pune itinerary")
        root1.configure(background="grey")
        T = tk.Text(root1, height=80, width=150,bg="black",fg="white",font=("calibri", 14))
        T.place(x=0,y=0)
        quote = """PUNE:

        *Overview:
        Pune is a sprawling city in the western Indian state of Maharashtra. It was once the base of the Peshwas (prime ministers) of the Maratha Empire,
        which lasted from 1674 to 1818. It's known for the grand Aga Khan Palace, built in 1892 and now a memorial to Mahatma Gandhi,
        whose ashes are preserved in the garden. The 8th-century Pataleshwar Cave Temple is dedicated to the Hindu god Shiva.

        *Highlights:
        -Sinhagad Fort
        -Katraj Snake Park
        -ISKON Temple
        -Aga Khan Palace
        -Shaniwar Wada
        -Dagdusheth Halwai Temple
        -Lal Mahal
        -Pataleshwar Cave."""
        
        T.insert(tk.END, quote)
        tk.mainloop()
        
        PUNE=open("Punepro.txt","r")#using file handling to import and display daywise itinerary for pune
        PP=PUNE.read()
        print(PP)
        
        import numpy as np #using pyplot to display stats of pune tourism 
        import matplotlib.pyplot as pl
        x=['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
        y=[1623,1823,1134,1034,1145,1267,613,734,1856,2646,2556,1613]
        pl.xlabel("months")
        pl.ylabel("average visitors")
        pl.bar(x,y,width=0.3,color='g')
        pl.show()

        print("\nThese are the different categories avalable")
        
        

        print("Choose your preferred category by entering the respective serial number")
        cp=int(input("1.Basic\n2.Semi-Deluxe\n3.Deluxe\n"))
        while True:
            if cp==1:
                print("NOTE 1:Price per head is the price only for 1 day including tax")
                print("NOTE 2:Price for passengers of age below 12 will be charged only half of the original price")
                print("\nPrice per head for age 12 and above:Rs. 2400")
                print("Price per head for age below 12:Rs. 1200")
                maj1=int(input("\nNumber of people aged 12 and above:"))
                min1=int(input("Number of people aged below 12:"))
                bill=4*((maj1*2400)+(min1*1200))
                print("\nWe offer a lucky lottery type of discount for our customers")
                print("The program would generate a random number from 10 to 20 and if you guess it right, there would be a discount of 10% on the final amount")
                lottery=int(input("Choose a number from 10 to 20"))
                d=random.randint(10,20)
                print("The number generated by the program is:",d) 
                print("Price for one day(inc tax):",bill/4)         
                print("Price for all dyas(inc ta)",bill)
                if d==lottery:
                    discount=0.1*bill
                    bill=0.9*bill
                print("Discount:",discount)
                print("Final amount to be paid:",bill)                   
                break
            

            elif cp==2:
                print("NOTE 1:Price per head is the price only for 1 day including tax")
                print("NOTE 2:Price for passengers of age below 12 will be charged only half of the original price")
                print("\nPrice per head for age 12 and above:Rs. 2700")
                print("Price per head for age below 12:Rs. 1350")
                maj1=int(input("\nNumber of people aged 12 and above:"))
                min1=int(input("Number of people aged below 12:"))
                bill=4*((maj1*2700)+(min1*1350))
                print("\nWe offer a lucky lottery type of discount for our customers")
                print("The program would generate a random number from 10 to 20 and if you guess it right, there would be a discount of 10% on the final amount")
                lottery=int(input("Choose a number from 10 to 20"))
                d=random.randint(10,20)
                print("The number generated by the program is:",d) 
                print("Price for one day(inc tax):",bill/4)         
                print("Price for all dyas(inc ta)",bill)
                if d==lottery:
                    discount=0.1*bill
                    bill=0.9*bill
                print("Discount:",discount)
                print("Final amount to be paid:",bill)                   
                break
            

            elif cp==3: 
                print("NOTE 1:Price per head is the price only for 1 day including tax")
                print("NOTE 2:Price for passengers of age below 12 will be charged only half of the original price")
                print("\nPrice per head for age 12 and above:Rs. 3100")
                print("Price per head for age below 12:Rs. 1550")
                maj1=int(input("\nNumber of people aged 12 and above:"))
                min1=int(input("Number of people aged below 12:"))
                bill=4*((maj1*3100)+(min1*1550))
                print("\nWe offer a lucky lottery type of discount for our customers")
                print("The program would generate a random number from 10 to 20 and if you guess it right, there would be a discount of 10% on the final amount")
                lottery=int(input("Choose a number from 10 to 20"))
                d=random.randint(10,20)
                print("The number generated by the program is:",d) 
                print("Price for one day(inc tax):",bill/4)         
                print("Price for all dyas(inc ta)",bill)
                if d==lottery:
                    discount=0.1*bill
                    bill=0.9*bill
                print("Discount:",discount)
                print("Final amount to be paid:",bill)                   
                break
        
        break

    else:
        print("Invalid please enter the right information")


print("\nFor more details or queries, contact Mr Hemanth at 9999999999/9090909090 who would be the guide for the tour")
print("\nWould you like to confirm the booking of the tour and go ahead with the online payment integrated within our site")
pay=input("Y for yes, N for no")
def abc():  #bill payment
        
    if pay=='Y' or pay=='y':
        
        print("\nYou would be transferring the amount and the site will have access to your bank account if you have registered with your phone number in the site")
        
        while True:
            paytm=int(input("Enter the amount to be paid"))
            if paytm==bill:
                print("Your payment of Rs.",paytm,"is successful")
                break
            else:
                print("Please enter the right amount")
abc()


print("\nThank you for choosing Bluestar Tours and Travels\nHave a nice day!! \n Your tickets will be sent to your registered email shortly")
