from time import sleep
import json
import  requests

EASY = 1/4
MEDIUM = 2/4
HEAVY = 3/4

r =  requests.get('https://tmlkivmd4e.execute-api.us-east-1.amazonaws.com/').json()

for ac in r:
  print (ac['name'][::-1] + "\t\t\t" + ac['last_update'] )
class MAYAN:

  def __init__(self, name = "", status = 0, size = 10):
    self._name = name
    self._status = status
    self._size = size
  
  def get_mayan(self):
    return self._name

  def get_status(self):
    return (self._status)

  def get_size(self):
    return self._size

  def update_status(self, num):
    self._status = num


def status_check(size, number):
  ratio = (number)/(size)
  if ratio < EASY:
    ratio = "empty"
  elif ratio >= EASY and ratio <= MEDIUM:
    ratio = "MEDIUM"
  elif ratio > MEDIUM:
    ratio = "HEAVY"
  return ratio

def main():
  input_file = open("mayanot.txt", "r+")
  
  ain_akaliptos = MAYAN("ain akliptus",5)
  fuhuora = MAYAN("fuhuora",10)
  lifta = MAYAN("lifta",20)
  sagme = MAYAN("sagme",25)
  dubak = MAYAN("dubak",15)
  
  

  
  list_to_file = []
  
  list_of_springs = [ain_akaliptos, fuhuora, lifta, sagme, dubak]
  
  

  
  while True:
    
    act = input("Select an action by number \n 1. The amount of people in the spring \n 2. Up-to-date reporting of people\n 3. Add a spring\n 4. finish \n")

    if act == "1":
      name = input("Insert a spring name: ")
      for spring in list_of_springs:
        if spring.get_mayan() == name:
          statuse = int(spring.get_status())
          size = int(spring.get_size())
      print(statuse)
      print(status_check(size, statuse))


    
    if act == "2":
      num = input("enter number: ")
      for spring in list_of_springs:
        if spring.get_mayan() == name:
          spring.update_status(int(num)) 
    
    if act == "3":
      list_of_springs.append(MAYAN(input("enter name of spring: ")))
      input_file.writelines(list_of_springs[len(list_of_springs)-1].get_mayan() +"\n")
       
    if act == "4":
      print("goodby")
      break
  
  for spring in list_of_springs:
    list_to_file.append(spring.get_mayan() + "\n")    
  
  
  input_file.close()
  
  if __name__ == "__main__":
    main()
