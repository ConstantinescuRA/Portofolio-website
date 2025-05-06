from flask import Flask, render_template, url_for, request
import mysql.connector
app =Flask(__name__)
def get_db_connection():
    connection = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'constantinescu2005',
        database = 'portofolio',
        port = 3307

        
    )
    return connection

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/contact-me", methods =  ['Get','POST'])
def get_started():

    if request.method == "POST":
        first_name = request.form["firstName"]
        last_name = request.form["lastName"]
        email = request.form["email"]
        message = request.form["message"]

        


        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO informations (first_name, last_name, email, message) VALUES (%s, %s, %s, %s)",
                (first_name, last_name, email, message),
            )
            conn.commit()
            cursor.close()
            conn.close()
            return "Mesaj trimis cu succes!"
        except Exception as e:
            return f"Eroare: {e}"





    return render_template("contact-me.html")


if __name__=='__main__':
    app.run(debug=True, port=8080)