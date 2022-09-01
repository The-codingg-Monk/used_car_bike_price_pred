


from flask import Flask,render_template,request,jsonify
app=Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template("About.html")

@app.route("/feedback" )
def feedback():
    return render_template("feedback.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/instruction")
def instruction():
    return render_template("instruction.html")

@app.route("/faq")
def faq():
    return render_template("faq.html")

@app.route("/submit", methods=["POST"])
def submit():
    data=request.form
    print(data)
    return render_template("sub_feed.html")






if __name__=="__main__":
    app.run(debug=True)