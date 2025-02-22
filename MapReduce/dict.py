diz = {
    'nome': 'João',
    'eta' : 20,
    'sesso': 'M'
}
print(diz)

diz['eta'] = 21

print(diz)

diz['country'] = ['Italy']

print(diz)

diz['country'].append('Germany')

print(diz)


'''Remember when you iterate on dictionary by default it iterate only on keys.
so if you write for i in diz: you will have only the keys value 
if you want to iterate on both the keys and values, you have to use the .items() method.'''