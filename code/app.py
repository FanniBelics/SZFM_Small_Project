import sqlite3 as sql

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
    print(session["users"],session["images"],session["levels"],session["roles"],session["userlevels"])
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
        print('USER PSW: ',user_psw)

        
        

        cursor.execute("INSERT INTO user (email, user_name, user_psw, total_score, role_id) VALUES (?,?,?,?,?)",
        (e_mail, user_name, user_psw,0,2))

        db.commit()

        msg = 'Record successfully added'
    except:
        db.rollback()
        msg = 'Error'
    finally:
        print(msg)
        db.close()

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

@app.route('/addrec', methods= ['POST', 'GET'])
def addrec():
    if request.method == 'POST':
        try:
            e_mail = request.form('e_mail')
            user_name = request.form('user_name')
            user_psw = request.form('user_psw')

            with sql.connect('user_database.db') as con:
                cur = con.cursor

                cur.execute("INSERT INTO user (e-mail, user_name, user_psw, total_score, role_id) VALUES (?,?,?,?,?)",
                (e_mail, user_name, user_psw, None, 2))

                con.commit()

                msg = 'Record successfully added'
        except:
            con.rollback()
            msg = 'Error'
        finally:
            print(msg)
            con.close()

if __name__ == '__main__':
    app.run(debug=True)

            


