class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score

    def myfunc(self):
        print("Hello my name is " + self.name, ", age",
              self.age, ",my tracks are,",  self.tracks, "my current score is", self.score,)


s1 = Student("Bob", 26, "FE and BE", 20.90)

s1.name = "Peter"
s1.age = 34
s1.tracks = "UI/UX"
s1.score = 20.90

s1.myfunc()
