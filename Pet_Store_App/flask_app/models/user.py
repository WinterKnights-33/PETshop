from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:
    db = 'pet_shop_schema'

    def __init__(self, data):
        self.id = data['id']
        self.first_name= data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.workout = []


    @classmethod
    def create_user(cls,data):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        new_user_id = connectToMySQL('pet_shop_schema').query_db(query,data)
        return new_user_id


    @classmethod
    def get_one_by_id(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        this_user = cls(results[0])
        return this_user


    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s"
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) == 0:
            return False
        return cls(results[0])


    @staticmethod
    def validate_registration(data):
        is_valid = True
        info_dict = {
            'email': data['email']
        }
        users_with_email = User.get_by_email(info_dict)
        if len(data['first_name']) == 0:
            flash("Input a first name")
            is_valid = False
        elif len(data['first_name']) < 2:
            flash("First name must be longer than 2 charactors")
            is_valid = False
        if len(data['last_name']) == 0:
            flash("Input a last name")
            is_valid = False
        elif len(data['last_name']) < 2:
            flash("Last name must be longer than 2 charactors")
            is_valid = False
        if len(data['email']) == 0:
            flash("Input an email address")
            is_valid = False
        elif not EMAIL_REGEX.match(data['email']): 
            flash("Invalid email address!")
            is_valid = False
        elif users_with_email != False:
            flash("Email already exists!", 'register')
            is_valid = False
        if len(data['password']) == 0:
            flash('Please input a password.', 'login')
            is_valid = False
        elif len(data['password']) < 8:
            flash("Password must be at least 8 charactors long!")
            is_valid = False
        return is_valid





    @staticmethod
    def validate_login(data):
        is_valid = True

        if len(data['email']) == 0:
            flash('Please input an email address.', 'login')
            is_valid = False
        if len(data['password']) == 0:
            flash('Please input a password.', 'login')
            is_valid = False
        return is_valid