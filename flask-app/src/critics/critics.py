from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db


critics = Blueprint('critics', __name__)

# Get all the critics' information from the database
@critics.route('/critic_profile', methods=['GET'])
def get_critic_profile():
    # get a cursor object from the database
    cursor = db.get_db().cursor()
    # use cursor to query the database for a list of critics
    cursor.execute('select *, CONCAT(firstname, " ", lastname) as name from CRITIC')
    # grab the column headers from the returned data
    row_headers = [x[0] for x in cursor.description]
    # create an empty dictionary object to use in
    # putting column headers together with data
    json_data = []
    # fetch all the data from the cursor
    theData = cursor.fetchall()
    # for each of the rows, zip the data elements together with
    # the column headers.
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return jsonify(json_data)

# Get restaurant detail for restaurant with particular restaurantID
@critics.route('/details', methods=['GET'])
def detail_restaurant_ID():
    cursor = db.get_db().cursor()
    cursor.execute('select * from RESTAURANT')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response


 # Post a review 
@critics.route('/post_reviews', methods=['POST'])
def post_review():
    current_app.logger.info(request.form)
    cursor = db.get_db().cursor()
    critic_ID = request.form['critic_ID']
    restaurant_ID = request.form['restaurant_ID']
    review = request.form['review']
    query = f'INSERT INTO REVIEW(customer_ID, critic_ID, restaurant_ID, reviewdetails, postdate, rating) \
        VALUES("16283746392013648946", \"{critic_ID}\", \"{restaurant_ID}\", \"{review}\", CURDATE(), 2.5)'
    cursor.execute(query)
    db.get_db().commit()    
    return "Success!"


  # Add a restaurant recommendation
@critics.route('/add_recommendation', methods=['POST'])
def add_recommendation():
    current_app.logger.info(request.form)
    cursor = db.get_db().cursor()
    critic_ID = request.form['critic_ID']
    restaurant_ID = request.form['restaurant_ID']
    query = f'INSERT INTO RECOMMENDATION(critic_ID, restaurant_ID) \
        VALUES(\"{critic_ID}\", \"{restaurant_ID}\")'
    cursor.execute(query)
    db.get_db().commit()    
    return "Success!"
   
# add an critic
@critics.route('/add_critic', methods =['POST']) 
def add_critics():
    current_app.logger.info(request.form)
    cursor = db.get_db().cursor()
    critic_ID= request.form['critic_ID']
    firstname = request.form['firstname']
    lastname = request.form['lastname']
    preference = request.form['preference']
    age = request.form['age']
    city = request.form['city']
    zip = request.form['zip']
    street = request.form['street']
    states = request.form['states']
    birthday = request.form['birthday']
    descriptions = request.form['description']
    numbers = request.form['numbers']
    emails = request.form['emails']
    query = f'INSERT INTO CRITIC(critic_ID, firstname, lastname, preference, \
        age, city, zip, street, states, birthday, \
            descriptions, numbers, emails) \
                VALUES(\"{critic_ID}\", \"{firstname}\", \"{lastname}\", \"{preference}\",\
                     \"{age}\", \"{city}\", \"{zip}\", \"{street}\", \"{states}\", \
                     \"{birthday}\", \"{descriptions}\", \"{numbers}\", \"{emails}\")'
    cursor.execute(query)
    db.get_db().commit()
    return "Success!"


