# NIYONSHUTI Florence 
# reg no: 223011216
# ASSIGNMENT OF DATA STRUCTURE AND ALGORITHM
# Q78.conferance room booking system :stack for undoing room reservations ,queue for processing room booking requests ,and list 
# for available room

from collections import deque

# Global variables to manage the booking system
available_rooms = ["Room A", "Room B", "Room C"]
booking_requests = deque()
undo_stack = []
current_bookings = {}

def book_room(room, user):
    global available_rooms, current_bookings, undo_stack
    if room in available_rooms:
        available_rooms.remove(room)
        current_bookings[room] = user
        undo_stack.append((room, user))  
        print(f"Room '{room}' booked for {user}.")
    else:
        print(f"Room '{room}' is not available.")

def undo_last_booking():
    global available_rooms, current_bookings, undo_stack
    if undo_stack:
        room, user = undo_stack.pop()
        available_rooms.append(room)  
        del current_bookings[room]  
        print(f"Booking for room '{room}' by {user} has been undone.")
    else:
        print("No bookings to undo.")

def process_booking_request():
    if booking_requests:
        room, user = booking_requests.popleft()  # Get the next request
        book_room(room, user)
    else:
        print("No booking requests to process.")

def add_booking_request(room, user):
    booking_requests.append((room, user))
    print(f"Booking request for room '{room}' by {user} added.")

def show_available_rooms():
    print("Available rooms:", available_rooms)

def show_current_bookings():
    print("Current bookings:", current_bookings)

# Example usage
if __name__ == "__main__":
    show_available_rooms()

    add_booking_request("Room A", "ANITHA")
    add_booking_request("Room B", "ange")
    process_booking_request()   
    process_booking_request()   

show_current_bookings()
show_available_rooms()
undo_last_booking() 
show_current_bookings()
show_available_rooms()
