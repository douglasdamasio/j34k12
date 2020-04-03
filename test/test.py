import sys

listPeople = []

for numberLine, dataLine in enumerate(sys.stdin):
    listPeople.append(dataLine.strip())
    
print(listPeople)

ttask = listPeople[0]
umax = listPeople[1]

listPeople.pop(0)
listPeople.pop(0)

print(ttask, umax)

with open('new.txt', 'a') as file:
    for person in listPeople:
        file.write(person + '\n')
    file.close()

# try:
#     print(pc.criacaoVM())
# except Exception:
#     print('classe não instanciada')


# try:
#     print(pc.criacaoVM())
# except Exception as e:
#     print('classe não instanciada')