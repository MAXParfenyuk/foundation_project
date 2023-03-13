from flask import Flask, render_template

app = Flask(__name__)

# Define routes for each HTML file
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/account')
def account():
    return render_template('account.html')

@app.route('/bet_history')
def bet_history():
    return render_template('bet_history.html')

@app.route('/game')
def game():
    return render_template('game.html')

@app.route('/rules')
def rules():
    return render_template('rules.html')

# Define a dynamic route that changes the contents of the page based on the parameter passed in the URL (I am not sure how to do that)
@app.route('/user/<username>')
def user_profile(username):
    # fetch user data from database using the username parameter
    user_data = get_user_data(username)
    
    # render the user profile page with the user data
    return render_template('user_profile.html', user=user_data)

if __name__ == '__main__':
    app.run(debug=True)
