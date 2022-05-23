from flask import render_template, redirect, request, flash, session
from flask_app import app
from flask_app.models.pet import Pet
from flask_app.models.user import User



@app.route('/home')
def results_page():
    # this first part is a check to make sure our users are logged in and have access to see this page
    if 'user_id' not in session:
        return redirect('/logout')

    return render_template('home.html', all_pets = Pet.get_all())


@app.route('/add_new_pet')
def add_new_pet():
    # this first part is a check to make sure our users are logged in and have access to see this page
    if 'user_id' not in session:
        return redirect('/logout')

    return render_template('create_page.html')


@app.route('/create',methods=['POST'])
def create():
    if not Pet.validate_create(request.form):
        return redirect('/add_new_pet')
    data = {
        "name":request.form['name'],
        "birthdate":request.form['birthdate'],
        "description": request.form['description'],
        "parent": request.form['parent'],
        "user_id": session['user_id']
    }
    Pet.create(data)
    return redirect('/home')


@app.route('/show/<int:pet_id>')
def detail_page(pet_id):
    # this first part is a check to make sure our users are logged in and have access to see this page
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        'id': pet_id
    }
    return render_template("details_page.html", workout = Pet.get_one(data))


@app.route('/edit_page/<int:pet_id>')
def edit_page(pet_id):
    # this first part is a check to make sure our users are logged in and have access to see this page
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        'id': pet_id
    }
    return render_template("edit_page.html", workout = Pet.get_one(data))


@app.route('/update/<int:pet_id>', methods=['POST'])
def update(pet_id):
    if not Pet.validate_edit(request.form):
        return redirect(f"/edit_page/{pet_id}")
    data = {
        'id': pet_id,
        "name":request.form['name'],
        "birthdate":request.form['birthdate'],
        "description": request.form['description'],
        "parent": request.form['parent']
    }
    Pet.update(data)
    return redirect(f"/show/{pet_id}")


@app.route('/delete/<int:pet_id>')
def delete(pet_id):
    data = {
        'id': pet_id,
    }
    Pet.destroy(data)
    return redirect('/home')