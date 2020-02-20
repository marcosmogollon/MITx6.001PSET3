animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

#print(animals)


def how_many(aDict):
    suma2=0
    #valor = aDict.values()
    for k in aDict.values():
        for i in k:
            suma2 = suma2+1
    return suma2

print(how_many(animals))