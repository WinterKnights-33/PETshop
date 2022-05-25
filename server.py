from Pet_Store_App.flask_app import app
from Pet_Store_App.flask_app.controllers import users
from Pet_Store_App.flask_app.controllers import pets

if __name__=="__main__":
    app.run(debug=True)