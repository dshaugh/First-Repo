import random
import requests



baseURL = 'https://api.darksky.net/forecast/f3b60e3860754a0934693e5bbe7cf56e/'
lat = '34.683437'
long = '-82.837364'
def firstfunction():
    for i in range(0,10):
        int = random.randint(0,10)
        print(int)


# fo = 'drewpieweiners'
#
# # this is my for loop
# for i in range(0,4):
#     print('{1} hello {0} world {1}'.format(i, fo))

def getweather():
    r = requests.get(baseURL + lat + ',' + long )
    rf = r.json()
    currently = rf['currently']

    print('OPTIONS:')
    dannyDict = {}

    for i, key in enumerate(currently):
        print('{}.\t{}'.format(i, key))
        dannyDict[i] = key
    drew = int(input('Choose from the number from the list you dumb wankstain.   '))
    drew = dannyDict[drew]
    requisition = currently[drew]
    drew = drew.upper()
    print('{}:\t{}'.format(drew, requisition))

if __name__ == '__main__':
    getweather()
