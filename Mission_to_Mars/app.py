from flask import Flask, render_template, redirect
import pymongo
import scrape_mars

app = Flask(__name__)

# Create connection variable
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

# Set route
@app.route('/')
def index():
    data_from_mongo=client.mars_db.mars.find_one()
    if data_from_mongo: 
        return render_template('index.html', data_from_flask=data_from_mongo)
    else: 
        return 'No Data'

@app.route('/scrape')
def scrape():
    mars_data = scrape_mars.scrape()
    print(mars_data)
    client.mars_db.mars.update({}, mars_data, upsert= True)
    return redirect('/')



if __name__ == "__main__":
    app.run(debug=True)
