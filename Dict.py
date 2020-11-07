words = {"favorite dessert": "apple pie","never eat": "scallop","always have" : "parachute","don't have" :"accident","do this" : "fare","bug" : "flea"}

print(words['bug'])
words['parachute']= 'water'


words['oar']= 'girrafe'

del words['never eat']



for key, value in words.items():
    
    print(key)
