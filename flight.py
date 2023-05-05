#In the Flight class, include the code for the airline and origin/destination airports(date, airline_code, flight_num, origin_airport_code, dest_airport_code,   scheduled_departure, departure_time, departure_delay, scheduled_arrival, arrival_time, arrival_delay)

class Flight:

  #constructor: defines & initializes members - args
    def __init__(self, y, m, d, al, fn, oa, da, sd, dt, dd, sa, at, ad):
        self._date = format(y, '0004') + '-' + format(m, '02') + '-' + format(d, '02')
        self._year = y
        self._month = m
        self._day = d
        self._airline = al
        self._flight_num = fn
        self._origin_airport = oa
        self._dest_airport = da
        self._scheduled_departure = sd
        self._departure_time = dt
        self._departure_delay = dd
        self._scheduled_arrival = sa
        self._arrival_time = at
        self._arrival_delay = ad

    #Getter methods for each variable
    def get_date(self):
      return self._date

    def get_year(self):
      return self._year
    
    def get_month(self):
      return self._month

    def get_day(self):
      return self._day
    
    def get_airline(self):
      return self._airline
    
    def get_flight_num(self):
      return self._flight_num

    def get_origin_airport(self):
      return self._origin_airport
    
    def get_dest_airport(self):
      return self._dest_airport

    def get_scheduled_departure(self):
      return self._scheduled_departure

    def get_departure_time(self):
      return self._departure_time
    
    def get_departure_delay(self):
      return self._departure_delay

    def get_scheduled_arrival(self):
      return self._scheduled_arrival

    def get_arrival_time(self):
      return self._arrival_time

    def get_arrival_delay(self):
      return self._arrival_delay

  #Special Method __rep__, return as string in form of tuple including
  #Every var in this class - return str(len()) of lists
  #obj.class_method(param) for other class ref
    def __repr__(self):
        return "(" + self._date + ", " + self._airline.get_code() + ", " + str(self._flight_num)+ ", " + self._origin_airport.get_code() + ", " + self._dest_airport.get_code() + ", " + str(self._scheduled_departure) + ", " + str(self._departure_time) + ", " + str(self._departure_delay) + ", " + str(self._scheduled_arrival) + ", " + str(self._arrival_time) + ", " + str(self._arrival_delay) + ")"         