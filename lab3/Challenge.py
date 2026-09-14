import subprocess, platform

def clear_screen():
    if platform.system()=="Windows":
        if platform.release() in {"10", "11"}:
            subprocess.run("", shell=True) #win 10 fix
            print("\033c", end="")
        else:
            subprocess.run(["cls"])
    else: #Linux and Mac
        print("\033c", end="")

class Flight: #A class was not used in original solution. We have several flights that need the same attributes, so using a class makes sense
    def __init__(self, flight_number, destination, departure_time, gate,
                 passengers, maximum_capacity, delay_in_minutes, cancelled_status):
        self.flight_number = flight_number
        self.destination = destination
        self.departure_time = departure_time
        self.gate = gate
        self.passengers = passengers
        self.maximum_capacity = maximum_capacity
        self.delay_in_minutes = delay_in_minutes
        self.cancelled_status = cancelled_status

flights = [ #Originally flights was a lst of dictionaries, with a class Flight this code looks much cleaner and we don't run the risk of defining different attributes for different flights
    Flight("SK100","Barcelona","10:42","C1",91,142,0,False),
    Flight("SK101","Copenhagen","05:01","A4",52,82,0,False),
    Flight("AF102","Paris","16:33","A1",100,142,5,False),
    Flight("LH103","Berlin","12:00","C1",113,142,0,False),
    Flight("BA104","London","22:01","B1",142,142,0,False),
    Flight("LH105","Zürich","18:05","B2",96,142,0,False),
    Flight("SK106","Malmö","13:57","A4",75,82,0,False),
    Flight("LH107","Hamburg","07:30","",95,142,0,False),
    Flight("SK108","Copenhagen","20:12","A3",79,82,0,False),
    Flight("LF109","Münich","17:25","A2",110,142,0,True)
]

def status(delay, cancel_Status):
    if (cancel_Status):
        return "CANCELLED"
    elif(delay == 0):
        return "ON TIME"
    elif(delay < 20):
        return "SLIGHT DELAY"
    elif(delay < 60):
        return "DELAYED"
    else:
        return "SEVERLY DELAYED"    

def show_Board(flights):
    for num, flight in enumerate(sorted(flights, key=lambda x: x.departure_time)):
        gate_string = flight.gate or "not assigned"
        print(f"{str(num+1).rjust(2)}. {flight.flight_number} - {flight.destination.ljust(10)} - " +
              f"{flight.departure_time} - Gate {(gate_string).ljust(12)} - {status(flight.delay_in_minutes, flight.cancelled_status)}")

def scheduled_flights(flights):
    return len(flights)

def cancelled_flights(flights):
    r = []
    for flight in flights:
        if flight.cancelled_status == True:
            r.append(flight)
    return r

def delayed_flights(flights):
    r = []
    for flight in flights:
        if (flight.cancelled_status == False and flight.delay_in_minutes):
            r.append(flight)
    return r

def on_time_flights(flights):
    return sum(1 for flight in flights if flight.cancelled_status == False and
               not flight.delay_in_minutes)

def total_passengers(flights):
    return sum(flight.passengers for flight in flights)

def average_passengers(flights):
    num_flights = sum(1 for flight in flights if flight.passengers)
    return round(total_passengers(flights)/num_flights)

def max_passengers_flight(flights):
    max_flight = None
    for flight in flights:
        if max_flight == None or flight.passengers > max_flight.passengers:
            max_flight = flight
    return flight

def filled_flights(flights):
    filled = []
    for flight in flights:
        if flight.passengers / flight.maximum_capacity > 0.8:
            filled.append(flight)
    return filled

#show_Board(flights)


def show_flight(flight_number, flights):
    flight = next((flight for flight in flights if flight.flight_number == flight_number), None) 
    if (flight):
        print("Destination: ", flight.destination)
        print("Departure", flight.departure_time)
        print("Gate", flight.gate)
        print("Passengers", flight.passengers)
        print("Status", status(flight.delay_in_minutes,flight.cancelled_status))
    else:
        print("Flight not found.")

def user_get_flight():
    user_flight = (input("Enter flight number: "))
    try:
        user_flight_number = int(user_flight)
        show_flight(user_flight_number, flights)
    except:
        True #Swallow exception and do nothing

#user_get_flight()

def show_gates():
    for y in range(3):
        for x in range(1, 5):
            print(f"Gate {chr(y+ord('A'))}{x}")

#how_gates()

menu = ["View all flights", "View delayed flights", "View cancelled flights",
        "Search for a flight", "View flight statistics", "Quit"]
while True:
    selected = None
    clear_screen()
    for num, menu_item in enumerate(menu):
        print (num + 1, menu_item)

    inp = input("choose option: ")
    if inp in menu:
        selected = menu.index(inp)
    else:
        try:
            num = int(inp)
            selected = num - 1
        except:
            continue #swallow exception and do nothing
    if selected != None and selected >= 0 and selected < len(menu):
        if menu[selected] == "Quit":
            break
        else:
            if menu[selected] == "View all flights":
                clear_screen()
                show_Board(flights)
                input("-continue-")
            elif menu[selected] == "View delayed flights":
                clear_screen()
                show_Board(delayed_flights(flights))
                input("-continue-")
            elif menu[selected] == "View cancelled flights":
                clear_screen()
                show_Board(cancelled_flights(flights))
                input("-continue-")
            elif menu[selected] == "Search for a flight":
                clear_screen()
                selected_flight = None                
                if(len(flights)):
                    user_get_flight()                
                input("-continue-")
            elif menu[selected] == "View flight statistics":
                clear_screen()
                print("AIRPORT OPERATIONS REPORT")
                print("")
                print("Scheduled flights: ", scheduled_flights(flights))
                print("Cancelled flights: ", len(cancelled_flights(flights)))
                print("Delayed flgiths: ", len(delayed_flights(flights)))
                print("On-time flights: ", on_time_flights(flights))
                print("")
                print("Passengers today: ", total_passengers(flights))
                print("")
                mpf = max_passengers_flight(flights)                
                print("Busiest flight:")
                print(f"{mpf.flight_number} - {mpf.destination} - {mpf.passengers} passengers")
                print("")
                print("Flights above 80% capacity:")
                for flight in filled_flights(flights):
                    print(f"{flight.flight_number} - {flight.destination}")
                print("")
                print("Average passengers: ", average_passengers(flights))
                input("-continue-")

