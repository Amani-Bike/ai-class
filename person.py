class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"I'm {self.name} and I'm {self.age} years old")    

    def adult(self):
        if self.age >18:
            print(f"{True} I'm {self.name} and I'm {self.age} years old") 
        else:
            return print(f"{False} I'm {self.name} and I'm {self.age} years old") 

first_individual = person("John",23)
second_individual = person("Rose",21)
third_individual = person("Paul",18)
fourth_individual = person("Joyce",13)

first_individual.greet()
second_individual.greet()
third_individual.greet()
fourth_individual.greet()

first_individual.adult()
second_individual.adult()
third_individual.adult()
fourth_individual.adult()
