from flask import Flask, redirect, url_for, request, render_template

#import psycopg2
#import react from react


#Note by default (without template_folder) it searches for html in the templates folder
# but since i created the html files under project not inside templates or statics i need
# to provide path for index files

# app = Flask(__name__, template_folder='/Users/tech/PycharmProjects/Flask_python_Mysql')
app = Flask(__name__)
@app.route('/')
def index_page():
   return render_template('index_page.html')
if __name__ == '__main__':
    # app.debug = True
    app.run()


