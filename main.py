
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

    def Information(self):
        print( "Your identification number is: " + self.id_number())
        print( "Your school email is: " + self.school_email ()) #Calling directly from attribute - should do something about this if
        #attribute changes
        course_list = []
        for course in self.courses:
            course_list.append(course.name)
        print("The list of your courses are: " .join(course_list))

        for i, course in enumerate(course_list):
            print("Your assignments and greades for " + course + " are: ")
            #cycling through the list of courses 
            if self.courses[i].assignments != [] #ensure that assignments is presented
                for assignment, grade in zip(self.courses[i].assignments, self.grades):
                    print(assignment.name + " - " + str(grade.grade.getGrade()))
            else: 
                print("No assignments are provided in this course")

class Courses: 
    def __init__(self, name, id_number, units, teacher): #Teacher will be attribute, professor class
        self.name = name
        self.id_number = id_number
        self.units = units
        self.teacher = teacher
        self.assignments = []

    





    