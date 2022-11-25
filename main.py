import json
# Read data from a file

f = open('result.json',encoding='utf8').read()
data = json.loads(f)

messages = data['messages']
count = 0 
# Print messages
for msg in messages:
    if msg['type']=='message':
        count+=1

print(count)