import requests
import random
from random import randint as rand
import config0 as cfg0

print("Alumka stress")
print("DataBase: "+cfg0.dataBase)
  
database = cfg0.dataBase
userName = cfg0.name
stars = cfg0.stars
demons = cfg0.demons
diamonds = cfg0.diamonds
userCoins = cfg0.userCoins

def createUser(userName, stars, demons, udid):
    
    numbers=str(random.randint(8546845, 99999999))
    color1=str(random.randint(1, 96))
    color2=str(random.randint(1, 96))
    icon=str(random.randint(1, 96))
    print('Icon info:')
    print('Icon id: '+icon)
    print('Color 1: '+color1)
    print('Color 2: '+color2)
    print('-------------------------------')
    
    endpoint = database
    data = {
        'userName': userName+' '+numbers, 
        'secret': 'Wmfv3899gc9', 
        'stars': stars, 
        'demons': demons,
        'diamonds': diamonds, 
        'userCoins': userCoins,
        'icon': icon, 
        'color1': color1, 
        'color2': color2,
        'udid' : udid
    }
    headers = {'User-Agent': ''}
    r = requests.post(endpoint+"updateGJUserScore.php", data=data, headers=headers)
    return r.text
def generateUDID():
    udid = "S"+str(rand(111111111, 999999999))+str(rand(111111111, 999999999))+str(rand(111111111, 999999999))+str(rand(111111111, 999999999))+str(rand(1,9))
    return udid
    
    
while True:
    print('')
    print('')
    print('User create:')
    print('ID: '+createUser(userName, stars, demons, generateUDID()))
    print("Name: "+cfg0.name)
    print('Stars: '+cfg0.stars)
    print('Demons: '+cfg0.demons)
    print('diamonds: '+cfg0.diamonds)
    print('userCoins: '+cfg0.userCoins)
    print('----------------------------------')
    print('Ваш запрос выполнен!')