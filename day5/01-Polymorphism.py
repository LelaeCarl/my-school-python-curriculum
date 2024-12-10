# 01 - Polymorphism
'''
# 1. Parent class
'''
class Dog(object):
    def work(self):
        print("Do something....")

'''
# 2. Subclass
'''
class ArmyDog(Dog):
    def work(self):
        print("Chase enemies....")

'''
# 3. Subclass
'''
class DrugDog(Dog):
    def work(self):
        print("Search for drugs....")

'''
# 4. Human class
'''
class Person(object):
    def workWithDog(self, dog):
        dog.work()

# Create various objects
ad = ArmyDog()
dd = DrugDog()

zh = Person()
zh.workWithDog(ad)  # Military dog
zh.workWithDog(dd)  # Drug-detecting dog
