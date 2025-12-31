# Orders API – Event-ready Backend with FastAPI

Backend API implement with clean architecture, strict typing and ready to scaling to a event-driven system with Kafka.

## 🎯 Problem

Many APi's of e-commerce or orders management start with a simple CRUD and they turn difficult to maintain when scaling
This project search on resolving this problema from beginning, separating domain, persistent and application, and preparing the system to scaling to events.

### Some case problems

For example, when we have to create an order, we starting to save the started-info on the database and call other services like S3 and ProductService for execute some dependencies, but 
when the use-case need to scaling, it's difficult to orchestrate, debug and test the use-case and all the services that intervene

## 🧭 Goals

- Design a scalable and maintaining API
- Apply Clean Architecture and DDD principles
- Use strict typing (TypeVar, Generic, Protocol)
- Mantain the domain decoupled of frameworks
- Preparing the base for future integration with Kafka

## 🛠️ Stack

- Python 3.12
- FastAPI
- GraphQL
- SQLModel
- PostgreSQL
- Pydantic
- Kafka
- Redis

