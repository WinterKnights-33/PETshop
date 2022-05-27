from flask import render_template,redirect,request,session

from flask_app import app

from flask_app.models.pet import Pet 

from flask_app.controllers.users import User


@app.route('/home')
def home():
    if 'user_id' not in session:
        return redirect('/logout')
    data ={
        'id': session['user_id']
    }
    #print (session["user_id"])
    return render_template("dashboard.html", user=User.get_w_id(data), pets=Pet.get_all_t())


@app.route('/pet/veiw/<int:id>')
def view(id):
    data = {
        'id': id
    }
    return render_template("petProfile.html", pet=Pet.get_one_t(data))


@app.route('/pet/addPet')
def report():
    return render_template("addPet.html")


@app.route('/pet/addPet/save', methods=['POST'])
def save():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        'id' : id,
        "name":request.form['name'],
        "birthdate":request.form['birthdate'],
        "description": request.form['description'],
        "parents": request.form['parents'],
        "user_id": session['user_id']
    }
    Pet.save(data)
    return redirect('/home')


@app.route('/pet/editPet/<int:id>')
def edit(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        'id': id
    }
    return render_template("editPet.html", pet=Pet.get_one_t(data))



@app.route('/addPet/pet/update/<int:id>', methods=['POST'])
def update(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        'id' : id,
        "name":request.form['name'],
        "birthdate":request.form['birthdate'],
        "description": request.form['description'],
        "parents": request.form['parents'],
        "user_id": session['user_id']
    }
    Pet.update(data)
    return redirect('/home')


@app.route('/pet/delete/<int:id>')
def destroy(id):
    data = {
        'id': id
    }
    Pet.destroy(data)
    return redirect('/home')


