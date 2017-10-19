class Employee(object):
  '''Common base class for all employees'''
  
  
  employee_Count = 0
  
  def __init__(self, first, last, pay):
    self.first = first
    self.last = last
    self.email = first + "." + last + "@company.com"
    self.pay = pay
    Employee.employee_Count += 1
    
  def fullname(self):
    return "{} {}".format(self.first, self.last)
  
  
class Agent(Employee):
  
  def __init__(self, first, last, pay, project):
    super().__init__(first,last,pay)
    self.project = project
  
 
class Admin(Employee):
  
  def __init__(self, first, last, pay, employees = None):
    super().__init__(first,last,pay)
    self.employees = employees
    

  
   
    
agent1 = Agent("Joe", "try", 450000, "Gar2")
agent2 = Agent("Pama", "CI", 500000, "Andela")
admin1 = Admin("Sue", "Tam", 78000, agent2.fullname())
print("I am {}, I earn {} and I manage {} from {}".format(admin1.fullname(), admin1.pay, admin1.employees, agent2.project) )
print(Employee.employee_Count)