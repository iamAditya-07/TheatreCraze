from flask import *
import random
import os
from authy.api import AuthyApiClient
app = Flask(__name__)
app.secret_key = "aps52@123"
from appwrite.services.databases import Databases
import json

"""class SetEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, set):
            return list(obj)
        return json.JSONEncoder.default(self, obj)"""

#@app.route("/")
#def home():
    #return render_template('home.html')

#@app.route("/", methods=['GET','POST'])
#def func_test():
    #if request.m   ethod == 'POST':
        #text = request.form['Value1']
        #return render_template('test.html', value1=text)

@app.route("/",methods=['GET','POST'])
def home():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        #height = request.form["height"]
        #weight = request.form["weight"]
        phone = request.form["phone"]
        #city = request.form["city"]
        #set = {email, password}
        #json_set = json.dumps(list(set))

        #list = ['PARVATASANA','ARDHA TITALI ASANA','GATYATMAK MERU','SIDEWAYS VIEWING','MAKARASANA','PADMASANA','VAJRASANA','ARDHA','YOGAMUDRASANA','BHUJANGASANA','SAITHALYASANA','BHU NAMANASANA','SARVANGASANA']

        #data = request.get_json()
        # print(request.form["name"])
        # print(request.form["email"])
        # return
        #age = request.form["age"]
        #gender = request.form["gender"]
        #height = request.form["height"]
        #weight = request.form["weight"]
        #return 
        #print("MAKARASANA")
        #text = request.form['Value1']
        #return render_template('home.html', value1=text)
        """n = 2
        i=0
        newlist=[]
        for i in range(n):
            x = random.choice(list)
            newlist.append(x)"""
        #return (newlist[0] + "Second yoga is:" + newlist[1])
        #session['var'] = newlist[0]
        #return redirect(url_for('submitted'))
        #X = newlist[0]
        #Z = newlist[1]
        
        """dict={'Delhi':'For Delhi - Prickly Heat Rash, Dehydration, Heat Stroke and Viral Infections',
        'Mumbai':'For Mumbai - Prickly Heat Rash, Dehydration, Heat Stroke and Viral Infections',
        'East Region':'For East Region - Prickly Heat Rash, Dehydration, Heat Stroke and Viral Infections',
        'Lucknow':'For Lucknow - Prickly Heat Rash, Dehydration, Heat Stroke and Viral Infections',
        'Kolkata':'For Kolkata - Prickly Heat Rash, Dehydration, Heat Stroke and Viral Infections'
        }s

        my_city = dict.get(city)"""
        from twilio.rest import Client
        account_sid = os.environ['TWILIO_ACCOUNT_SID']='ACae80370ac839f7515e545853177926f0'
        auth_token = os.environ['TWILIO_AUTH_TOKEN'] = '52ecffe594b042697e33bbd5c6ea239a'
        
        client = Client(account_sid, auth_token)

        #service = client.verify.v2.services.create(friendly_name='VerifyService')

        verification = client.verify \
                     .v2 \
                     .services('VAaf1132af1d2b1fe2b9f522c514718c29') \
                     .verifications \
                     .create(to='+91'+phone, channel='sms')

        print(verification.sid)

        
        myJson = {"email":email, "password":password}
        myObj = json.dumps(myJson)

        #print(message.sid)

        """authy_api = AuthyApiClient("YOUR_AUTHY_API_KEY")

        sms = authy_api.users.request_sms(authy_id)

        res = authy_api.phones.verification_start(
        phone_number=phone, 
        country_code=91, 
        via='sms')

        if res.ok():
            message = client.messages \
                .create(
                     body="Welcome to Theatre world",
                     from_='+18123591157',
                     to='+91' + phone
                 )
            print(message)"""
        from appwrite.client import Client
        newclient = Client()

        (newclient
        .set_endpoint('http://localhost/v1')
        .set_project('6381fd34959232db320f')
        .set_key('e42ed964ae01a8f890c2fb070116249293c37a096a18a13caf5dc98bd7f1e77e95e4b91041f8bbe2bd60e924629413dfb371dece93195c8520850e4976320367ecd62bcabe82dec18b737547ecd292db1d5e24f6e8d62d2642d0d105e9918e348931cb845b81a6e11c1a5342b035586a87a07698d4d8f52f1b2f6d7571276eba')
        )# Your API Endpoint

        """newclient.set_endpoint('http://localhost/v1') # Your API Endpoint
        newclient.set_project('6381fd34959232db320f')# Your project ID
        newclient.set_key('e42ed964ae01a8f890c2fb070116249293c37a096a18a13caf5dc98bd7f1e77e95e4b91041f8bbe2bd60e924629413dfb371dece93195c8520850e4976320367ecd62bcabe82dec18b737547ecd292db1d5e24f6e8d62d2642d0d105e9918e348931cb845b81a6e11c1a5342b035586a87a07698d4d8f52f1b2f6d7571276eba') #Your Secret API Key"""
        

        databases = Databases(newclient)
        result = databases.create_document('abc123', 'pqr123','newlydoc123', myObj)
        
        #session['my_var'] = X
        #session['new_var'] = Z

        return redirect(url_for('submitted'))
        #session['my_var'] = 'my_value'
        #return redirect(url_for('b'))

    return render_template('home.html')
        
        #for i in range(n):
            #return (newlist[i])

        #return "Recommended yogas are:"
        #return render_template('home.html', value1 = value1)
        #return "Your suggested yoga is"
    #return render_template('home.html')

@app.route('/submitted')
def submitted():
    #my_var = session.get('my_var',None)
    #new_var = session.get('new_var',None)
    #x = "Recommended yogas for you are:\n 1.PARVATASANA \n 2.MAKARASANA \n 3.ARDHA"
    return render_template('page1.html')

@app.route('/music_')
def music():
    return render_template('discover_music.html')

@app.route('/plays_')
def plays():
    return render_template('discover_plays.html')

@app.route('/dramas_')
def dramas():
    return render_template('discover_dramas.html')

if __name__ == "__main__":
    app.run(debug=True)