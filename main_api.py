

import sqlalchemy as sa
import pandas as pd
engine=sa.create_engine("mysql+pymysql://root:hindustaan@localhost:3306/bike_car_project")

from flask import Flask,render_template,request,jsonify,json
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
    data=dict(request.form)
    s1=pd.Series(data)
    df1=pd.DataFrame([s1["Name"]])
    df1.columns=[list(s1.index)[0]]
    df2=pd.DataFrame([s1["Feedback"]])
    df2.columns=[list(s1.index)[1]]
    df=pd.concat([df1,df2],axis=1)

    df.to_sql(name="feedback",con=engine,index=False,if_exists="append")
    
    
    return render_template("sub_feed.html")






if __name__=="__main__":
    app.run(host="0.0.0.0",port=8080,debug=False)