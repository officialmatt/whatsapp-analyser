# whatsapp-analyser
Program that can analyse exported WhatAapp chats, outputting a JSON in the following format: 

```python
{'NoOfMessages': int
  'date': {'day': int
           'month': int
           'year': int
          }
  'individual': {
                'name': string
                'amount': int
                }
}
```

To use, export a WhatsApp chat named  `chat.txt` into cloned repo and run  `main.py`
