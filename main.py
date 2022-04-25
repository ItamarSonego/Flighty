#Imports
import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Chrome(executable_path=r'chromedriver.exe')
import colorama
from colorama import Fore, Style
import playsound
#Program start(Inputs)
print("Welcome to flighty! please enter when do you want to fly. use", "'/',", "'-'", "(Example: 27/4-28/4)")
Start = input("Start: ")
End = input("End: ")
countryNum = int(input("How many countries do you want to travel?: "))
city = []
cityTime = []
cityTime2 = []
for i in range(countryNum):
    city.append(input("Enter the city that you want to travel. example: " + "'London ': "))
print(city)
for d in range(countryNum):
    cityTime.append(input("How many days do you want to be in " + city[d] + "? " + ("You can enter range of days, example: '2-5': ")))
print(cityTime)
for e in range(countryNum):
    e.append(range(int(cityTime[e].split('-')[0]), int(cityTime[e].split('-')[1])+1))





#print(cityTime)






