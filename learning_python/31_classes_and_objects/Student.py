#let's you create your own datatype
#let's you represent your student object inside python.
#let's you model realworld objects. 

class Student: #this defines a student. and object is the actual student. 
    def __init__(self, name, major, gpa, is_on_probation): #values that represent student datatype. these are just parameters.
        self.name = name #the actual object's name is equal to name
        self.major = major #student's major  will be equal to major we passed in.
        self.gpa = gpa #the student's gpa will be equal to gpa we passed in and so on. 
        self.is_on_probation = is_on_probation