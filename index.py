from flask import Flask, request, render_template
import os
from catalog import db
from catalog import create_app

app = create_app()

@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        user_name = request.form.get("name")
        user_property_type = request.form.get("type")
        user_square = request.form.get("square")
        user_bathrooms = request.form.get("bathrooms")
        user_bedrooms = request.form.get("bedrooms")
        print(user_name)
        database = db.get_db()
        database.execute(
            "INSERT INTO realty (name, type, square, bathrooms, bedrooms) VALUES (?, ?, ?, ?, ?)",
            (user_name, user_property_type, user_square, user_bathrooms, user_bedrooms)
        )
        database.commit()
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=os.getenv("DEVELOPMENT"))
