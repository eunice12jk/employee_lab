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
    
  def work(self):
      return "Do job!"
