from flask import render_template,redirect,request,flash,session
from flask_app.models.pet import pet
from flask_app.models.user import user
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/register',methods=['POST'])
def register():
    if not user.User.validate_registration(request.form):
        return redirect('/')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])

    user_info = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': pw_hash
    }

    new_user_id = user.User.create_user(user_info)

    # check whether or not someone has logged in and who logged in
    session['user_id'] = new_user_id
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']

    return redirect('/home')


@app.route('/logout')
def logout():
    session.clear
    return redirect('/')


@app.route('/login', methods = ['POST'])
def login():
    if not user.User.validate_login(request.form):
        return redirect('/')
    #check for anyone in the database that has the email of the input on the form
    data = {
        'email': request.form['email']
    }
    user_from_db = user.User.get_by_email(data)
    if not user_from_db:
        flash('Invalid email or password')
        return redirect('/')

    if not bcrypt.check_password_hash(user_from_db.password, request.form['password']):
        flash('Invalid email or password')
        return redirect('/')

    session['user_id'] = user_from_db.id
    session['first_name'] = user_from_db.first_name
    session['last_name'] = user_from_db.last_name
    return redirect('/home')