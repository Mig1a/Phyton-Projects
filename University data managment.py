# Million Aboye
# 10/30/2023
import datetime

class Person:
    currentYear = datetime.date.today().year
    personCount = 0

    def __init__(self, name, address, telephone, email):
        self.name = name
        self.address = address
        self.telephone = telephone
        self.email = email
        Person.personCount += 1
        self.g_num = f'G{str(Person.personCount).zfill(6)}'

    def __str__(self):
        return f"{self.g_num} - {self.name} - {self.address}"

    def dupePerson(self, other_person):
        if isinstance(other_person, Person) and self.name == other_person.name and self.g_num == other_person.g_num:
            return True
        else:
            return False

class Student(Person):
    totalEnrollment = 0

    def __init__(self, name, address, telephone, email, major='IST', enrolled='Y', credits=0, qpoints=0):
        super().__init__(name, address, telephone, email)
        self.major = major
        self.enrolled = enrolled.upper()
        self.credits = credits
        self.qpoints = qpoints

    def __str__(self):
        return f"{super().__str__()} - {self.major} - {self.isActive()[0]}"

    def gpa(self):
        if self.credits > 0:
            return self.qpoints / self.credits
        else:
            return 0.0

    def addGrade(self, grade, credits):
        grade_values = {'A': 4, 'B': 3, 'C': 2, 'D': 1, 'F': 0}
        if grade in grade_values and 0 <= credits <= 4:
            self.credits += credits
            self.qpoints += grade_values[grade] * credits
            return True
        else:
            return False

    def isActive(self):
        if self.enrolled == 'Y':
            return self.enrolled == 'Y','Enrolled'
        else:
            return False, 'Not Enrolled'

    def classLevel(self):
        if self.credits >= 90:
            return 'Senior'
        elif 60 <= self.credits < 90:
            return 'Junior'
        elif 30 <= self.credits < 60:
            return 'Sophomore'
        else:
            return 'Freshman'

    def dupePerson(self, other_person):
        if isinstance(other_person, Person) and self.name == other_person.name and self.g_num == other_person.g_num:
            return True
        else:
            return False
    def case_summary(self):
        print(f"{self.name} is a student at GMU, with g-number {self.g_num}\n"
        f"They are a {self.classLevel()} majoring in {self.major}\n" 
        f"Their gpa is {self.gpa()} and they are currently {self.isActive()[1]}")
    def activate(self):
        if self.enrolled == 'Y':
            return 'Student is already enrolled'
        else:
            self.enrolled = 'y'
            return True
    def deactivate(self):
        if self.enrolled == 'N':
            return 'Student was not enrolled'
        else:
            self.enrolled = 'N'
            return True
    def getStatus(self):
        if self.enrolled == 'Y':
            return 'Enrolled'
        else:
            return 'not currently enrolled'


class Faculty(Person):
    def __init__(self, name, address, telephone, email, rank, active, teach_load, speciality, yearStarted):
        super().__init__(name, address, telephone, email)
        self.rank = rank
        self.active = active
        self.teach_load = teach_load
        self.speciality = speciality
        self.yearStarted = yearStarted

    def __str__(self):
        return f"{super().__str__()} - {self.rank} - {self.speciality} - {self.tenure()}"

    def tenure(self):
        return Person.currentYear - self.yearStarted
    def case_summary(self):
        print(f"{self.name} is a faculty member at GMU with g-number {self.g_num}\n"
              f"Their rank is {self.rank} specializing in {self.speciality}\n"
              f"Their teaching load is {self.teach_load} credit hours per year")

    def activate(self):
        if self.active == 'Y':
            return 'This person is already active'
        else:
            self.active = 'y'
            return True

    def deactivate(self):
        if self.active == 'N':
            return 'This person was not active'
        else:
            self.active = 'N'
            return True

    def getStatus(self):
        if self.active == 'Y':
            return 'Active'
        else:
            return 'Not Active'


class Department:


    def __init__(self, d_code, d_name, capacity, miniGPA):
        self.d_code = d_code
        self.d_name = d_name
        self.capacity = capacity
        self.miniGPA = miniGPA
        self.avgGPA = 0
        self.directory = []

    def __str__(self):
        return f"{self.d_code} - {self.d_name} - {self.capacity} - {len(self.directory)}"

    def addStudent(self, newStu):
        qualify = self.isQualified(newStu)
        if len(self.directory) < self.capacity and qualify[0] is True:
            self.directory.append(newStu)
            self.avgGPA += newStu.gpa() / len(self.directory)
            newStu.major = self.setMajor(self.d_code)
            return True, 'Added'
        elif len(self.directory) < self.capacity and qualify[0] is False:
            return False, f'Not added because not qualified - {qualify[1]}'
        elif len(self.directory) > self.capacity and qualify[0] is True:
            return False, 'Not added because full capacity'
        else:
            return False, 'Not added because full capacity and not qualified'

    def addFaculty(self, newfaculty):
        if isinstance(newfaculty, Faculty):
            self.directory.append(newfaculty)

    def isQualified(self, checkq):
        if checkq.isActive() and checkq not in self.directory and checkq.gpa() >= self.miniGPA:
            return True, 'Qualified'
        elif not checkq.isActive():
            return False, 'Not enrolled'
        elif checkq in self.directory:
            return False, 'Duplicate'
        elif checkq.gpa() < self.miniGPA:
            return False, 'GPA too low'

    def showRoster(self, showme='b'):
        if showme == 'b':
            for all in self.directory:
                all.case_summary()
                print()
        elif showme == 's':
            for student in self.directory:
                if isinstance(student, Student):
                    student.case_summary()
                    print()
        elif showme == 'f':
            for faculty in self.directory:
                if isinstance(faculty, Faculty):
                    faculty.case_summary()
                    print()

    def setMajor(self, newMajor):
        self.major = newMajor
        return self.d_code


# Global Code starts here ---------------------------------------------------

print('\nStart of A6 test script *****************************\n')
print('\nTest 1.  Creating 6 Student objects, 3 Faculty objects, ')
print(' and one Department object - Engineering - for use in this testscript.')
print('---------------------------------------------------------------------------')
s1 = Student('David Miller', '321 Maple Lane, Vienna, VA',
             '571-285-4567', 'dmiller8@gmu.edu', major='Hist', enrolled='y',
             credits=30, qpoints=90)
s2 = Student('Bonnie Bonilla', '123 Oak Street, Potomac, MD',
             '301-285-4567', 'bbonilla@gmu.edu', major='Math', enrolled='y',
             credits=90, qpoints=315)
s3 = Student('Chris Squire', '4567 Park Lane, London, UK',
             '425-285-4567', 'csquire8@gmu.edu', major='Musc', enrolled='y',
             credits=45, qpoints=160)
s4 = Student('Tal Wilkenfeld', '423 Outback Way, Sydney, AU',
             '524-485-5674', 'twilkenfeld@AU.gov', major='Musc', enrolled='y',
             credits=75, qpoints=250)
s5 = Student('Geddy Lee', '1240 Pacific Road, Loa Angeles, CA',
             '231-44-2596', 'grahamcentralsta@gmail.com', major='CHHS', enrolled='y',
             credits=105, qpoints=320)
s6 = Student('John Entwistle', '6 Stable Way, Leeds, UK',
             '416-223-1967', 'johnwho@apple.com', major='CSci', enrolled='y',
             credits=15, qpoints=35)

f1 = Faculty('Amanda Shuman', '3062 Covington Street, Fairfax, VA',
             '571-235-2345', 'ashuman@gmu.edu', 'Assistant Professor', 'y',
             18, 'teaching', 2017)
f2 = Faculty('A. Einstein', '2741 University Blvd, Priceton, NJ',
             '212-346-3456', 'aeinstein@gmu.edu', 'Professor', 'y',
             6, 'research', 1938)

d1 = Department('ENGR', 'Engineering', 5, 3.0)
d1.addFaculty(Faculty('Alan Turing', '6 Stable Way, Bletchly Park, U.K.',
                      '9-56-4955', 'aturing@UK.gov', 'Associate Professor', 'y',
                      6, 'research', 1943))

d1.addStudent(s1)
d1.addStudent(s2)
d1.addStudent(s3)
d1.addStudent(s4)
d1.addFaculty(f1)
d1.addFaculty(f2)
d1.addStudent(s4)
d1.addStudent(s5)

print(s1)
print(s2)
print(s3)
print(s4)
print(s5)
print(f1)
print(f2)
print('Faculty #3 is Alan Turing')
print(d1)

# --------------------------------------------------------------------------------------------
input('\n\n\nTest 2.  Hit "Enter" to see Engineering Dept. Student case summaries - 5 students: ')
print('----------------------------------------------------------------------------------\n')
d1.showRoster('s')

# --------------------------------------------------------------------------------------------
input('\n\n\nTest 3.  Hit "Enter" to see Engineering Dept. All case summaries - 5 students and 3 faculty: ')
print('------------------------------------------------------------------------------\n')
d1.showRoster('b')

# --------------------------------------------------------------------------------------------
input('\n\n\nTest 4.  Hit "Enter" to deactivate  ' + s1.name + ' and ' + f2.name)
print('---------------------------------------------------------------------------\n')
print(s1.name, ' current status is ', s1.getStatus())
print(f2.name, ' current status is ', f2.getStatus())
print(s1.name, ' deactivation result: ', s1.deactivate())
print(f2.name, ' deactivation result: ', f2.deactivate())
print(s1.name, ' updated status is ', s1.getStatus())
print(f2.name, ' updated status is ', f2.getStatus())

# --------------------------------------------------------------------------------------------
input('\n\n\nTest 5.  Hit "Enter" to activate  ' + s1.name)
print('---------------------------------------------------------------------------\n')
print(s1.name, ' activation result: ', s1.activate())

print('\n\n\n***** End of A6 test **********')