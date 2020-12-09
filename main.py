
#New Program Take 3

#SuperClass / Parent Class
class UniversityPerson:
    def __init__(self, first_name, last_name, school_email, password, id_number):
        self.first_name = first_name
        self.last_name = last_name
        self.school_email = school_email
        self.password = password
        self.id_number = id_number

    #These are done to ensure that there are no uneccessary spaces
    def FirstName(self, first_name):
        if first_name != "":
            return self.first_name
        
    def LastName(self, last_name):
        if last_name != "":
            return self.last_name

    def SchoolEmail(self, school_email):
        if school_email != "":
            return self.school_email
    
    def Password(self, password):
        if password != "":
            return self.password
    
    def Identification(self, id_number):
        if id_number != "":
            return self.id_number

#Child Class for Professors, will inherit the Super Class of the Parent
class Professor(UniversityPerson):
    def __init__(self, first_name, last_name, school_email, password, id_number)
        super().__init__(first_name, last_name, school_email, password, id_number)
        #Inheriting from the super class these attributes into the Professor Class 
        self.courses = []

    def AddCourse(self):
        return self.courses
        #Courses is a list to ensure that addition of multiple courses can be passed through easily

#child class for Students inheriting from super class of University
class Student(UniversityPerson):
    def __init__(self, first_name, last_name, school_email, password, id_number):
        super().__init__(first_name, last_name, school_email, password, id_number)
        self.courses = []
        self.grades = []

    