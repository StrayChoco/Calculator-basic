import requests
from math import sqrt
x = print("type anything to calculate \n >leave it empty and enter if you want to exit calculator")
while x != "":
  x = input()
  if x != "":
    x = "undefined"if "/0" in x else eval(x)
    print(x)
    f = open("history.txt", "a")
    f.write(f"{x}\n")
    f.close()
    