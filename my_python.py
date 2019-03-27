# Question 1
import time
from itertools import izip as zip

def get_resource_identifier():
  dict = {'foo': 'L9UKvnomjq', 'bar': '7U9eyOv7M'}

  for i in range(0, 100):
    print(dict.get("foo"))
    print(dict.get("bar"))
    # print(v.time())

colours = ['blue','green','yellow','black','orange']
fruits  = ['berry','apple','banana','currant']

def question2Refactor(colours):
  for colour in reversed(colours):
    print colour
########################################
def question3Refactor(colours):
  for i, colour in enumerate(colours):
    print(i, colour)
########################################
def question4Refactor(colours, fruits):
  for fruit, colour in zip(colours, fruits):
    print(fruit, '==', colour)
######################################## 
def question5Refactor():
  a = 1
  b = 2 
  c = 3
  d = 4
  f = 5
  g = 6
  if (a, b, c ) <= (d, f, g):
    print('pass')
  else:
    print('fail')
########################################
def question6Refactor():
  d = {'0':'blue', '1':'green', '2':'yellow', '3':'black', '4':'orange'}

  while d:
    key, value = d.popitem()
    print(key, '--->', value)
########################################
def question7Refactor():
  arrObj    = []
  first     = [2,2,5,6,7,2,1,8,9,9]
  second    = [2,1,5,6,66,7,77]

  for i in second:
    if i not in first:
      arrObj.append(i)
  print(arrObj)
########################################################################################################################
########################################################################################################################
if __name__ == '__main__':
  question2Refactor(colours)
  question3Refactor(colours)
  question4Refactor(colours, fruits)
  question5Refactor()
  question6Refactor()
  question7Refactor()
