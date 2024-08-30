
class Person:
    def __init__(self, name: str, address: str):
        self.name = name
        self.address = address

    def getName(self):
        return self.name
    
    def getAddress(self):
        return self.address
    
    def setAddress(self, address):
        self.address = address

    def __str__(self):
        return f"Person[name={self.name}, address={self.address}]"
    
class Student(Person):
    def __init__(self, name: str, address: str, program: str, year: int, fee: float):
        super().__init__(name, address)
        self.program = program
        self.year = year
        self.fee = fee

    def getProgram(self):
        return self.program
    def setProgram(self, program):
        self.program = program
    def getYear(self):
        return self.year
    def setYear(self, year):
        self.year = year
    def getFee(self):
        return self.fee
    def setFee(self, fee):
        self.fee = fee

    def __str__(self):
        return f"Student[name={self.name}, address={self.address}, program={self.program}, year={self.year}, fee={self.fee}]"
    
class Staff(Person):
    def __init__(self, name: str, address: str, school: str, pay: float):
        super().__init__(name, address)
        self.school = school
        self.pay = pay

    def getSchool(self):
        return self.school
    def setSchool(self, school):
        self.school = school
    def getPay(self):
        return self.pay
    def setPay(self, pay):
        self.pay = pay

    def __str__(self):
        return f"Staff[name={self.name}, address={self.address}, school={self.school}, pay={self.pay}]"
    

person1 = Person("Diego Rosero", "alejandro@gmail.com")
print(person1)
print("Persona: ", person1.getName(), "correo: ", person1.getAddress())

student1 = Student("kenji David", "kenji@gmail", 2024,  "ingenieria de software", 2255845)
print(student1)
print("Estudiante: ", student1.getName(), "- Correo: ", student1.getAddress(), " - programa: ", student1.getProgram(), " - Año: ", student1.getYear(), " Precio del semestre: ", student1.getFee())

staff1 = Staff("Nelson Chaves", "nelsiton@gmail.com", " institucion ipiales", 2500000)
print(staff1)
print("personal: ", staff1.getName(), "correo: ", staff1.getAddress(), " escuela: ", staff1.getSchool(), " pay: ", staff1.getPay() )