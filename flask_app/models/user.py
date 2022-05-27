from flask_app.config.mysqlconnection import connectToMySQL

import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

from flask import flash


class User:
    db = "pet_shop_schema"
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
#        self.created_by = data['created_by']
#        self.updated_by = data['updated_by']
        

    @classmethod
    def save(cls,data):
        query = "INSERT INTO users ( first_name, last_name, email, password ) VALUES ( %(first_name)s, %(last_name)s, %(email)s, %(password)s );"
        return connectToMySQL(cls.db).query_db(query,data)
    
    @classmethod
    def update(cls,data):
        query = "UPDATE users SET first_name=%(first_name)s,last_name=%(last_name)s,email=%(email)s,updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL('users_schema').query_db(query,data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(cls.db).query_db(query)
        users = []
        for row in results:
            users.append( cls(row))
        return users

    @classmethod
    def get_w_id(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        return cls(results[0])

    @classmethod
    def get_w_email(cls,data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(cls.db).query_db(query,data)
        if len(results) < 1:
            return False
        return cls(results[0])

    @staticmethod
    def validate_reg(user):
        is_valid = True
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL(User.db).query_db(query,user)
        if len(results) >= 1:
            flash("Email already registered", 'register')
            is_valid= False
        if not EMAIL_REGEX.match(user['email']):
            flash("Invalid Email Information", 'register')
            is_valid= False
        if len(user['first_name']) < 2:
            flash("First name must be at least 2 characters", 'register')
            is_valid= False
        if len(user['last_name']) < 2:
            flash("Last name must be at least 2 characters", 'register')
            is_valid= False
        if len(user['password']) < 8:
            flash("Password must be at least 8 characters", 'register')
            is_valid= False
        if user['password'] != user['confirm']:
            flash("Passwords must match", 'register')
        return is_valid