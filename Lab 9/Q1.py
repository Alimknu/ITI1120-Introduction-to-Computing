class student:
    def __init__(self, firstname, lastname, labs, a1, a2, a3, a4, a5, termtest, midterm, final):
        self.firstname = firstname
        self.lastname = lastname
        
        self.labs = 10*(float(labs)/10)
        self.a1 = 5*(float(a1)/30)
        self.a2 = 5*(float(a2)/30)
        self.a3 = 5*(float(a3)/30)
        self.a4 = 5*(float(a4)/30)
        self.a5 = 5*(float(a5)/30)
        self.termtest = 15*(float(termtest)/15)
        self.midterm = 20*(float(midterm)/20)
        self.final = 30*(float(final)/30)

    def calcGrade(self):
        total = self.labs + self.a1 + self.a2 + self.a3 + self.a4 + self.a5 + self.termtest + self.midterm + self.final

        if total >= 90:
            finalGrade = "A+"
        elif total < 90 and total >= 85:
            finalGrade = "A"
        elif total < 85 and total >= 80:
            finalGrade = "A-"
        elif total < 80 and total >= 75:
            finalGrade = "B+"
        elif total < 75 and total >= 70:
            finalGrade = "B"
        elif total < 70 and total >= 65:
            finalGrade = "C+"
        elif total < 65 and total >= 60:
            finalGrade = "C"
        elif total < 60 and total >= 55:
            finalGrade = "D+"
        elif total < 55 and total >= 50:
            finalGrade = "D"
        elif total < 50 and total >= 40:
            finalGrade = "E"
        else:
            finalGrade = "F"

        self.finalMark = total
        self.finalGrade = finalGrade

    def print(self):
        self.calcGrade()
        print("Firstname: " + str(self.firstname))
        print("Lastname: " + str(self.lastname))
        print("Lab mark: " + str(self.labs) + "%")
        print("Assignment 1: " + str(self.a1) + "%")
        print("Assignment 2: " + str(self.a2) + "%")
        print("Assignment 3: " + str(self.a3) + "%")
        print("Assignment 4: " + str(self.a4) + "%")
        print("Assignment 5: " + str(self.a5) + "%")
        print("Term test: " + str(self.termtest) + "%")
        print("Midterm: " + str(self.midterm) + "%")
        print("Final exam: " + str(self.final) + "%")
        print("Final mark: " + str(self.finalMark) + "%")
        print("Letter Grade:", self.finalGrade)
        print()


students = []
n = int(input("Enter the amount of students: "))
for i in range(n):
    name = input("Enter your name (First name and Last name): ")
    name = name.split(" ", 1)#splits the name into two and will put the person's middle name among the last names

    marks = input("Enter the total mark for all labs, assignment 1, assignment 2, assignment 3, assignment 4, assignment 5, the term test, the midterm, and the final exam respectively: ")
    marks = marks.split(" ", 8)

    s = student(name[0], name[1], marks[0], marks[1], marks[2], marks[3], marks[4], marks[5], marks[6], marks[7], marks[8])
    students.append(s)

for i in range(n):
    students[i].print()