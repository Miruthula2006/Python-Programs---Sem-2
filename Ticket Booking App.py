"""    def view_tickets(self,customer):
           print("******TICKET Information******")
           cus_ticket=[t for i in self.booked_tickets if ["customer_id"]==customer.cus_id]
           if not cus_ticket:
               print("No Tickets booked")
           else:
               for tick in cus_ticket:
                   print(f"Event: ticket{"event"},Quantity:ticket{"quantity"},Total cost:ticket{"totalprice"}")
if __name__=="__main__":
    booking_system = TicketBooking()
                    
book=TicketBooking()            
print("******Welcome To TICKET Booking Application******")
cus_id=input("Enter the Customer ID")
if Customer.verify_customer_id(cus_id):
    name=input("Enter your Name: ")
    phone=int(input("Enter your phone number: "))
    customer=Customer(cus_id,name,phone)
    print("******Booking Details******")
else:
    name=input("Enter your Name: ")
    phone=int(input("Enter your phone number: "))
    cus_id=gen_rand_id()
    customer=Customer(cus_id,name,phone)
    print("Your Customer ID is ",cus_id)

while True:
    print("*****Booking Info*****")
    print("\n1. View Events")
    print("\n2. Book Tickets")
    print("\n3. View My Tickets")
    print("\n4. Exit")
    choice = int(input("Enter any option to continue booking: "))
    if choice==1:
        book.view_events()
    elif choice==2:
        event_name=input("Enter any event: ")
        quantity=int(input("Enter the number of tickets: "))
        book.book_tickets(event_name,quantity,customer)
    elif choice==3:
        book.view_tickets()
    elif choice==4:
        quit()
        
"""

import random
class Customer:
    def __init__(self, cus_id, name, phone):
        self.cus_id = cus_id
        self.name = name
        self.phone = phone

    def gen_rand_id(self):
        c_id = random.randint(1000, 9999)
        return f"TICK{c_id}"

    def verify_customer_id(cus_id):
        if cus_id[:4] == "TICK" and cus_id[4:8].isdigit():
            print("Customer ID is Valid")
        else:
            print("Customer ID  is Invalid")
    
class TicketBooking:
    def __init__(self):
        self.events = {"Concert": {"price": 1500, "seats": 500},"Drama": {"price": 100, "seats": 100},"Movie": {"price": 250, "seats": 200}}
        self.booked_tickets = []

    def view_events(self):
        for event, details in self.events.items():
            print(f"{event}: {details['price']} per ticket, {details['seats']} seats available")

    def book_tickets(self, event_name, quantity, customer):
        if event_name in self.events:
            event = self.events[event_name]
            if event["seats"] >= quantity:
                totalprice = event["price"] * quantity
                event["seats"] -= quantity
                self.booked_tickets.append({"customer_id": customer.cus_id,"event": event_name,"quantity": quantity,"total_price": totalprice})
                print(f"Booked {quantity} tickets for {event_name}. Total cost: {totalprice}")
            else:
                print("Seats not available!!!")
        else:
            print("Event name is not available")

    def view_tickets(self, customer):
        print("****** TICKET Information ******")
        cus_tickets = [t for t in self.booked_tickets if t["customer_id"] == customer.cus_id]
        if not cus_tickets:
            print("No tickets booked")
        else:
            for ticket in cus_tickets:
                print(f"Event: {ticket['event']}, Quantity: {ticket['quantity']}, Total cost: {ticket['total_price']}")

if __name__ == "__main__":
    booking_system = TicketBooking()
    
    print("****** Welcome To TICKET Booking Application ******")
    cus_id = input("Enter the Customer ID: ")
    
    if Customer.verify_customer_id(cus_id):
        name = input("Enter your Name: ")
        phone = input("Enter your phone number: ")
        customer = Customer(cus_id, name, phone)
        print("****** Booking Details ******")
    else:
        name = input("Enter your Name: ")
        phone = input("Enter your phone number: ")
        customer = Customer("", name, phone)
        cus_id = customer.gen_rand_id()
        customer.cus_id = cus_id
        print("Your Customer ID is ", cus_id)

    while True:
        print("***** Booking Info *****")
        print("\n1. View Events")
        print("\n2. Book Tickets")
        print("\n3. View My Tickets")
        print("\n4. Exit")
        choice = int(input("Enter any option to continue booking: "))
        
        if choice == 1:
            booking_system.view_events()
        elif choice == 2:
            event_name = input("Enter event name: ")
            quantity = int(input("Enter the number of tickets: "))
            booking_system.book_tickets(event_name, quantity, customer)
        elif choice == 3:
            booking_system.view_tickets(customer)
        elif choice == 4:
            quit()
        else:
            print("Invalid choice. Please try again.")
      
        
        

    
