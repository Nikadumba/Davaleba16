

class Student:

    courses = []
    
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        # self.courses = courses

    def add_courses(self):
        while True:
            course_list = input(f"Please add a courses for {self.name} (Id: {self.student_id}) (If the list is complete, please type the word: End): ")
            self.courses.append(course_list)
            
            while course_list == "End":
                self.courses.pop(-1)
                print(f"Student Name: {self.name}\nStudent ID: {self.student_id}\nList of Courses: {self.courses}")
                self.courses.clear()
                return False
               

student1 = Student("Nikoloz Dumbadze", "0001")
student1.add_courses()

student2 = Student("Giorgi Giorgadze", "0002")
student2.add_courses()
