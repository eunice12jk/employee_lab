from employees import Employee    

class Admin(Employee):
  
  def __init__(self, first, last, pay, employees = None):
    super().__init__(first,last,pay)
    self.employees = employees
    
  def work(self):
      return "Hire!"

admin1 = Admin.Admin("Pama", "CI", 500000, "Andela")

print(admin1.work())
