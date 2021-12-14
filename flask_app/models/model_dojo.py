from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import model_ninja

DATABASE = 'ninjas_dojos_db'

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []
        
    @classmethod
    def get_all_dojos(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(DATABASE).query_db(query)
        dojos = []
        for dojo in results:
            dojos.append(cls(dojo))
        return results 
    
    @classmethod
    def create_dojo(cls, data):
        query = 'INSERT INTO dojos (name) VALUES (%(name)s);'
        results = connectToMySQL(DATABASE).query_db(query, data)
        return results
    
    @classmethod
    def get_one_dojo(cls, data):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if results:
            return cls(results[0])
        return False
    
    @classmethod
    def get_dojos_with_ninjas(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id Where dojos.id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        dojos = cls(results[0])
        for row_from_db in results:
            ninja_data = {
                "id": row_from_db["ninjas.id"],
                "first_name": row_from_db["first_name"],
                "last_name": row_from_db["last_name"],
                "age": row_from_db["age"],
                "dojo_id": row_from_db["id"],
                "created_at": row_from_db["ninjas.created_at"],
                "updated_at": row_from_db["ninjas.updated_at"]
            }
            dojos.ninjas.append(model_ninja.Ninja(ninja_data))
        return dojos
