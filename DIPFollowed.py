from abc import ABC, abstractmethod


class DataBase(ABC):
    @abstractmethod
    def save(self, data: str):
        pass

class SqlDb(DataBase):
    def save(self, data: str):
        print(f"Executing SQL Query: INSERT INTO users VALUES('{data}')")


class MongoDb(DataBase):
    def save(self, data: str):
        print(f"Executing Mongo Query: db.users.insert({{'name': '{data}'}})")

class UserService:
    def __init__(self, database: DataBase):
        self.db = database

    def store_user(self, user: str):
        self.db.save(user)


sql_db = SqlDb()
sql_service = UserService(sql_db)
sql_service.store_user("Sankalp")

print("-" * 50)

# Use MongoDB
mongo_db = MongoDb()
mongo_service = UserService(mongo_db)
mongo_service.store_user("Bishal")
