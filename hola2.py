animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def biggest(aDict):
    c=[]
    for i in aDict.keys():
        c.append(i)

    pos=0
    acum=[]
    for k in aDict.keys():
        a= aDict[k]
        conta=0
        pos+=1
        for i in a:
            conta = conta+1
        acum.append(conta)
    b=acum.index(max(acum))
    return c[b]


print(biggest(animals))


