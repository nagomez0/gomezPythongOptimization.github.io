#In the Airport class: include the number of origin_flights and the number of dest_flights – NOT the list of flights(code, name, city, state, number_origin_flights, number_dest_flights)

class Airport():

  #constructor: defines & initializes members - args
  #Empty lists
    def __init__(self, co, n, c, s):
        self._code = co
        self._name = n
        self._city = c
        self._state = s
        self._origin_flights = []
        self._dest_flights = []

    #Getter methods for each variable - return given var
    def get_code(self):
        return self._code
  
    def get_name(self):
        return self._name

    def get_city(self):
        return self._city
  
    def get_state(self):
        return self._state

    def get_origin_flights(self):
        return self._dest_flights

    def get_dest_flights(self):
        return self._dest_flights

  #add method - append flight param to empty list created for given var
    def add_origin_flight(self, flight):
        self._origin_flights.append(flight)
    

    def add_dest_flight(self, flight):
        self._dest_flights.append(flight)
  
  #Special Method __rep__, return as string in form of tuple including
  #Every var in this class - return str(len()) of lists
    def __repr__(self):
        return "(" + self._code + ", " + self._name + ", " + self._city + ", " + self._state + ", " + str(len(self._origin_flights)) + ", " + str(len(self._dest_flights)) + ")"