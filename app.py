from flask import Flask, render_template, request
import my_sql

app = Flask(__name__)

"""

"""


@app.route("/")
def index():
    return render_template('main_page.html')


@app.route("/data", methods=["GET", "POST"])
def data():
    my_list = my_sql.all_data()
    return render_template('data.html', list_my=my_list)


@app.route("/login", methods=["GET", "POST"])
def login():
    #
    email = request.form.get("email")
    password = request.form.get("password")

    my_bool = my_sql.search_list(email, password)

    if my_bool:
        return render_template('login_page.html', email=email, password=password)
    else:
        return render_template('login_page.html')


@app.route("/register", methods=["GET", "POST"])
def register():
    my_name = request.form.get("name")
    my_email = request.form.get("email")
    my_password = request.form.get("password")
    my_sql.add(my_name, my_email, my_password)

    return render_template('register.html', name=my_name, email=my_email, password=my_password)


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=8080)
