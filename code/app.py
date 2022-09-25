from crypt import methods
import email
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
    return render_template('layout.html')

@app.route('/add_user', methods=['POST'])
def new_user():
    try:
        db = getattr(g, '_database', None)
        if db is None:
            db = g._database = sql.connect('user_database.db')
        cursor = db.cursor()

        e_mail = request.form['e_mail']
        if(len(e_mail) == 0):
            print('Please enter email')
            return render_template('layout.html')
        user_name = request.form['user_name']
        if(len(user_name) < 3):
            print('User name must contain at least 3 characters')
            return render_template('layout.html')
        user_psw = request.form['user_psw']
        if(len(user_name) == 0):
            print('Please enter password')
            return render_template('layout.html')
        encrypted = hl.md5(user_psw.encode()).hexdigest()

        cursor.execute("INSERT INTO user (email, user_name, user_psw, total_score, role_id) VALUES (?,?,?,?,?)",
        (e_mail, user_name, encrypted,0,2))

        db.commit()

    except:
        db.rollback()
    finally:
        db.close()

    return render_template('layout.html')

@app.route('/login', methods=["POST","GET"])
def login():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sql.connect('user_database.db')
    cursor = db.cursor()


    session["email"] = request.form['login_email']
    session["psw"] = request.form['login_psw']
    encrypted = hl.md5(session["psw"].encode()).hexdigest()

    cursor.execute("SELECT user_name FROM user WHERE email = ? AND user_psw = ?",(session["email"],encrypted))
    record = cursor.fetchone()
    if record is not None:
        session["user_name"] = record[0]
        cursor.execute("SELECT total_score, role_id FROM user WHERE user_name = ?",(session["user_name"],))
        user = cursor.fetchone()
        session["total_score"] = user[0]
        session["role_id"] = user[1]
        return render_template('game.html', user_name=session["user_name"], total_score=session["total_score"], role_id=session["role_id"])
    return render_template('layout.html')

@app.route('/logout', methods=['POST', 'GET'])
def logout():
    session["user_name"] = None
    session["total_score"] = None
    session["email"] = None
    session["psw"] = None

    return render_template('layout.html')

@app.route('/admin', methods=['POST', 'GET'])
def admin():
    session["users"] = get_users()

    return render_template('admin.html',users=session["users"])

@app.route('/back_from_admin', methods=['POST'])
def go_back(): 
    return render_template('game.html', user_name=session["user_name"], total_score=session["total_score"], role_id=session["role_id"])

@app.route('/claimpoints', methods=['POST'])
def claim():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sql.connect('user_database.db')
    cursor = db.cursor()
    try:
        cursor.execute('UPDATE user SET total_score = (total_score + 10) WHERE email = ?',(session['email'],))
        session["total_score"] += 10
        db.commit()
    except:
        db.rollback()

    return render_template('game.html', user_name=session["user_name"], total_score=session["total_score"], role_id=session["role_id"])

@app.route('/delete_users', methods=['POST'])
def remove_users():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sql.connect('user_database.db')
    cursor = db.cursor()

    checked_users = request.form.getlist("check")

    for email in checked_users:
        for user in session["users"]:
            if user[0] == email:
                try:
                    cursor.execute('DELETE FROM user WHERE email = ?',(email,))
                    db.commit()

                    index = session["users"].index(user)
                    session["users"].pop(index)

                except:
                    db.rollback()


    return admin()

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

            


