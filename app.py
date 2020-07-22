from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
#this will tell where our database is located
#from here we can use like postgres
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'  #the three slashes means that it will reside inside the project
#initializing the database with the settings of the app
db = SQLAlchemy(app)

# this is specific for sqlite
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id





# to set up routes you use the @ symbol
@app.route('/', methods=['POST','GET'])

def index():
    if request.method == 'POST':
        # task_content = request.form['content']
        # new_task = Todo(content=task_content)

        # try:
        #     db.session.add(new_task)
        #     db.session.commit()
        #     return redirect('/')
        # except:
        #     return "there was an issue returning task"
        pass
    else:
        #tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template('index.html')

   


if __name__ == "__main__":
    app.run(debug=True)




#https://www.youtube.com/watch?v=Z1RJmh_OqeA&t=287s
#link to guide of lesson. Still incomplete