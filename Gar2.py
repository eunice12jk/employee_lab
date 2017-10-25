
from Agent import Agent

class Gar2(Agent):
    def __init__(self, first, last, pay, project):
        super(Gar2, self).__init__(first,last,pay,project)
        
        
    def work(self):
        print("Jira")
  
    



Galo = Gar2("Galgallo", "Wako", 4788889898, "Andela")
print(Galo.work())

