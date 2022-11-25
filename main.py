import json
# Read data from a file

f = open('result.json',encoding='utf8').read()
data = json.loads(f)

messages = data['messages']
count = 0 
# Print messages
for msg in messages:
    print(msg.get('from'))
    

print(count)