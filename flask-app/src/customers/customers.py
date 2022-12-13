from flask import Blueprint, request, jsonify, make_response, current_app
import json
from src import db


customers = Blueprint('customers', __name__)


# Get restaurant detail for restaurant
@customers.route('/get_details', methods=['GET'])
def get_detail_restaurant_ID():
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

## Get restaurant menu information
@customers.route('/get_menu', methods=['GET'])
def get_menu():
    cursor = db.get_db().cursor()
    cursor.execute('select * \
    from MENU JOIN RESTAURANT on RESTAURANT.restaurant_ID = MENU.restaurant_ID')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response


# Get detail for critics 
@customers.route('/cus_critics', methods=['GET'])
def get__cus_critic_details():
    cursor = db.get_db().cursor()
    cursor.execute('select critic_ID, CONCAT(firstname, " ", lastname) as name, preference,\
    descriptions, age, city from CRITIC')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# get critic review information for particular critic_ID
@customers.route('/critics_reviews', methods=['GET'])
def get_critics_review():
    cursor = db.get_db().cursor()
    cursor.execute('SELECT  avg_rating, a.critic_ID, a.restaurant_ID, b.reviewdetails, \
     b.postdate FROM \
        (SELECT AVG(trust_rating) as avg_rating, critic_ID, restaurant_ID \
        FROM REVIEW GROUP BY critic_ID, restaurant_ID) a LEFT JOIN (SELECT critic_ID, \
    restaurant_ID, reviewdetails, postdate FROM REVIEW) b \
    ON a.critic_ID = b.critic_ID AND a.restaurant_ID= b.restaurant_ID \
        WHERE b.reviewdetails IS NOT NULL')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Get favorite critics for a customer
@customers.route('/fav_critics', methods=['GET'])
def get_favorite_critic():
    cursor = db.get_db().cursor()
    cursor.execute('SELECT CRITIC.critic_ID, customer_ID, firstname, lastname, preference,\
    descriptions, age, city FROM FAVORITECRITIC JOIN \
        CRITIC ON FAVORITECRITIC.critic_ID = CRITIC.critic_ID ')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# Get favorite critics for a customer
@customers.route('/fav_restaurants', methods=['GET'])
def get_favorite_restaurant():
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM RESTAURANT \
        JOIN FAVORITERESTAURANT on RESTAURANT.restaurant_ID \
            = FAVORITERESTAURANT.restaurant_ID')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

 # Get a customer personal information
@customers.route('/customer_profile', methods=['GET'])
def get_customer_profile():
    cursor = db.get_db().cursor()
    cursor.execute('SELECT * FROM CUSTOMER')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response


    
 # Post a rating about a critics review
@customers.route('/post_ratings', methods=['POST'])
def post_rating():
    current_app.logger.info(request.form)
    cursor = db.get_db().cursor()
    critic_ID = request.form['critic_ID']
    restaurant_ID = request.form['restaurant_ID']
    rating = request.form['rating']
    query = f'INSERT INTO REVIEW(customer_ID, critic_ID, restaurant_ID, trust_rating) \
        VALUES("16283746392013648946", \"{critic_ID}\", \"{restaurant_ID}\", {rating})'
    cursor.execute(query)
    db.get_db().commit()    
    return "Success!"


# get the recommendation restaurants from critics
@customers.route('/recommendation', methods=['GET'])
def get_recommendation():
    cursor = db.get_db().cursor()
    cursor.execute('SELECT CONCAT(CRITIC.firstname, " ", CRITIC.lastname) as name, \
    RESTAURANT.names FROM RECOMMENDATION JOIN CRITIC ON RECOMMENDATION.critic_ID = CRITIC.critic_ID \
    JOIN RESTAURANT ON RECOMMENDATION.restaurant_ID = RESTAURANT.restaurant_ID')
    row_headers = [x[0] for x in cursor.description]
    json_data = []
    theData = cursor.fetchall()
    for row in theData:
        json_data.append(dict(zip(row_headers, row)))
    the_response = make_response(jsonify(json_data))
    the_response.status_code = 200
    the_response.mimetype = 'application/json'
    return the_response

# add an customer account
@customers.route('/add_customer', methods =['POST'])
def add_customer():
    current_app.logger.info(request.form)
    cursor = db.get_db().cursor()
    cus_id= request.form['customer_ID']
    birthday = request.form['birthday']
    passwords = request.form['passwords']
    username = request.form['username']
    age = request.form['age']
    numbers = request.form['numbers']
    emails = request.form['emails']
    query = f'INSERT INTO CUSTOMER(customer_ID, birthday, passwords, username, age, numbers, emails) VALUES(\"{cus_id}\", \"{birthday}\", \"{passwords}\", \"{username}\", \"{age}\", \"{numbers}\", \"{emails}\")'
    cursor.execute(query)
    db.get_db().commit()
    return "Success!"





