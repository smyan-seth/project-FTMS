import random
import csv
flight1=[20,20]
flight2=[20,20]
flight3=[20,20]
flight4=[20,20]
flight5=[20,20]
tic_list=[]
passen={}
class passenger:
    def info(self):
        Name=input(" Please Enter Your Name: ")
        self.name=Name
        passport_number=int(input(" Please Enter Your Passport Number: "))
        self.pass_number=passport_number
        gender=input(" Enter Your Gender(Male/Female/OTHER): ")
        self.sex=gender
        Age=int(input(" Enter Your Age: "))
        self.age=Age
        phone_number=int(input(" Enter Your Phone Number: "))
        if phone_number>10 and phone_number<10:
                print(" Enter a valid Number")
                phone_number=int(input(" Enter Your Phone Number: "))
        else:
            self.cell_number=phone_number
        email=str(input(" Enter your Email id: "))
        self.email=email

        
    def print_details(self):
        print("\n********* PASSENGER DETAILS **************")
        print("Passenger Name = ",self.name)
        print("Passport Number = ",self.pass_number)
        print("Cell Number = ",self.cell_number)
        print("Email Id = ",self.email)
        print("Age = ",self.age)
        print("Gender = ",self.sex)
        
# Initialize CSV file headers
with open('tickets.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Ticket Number", "Passenger Name", "Passport Number", "Gender", "Age", "Cell Number","Email","Seat Number"])
def reserve_seat():
    print("\n                             SEAT RESERVATION                                        ")
    seat_no=available_flights()
    ticket=random.randrange(100000,900000)
    passen[ticket]=passenger()
    passen[ticket].info()
    passen[ticket].print_details()
    print("Ticket Number = ",ticket)
    print("Seat Number = ",seat_no)
    print("\n****Ticket Booked Successfully***")
    
    # Write to CSV file
    with open('tickets.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([ticket, passen[ticket].name, passen[ticket].pass_number, passen[ticket].sex, passen[ticket].age, passen[ticket].cell_number,passen[ticket].email, seat_no])
    
    # Print to interpreter
    print("\nTicket Details:")
    print("Ticket Number:", ticket)
    print("Passenger Name:", passen[ticket].name)
    print("Passport Number:", passen[ticket].pass_number)
    print("Gender:", passen[ticket].sex)
    print("Age:", passen[ticket].age)
    print("Cell Number:", passen[ticket].cell_number)
    
    print("Email:",passen[ticket].email)
    print("Seat Number:", seat_no)
    
    tic_list.append(ticket)
    con=input("\nDo You Want To Enter Again(Y/N)? ")
    if(con=='Y' or con=='y'):
        reserve_seat()


def available_flights():
    print("************************************************************************************")
    print("                                 AVAILABLE FLIGHTS                                  ")
    print("************************************************************************************")
    print(" Serial Number   Flight Number    From       Destination      Time      Cost    ")
    print("     1              IND-108      Mumbai        Rome         11:00PM     100$    ")
    print("     2              IND-320     Hyderabad      Dubai        01:00AM     250$    ")
    print("     3              IND-170       Delhi        Tokyo        03:00AM     150$    ")
    print("     4              IND-102      Chennai       Paris        02:00AM     500$    ")
    print("     5              IND-101      Kolkata      New York      09:00AM     400$    ")
    s=int(input(" \nEnter the Serial number of flight in which you want to travel : "))
    print("\n")
    if(s==1):
          print(" Serial Number   Flight Number    From       Destination      Time      Cost    ")
          print("     1              IND-108      Mumbai        Rome         11:00PM     100$    ")
          print("\n")
          print(" 1. Business Class ")
          print("    Available Seats:",flight1[0])
          print("\n")
          print(" 2. Economic Class ")
          print("    Available seats:",flight1[1])
          print("\n")
          seat_type=int(input("Enter Type of seat you want: "))
          if(seat_type==1):
              if(flight1[0]!=0):
                  seat_number=flight1[0]
                  flight1[0]=flight1[0]-1
                  return seat_number
              else:
                  print("\n")
                  print("All seats are reserved in this class ")
                  available_flights()
          else:
              if(flight1[1]!=0):
                  seat_number=flight1[1]
                  flight1[1]=flight1[1]-1
                  return seat_number
              else:
                  print("\n")
                  print("All seats are reserved in this class ")
                  available_flights()
    elif(s==2):
          print(" Serial Number   Flight Number    From       Destination      Time      Cost    ")
          print("     2              IND-320     Hyderabad      Dubai        01:00AM     250$    ")
          print("\n")
          print(" 1. Business Class ")
          print("    Available Seats:",flight2[0])
          print("\n")
          print(" 2. Economic Class ")
          print("    Available Seats:",flight2[1])
          print("\n")
          seat_type=int(input("Enter Type of seat you want: "))
          if(seat_type==1):
              if(flight2[0]!=0):
                  seat_number=flight2[0]
                  flight2[0]=flight2[0]-1
                  return seat_number
              else:
                  print("\n")
                  print("All seats are reserved in this class ")
                  available_flights()
          else:
              if(flight2[1]!=0):
                  seat_number=flight2[1]
                  flight2[1]=flight2[1]-1
                  return seat_number
              else:
                  print("\n")
                  print("All seats are reserved in this class ")
                  available_flights()
    elif(s==3):
          print(" Serial Number   Flight Number    From       Destination      Time      Cost    ")
          print("     3              IND-170       Delhi        Tokyo        03:00AM     150$    ")
          print("\n")
          print(" 1. Business Class ")
          print("    Available Seats:",flight3[0])
          print("\n")
          print(" 2. Economic Class ")
          print("    Available Seats:",flight3[1])
          print("\n")
          seat_type=int(input("Enter Type of seat you want: "))
          if(seat_type==1):
              if(flight3[0]!=0):
                  seat_number=flight3[0]
                  flight3[0]=flight3[0]-1
                  return seat_number
              else:
                  print("\n")
                  print("All seats are reserved in this class ")
                  available_flights()
          else:
              if(flight3[1]!=0):
                  seat_number=flight3[1]
                  flight3[1]=flight3[1]-1
                  return seat_number
              else:
                  print("All seats are reserved in this class ")
                  available_flights()
    elif(s==4):
          print(" Serial Number   Flight Number    From       Destination      Time      Cost    ")
          print("     4              IND-102      Chennai       Paris        02:00AM     500$    ")
          print("\n")
          print(" 1. Business Class ")
          print("    Available Seats:",flight4[0])
          print("\n")
          print(" 2. Economic Class ")
          print("    Available Seats:",flight4[1])
          print("\n")
          seat_type=int(input("Enter Type of seat you want: "))
          if(seat_type==1):
              if(flight4[0]!=0):
                  seat_number=flight4[0]
                  flight4[0]=flight4[0]-1
                  return seat_number
              else:
                  print("\n")
                  print("All seats are reserved in this class ")
                  available_flights()
          else:
              if(flight4[1]!=0):
                  seat_number=flight4[1]
                  flight4[1]=flight4[1]-1
                  return seat_number
              else:
                  print("\n")
                  print("All seats are reserved in this class ")
                  available_flights()
    elif(s==5):
          print(" Serial Number   Flight Number    From       Destination      Time      Cost    ")
          print("     5              IND-101      Kolkata      New York      09:00AM     400$    ")
          print("\n")
          print(" 1. Business Class ")
          print("    Available Seats:",flight5[0])
          print("\n")
          print(" 2. Economic Class ")
          print("    Available Seats:",flight5[1])
          print("\n")
          seat_type=int(input("Enter Type of seat you want: "))
          if(seat_type==1):
              if(flight5[0]!=0):
                  seat_number=flight5[0]
                  flight5[0]=flight5[0]-1
                  return seat_number
              else:
                  print("\n")
                  print("All seats are reserved in this class ")
                  available_flights()
          else:
              if(flight5[1]!=0):
                  seat_number=flight5[1]
                  flight5[1]=flight5[1]-1
                  return seat_number
              else:
                  print("\n")
                  print("All seats are reserved in this class ")
                  available_flights()
    
def Flights_Available():
    print("************************************************************************************")
    print("                                 AVAILABLE FLIGHTS                                  ")
    print("************************************************************************************")
    print(" Serial Number   Flight Number    From       Destination      Time      Cost    ")
    print("     1              IND-108      Mumbai        Rome         11:00PM     100$    ")
    print("     2              IND-320     Hyderabad      Dubai        01:00AM     250$    ")
    print("     3              IND-170       Delhi        Tokyo        03:00AM     150$    ")
    print("     4              IND-102      Chennai       Paris        02:00AM     500$    ")
    print("     5              IND-101      Kolkata      New York      09:00AM     400$    ")
    
def cancel_seat():
    check_ticket=int(input("\nEnter your Ticket number: "))
    if check_ticket in tic_list:
        passen[check_ticket].print_details()
        flight_number=int(input("Enter Your Flight Number: "))
        clas_s=int(input("1. Business Class \n2. Economic Class\n"))
        if(flight_number==1):
            if clas_s==1:
                flight1[0]+=1
                print("\n")
                print("****Cancelled Successfully****")
            elif clas_s==2:
                flight1[1]+=1
                print("\n")
                print("****Cancelled Successfully****")
            else:
                print("Enter correct option")
        elif(flight_number==2):
            if clas_s==1:
                flight2[0]+=1
                print("\n")
                print("****Cancelled Successfully****")
            elif clas_s==2:
                flight2[1]+=1
                print("\n")
                print("****Cancelled Successfully****")
            else:
                print("Enter correct option")
        elif(flight_number==3):
            if clas_s==1:
                flight3[0]+=1
                print("\n")
                print("****Cancelled Successfully****")
            elif clas_s==2:
                flight3[1]+=1
                print("\n")
                print("****Cancelled Successfully****")
            else:
                print("Enter correct option")
        elif(flight_number==4):
            if clas_s==1:
                flight4[0]+=1
                print("\n")
                print("****Cancelled Successfully****")
            elif clas_s==2:
                flight4[1]+=1
                print("\n")
                print("****Cancelled Successfully****")
            else:
                print("Enter correct option")
        elif(flight_number==5):
            if clas_s==1:
                flight5[0]+=1
                print("\n")
                print("****Cancelled Successfully****")
            elif clas_s==2:
                flight5[1]+=1
                print("\n")
                print("****Cancelled Successfully****")
            else:
                print("Enter correct option")
    else:
        print("Invalid ticket number ")
def quit_program():
    print("\n")
    print("                                                             Thank You")
    print("                                              Good Bye from Airways Reservation System")

print("\n\n")   
print("                                                  WELCOME TO AIRWAYS RESERVATION SYSTEM                 ")
req=True
whilereq==True:
    print("\n")
    print("WHAT WOULD YOU LIKE TO DO? ")
    print(" 1) Reserve Seats ")
    print(" 2) Flights Available" )
    print(" 3) Cancel Seat ")
    print(" 4) Quit Program ")
    ch=int(input(" Enter Your Choice: "))
    if(ch==1):
        reserve_seat()
    elif(ch==2):
        Flights_Available()
    elif(ch==3):
        cancel_seat()
    elif(ch==4):
        quit_program() 
        req=False
