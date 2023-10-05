import pickle
from flask import Flask,request

model_pk=open('./classifier.pkl','rb')
clf=pickle.load(model_pk)

app = Flask(__name__)


@app.route("/ping")
def ping():
    return "This is ping"

@app.route("/predict")
def predict():

    loan_application=request.get_json()

    if loan_application['Gender']=='Male':
        Gender=0
    else:
        Gender=1
    
    if loan_application['Married']=='Unmarried':
        Married=0
    else:
        Married=1

    if loan_application['Credit_History']=='Unclear Debts':
        Credit_History=0
    else:
        Credit_History=1

    loanamount=loan_application['LoanAmount']
    ApplicantIncome=loan_application['ApplicantIncome']

    prediction = clf.predict([[Gender,Married,ApplicantIncome,loanamount,Credit_History]])
    

    if prediction[0]==0:
        pred='Rejected'
    else:
        pred='Accepted'
    print(prediction)
    return pred