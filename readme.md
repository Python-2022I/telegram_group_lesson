# Telegram group data 

Structure of "result.json" file:
```json
{
    "name": "Group name",
    "type": "group",
    "id": "group id",
    "messages": [
        {
            "id": "message id",
            "from": "user name",
            "text": "message text",
            "date": "message date"
        },
        {
            "id": "message id",
            "from": "user name",
            "text": "message text",
            "date": "message date"
        }
    ]
}
    
```

## 1. Get telegram group name from "result.json" file

- Open "result.json" file
- Convert "result.json" file to python dictionary
- Get "name" value from dictionary


## 2. Get messages from "result.json" file

- Get "messages" value from dictionary and assign to "messages" variable
- Find length of "messages" variable.
- Print each message id, from messages list.
- Print each message type, from messages list.
