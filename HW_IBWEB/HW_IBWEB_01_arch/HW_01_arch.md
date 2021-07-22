# 1.1 Архитектура современных веб-сервисов

## 1. Каким образом проходит путь запроса(ов) от клиента (на какой сервис и через какие сервисы)?
1. Client --> Server 1 (запрос):
2. Server 1 --> Client (ответ):
3. Server 1 --> Server 2 (запрос):
4. Server 2 --> Server 3 (запрос):
5. Server 3 --> Server 4 (запрос):
6. Server 4 --> Server 3 (ответ):
7. Server 3 --> Server 2 (ответ):

> После последнего ответа 200 OK посланного на второй сервер, происходит завершение передачи данных по всем каналам, видимо тут есть ответ на вторую задачу под "*", но я не до конца понял как ответ долетает до клиента...

![](pic/FIN.png)

## 2. Какие делаются запросы на каждом этапе и какие ответы на них приходят?

1. Client --> Server 1 (запрос):

    PUT http://localhost:9001/users
    application/x-www-form-urlencoded
    Form item: "login" = "user"
    Form item: "password" = "111111"

![](pic/c-9001.png)


2. Server 1 --> Client (ответ):

    200 OK 
    application/json
    
    JavaScript Object Notation: application/json
    Object
        Member Key: token
            String value [truncated]: eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjIsImxvZ2luIjoidXNlciIsInJvbGVzIjpbIlVTRVIiXSwiaWF0IjoxNjI2Njk5MzIwLCJleHAiOjE2MjY3MDI5MjB9.kt1wHXdkmXacvTDCYvEGMzbjywhAfIRqsQcx-MDRZTo0OH9hFEQEsRnCzSBggRzcAMARr_
            Key: token


![](pic/9001-c.png)

3. Server 1 --> Server 2 (запрос):

    GET http://localhost:9002/api/transactions
    
    [truncated]Authorization: eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOjIsImxvZ2luIjoidXNlciIsInJvbGVzIjpbIlVTRVIiXSwiaWF0IjoxNjI2Njk2MjU2LCJleHAiOjE2MjY2OTk4NTZ9.n89wTmLOb1AuJYomVJmZlal_iBIBardI1vIT2T1WYDIq4exDc-SHYlxIx6EddV7iPw1LV

![](pic/9001-9002.png)

4. Server 2 --> Server 3 (запрос):

    GET http://localhost:9003/api/transactions
    X-Userid: 2\r\n


![](pic/9002-9003.png)

5. Server 3 --> Server 4 (запрос):

    GET http://localhost:9004/api/transactions
    X-Userid: 2\r\n

![](pic/9003-9004.png)

6. Server 4 --> Server 3 (ответ):

    200 ОК
    
    JavaScript Object Notation: application/json
    Array
        Object
            Member Key: id
                Number value: 1
                Key: id
            Member Key: userId
                Number value: 2
                Key: userId
            Member Key: category
                String value: auto
                Key: category
            Member Key: amount
                Number value: 1000000
                Key: amount
            Member Key: created
                Number value: 1626688616
                Key: created
        Object
            Member Key: id
                Number value: 2
                Key: id
            Member Key: userId
                Number value: 2
                Key: userId
            Member Key: category
                String value: auto
                Key: category
            Member Key: amount
                Number value: 100000
                Key: amount
            Member Key: created
                Number value: 1626688616
                Key: created
        Object
            Member Key: id
                Number value: 3
                Key: id
            Member Key: userId
                Number value: 2
                Key: userId
            Member Key: category
                String value: food
                Key: category
            Member Key: amount
                Number value: 100000
                Key: amount
            Member Key: created
                Number value: 1626688616
                Key: created

7. Server 3 --> Server 2 (ответ):

    200 ОК


    JavaScript Object Notation: application/json
    Object
        Member Key: transactions
            Array
                Object
                    Member Key: id
                        Number value: 1
                        Key: id
                    Member Key: userId
                        Number value: 2
                        Key: userId
                    Member Key: category
                        String value: auto
                        Key: category
                    Member Key: amount
                        Number value: 1000000
                        Key: amount
                    Member Key: created
                        Number value: 1626688616
                        Key: created
                Object
                    Member Key: id
                        Number value: 2
                        Key: id
                    Member Key: userId
                        Number value: 2
                        Key: userId
                    Member Key: category
                        String value: auto
                        Key: category
                    Member Key: amount
                        Number value: 100000
                        Key: amount
                    Member Key: created
                        Number value: 1626688616
                        Key: created
                Object
                    Member Key: id
                        Number value: 3
                        Key: id
                    Member Key: userId
                        Number value: 2
                        Key: userId
                    Member Key: category
                        String value: food
                        Key: category
                    Member Key: amount
                        Number value: 100000
                        Key: amount
                    Member Key: created
                        Number value: 1626688616
                        Key: created
            Key: transactions
        Member Key: categoryStats
            Object
                Member Key: auto
                    Number value: 1100000
                    Key: auto
                Member Key: food
                    Number value: 100000
                    Key: food
            Key: categoryStats