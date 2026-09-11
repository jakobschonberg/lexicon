flights = [
    {"flight number": 100,
     "destination": "Barcelona",
     "departure time": "10:42",
     "gate": "C1",
     "passengers": 91,
     "maximum capacity": 142,
     "delay in minutes": 0,
     "cancelled status": False},
    {"flight number": 101,
     "destination": "Copenhagen",
     "departure time": "05:01",
     "gate": "A4",
     "passengers": 52,
     "maximum capacity": 82,
     "delay in minutes": 0,
     "cancelled status": False},
    {"flight number": 102,
     "destination": "Paris",
     "departure time": "16:33",
     "gate": "A1",
     "passengers": 100,
     "maximum capacity": 142,
     "delay in minutes": 5,
     "cancelled status": False},
    {"flight number": 103,
     "destination": "Berlin",
     "departure time": "12:00",
     "gate": "C1",
     "passengers": 113,
     "maximum capacity": 142,
     "delay in minutes": 0,
     "cancelled status": False},
    {"flight number": 104,
     "destination": "London",
     "departure time": "22:01",
     "gate": "B1",
     "passengers": 142,
     "maximum capacity": 142,
     "delay in minutes": 0,
     "cancelled status": False},
    {"flight number": 105,
     "destination": "Zürich",
     "departure time": "18:05",
     "gate": "B2",
     "passengers": 96,
     "maximum capacity": 142,
     "delay in minutes": 0,
     "cancelled status": False},
    {"flight number": 106,
     "destination": "Malmö",
     "departure time": "13:57",
     "gate": "A4",
     "passengers": 75,
     "maximum capacity": 82,
     "delay in minutes": 0,
     "cancelled status": False},
    {"flight number": 107,
     "destination": "Hamburg",
     "departure time": "07:30",
     "gate": "",
     "passengers": 95,
     "maximum capacity": 142,
     "delay in minutes": 0,
     "cancelled status": False},
    {"flight number": 108,
     "destination": "Copenhagen",
     "departure time": "20:12",
     "gate": "A3",
     "passengers": 79,
     "maximum capacity": 82,
     "delay in minutes": 0,
     "cancelled status": False},
    {"flight number": 109,
     "destination": "Münich",
     "departure time": "17:25",
     "gate": "A2",
     "passengers": 110,
     "maximum capacity": 142,
     "delay in minutes": 0,
     "cancelled status": True}
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
    for num, flight in enumerate(sorted(flights, key=lambda x: x["departure time"])):
        gate_string = flight["gate"] or "not assigned"
        print(f"{str(num+1).rjust(2)}. {flight["flight number"]} - {flight["destination"].ljust(10)} - " +
              f"{flight["departure time"]} - Gate {(gate_string).ljust(12)} - {status(flight["delay in minutes"], flight["cancelled status"])}")

def scheduled_flights(flights):
    return len(flights)

def cancelled_flights(flights):
    return sum(1 for flight in flights if flight["cancelled status"] == True)

def delayed_flights(flights):
    return sum(1 for flight in flights if flight["cancelled status"] == False and
               flight["delay in minutes"])

def on_time_flights(flights):
    return sum(1 for flight in flights if flight["cancelled status"] == False and
               not flight["delay in minutes"])

def total_passengers(flights):
    return sum(flight["passengers"] for flight in flights)

def average_passengers(flights):
    num_flights = sum(1 for flight in flights if flight["passengers"])
    return round(total_passengers/num_flights)

def max_passengers_flight(flights):
    max_flight = None
    for flight in flights:
        if max_flight == None or flight["passengers"] > max_flight["passengers"]:
            max_flight = flight
    return flight

def filled_flights(flights):
    filled = 0
    for flight in flights:
        if flight["passengers"] / flight["maximum capacity"] > 0.8:
            filled += 1
    return filled

show_Board(flights)
'''
print (scheduled_flights(flights))
print (cancelled_flights(flights))
print (delayed_flights(flights))
print (on_time_flights(flights))
print (average_passengers(flights))
print (max_passengers_flight(flights)["flight number"])
print (filled_flights(flights))
'''

def show_flight(flight_number, flights):
    flight = next((flight for flight in flights if flight["flight number"] == flight_number), None) 
    if (flight):
        print("Destination: ", flight["destination"])
        print("Departure", flight["departure time"])
        print("Gate", flight["gate"])
        print("Passengers", flight["passengers"])
        print("Status", status(flight["delay in minutes"],flight["cancelled status"]))
    else:
        print("Flight not found.")

user_flight = (input("Enter flight number: "))
try:
    user_flight_number = int(user_flight)
    show_flight(user_flight_number, flights)
except:
    True #Swallow exception and do nothing

def show_gates():
    for y in range(3):
        for x in range(1, 5):
            print(f"Gate {chr(y+ord('A'))}{x}")

show_gates()