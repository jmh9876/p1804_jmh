class Student(object):
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def get_score(self):
        return max(self.score)
zm = Student('张三',29,[90,90,90])
print(zm.get_name)
print(zm.get_age())
print(zm.get_score())
