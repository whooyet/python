from flask import Flask, render_template, request, redirect
from test import tf_scrap

app = Flask(__name__)

db = {}

@app.route('/')
def hello_world():
    return render_template("potato.html")

@app.route("/report")
def report():
    word = request.args.get('word') #검색 내용 추출
    if word:
        word = word.lower()
        ex = db.get(word)
        if ex:
            jobs = ex
        else:
            jobs = tf_scrap()
            db[word] = jobs
    # else:
    #     return redirect("/")
    return render_template("report.html",
                           searchingBy=word,
                           resultsNumber=len(jobs),
                           jobs=jobs)

#app.run()