from flask import Flask,render_template,request,url_for,redirect

#for database starts
from  models import db,Details
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1122@localhost/test_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)
#here ends

@app.route('/')
def show():
    all_details = Details.query.all()
    return render_template('show.html',detail =all_details)

@app.route("/details/add", methods=['GET', 'POST'])
def det_add():
    if request.method == 'POST':

        name = request.form['user_name']
        age = request.form['age']
        new_details = Details(name = name, age = age)
        db.session.add(new_details)
        db.session.commit()
    
    return render_template('details.html')



@app.route('/details/edit/<int:id>', methods=['GET', 'POST'] )
def edit(id):
    data=Details.query.get(id)
    if request.method == 'POST':
        data.name = request.form['user_name']
        data.age = request.form['age']
        db.session.commit()
    return render_template('edit.html',detail=data)

@app.route('/details/delete/<int:id>')
def delete(id):

    datas = Details.query.get(id)
    db.session.delete(datas)
    db.session.commit()

    return redirect(url_for('show'))
    


if __name__ == "__main__":
    app.run(debug=True)
