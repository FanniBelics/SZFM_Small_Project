import sqlite3 as sql
import hashlib as hl
from flask import Flask, g, render_template, request, session

app = Flask(__name__, template_folder='html')
app.secret_key = '42069'

@app.route('/')
def index():
    session["users"] = get_users()
    session["images"] = get_images()
    session["levels"] = get_levels()
    session["roles"] = get_roles()
    session["userlevels"] = get_userlevel()
    #print(session["users"],session["images"],session["levels"],session["roles"],session["userlevels"])
    return render_template('layout.html')

@app.route('/add_user', methods=['POST'])
def new_user():
    try:
        db = getattr(g, '_database', None)
        if db is None:
            db = g._database = sql.connect('user_database.db')
        cursor = db.cursor()

        e_mail = request.form['e_mail']
        print('USER EMAIL: ',e_mail)
        user_name = request.form['user_name']
        print('USER NAME: ',user_name)
        user_psw = request.form['user_psw']
        encrypted = hl.md5(user_psw.encode()).hexdigest()
        print('USER PSW: ',user_psw, ' ENCODED: ',encrypted)

        
        

        cursor.execute("INSERT INTO user (email, user_name, user_psw, total_score, role_id) VALUES (?,?,?,?,?)",
        (e_mail, user_name, encrypted,0,2))

        db.commit()

        msg = 'Record successfully added'
    except:
        db.rollback()
        msg = 'Error'
    finally:
        print(msg)
        db.close()

    return render_template('layout.html')

@app.route('/login', methods=["POST","GET"])
def login():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sql.connect('user_database.db')
    cursor = db.cursor()

    email = request.form['login_email']
    psw = request.form['login_psw']
    encrypted = hl.md5(psw.encode()).hexdigest()

    print('EMAIL: ',email,' PSW: ',psw, ' ENCRYPTED: ',encrypted)

    cursor.execute("SELECT user_name FROM user WHERE email = ? AND user_psw = ?",(email,encrypted))
    record = cursor.fetchone()
    if record is not None:
        session["user_name"] = record[0]
        print(session["user_name"])
        cursor.execute("SELECT total_score FROM user WHERE user_name = ?",(session["user_name"],))
        session["total_score"] = cursor.fetchone()[0]
        print('USER NAME: ',session["user_name"], 'SCORE: ',session["total_score"])
        return render_template('game.html', user_name=session["user_name"], total_score=session["total_score"])
    return render_template('layout.html')

def get_users():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sql.connect('user_database.db')
    cursor = db.cursor()
    cursor.execute('SELECT * FROM user')
    return cursor.fetchall()

def get_images():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sql.connect('user_database.db')
    cursor = db.cursor()
    cursor.execute('SELECT * FROM image')
    return cursor.fetchall()

def get_levels():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sql.connect('user_database.db')
    cursor = db.cursor()
    cursor.execute('SELECT * FROM level')
    return cursor.fetchall()

def get_roles():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sql.connect('user_database.db')
    cursor = db.cursor()
    cursor.execute('SELECT * FROM roles')
    return cursor.fetchall()

def get_userlevel():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sql.connect('user_database.db')
    cursor = db.cursor()
    cursor.execute('SELECT * FROM user_level')
    return cursor.fetchall()

if __name__ == '__main__':
    app.run(debug=True)

            


