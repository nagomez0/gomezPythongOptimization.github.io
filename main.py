import airline, airport, flight, csv
airline_dict = {}
airport_dict = {}
date_dict = {}

#Process CSV File
#use dictionary reader to read file by row
with open('flights_info.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:

        #airline_dict - if not already in - populate with value Airline code & name
        if row['AIRLINE'] not in airline_dict:
            airline_dict[row['AIRLINE']] = airline.Airline(row['AIRLINE'], row['AIRLINE_NAME'])

        #airport_dict - if not already in - create object, key ORIGIN_AIRPORT with values of Origin: airport, name, city, state
        #Second if statement does the same as Origin but with DESTINATION_AIRPORT key with values of Destination: airport, name, city, state
        if row['ORIGIN_AIRPORT'] not in airport_dict:
            airport_dict[row['ORIGIN_AIRPORT']] = airport.Airport(row['ORIGIN_AIRPORT'], row['ORIGIN_NAME'], row['ORIGIN_CITY'], row['ORIGIN_STATE'])
        if row['DESTINATION_AIRPORT'] not in airport_dict:
            airport_dict[row['DESTINATION_AIRPORT']] = airport.Airport(row['DESTINATION_AIRPORT'], row['DESTINATION_NAME'], row['DESTINATION_CITY'], row['DESTINATION_STATE'])

        #object fl - parameters(var of flight class)
        fl = flight.Flight(int(row['YEAR']), int(row['MONTH']), int(row['DAY']), airline_dict[row['AIRLINE']], int(row['FLIGHT_NUMBER']), airport_dict[row['ORIGIN_AIRPORT']], airport_dict[row['DESTINATION_AIRPORT']], int(row['SCHEDULED_DEPARTURE']), int(row['DEPARTURE_TIME']), int(row['DEPARTURE_DELAY']), int(row['SCHEDULED_ARRIVAL']), int(row['ARRIVAL_TIME']), int(row['ARRIVAL_DELAY']))
        
        d = fl.get_date()

        #date_dict - if not in dict, get_data into empty list
        #append fl object to date_dict list - to airport & airline dict add fl param to row referances 
        if fl.get_date() not in date_dict:
            date_dict[fl.get_date()] = []
        date_dict[fl.get_date()].append(fl)
        airline_dict[row['AIRLINE']].add_flight(fl)
        airport_dict[row['ORIGIN_AIRPORT']].add_origin_flight(fl)
        airport_dict[row['DESTINATION_AIRPORT']].add_dest_flight(fl)


#Queries
#list comprehension and max (sort list)
#Query  1:  For  each  date  in  chronological  order,  which  flight  on  that  day  had  the  longest  arrivaldelay? Include duplicates, if any. 
def query1():
    #Process Query 1 here
    arrivalDelay = [d for d in date_dict]
    for d in arrivalDelay:
        arrivalDelay = [date_dict[d]]
        max(arrivalDelay, key=lambda d: d)
        sorted(arrivalDelay, key = lambda d: d[:-1])

        print(str(d)+':' + '\n' + str(arrivalDelay)+'\n')   

#use list comprehension
#Query 2: For each airport, find the  number  of  origin  flights with departure delays more than 15 minutes and the number of destination flights with arrival delays more than 15 minutes.
def query2():
    #Process Query 2 here
    delays = [a for a in airport_dict]
    for a in delays:
        delays = [airport_dict]

        if a in delays >= 15:
            a = a + delays

    print(delays)

#For  each  airline in alphabetical  order,  determine  the  number  of  flights  per  day  in chronological order from (origin, dest),  ordered by (origin, dest), with percentage of on-time flights for that day which were within 15 minutes of their scheduled time. 
def query3():
    #Process Query 3 here
    scheduled = [f for f in airline_dict]
    for f in airline_dict: 
        scheduled = [airline_dict]
        sorted(scheduled, key=lambda f: f)

        if f in scheduled <= 15:
            f+=f
            eq = (f / scheduled * 100)
            scheduled.append(eq)

    print(scheduled)

#Input Output Testing - DO NOT MODIFY ANYTHING BELOW THIS LINE
testcase = input()
print(testcase)
if testcase == 'testcase 1':
    #Tests classes are created correctly
    airport1 = airport.Airport('PHX','Phoenix Sky Harbor International Airport','Phoenix','AZ')
    airport2 = airport.Airport('LAS','McCarran International Airport','Las Vegas','NV')
    airline1 = airline.Airline('WN','Southwest Airlines Co.')
    flight1 = flight.Flight(2021,2,16,airline1,'240',airport1, airport2, 1230,1235,5,215,225,10)
    airport1.add_origin_flight(flight1)
    airport2.add_dest_flight(flight1)
    airline1.add_flight(flight1)
    #Repr Functions
    print(airport1, airport2, airline1, flight1, sep='\n')
    #Airline Getter Functions
    print(airline1.get_code(), airline1.get_name(),airline1.get_flights())
    #Airport Getter Functions
    print(airport1.get_code(), airport1.get_name(), airport1.get_city(), airport1.get_state(), airport1.get_origin_flights(), airport1.get_dest_flights())
    #Flight Getter Functions
    print(flight1.get_date(),flight1.get_year(),flight1.get_month(),flight1.get_day(),flight1.get_airline(),flight1.get_flight_num(),flight1.get_origin_airport(),flight1.get_dest_airport(),flight1.get_scheduled_departure(),flight1.get_departure_time(),flight1.get_departure_delay(),flight1.get_scheduled_arrival(),flight1.get_arrival_time(),flight1.get_arrival_delay())
elif testcase == 'testcase 2':
    print(airline_dict)
    print(airport_dict)
    print(date_dict['2015-01-10'])
    if (len(set([f.get_airline() for d in date_dict.keys() for f in date_dict[d]]))) != 3:
        print("DUPLICATE AIRLINE OBJECTS")
    if (len(set([f.get_origin_airport() for d in date_dict.keys() for f in date_dict[d]]))) != 6:
        print("DUPLICATE AIRPORT OBJECTS: origin")
    if (len(set([f.get_dest_airport() for d in date_dict.keys() for f in date_dict[d]]))) != 6:
        print("DUPLICATE AIRPORT OBJECTS: destination")
elif testcase == 'testcase 3':
    query1()
elif testcase == 'testcase 4':
    query2()
elif testcase == 'testcase 5':
    query3()