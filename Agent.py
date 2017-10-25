from employees import Employee

class Agent(Employee):
  
  def __init__(self, first, last, pay, project):
    super().__init__(first,last,pay)
    self.project = project

  def work(self):
      return "Crawl!"