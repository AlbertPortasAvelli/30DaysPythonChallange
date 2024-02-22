from flask import Flask, render_template, request, redirect, url_for, jsonify
import pymongo
from bson.objectid import ObjectId

app = Flask(__name__)

# Connect to MongoDB
MONGODB_URI = 'mongodb+srv://albertportasavelli:.85WpchLTgGqQuS@30daysofpython.rjrgfc6.mongodb.net/gamebuster'
client = pymongo.MongoClient(MONGODB_URI)
db = client.get_database('Gamebuster')
games_collection = db.games
members_collection = db.members
rentals_collection = db.rentals

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_game', methods=['GET', 'POST'])
def add_game():
    if request.method == 'POST':
        game_title = request.form['game_title']
        game_platform = request.form['game_platform']
        game_genre = request.form['game_genre']
        game_rating = request.form['game_rating']
        game_description = request.form['game_description']
        game_image = request.form['game_image']

        # Insert new game into MongoDB
        games_collection.insert_one({
            'title': game_title,
            'platform': game_platform,
            'genre': game_genre,
            'rating': game_rating,
            'description': game_description,
            'image': game_image,
            'available': True  # Set game as available for rent
        })
        return redirect(url_for('add_game'))

    return render_template('add_game.html')

@app.route('/add_member', methods=['GET', 'POST'])
def add_member():
    if request.method == 'POST':
        member_name = request.form['member_name']
        member_surname = request.form['member_surname']
        member_email = request.form['member_email']
        member_phone = request.form['member_phone']
        member_credit_card = request.form['member_credit_card']

        # Insert new member into MongoDB
        members_collection.insert_one({
            'name': member_name,
            'surname': member_surname,
            'email': member_email,
            'phone': member_phone,
            'credit_card': member_credit_card
        })
        return redirect(url_for('add_member'))

    return render_template('add_member.html')

@app.route('/list_members')
def list_members():
    # Retrieve all members from MongoDB
    members = members_collection.find()
    return render_template('list_members.html', members=members)

@app.route('/games')
def games():
    # Retrieve all games from MongoDB
    games = games_collection.find()
    return render_template('games.html', games=games)

@app.route('/rent', methods=['GET', 'POST'])
def rent():
    if request.method == 'POST':
        selected_games = request.form.getlist('game')  # Get selected games
        renter_name = request.form['renter_name']
        rental_days = int(request.form['rental_days'])

        # Update game availability and record rental
        for game_id in selected_games:
            game = games_collection.find_one({'_id': ObjectId(game_id)})
            if game and game['available']:
                games_collection.update_one({'_id': ObjectId(game_id)}, {'$set': {'available': False}})
                rentals_collection.insert_one({
                    'game_id': game_id,
                    'renter_name': renter_name,
                    'rental_days': rental_days
                })

        return redirect(url_for('games'))

    # Retrieve available games for rent
    available_games = games_collection.find({'available': True})
    unavailable_games = games_collection.find({'available': False})
    return render_template('rent.html', available_games=available_games, unavailable_games = unavailable_games)


@app.route('/search_members')
def search_members():
    name = request.args.get('name', '')
    members = members_collection.find({'name': {'$regex': f'^{name}', '$options': 'i'}})
    return jsonify([str(member['_id']) for member in members])



if __name__ == '__main__':
    app.run(debug=True)
