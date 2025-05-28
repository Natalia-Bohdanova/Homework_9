# myArray=[4, 4, 8, 3, 3, 3, 2, 4, 4]

# Вивести кожен елемент масиву
# for element in myArray:
#     print(element)

# Вивести перші 3 елементи масиву
# for i in range(3):
#     print(myArray[i])
# або
# print(myArray[:3])

# Вивести суму всіх елементів
# print(sum(myArray))

# Вивести суму всіх елементів окрім елемента що = 4
# total = sum(x for x in myArray if x != 4)
# print("Сума без 4:", total)


from faker import Faker
fake = Faker()
import json
with open('list.json', 'r') as json_file:
    data = json.load(json_file)
    print(data['lists'][0]['name'])
    fake.user_name()

for item in data['lists']:
    print("ID:", item['id'], "| Name:", item['name'])