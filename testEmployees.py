import unittest
from Employees import *

class employeesTestCase(unittest.TestCase):
  
  def is_fullname_string(self):
    """asserts if fullname is a string"""
    
    self.isinstanceEquals(fullname("Name"), True)
    
  def is_pay_integer(self):
    """asserts if pay is integer"""
    
    self.assertsTrue((int),34000)
    
    
    
    
    

if __name__ == '__main__':
  unittest.main()