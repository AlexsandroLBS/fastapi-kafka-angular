# fastapi-kafka-angular

This project is a full stack application made with [FastAPI](https://fastapi.tiangolo.com) and [Angular](https://angular.io). It also has a [Kafka](https://kafka.apache.org) microservice and a [Postgres](https://www.postgresql.org) database, both running in a [Docker](https://www.docker.com) container.

## Execution

To execute the db, front and kafka, run:
```bash
  docker-compose up
```
to run the container. 
And to run the API:
```python
  pip install -r requirements.txt
  uvicorn api.main:app
```
## App

The app ideia is create a subscription service with the following architecture

![image](https://user-images.githubusercontent.com/89843505/215002843-ec3657e9-5030-44f2-a231-5234c3afef1d.png)

The application will have the following execution flow:

- HTTP Notification Receive 
- Queuing
- Processing and Persistence

The service will recieve the following methods:
```http
  GET /getUserStatus/${userName}
```

| Parameter  | Type     | Description                                   |
| :---------- | :--------- | :------------------------------------------ |
| `userName`      | `string` | **Required**. Will return the user subscription status.|

```http
  POST /users/login/
  POST /users/createAccount/
```
Both will recieve a request body with
`
{
  "full_name": "string",
  "password": "string"
}
`
To manage users sign in and sign up.

And to manage the subscriptions, it has
```http
  POST /send_requisition
```
It will recieve a request body with
`
{
  "action": "string",
  "full_name": "string"
}
`
The action can be one of the following
-  "SUBSCRIPTION_PURCHASED" - The purchase has been made and the subscription must be in active status.

-  "SUBSCRIPTION_CANCELED" - The purchase has been canceled and the subscription must be in canceled status.

-  "SUBSCRIPTION_RESTARTED" - The purchase has been retrieved and the subscription must be in active status.

## Database
The Database will follow this structure, making possible to see the users subscriptions status and all event history
![image](https://user-images.githubusercontent.com/89843505/215003662-93638c7d-f115-46c9-9ce3-30481079eab8.png)

## Code structure
The project has the following structure
```
├───src
├───api
│   ├───config.py
│   ├───main.py
│   ├───processing.py
│   ├───requirements.txt
│   ├───router.py
│   └───schema.py
├───db
│   ├───sql
│   │   ├───create_tables.sql
│   │   ├───fill_tables.sql
│   │   └───database.py
│   └───database.py
├───db
└───subscription-ui
```
