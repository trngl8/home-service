from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        user_name = request.form.get("name")
        user_property_type = request.form.get("type")
        user_square = request.form.get("square")
        user_bathrooms = request.form.get("bathrooms")
        user_bedrooms = request.form.get("bedrooms")
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)