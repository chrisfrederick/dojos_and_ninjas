from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja
class Dojo:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.ninjas = []

    @classmethod
    def get_all_dojos(cls):
        query = "SELECT * FROM dojos"
        db_dojos = connectToMySQL("mydb").query_db(query)
        dojos = []
        for dojo in db_dojos:
            dojos.append(Dojo(dojo))
        return dojos
    
    @classmethod
    def save_dojo(cls, data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s)"
        return connectToMySQL("mydb").query_db(query,data)
    
    @classmethod
    def get_dojo(cls, data):
        data = {
            "id": id
        }
        query = "SELECT * FROM dojos WHERE id = %(id)s"
        dojo = connectToMySQL("mydb").query_db(query,data)
        return Dojo(dojo[0])

    @classmethod
    def get_dojos_ninjas(cls, data):
        query = "SELECT * FROM dojos JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE ninjas.dojo_id = %(id)s;"
        dojos_ninjas = connectToMySQL("mydb").query_db(query, data)
        print(dojos_ninjas)
        dojo = Dojo(dojos_ninjas[0])
        for ninjas in dojos_ninjas:
            ninja_data = {
                "id": ninjas["id"],
                "first_name": ninjas["first_name"],
                "last_name": ninjas["last_name"],
                "age": ninjas["age"],
                "created_at": ninjas["created_at"],
                "updated_at": ninjas["updated_at"],
                "dojo_id": ninjas["dojo_id"]
            }
            dojo.ninjas.append(ninja.Ninja(ninja_data))
        return dojo

    @classmethod
    def delete_dojo(cls, data):
        query = "DELETE FROM dojos WHERE id = %(id)s"
        return connectToMySQL("mydb").query_db(query,data)