from flask import Flask, render_template,request, url_for, redirect
app = Flask(__name__)


@app.route('/')
def homepage():
   return render_template('homepage.html')


@app.route('/page1')
def page1():
   return render_template('page1.html')


@app.route('/page2')
def page2():
   return render_template('page2.html')


@app.route('/page3')
def page3():
   return render_template('page3.html')



if __name__ == '__main__':
   app.run()
