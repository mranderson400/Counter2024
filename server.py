from flask import Flask, render_template, session, redirect
app = Flask(__name__)  
app.secret_key = 'kcaaaarrrlll' # set a secret key for security purposes




@app.route('/counter')
def count_refreshes():
    
    if 'counter' not in session:
        session['counter'] = 0 
        #   Counter the number variable increments because of session 
        #     and session gets counter from html
        # session creates cookie and saves data
    else:
        session['counter'] += 1 
    
    
    return render_template('counter.html')

@app.route('/')
def home():
    username = "Robert Anderson"  
    bio = "Software developer with a passion for web development and open source."
    projects = ["count_refreshes", "daryl", "portfolio"]  
    
    return render_template('home.html', username=username, bio=bio, projects=projects)
    
@app.route('/daryl')
def daryl():
    return render_template('daryl.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')



@app.route('/destroy_session')          
def destroy():
    
    session.clear()
    return count_refreshes()


if __name__ == "__main__":
    app.run(debug=True, port=1024, host="0.0.0.0")

