from employees import Employee

class Agent(Employee):
  
  def __init__(self, first, last, pay, project):
    super().__init__(first,last,pay)
    self.project = project

  def work(self):
      return "Crawl!"
      
agent1 = Agent("Joe", "try", 450000, "Gar2")

print(agent1.work())
