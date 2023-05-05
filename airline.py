#In the Airline class: include the number of flights – NOT the list of flights(code, name, number_flights)

class Airline():

  #constructor: defines & initializes members - args
  #Emptu list
    def __init__(self, c, n):
        self._code = c
        self._name = n
        self._flights = []

    #Getter methods for each 
    def get_code(self):
        return self._code
    
    def get_name(self):
        return self._name

    def get_flights(self):
        return self._flights  

  #add method - append flight param to empty list created for given var
    def add_flight(self, flight):
        self._flights.append(flight)
    
  #Special Method __rep__, return as string in form of tuple including
  #Every var in this class - return len of lists
    def __repr__(self):
        return "(" + self._code + ", " + self._name + ", " + str(len(self._flights)) + ")"

 