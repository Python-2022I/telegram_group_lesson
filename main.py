import json
# Read data from a file

f = open('result.json',encoding='utf8').read()
data = json.loads(f)

messages = data['messages']
# Print messages
for msg in messages:
    print(msg['id'])