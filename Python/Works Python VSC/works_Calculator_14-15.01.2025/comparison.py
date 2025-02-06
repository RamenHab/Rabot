class Comparison:
   def __init__(self, str1, str2):
      self.str1=str1
      self.str2=str2

   def subtract (self):
      return str(abs(len(self.str1)-len(self.str2)))
   
   def print_result(self):
      print(self.subtract())

string=Comparison("яблоко", "apple")
string.print_result()