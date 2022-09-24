from flask import Flask, render_template, request
import sqlite3 as sql

app = Flask(__name__, template_folder='html')

@app.route('/')
@app.route('/users')

def new_user():
    return render_template('registration.html')

@app.route('/addrec', methods= ['POST', 'GET'])
def addrec():
    if request.method == 'POST':
        try:
            e_mail = request.form('e_mail')
            user_name = request.form('user_name')
            user_psw = request.form('user_psw')
            role_id = request.form('role_id')

            with sql.connect('user_database.db') as con:
                cur = con.cursor

                cur.execute("INSERT INTO user (e-mail, user_name, user_psw, total_score, role_id) VALUES (?,?,?,?,?)",
                (e_mail, user_name, user_psw, None, role_id))

                con.commit()

                msg = 'Record successfully added'
        except:
            con.rollback()
            msg = 'Error'
        finally:
            con.close()
            return render_template('results.html', msg=msg)

if __name__ == '__main__':
    app.run(debug=True)

            


