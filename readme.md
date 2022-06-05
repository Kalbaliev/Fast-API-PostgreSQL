
# Fast-Api with PostgreSQL on Python 

First of All, for using **PostgreSQL** on Python we have to up PostgreSQL, Pgadmin Servers on Docker.
Pgadmin depends on PostgreSQL server.




## PostgreSQL, Pgadmin up on Docker

Pull __Zookeeper, Kafka__ image from [DockerHub](https://hub.docker.com/search?q=zookeeper)
```console
docker pull postgres

docker pull dpage/pgadmin4
```
Pgadmin port is 80 we will change to 5050, PostgreSQL port is 5432 ___do not change it!___.






# Fast-Api
Here we use several libraries for making Fast-API projects. In this case we prepare DockerFile for python projects.

There are libraries from requirements.txt:

- fastapi==0.78.0
- pydantic==1.9.1
- SQLAlchemy==1.4.37
- uvicorn==0.17.6
- psycopg2-binary

```docker
FROM python:3.8

WORKDIR /
COPY . .

RUN pip install -r requirements.txt
EXPOSE 8000
ENTRYPOINT ["uvicorn"]
CMD ["main:app","--host=0.0.0.0","--reload"]

```

## What are python files on this project?

- main.py - ***`Api route functions (CRUD operations)`***
- database.py -  ***`Configuration of PostgreSQL server with SQLAlchemy`***
- schema.py - ***`Schema of requested JSON body params`***
- models.py - ***`Database Table Structure`***
- decorator.py - ***`Check Api Key for all routes`***

## Deploy Fast-Api project
`docker-compose.yml` file which help you  to up three servers with dependencies


```console
docker-compose -p jobs-app up --build
```

# Fast-Api - Swagger UI

It is located : `localhost:8000/docs` url

![SwaggerUi](https://i.ibb.co/jfj4Sgj/swagger.png)

# Pgadmin

It is located : `localhost:5050` url

Email: ***admin@admin.com*** | Password: ***mysecretpassword*** (from `docker-compose.yml` environments variables)

![Pgadmin](https://i.ibb.co/P1xCYF1/pgadmin.png)
