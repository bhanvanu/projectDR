from flask import Flask
import psycopg2
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    print("ajhdg")
    try:
        conn = psycopg2.connect("dbname='template1' user='dbuser' host='localhost' password='dbpass'")
    except:
        print "I am unable to connect to the database"
    app.run()
