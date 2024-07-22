from flask import request, render_template, redirect, flash, url_for
import os
from catalog import db
from catalog import create_app
from forms import RealtyForm
from commands import show_environment_configuration, show_order_requests

app = create_app()
app.secret_key = b'_ReB-9qVr-ghJ+n7+I.xu='
app.cli.add_command(show_environment_configuration)
app.cli.add_command(show_order_requests)

db_path = os.path.join(app.instance_path, 'catalog.db')
if not os.path.exists(db_path):
    with app.app_context():
        db.init_db()


@app.route('/', methods=["GET", "POST"])
def home():
    form = RealtyForm(request.form)
    if request.method == "POST" and form.validate():
        database = db.get_db()
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


if __name__ == "__main__":
    app.run(debug=os.getenv("DEVELOPMENT"))
