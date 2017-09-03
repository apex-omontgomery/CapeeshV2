from database.models import db, pick_words
from flask import Flask, render_template, jsonify

application = Flask(__name__)
application.config.from_object('config')
db.init_app(application)

'''
1. Get five words- if don't have the audio of word- request it. 
2. Ask how to spell or read
2a. wait 5 seconds for response (exit, repeat, <some answer>
2b. if response is seen in 5 seconds extend to 3 seconds. 

3. Get google results, 




'''





# encode in rest_url, or post a body (html/ json) http post-> get a body
@application.route('/')
def main():
    return render_template('index.html')    
    
    
@application.route('/showSignUp')
def showSignUp():
    return render_template('start.html')
    
    
@application.route('/NewPlayer')
def new_Player():
    return render_template('Waiting_Response.html')
    #request echo to ask for name and grade level
    # get data from echo, try to make database. 
    # if return None (duplicate) then you ask for them to chose different nickname
    
@application.route('/fivewords/<int:user_level>')
def five_words(user_level):
    print('here are 5 words')
    return jsonify(results = pick_words(user_level))        
        
        
@application.route('/Continue')
def Continue():
    return render_template('Waiting_Response.html')
    # send request to echo for user name. 
    # look up person, if cannot find prompt again
    # if user not entered:
    #   new_player()
    
    
    
if __name__ == "__main__":
    app.run(debug= True)