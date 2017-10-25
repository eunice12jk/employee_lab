import Admin
import employees 
from Agent import Agent

class Gar2(Agent):
    def work(self):
        print("Jira")
  
    

agent1 = Agent("Joe", "try", 450000, "Gar2")
admin1 = Admin.Admin("Pama", "CI", 500000, "Andela")  
Galo = Gar2("Galgallo", "Wako", 4788889898, "Andela")
print(Galo.work())

print(agent1.work())
print(admin1.work())
