import re
#print(dir(re))

#result=re.match(r'AV','AV Nitin Yewale AV')
#print(result)

#result=re.match(r'AV2','AV Nitin Yewale AV')
#print(result)


#result=re.match(r'AV','AV Nitin Yewale AV')
#print(result.group(0))#AV

#result=re.match(r'AV2','AV Nitin Yewale AV')
#print(result.group(0))#Error


'''
result=re.match(r'AV','AV Nitin Yewale AV')
print(result.start())#0
print(result.end())#2
'''


#result=re.search(r'Nitin','AV Nitin Yewale AV')
#print(result.group(0))#Nitin


#result=re.findall(r'AV','AV Nitin Yewale AV')
#print(result)#['AV', 'AV']

#result=re.split(r'n','HnitinYewale')#split string where n found
#print(result)#['H', 'iti', 'Yewale']


#result=re.split(r'n','HnitinYewale',maxsplit=1)
#print(result)#['H', 'itinYewale']



#result=re.sub(r'india','the world','AV is largest Analytics community of india')
#print(result)#AV is largest Analytics community of the world

'''
pattern=re.compile('AV')

result=pattern.findall('AV Nitin AV Yewale AV')
print(result)

result2=pattern.findall('is largest company AV')
print(result2)
'''

