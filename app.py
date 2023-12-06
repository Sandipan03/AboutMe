from flask import Flask, render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
sandy = Flask(__name__)
sandy.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///sandy.db"
sandy.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(sandy)
class Sandy(db.Model):
    name =  db.Column(db.String(100), primary_key=True)
    # gender=  db.Column(db.String(7), nullable=False)
    email= db.Column(db.String(100), nullable=False)
    phone= db.Column(db.Integer,nullable=False)
    country =  db.Column(db.String(50), nullable=False)
    desc =  db.Column(db.String(1000), nullable=True)

@sandy.route('/',methods=['GET','POST'])
def mainf():
    if request.method=='POST':
        name=request.form['name']
        # Gender=request.form['Gender']
        email=request.form['email']
        phone=request.form['phone']
        country=request.form['country']
        desc=request.form['desc']
        print(name)
        s1= Sandy(name=name,email=email,phone=phone,country=country,desc=desc)
        db.session.add(s1)
        db.session.commit()
        return redirect("/ThankYou")
    return render_template('sandy.html')
@sandy.route('/ThankYou')
def thanks():
    return render_template('thankspage.html')
if __name__=="__main__":
    sandy.run(debug=True)