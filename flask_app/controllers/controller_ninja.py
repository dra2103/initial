from flask_app import app 
from flask_app.models import model_ninja, model_dojo
from flask import render_template, redirect, request,session, flash


@app.route('/new/ninja')
def new():
    all_dojos = model_dojo.Dojo.get_all_dojos()
    return render_template('new_ninja.html' ,all_dojos = all_dojos)

@app.route('/add_ninja', methods=['POST'])
def create_ninja():
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "age": request.form["age"],
        "dojo_id": request.form["dojo_id"]
    }
    model_ninja.Ninja.create_ninja(data)
    return redirect(f"/{data['dojo_id']}/show")




# data = {
#     "dojo_id": request.form["dojo_id"],
#     "first_name": request.form["first_name"],
#     "last_name": request.form["last_name"],
#     "age": request.form["age"]
# }
# ninja_id = Ninja.create_ninja(data)
