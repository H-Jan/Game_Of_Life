
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
    def __init__(self, first_name, last_name, school_email, password, id_number):
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
            if self.courses[i].assignments != []: 
            #ensure that assignments is presented
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

class Assignment:
    min = 0
    max = 100

    def __init__(self, name, due_date, description):
        self.name = name
        self.due_date = due_date
        self.description = description

    def Name(self, name):
        if name != "":
            return self.name 

    def DueDate(self, due_date):
        if due_date != "":
            return self.due_date
    
    def Description(self, description):
        if description != "":
            return self.description

class AssignmentGrades: 
    def __init__(self, course, assignment, grade, grade_percentage):
        self.course = course
        self.assignment = assignment
        self.grade = Grading(grade)
        self.grade_percentage = grade_percentage

    def Percentage(self, percentage):
        if percentage != "":
            return self.Percentage
    
class Grading:
    min = 0
    max = 100

    def __init__(self, grade):
        self.grade = grade

    def Grade(self, grade):
        while grade == "" or grade < Grading.min or grade > Grading.max:
            grade = int(input("Incorrect grade, try again"))
        self.grade = grade
        return True




print(UniversityPerson(Hani, Jandali, hanijandali@makeschool.com, LalaLAnd, 93920203))
    