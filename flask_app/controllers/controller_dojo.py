from flask_app import app 
from flask import render_template, redirect, request,session, flash
from flask_app.models import model_dojo, model_ninja

@app.route('/')
def all_dojos():
    all_dojos = model_dojo.Dojo.get_all_dojos()
    print('dojo.name')
    return render_template('dojos.html', all_dojos=all_dojos)

@app.route('/create_dojo', methods=['POST'])
def create_dojo():
    model_dojo.Dojo.create_dojo(request.form)
    return redirect ('/')

@app.route('/<int:id>/show')
def ninjas_in_dojo(id):
    dojo = model_dojo.Dojo.get_dojos_with_ninjas({'id': id})
    return render_template('dojo_show.html', dojo = dojo)

