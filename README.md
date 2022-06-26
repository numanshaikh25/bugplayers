
# iNeuronKiraBot

Technology Stack : Django and Django Rest Framework


## API Reference

#### Post a message

```http
   POST /api/chat
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
|   `None`  | `string` | **Required**. Message.     |


#### send data as {"message":"hi"}

#### Receive response as {"reply":"hi how are you"}

## Demo

You can test the API which is available at https://ineuron-hackathon.herokuapp.com/api/chat/
at postman or similar


## Installation

Clone the github repo 

```bash
  cd project name
  pip freeze > requirements.txt
```

Install the requirements.txt 
```bash
  run python manage.py runserver
```
