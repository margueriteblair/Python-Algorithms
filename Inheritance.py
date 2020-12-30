class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self, firstName, lastName, idNumber, scores):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
        self.scores = scores

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self):
        sum = 0
        for score in self.scores:
            sum += score
        average = sum/len(self.scores)
        if (average >= 90.0 & average <= 100.0):
            return ("O")
        elif (average < 90.0 & average >= 80.0):
            return("E")
        elif (average < 80.0 & average >= 70.0):
            return("A")
        elif (average >= 55.0 & average < 70.0):
            return("P")
        elif (average < 55.0 & average >= 40.0):
            return("D")
        else:
            return("T")

line = input().split()