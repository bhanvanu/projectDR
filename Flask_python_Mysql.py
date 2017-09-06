from flask import Flask
#import psycopg2
#import react from react



app = Flask(__name__)


@app.route('/<var>')
def hello_world(var):
    return "%s" %var

#python.............................
if __name__ == '__main__': #default code
    print("ajhdg") #print to console
    #database checking.......................
    try:
        conn = psycopg2.connect("dbname='template1' user='dbuser' host='localhost' password='dbpass'")
    except:
        print "I am unable to connect to the database"
    app.run()
