from flask import Flask, render_template, url_for, request

app = Flask(__name__,static_url_path='/static')


@app.route('/',methods=['GET','POST'])
def Online_Shop():
    return render_template('Online_Shop.html')

@app.route('/login/',methods=['GET','POST'])
def login():
	return render_template('login.html')

@app.route('/signup/',methods=['GET','POST'])	
def signup():
	return render_template('signup.html')

@app.route('/about/', methods=['GET','POST'])
def about():
	return render_template('about.html', methods=['GET','POST'])

@app.route('/items/')
def items():
	return render_template('items.html', methods=['GET','POST'])

if __name__ == '__main__':
    app.run(debug=True)