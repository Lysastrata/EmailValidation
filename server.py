from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'email_validation')
app.secret_key = 'KeepItSecretKeepItSafe'
@app.route('/')
def index():
    query = 'select * from email'
    emails = mysql.query_db(query)
    return render_template('index.html', all_emails=emails)
@app.route('/validate', methods=['POST'])
def validate():
    query = "select email from email where email = :email limit 1"
    data= {
    'email': request.form['email']
    }
    emails = mysql.query_db(query, data)
    if len(emails) <1 :
        flash('email is not valid')
        return redirect('/')
    else:
        flash('The email you entered ('+ request.form["email"] +') is valid')
        return render_template('valid.html', all_emails=emails)
app.run(debug=True)
