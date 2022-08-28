from flask import Flask, redirect
from flask import request, make_response
from flask import render_template
from flask import url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

adminNNN = [
    "SexyNigger123PRO_VARDGES",
    "kalivhack@notgmail.com",
    "kotyaPRO"
]

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///forum.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'VardgesChat_NIGGER!'
db = SQLAlchemy(app)
name = ''


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # intro = db.Column(db.String(300), nullable=False)
    title = db.Column(db.String(75), nullable=False)
    name = db.Column(db.String(15), nullable=False, default="user")
    text = db.Column(db.Text, nullable=False)
    time = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Article %r>' % self.id


@app.route("/", methods=['GET'])
@app.route("/home", methods=['GET'])
def index():
    # if request.method == "POST":
    #     title = request.form['title']
    #     text = request.form['text']
    #
    #     responce = make_response(render_template("index.html"))
    #     responce.set_cookie('UserName', value=name)
    #     print("Responce is Done", responce)
    #
    #     article = Article(title=title, text=text)
    #
    #     try:
    #         db.session.add(article)
    #         db.session.commit()
    #
    #         print(f"Cookie of {name} is Done")
    #
    #         return redirect("/home")
    #         # return responce
    #
    #     except Exception as ex:
    #         return "An error in making comment" + str(ex)
    articles = Article.query.order_by(Article.time).all()
    # name = request.cookies.get('UserName')

    isAdmin = request.cookies.get("isAdmin")

    print(name, "is cookie")
    return render_template("index.html", articles=articles, isAdmin=isAdmin)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/createQuery", methods=['POST', 'GET'])
def createQuery():
    if request.method == "POST":
        title = request.form['title']
        # intro = request.form['intro']
        text = request.form['text']
        name = request.form['name']

        print(f"{name} sanded message :")

        article = Article(title=title, text=text, name=name)

        try:
            db.session.add(article)
            db.session.commit()

            return redirect("/home")

        except Exception as ex:
            return "An error in making comment" + str(ex)
    else:
        isAdmin = request.cookies.get("isAdmin")
        print("The user is admin: " + str(isAdmin))

        return render_template("myquery.html", isAdmin=isAdmin)


@app.route("/admin", methods=['POST', 'GET'])
def adminCheck():
    if request.method == "POST":
        data = [
            request.form['name'],
            request.form['email'],
            request.form['pat']
        ]
        # print(data, adminNNN)
        if data[0] == adminNNN[0] and data[0] == adminNNN[0] and data[0] == adminNNN[0]:
            responce = make_response(redirect("/createQuery"))
            cookie = responce.set_cookie("isAdmin", value='true')
            print("Making cookie " + str(cookie))

            return responce

        else:
            return redirect("/admin")


    else:
        return render_template("admin.html")


@app.route("/home/<int:id>/del")
def delete(id):
    article = Article.query.get_or_404(id)

    try:
        db.session.delete(article)
        db.session.commit()

        return redirect("/home")

    except:
        return "The article not found"


@app.route("/home/<int:id>/edit", methods=['GET', 'POST'])
def edit(id):
    article = Article.query.get(id)
    if request.method == 'POST':
        article.title = request.form['title']
        article.text = request.form['text']
        article.name = request.form['name']

        print(f"{name} edited message :")

        try:
            db.session.commit()

            return redirect("/home")

        except Exception as ex:
            return "An error in making comment" + str(ex)
    else:
        isAdmin = request.cookies.get("isAdmin")

        return render_template("edit.html", article=article, isAdmin=isAdmin)


if __name__ == "__main__":
    app.run(debug=True)
