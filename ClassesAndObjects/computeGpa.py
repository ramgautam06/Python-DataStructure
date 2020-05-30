'''
Computing the GPA of students using the data from text files
'''

#defining the student class
class Student:
    def __init__(self,student,hours,qualitypoints):
        self.student = student
        self.hours = float(hours)
        self.qualitypoints = float(qualitypoints)

    #setting up getters
    def getName(self):
        return self.student

    def getHours(self):
        return self.hours

    def getQPoints(self):
        return self.qualitypoints

    def GPA(self):
        return (self.qualitypoints/self.hours)

def main():
    #opening the text file to read
    file = open('Data.txt', 'r')

    #splitting the lines based on space
    student, hours, qualitypoints = file.readline().split('-')
    bestStudent = Student(student, hours, qualitypoints)

    for lines in file:
        #print (lines)
        student, hours, qualitypoints = lines.split('-')

        nextStudent = Student(student,hours, qualitypoints)
        if(nextStudent.GPA()>bestStudent.GPA()):
            bestStudent = nextStudent

    file.close()

    #getting the best student
    print ("Name: " + bestStudent.getName())
    print ("Credits: " , bestStudent.getHours())
    print ("GPA: " , bestStudent.GPA())

if __name__ == "__main__":
    main()


