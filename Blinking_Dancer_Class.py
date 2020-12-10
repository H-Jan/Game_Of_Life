

class UniversityPerson():
    def __init__(self, name, age, year_started, field):
        self.name = name
        self.age = age
        self.year_started = year_started
        self.field = field
    
    def generalYear(self):
        if ((2020 - self.year_started) <= 1):
            return ("You are a freshman")
        elif ((2020 - self.year_started) <=2):
            return ("You are a sophomore")
        elif ((2020 - self.year_started) <=3):
            return ("You are a junior")
        elif ((2020 - self.year_started) <=4):
            return ("You are a senior")
        else:
            return ("You are likely a senior")

    def tenure(self):
        time = (2020 - self.year_started)
        print (f"You've been here since {self.year_started}, that's {time} years!")
    
    def department(self):
        if self.field == "Biology":
            return ("Kirkland Department")
        elif self.field == "Math":
            return ("Johannsen Department")
        elif self.field == "History":
            return ("Gates Department")
        else:
            return ("Sorry, we do not have your specified department!")
    

class MakeSchoolStudent(UniversityPerson):
    #Inheritance of SuperClass
    def __init__(self, name, age, year_started, field, scholarships, GPA):
        super().__init__(name, age, year_started, field)
        self.GPA = GPA
        self.scholarships = scholarships

    #Method Overrides
    def generalYear(self):
        if ((2020 - self.year_started) <= 1):
            return ("You are a junior")
        else:
            return ("You are a senior")
    
    #Method Overrides
    def department(self):
        if self.field == "DS":
            return ("Your Department is Data Science")
        elif self.field == "MOB":
            return ("Your Department is Mobile Development")
        elif self.field == "FEW":
            return ("Front End Web? Really? Good Luck")
        elif self.field == "BEW":
            return ("That is Back End Web Development")
        else:
            return ("That department is not offered here")
        
    def studyhelp(self):
        if self.GPA <= 3.5:
            return ("You should be attending CoWork")
        else:
            return ("You are on track, but CoWork never hurts")

    
    def financialaid(self):
        if (self.scholarships == "No"):
            return ("You are paying a hefty price for school")
        else:
            return ("Thats good! Perhaps we can find you more scholarships!")

class TAs:
    def __init__(self, timing, academic_standing):
        self.timing = timing
        self.academic_standing = academic_standing

    def Timing(self):
        if (self.timing > 1):
            return ("Congratulations, you are partially eligible to TA")
        else:
            return ("You can't TA just yet")
    
    def Academics(self):
        if self.academic_standing == "Good":
            return ("Congratulations, you are eligible to TA")
        else:
            return ("Improve your grades before you TA")

#Composition
class NewCourses:
    def __init__(self, future_year, have_professor, timing, academic_standing):
        self.future_year = future_year
        self.have_professor = have_professor
        self.object_TAs = TAs(timing, academic_standing)
    
    def NewClass(self):
        if ((self.future_year > 2020) and (self.have_professor == "Yes")):
            return ("This can possibly be a course provided in the future")
        else:
            return("There is still more to process")

    def HaveTA(self):
        self.object_TAs.Timing() and self.object_TAs.Academics()

#Composition 

class MakeSchoolProfessor(UniversityPerson):
    def __init__(self, name, age, year_started, field, years_experienced, research, timing, academic_standing):
        super().__init__(name, age, year_started, field)
        self.years_experienced = years_experienced
        self.research = research
        self.obj_TAs = TAs(timing, academic_standing)

    def professorHaveTA(self):
        return self.obj_TAs.Timing
        return self.obj_TAs.Academics

    def retirement(self):
        if ((self.age > 65), (self.year_started <= 2010), (self.research == "Yes"), (self.years_experienced >= 35)):
            return ("You have accomplished quite a time here, you can retire")
        else:
            return ("You still have much to do before you can relax!")
    
    def salary(self):
        if (self.years_experienced > 20):
            return "You are a professional, your salary is 1 million dollars"
        else:
            return "Your current salary is $10, get better!"


Test1 = UniversityPerson("Hani", 12, 2019, "Datascience")
print(Test1.tenure())
print(Test1.department())
print(Test1.generalYear())

Test2 = MakeSchoolStudent("Hane", 22, 2020, "DS", "No", 2.2)
print(Test2.department())
print(Test2.studyhelp())
print(Test2.financialaid())

Test3 = TAs(2, "Good")
print(Test3.Timing())
print(Test3.Academics())

Test5 = NewCourses(2022, "Yes", 2, "Good")
print(Test5.HaveTA())

Test4 = MakeSchoolProfessor("Johan", 48, 2010, "BEW", 35, "Yes", 1, "Yes")
print(Test4.retirement())
print(Test4.salary())
