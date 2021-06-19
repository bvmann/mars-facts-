
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars


app = Flask(__name__)

mongo=PyMongo(app, uri="mongodb://localhost:27017/mars_app")

@app.route("/")
def home():

    forth_planet=mongo.db.red_planet.find_one()

    return render_template("index.html",mars_attacks=forth_planet )

@app.route("/scrape")
def scrape():

    mars_landing=scrape_mars.scrape()

    planet=mongo.db.red_planet
    planet.update({},mars_landing,upsert=True)

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)


