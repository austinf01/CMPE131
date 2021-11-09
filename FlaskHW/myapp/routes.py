from myapp import myobj
from myapp import db
from myapp.models import City
from myapp.forms import CityForm
from flask import render_template, flash, redirect

@myobj.route("/clear")
def clear():
    """Clears the database of all entries
    """
    cities = City.query.all()
    for city in cities:
        db.session.delete(city)
    db.session.commit()
    return redirect('/')    
    
@myobj.route("/", methods = ['GET', 'POST'])
def home():
    """Return title as 'Top Cities' and a heading that says Welcome Austin, here are top destinations!
       then a link to https://www.google.com with the text to the link saying 'goooogle'
       and an unordered list of the top cities
    """
    title = 'Top Cities'
    name = 'Austin'
    form = CityForm()
    #creates the schema for the database
    db.create_all()
    cities = City.query.all()
    #if the user hits submit on the form page
    if form.validate_on_submit():
        city = City(city_name = form.city_name.data, city_rank = form.city_rank.data, is_visited = form.is_visited.data)
        db.session.add(city)      
        db.session.commit()
        cities = City.query.all()
        flash(f'{form.city_name.data} added')	
    return render_template("home.html", name = name, title = title, form = form, cities = cities) 
