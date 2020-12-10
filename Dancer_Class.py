
class UniversityPerson():
    def __init__(self, name, age, year_started, field):
        self.name = name
        self.age = age
        self.year_started = year_started
        self.field = field

    def tenure(self):
        time = (2020 - self.year_started)
        print (f"You've been here since {self.year_started}, that's {time} years!")
    
    def department(self):
        if self.field == "Biology":
            return "Kirkland Department"
        elif self.field == "Math":
            return "Johannsen Department"
        elif self.field == "CS":
            return "Gates Department"
        else:
            return "Sorry, we do not have a specified department!"
    

class Student(UniversityPerson):
    def __init__(self, student_id, GPA):
        self.student_id = student_id
        self.GPA = GPA
    
    def tenure(self):
        if time < 1:
            return ("Ah! A transfer student")
        
    def study_habits(self):
        if self.field == "Art":
            return ("Sounds nice and relaxing - go out and have fun! Study later!")
        else:
            return ("Sounds like a difficult curriculum, better hit the books!")

    def transfer_field(self):
        if self.fields == "Changing":
            year_started = "I have yet to begin"
            print("I don't know yet")

    def student_enrollment(self):


    class Professor(UniversityPerson):
        def __init__(self, research, TA, course_offerings):
            self.research = research
            self.TA = TA
            self.course_offerings = course_offerings

        def retirement(self):
            if ((self.age > 65), (self.year_started <= 2010), (self.research == True), (self.course_offerings > 2)):
                return ("Time to retire")
            else:
                return ("You have not done anything yet!")

        def TA_needed(self):
            if self.course_offerings <= 2:
                self.TA = 2
                print ("You need 2 TA's")
            elif self.course_offerings <= 4:
                self.TA = 4
                print ("You need 4 TA's")
            else:
                self.TA = 7
                print ("You need at least 7 TA's - maybe more!")

class Course:
    def __init__(self, course_name, max_students):
        self.course_name = course_name
        self.max_students = max_students

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def required_GPA(self, student):
        if (student.GPA) < 2.0:
            return ("You cannot enroll")
        elif (student.GPA) < 3.5:
            print("You are required to take tutoring while enrolled")
        else:
            print("You are amazing! Good Luck!")
    


J = Student("Johm", 12, 2020, "Changing")
J.tenure()