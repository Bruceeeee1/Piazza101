from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db


restaurants = Blueprint('restaurants', __name__)

# Get all the announcement for a particular restaurant
@restaurants.route('/announcement', methods=['GET'])
def get_announcement():
    cursor = db.get_db().cursor()
    cursor.execute('select ANNOUNCEMENT.restaurant_ID, a_time, a_details from ANNOUNCEMENT \
    JOIN RESTAURANT on ANNOUNCEMENT.restaurant_ID = RESTAURANT.restaurant_ID')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Get the reviews for a particular restaurant
@restaurants.route('/reviews', methods=['GET'])
def get_reviews():
    cursor = db.get_db().cursor()
    cursor.execute('select critic_ID, postdate, AVG(trust_rating) as avg_rating, reviewdetails from REVIEW \
    JOIN RESTAURANT on REVIEW.restaurant_ID = RESTAURANT.restaurant_ID \
    GROUP BY critic_ID, postdate, reviewdetails')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# add a menu for the restaurant
@restaurants.route('/add_menu', methods =['POST'])
def add_menu():
    current_app.logger.info(request.form)
    cursor = db.get_db().cursor()
    restaurant = request.form['restaurant_ID']
    new_menu = request.form['dish_ID']
    new_price = request.form['prices']
    query = f'INSERT INTO MENU(restaurant_ID, dish_ID, prices) VALUES(\"{restaurant}\", \"{new_menu}\", \"{new_price}\")'
    cursor.execute(query)
    db.get_db().commit()
    return "Success!"

# add an announcement for the restaurant
@restaurants.route('/add_annouce', methods =['POST'])
def add_annouce():
    current_app.logger.info(request.form)
    cursor = db.get_db().cursor()
    restaurant= request.form['restaurant_ID']
    time = request.form['a_time']
    details = request.form['a_details']
    query = f'INSERT INTO ANNOUNCEMENT (restaurant_ID, a_time, a_details) VALUES(\"{restaurant}\", \"{time}\", \"{details}\")'
    cursor.execute(query)
    db.get_db().commit()
    return "Success!"


# create a new restaurant
@restaurants.route('/add_restaurant', methods =['POST'])
def add_restaurant():
    current_app.logger.info(request.form)
    cursor = db.get_db().cursor()
    restaurant= request.form['restaurant_ID']
    city = request.form['city']
    zip = request.form['zip']
    street = request.form['street']
    states = request.form['states']
    emails = request.form['emails']
    numbers = request.form['numbers']
    cuisine = request.form['cuisine']
    names = request.form['names']
    description = request.form['description']
    openinghours = request.form['openinghours']
    query = f'INSERT INTO RESTAURANT(restaurant_ID, city, zip, street, \
        states, emails, numbers, cuisine, names, descriptions,\
             openinghours) VALUES(\"{restaurant}\", \"{city}\", \"{zip}\", \"{street}\" \
                ,  \"{states}\",  \"{emails}\",  \"{numbers}\",  \"{cuisine}\", \
                     \"{names}\",  \"{description}\",  \"{openinghours}\")'
    cursor.execute(query)
    db.get_db().commit()
    return "Success!"