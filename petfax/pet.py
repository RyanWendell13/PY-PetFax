from flask import (Blueprint, render_template)
import json

pets = json.load(open('pets.json'))
print(pets)

bp = Blueprint('pet', __name__, url_prefix="/pets")



print()

print()
@bp.route('/')
def index(): 
    return render_template('index.html', pets = pets)

@bp.route('/<index>')
def pet(index): 
    
    return render_template('pet.html', pet = pets[int(index)-1])

@bp.route('/new')
def new(): 
    return render_template('new.html')
