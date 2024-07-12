from flask import request, render_template
import os
from catalog import db
from catalog import create_app

app = create_app()

db_path = os.path.join(app.instance_path, 'catalog.db')
if not os.path.exists(db_path):
    with app.app_context():
        db.init_db()


@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        user_name = request.form.get("name")
        user_property_type = request.form.get("type")
        user_square = request.form.get("square")
        user_bathrooms = request.form.get("bathrooms")
        user_bedrooms = request.form.get("bedrooms")
        user_water_supply = request.form.get("water")
        user_electricity = request.form.get("electricity")
        user_straits = request.form.get("straits")
        user_kitchen_squares = request.form.get("kitchen")


        database = db.get_db()
        database.execute(
            "INSERT INTO realty (name, type, square, bathrooms, bedrooms, water_supply, electricity, straits, kitchen) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (user_name, user_property_type, user_square, user_bathrooms, user_bedrooms, user_water_supply, user_electricity, user_straits, user_kitchen_squares)
        )
        database.commit()
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=os.getenv("DEVELOPMENT"))
