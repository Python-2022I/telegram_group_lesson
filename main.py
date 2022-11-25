import json
# Read data from a file

f = open('result.json',encoding='utf8').read()
data = json.loads(f)
print(data['name'])