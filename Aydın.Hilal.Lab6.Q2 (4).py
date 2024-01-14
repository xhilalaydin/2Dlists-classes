# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 09:14:49 2023

@author: hilala-ug
"""
"""
Write a class called Passenger which represents a a Passenger object. Write a class
(Passenger.py) which represents this object.
a) The class will store the following attributes:
 passengerName: name of the passenger
 passengerSurname: surname of the passenger
 seatNo: seat number of the passenger in the plane
 fare: ticket price
a) Your class should have an init() method that takes the values of all four
attributes as parameters. The default value for fare is 1000 if not given.
b) In addition, the class will have the following methods:
● get methods for the name, surname and seat number of the passenger.
● set method for updating the seatNo with the new seat number.
● calculateFare: if the fare of the Passenger object is less than 1000 TL,
then the function returns the fare increased by 5%, else the method
returns the normal fare amount.
c) In addition to the above methods, your class should define the following special
methods:
● __str__ method which returns a string as follows:
Passenger Name: John Guttag Seat: 9F
● __repr__ method which returns a string as follows:
(Pearson D. 9F 1000TL)
"""

class Passenger(object):
    def __init__(self,name , surname ,no , price=1000):
        self.__passengerName = name
        self.__passengerSurname = surname
        self.__seatNo = no
        self.__fare = float(price)
        
    def calculateFare(self, price):
        if price < 1000:
            price= price*1.05
            return price
        else:
            return price
        
    def getName(self):
        return self.__passengerName
    
    def getSurname(self):
        return self.__passengerSurname
    
    def getFare(self):
        return self.__fare
        
    
    def getNo(self):
        return self.__seatNo
    
    def setSeatno(self, no):
        self.__seatNo = no
    
    def setFare(self,fare):
        self.__fare = fare
        
    def __str__(self):
        return "Passenger Name:"+self.__passengerName+' '+self.__passengerSurname+" Seat: "+str(self.__seatNo)
    
    def __repr__(self):
        return "("+self.__passengerSurname+' '+f'{self.__passengerName:.1s}.'+' '+str(self.__seatNo)+' '+ f'{self.__fare}TL'+")"+"\n"
    
"""  
f1 = Passenger('Jane',' Doe','555-1234',2015)
f2 = Passenger('Carl',' Marx','975',800)

passenger_list=[f1,f2]

print(passenger_list)
"""
"""
Create an application that does the following:
a. Write a function load_passengers which reads passenger info from
passengers.txt and creates and returns a list of passenger objects.
b. Input name and surname of a passenger and if he/she exits in the list, input new
fare and update his/her fare with the new fare. If passenger does not exist, give a
message as in the sample run.
b. Display the list of all passengers.
Sample Run 1:
Enter name: Ruya
Enter surname: Yilmaz
Enter new price: 1220
Passenger Name: Yilmaz Ruya Seat: 08D
UPDATED
Passenger List:
[(Ozer A. 14A 1500TL)
, (Yuksel A. 15C 525.0TL)
, (Kose Tas E. 09B 1100TL)
, (Yalcin M. 04C 3100TL)
, (Aksoy Z. 18D 1500TL)
, (Turan F. 11A 1500TL)
, (Sen U. A02 913.5TL)
, (Yilmaz R. 08D 1220TL)
, (Ates O. 21F 4600TL)
, (Keskin A. 20F 2280TL)
, (Tas O. 04C 829.5TL)
, (Aktas S. 15C 3200TL)
, (Yildiz Y. 01C 8100TL)
, (Demir M. 15D 2500TL)
, (Ozdemir Å. 22B 367.5TL)
, (Ozturk A. 215 1950TL)
, (Cakir B. 21C 4150TL)
, (Polat M. 07C 1800TL)
, (Gunes F. 16F 1850TL)
, (Yuksel F. 02D 2670TL)
]
Sample Run 2:
Enter name: Elif
Enter surname: Sonmez
Passenger is NOT Found!,

"""
objects=[]
def load_passengers():
    file = open("passengers.txt","r")
    for line in file:
        data = line.strip().split(";")
       # data= line.split('\n')
        name,surname,fare,no= data[0],data[1],float(data[2]),data[3]
        objects.append(Passenger(name,surname,no,fare))
    file.close()
    return objects

a = load_passengers()

name = input("Enter name: ")
surname = input("Enter Surname: ")

booly= False
    


for passenger in objects:
    passenger.setFare(passenger.calculateFare(passenger.getFare()))
    if name==passenger.getName() and surname== passenger.getSurname():
        booly = True
        passenger1 = passenger
       
 
if booly==True:
    new_fare = float(input("Enter new price: "))
    passenger1.setFare(new_fare)
    for passenger in objects:
        passenger.setFare(passenger.calculateFare(passenger.getFare()))
    print(passenger1.__str__())
    print("UPDATED")
else:
    print("Passenger is NOT Found!")       


print("Passenger List:")
print(a)









    

