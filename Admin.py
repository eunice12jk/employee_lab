from employees import Employee    

class Admin(Employee):
  
  def __init__(self, first, last, pay, employees = None):
    super(Admin, self).__init__(first,last,pay)
    self.employees = employees
    
  def work(self):
      return "Hire!"

admin1 = Admin("Pama", "CI", 500000, "Andela")

print(admin1.work())
