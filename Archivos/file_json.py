import json
with open ('mi_archivo.json', 'r') as file:
    data = json.load(file)
print(data)
# Imprimir el contenido del archivo JSON

data = [ { 'name': 'John', 'age': 30, 'city': 'New York'}, {'name': 'Anna', 'age': 22, 'city': 'London'}, {'name': 'Mike', 'age': 32, 'city': 'Chicago'} ]
with open('mi_archivo.json', 'w') as file:
    json.dump(data, file, indent=4)
