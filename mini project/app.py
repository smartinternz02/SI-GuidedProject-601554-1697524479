# import numpy as np
import pickle
from flask import Flask, request, render_template 
app = Flask(__name__)
 
model=pickle.load(open('C:/Users/motes_ridjwh5/OneDrive/Desktop/mini project/happiness.pkl','rb'))


# with open('C:/Users/jayac/OneDrive/Desktop/prani_miniProject/Software Industry Salary Prediction.pkl', 'wb') as f:
#     pickle.dump(rfr, f)

# with open('C:/Users/jayac/OneDrive/Desktop/prani_miniProject/Software Industry Salary Prediction.pkl', 'rb') as f:
#     model = pickle.load(f) 
@app.route('/') 
@app.route('/home', methods=['GET', 'POST']) 
def Home():
    # with app.app_context():
       return render_template("index.html")
    
    
@app.route('/happy', methods=['GET', 'POST'])
def happy():
    # with app.app_context():
       return render_template("Happy.html")
    
    
@app.route('/result', methods=['GET', 'POST'])
def result():
    # with app.app_context():
      if request.method == "POST":
         Country=request.form['Country']
         Region=request.form['Region']
         Happiness_Score=request.form['Happiness Score']
         Standard_Error=request.form['Standard Error']
         Economy=request.form['Economy (GDP per capita)']
         Family=request.form['Family']
         Health=request.form['Health (Life Expectancy)']
         Freedom=request.form['Freedom']
         Trust=request.form['Trust (Government Corruption)']
         Generosity=request.form['Generosity']
         Dystopia_Residual=request.form['Dystopia Residual']
         pred = [[float (Country), float (Region), float (Happiness_Score), float(Standard_Error),
         float (Economy), float (Family), float (Health), float (Freedom), float (Trust),
         float(Generosity), float (Dystopia_Residual)]]
         print(pred)
         output = model.predict(pred)
         print(output)
         
         return render_template("Prediction.html",output=output)
         
      
if _name_ == '_main_':
   app.run(debug=True)
#    Home()
#    Result()