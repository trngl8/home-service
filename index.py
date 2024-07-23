from flask import request, render_template, redirect, flash, url_for
import os
import zmq
import json
from catalog import db
from catalog import create_app
from forms import RealtyForm
from commands import show_environment_configuration, show_order_requests
from dotenv import load_dotenv

load_dotenv()
app = create_app()
app.secret_key = b'_ReB-9qVr-ghJ+n7+I.xu='
app.cli.add_command(show_environment_configuration)
app.cli.add_command(show_order_requests)

db_path = os.path.join(app.instance_path, 'catalog.db')
if not os.path.exists(db_path):
    with app.app_context():
        db.init_db()

context = zmq.Context()
zmq_socket = context.socket(zmq.PUB)
zmq_socket.bind("tcp://127.0.0.1:5555")

@app.route('/', methods=["GET", "POST"])
def home():
    form = RealtyForm(request.form)
    if request.method == "POST" and form.validate():
        database = db.get_db()
        data = {
            "name": form.name.data,
            "property_type": form.property_type.data,
            "square": form.square.data,
            "bathrooms": form.bathrooms.data,
            "bedrooms": form.bedrooms.data,
            "water_supply": form.water_supply.data,
            "electricity": form.electricity.data,
            "straits": form.straits.data,
            "kitchen_squares": form.kitchen_squares.data
        }
        json_data = json.dumps(data)
        zmq_socket.send_string(json_data)
        database.execute(
            "INSERT INTO realty (name, type, square, bathrooms, bedrooms, water_supply, electricity, straits, kitchen) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (form.name.data, form.property_type.data, form.square.data, form.bathrooms.data, form.bedrooms.data, \
            form.water_supply.data, form.electricity.data, form.straits.data, form.kitchen_squares.data)
        )
        database.commit()
        flash("Form submitted successfully!", "success")
        return redirect(url_for('home'))
    elif request.method == "POST" and not form.validate():
        return redirect(url_for('home'))
    return render_template("home.html")


@app.route('/about', methods=["GET"])
def about():
    return render_template("blank.html")


@app.route('/products', methods=["GET"])
def products():
    return render_template("products.html")


@app.route('/contacts', methods=["GET", "POST"])
def contacts():
    return render_template("contacts.html")


@app.route('/services', methods=["GET"])
def services():
    return render_template("services.html")


@app.route('/articles', methods=["GET"])
def articles():
    return render_template("articles.html")


@app.route('/order', methods=["GET", "POST"])
def order():
    return render_template("order.html")


if __name__ == "__main__":
    app.run(debug=os.getenv("DEVELOPMENT"))
