# 1.1 Архитектура современных веб-сервисов

1. Каким образом проходит путь запроса(ов) от клиента (на какой сервис и через какие сервисы)?
   1. Client --> Server 1 (запрос):

    GET http://localhost:9004/authenticate
    Content-Type: application/json

    {
     "login": "root",
    "password": "secret"
}

2. Server 4 --> Server 3 (запрос):

GET http://localhost:9003/authenticate
Content-Type: application/json

{
  "login": "root",
  "password": "secret"
}

3. Server 3 --> Server 4 (ответ):

200 OK
Content-Type: application/json

{
  "transactions": [
    {
      "id": 1,
      "userId": 999,
      "category": "auto",
      "amount": 1000000,
      "created": 1613389415
    }
  ],
  "categoryStats": {
    "auto": 1000000
  }
}

3. Server 4 --> Client (ответ):

200 OK
Content-Type: application/json

{
  "transactions": [
    {
      "id": 1,
      "userId": 999,
      "category": "auto",
      "amount": 1000000,
      "created": 1613389415
    }
  ],
  "categoryStats": {
    "auto": 1000000
  }
}



2. Какие делаются запросы на каждом этапе и какие ответы на них приходят?