
from flask import Flask,jsonify,request,render_template
from matplotlib.offsetbox import DEBUG
from project_app.utils import MedicalInsurance

import config

app = Flask(__name__)
#############################################################################################
################################ Home API ###################################################
#############################################################################################

@app.route("/")   # Home API
def hello_flask():
    print("Welcome to flask")
    #return "Hello Python"
    return render_template('user.html')
    

#############################################################################################
################################ Test API ###################################################
#############################################################################################
@app.route('/predict_charges',methods =['POST'])
def get_insurance_charges():

    
    age  = float(request.form.get('age'))
    sex  = request.form.get('sex')
    bmi  = float(request.form.get('m')) 
    children =float(request.form.get('children'))
    smoker = request.form.get('smoker')
    region = request.form.get('region')

    med_ins = MedicalInsurance(age,sex,bmi,children,smoker,region)
    charges = med_ins.get_predict_charges()

    return '''<html>
    <head></head>
    <center>
    <body style="background-color:rgb(204, 128, 141);">
    <p style="font-size:40px ; ">
    
    <label>PREDICTED MEDICAL INSURANCE CHARGES IS : %(charges)s </label><br>            
    </body>
    </center>
</html>
''' % locals()



if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080)  # server start