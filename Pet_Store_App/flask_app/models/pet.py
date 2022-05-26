
from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash

class Pet:
    db = "pet_shop_schema"
    def __init__(self,data):
        self.id = data['id']
        self.name= data['name']
        self.birthdate= data['birthdate']
        self.description = data['description']
        self.parents = data['parents']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO pets (name, birthdate, description, parents, user_id) VALUES (%(name)s, %(birthdate)s, %(description)s, %(parents)s, %(user_id)s);"

        # comes back as the new row id
        result = connectToMySQL('pet_shop_schema').query_db(query, data)
        return result

    @classmethod
    def get_my_t(cls,data):
        query = "SELECT first_name FROM users LEFT JOIN pets ON user.id = pet.user_id WHERE id = %(id)s;"
        query = "SELECT * FROM pets WHERE user_id = %(id)s;"
        results = connectToMySQL('pet_shop_schema').query_db(query,data)
        petstoreturn = []
        for result in results:
            petstoreturn.append(cls(result))
        return (petstoreturn)

    @classmethod
    def get_all_t(cls):
        query = "SELECT first_name FROM users LEFT JOIN pets ON user.id = pet.user_id WHERE id = %(id)s;"
        query = "SELECT * FROM pets;"
        results = connectToMySQL('pet_shop_schema').query_db(query)
        print (f"RESULTS{results}")
        pets = []
        for row in results:
            pets.append( cls(row))
        return pets

    @classmethod
    def get_one_t(cls,data):
        query = "SELECT first_name FROM users LEFT JOIN pets ON user.id = pet.user_id WHERE id = %(id)s;"
        query = "SELECT * FROM pets WHERE id = %(id)s;"
        results = connectToMySQL('pet_shop_schema').query_db(query,data)
        return cls(results[0])

    @classmethod
    def get_name(cls,data):
        query = "SELECT * FROM users LEFT JOIN pets ON user.id = pet.user_id WHERE id = %(id)s;"
        query = "SELECT first_name FROM users WHERE user_id = %(user_id)s;"
        results = connectToMySQL('pet_shop_schema').query_db(query,data)
        return cls(results[0])

    @classmethod
    def update(cls, data):
        query = "UPDATE pets SET birthdate = %(birthdate)s, description = %(description)s, user_id = %(user_id)s WHERE id = %(id)s;"
        return connectToMySQL('pet_shop_schema').query_db(query, data)

    @classmethod
    def submit_report(cls, data):
        query = "UPDATE pets SET birthdate = %(birthdate)s, description = %(description)s, user_id = %(user_id)s, created_by = %(created_by)s WHERE id = %(id)s;"
        return connectToMySQL('pet_shop_schema').query_db(query, data)
    
    @classmethod
    def report(cls, data):
        query = "UPDATE pets SET birthdate = %(birthdate)s, description = %(description)s, created_by = %(created_by)s, WHERE id = %(id)s;"
        return connectToMySQL('pet_shop_schema').query_db(query, data)


    @classmethod
    def destroy(cls, data):
        query  = "DELETE FROM pets WHERE id = %(id)s;"
        return connectToMySQL('pet_shop_schema').query_db(query, data)
        
#    @staticmethod
#    def validate_reg(pet):
#        is_valid= True
#        if len(pet['title']) < 2:
#            is_valid= False
#            flash("Title must be at least 2 characters")
#        if len(pet['description']) < 10:
#            is_valid= False
#            flash("Description must be at least 10 characters long")
#        if len(pet['price']) < 0:
#            is_valid= False
#            flash("price should be greater than 0")
#        return is_valid
