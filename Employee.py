from Person import Person


class Employee(Person):

    def __init__(self, name, age, company, salary):
        super().__init__(name, age)
        self.__company = company
        self.__salary = salary

    @property
    def company(self):
        return self.__company

    @company.setter
    def company(self, company):
        self.__company = company

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary):
        self.__salary = salary

    def print_employee(self):
        self.print_person()
        print(f'Company: {self.company}, Salary: {self.salary}')
