from flask_app.models.user import User
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.user import User
from flask import flash

class Pet:
    def __init__(self,data):
        self.id = data['id']
        self.name= data['name']
        self.birthdate= data['birthdate']
        self.description = data['description']
        self.parent = data['parent']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user = User.get_one_by_id({'id':data['user_id']})



    @classmethod
    def create(cls,data):
        query = "INSERT INTO pets (name, birthdate, description, parents, user_id) VALUES (%(name)s, %(birthdate)s, %(description)s, %(parent)s, %(user_id)s);"
        new_pet_id = connectToMySQL('pet_shop_schema').query_db(query,data)
        return new_pet_id


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM pets;"
        pets_from_db =  connectToMySQL('pet_shop_schema').query_db(query)
        pets =[]
        for b in pets_from_db:
            pets.append(cls(b))
        return pets


    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM pets WHERE id = %(id)s;"
        results = connectToMySQL('pet_shop_schema').query_db(query,data) #this is a list of 1 dictionaries
        # make a report object
        this_pet = cls(results[0])
        # now we make a user object
        user_info = {
            'id' : results[0]['user_id']
        }
        this_user = User.get_one_by_id(user_info)
        # make the user an attribute of this report
        this_pet.user = this_user
        return this_pet


    @classmethod
    def update(cls,data):
        query = "UPDATE pets SET name=%(name)s, birthdate=%(birthdate)s, description=%(description)s, parent=%(parent)s, updated_at = NOW() WHERE id = %(id)s;"
        return connectToMySQL('pet_shop_schema').query_db(query,data)


    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM pets WHERE id = %(id)s;"
        return connectToMySQL('pet_shop_schema').query_db(query,data)


    @staticmethod
    def validate_create(report):
        is_valid = True # we assume this is true
        if len(report['name']) == 0:
            flash("Your pet needs a name.")
            is_valid = False
        if len(report['birthdate']) == 0:
            flash("Your pet needs a birthdate.")
            is_valid = False
        if len(report['description']) == 0:
            flash("Give them a cute description!")
            is_valid = False
        return is_valid


    @staticmethod
    def validate_edit(report):
        is_valid = True # we assume this is true
        if len(report['date']) == 0:
            flash("Your pet needs a name.")
            is_valid = False
        if len(report['birthdate']) == 0:
            flash("Your pet needs a birthdate.")
            is_valid = False
        if len(report['description']) == 0:
            flash("Give them a cute description!")
            is_valid = False
        return is_valid