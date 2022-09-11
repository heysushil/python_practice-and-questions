# Parent aur child

class ParentClass:
    def __init__(self, fatherName, motherName):
        self.father = fatherName
        self.mother = motherName

    # Introduce to childs parent
    def parentIntroduction(self):
        introduction = '''
        -----------------------------------
            Introduc to Prent Class
        -----------------------------------
        Father's Name: {}
        Mohter's Name: {}
        '''.format(self.father, self.mother)
        
        print(introduction)

# Crate parent class object
# After cerating child calss and class form child class. comment line 22 to 26
# father = 'Ram'
# mohter = 'Sita'
# parentObj = ParentClass(father, mohter)
# # Call parentIntroduction method
# parentObj.parentIntroduction()


# Create anohter class
# Know convert this another class into child class
class ChildClass(ParentClass):
    def __init__(self, fatherName, motherName, childName):        
        self.child = childName
        # Call parent class constructer
        # ParentClass.__init__(self, fatherName, motherName)
        # use super() fucntio to pass requried values to parent class constructer
        # super() fucntion no need to user preant class name and self argument
        super().__init__(fatherName, motherName)

    def ayseHiFunctionBanaDiay():
        print('\nayseHiFunctionBanaDiay')

    def childIntroduction(self):
        introduction = '''
        ------------------------------
            Child Inroduction
        ------------------------------
        First Child Name: {}
        Second Child Name: {}
        '''.format(self.child[0], self.child[1])
        print(introduction)
        # ayseHiFunctionBanaDiay()
        self.ayseHiFunctionBanaDiay()

# Create child class object to pass requerd arguemt and call related method
# father = 'Ram'
# mohter = 'Sita'
# child = 'Love','Kush'
# childObj = ChildClass(father, mohter, child)
# # call method
# childObj.parentIntroduction()
# childObj.childIntroduction()



# Home work:
# local scope of method
# global scope of method
