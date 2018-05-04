#!/usr/bin/env python3
'''
    json_to_tables.py
    Jeff Ondich, 24 April 2017

    Sample code illustrating a simple conversion of the
    books & authors dataset represented as in books.json,
    into the books, authors, and books_authors tables (in
    CSV form).
'''
import sys
import flask
import json

app = flask.Flask(__name__)

# Who needs a database when you can just hard-code some actors and movies?
actors = [
    {'last_name': 'Pickford', 'first_name': 'Mary'},
    {'last_name': 'Rains', 'first_name': 'Claude'},
    {'last_name': 'Lorre', 'first_name': 'Peter'},
    {'last_name': 'Greenstreet', 'first_name': 'Sydney'},
    {'last_name': 'Bergman', 'first_name': 'Ingrid'},
    {'last_name': 'Welles', 'first_name': 'Orson'},
    {'last_name': 'Colbert', 'first_name': 'Claudette'},
    {'last_name': 'Adams', 'first_name': 'Amy'}
]

movies = [
    {'title': 'Casablanca', 'year': 1942, 'genre': 'drama'},
    {'title': 'North By Northwest', 'year': 1959, 'genre': 'thriller'},
    {'title': 'Alien', 'year': 1979, 'genre': 'scifi'},
    {'title': 'Bridesmaids', 'year': 2011, 'genre': 'comedy'},
    {'title': 'Arrival', 'year': 2016, 'genre': 'scifi'},
    {'title': 'It Happened One Night', 'year': 1934, 'genre': 'comedy'},
    {'title': 'Fargo', 'year': 1996, 'genre': 'thriller'},
    {'title': 'Clueless', 'year': 1995, 'genre': 'comedy'}
]

@app.route('/')
def hello():
    return 'Welcome to the world of MAGIC THE GATHERING (use a tiny elf voice when reading this)'

@app.route('/set/<set_id>')
def get_set(set_id):
    ''' Returns the first matching actor, or an empty dictionary if there's no match. '''

    return json.dumps()

@app.route('/sets')
def get_sets():
    ''' Returns the list of movies that match GET parameters:
          start_year, int: reject any movie released earlier than this year
          end_year, int: reject any movie released later than this year
          genre: reject any movie whose genre does not match this genre exactly
        If a GET parameter is absent, then any movie is treated as though
        it meets the corresponding constraint. (That is, accept a movie unless
        it is explicitly rejected by a GET parameter.)
    '''

    return json.dumps()

@app.route('/artists/<artist_id>')
def get_artist(artist_id):
    return json.dumps()

@app.route('/artists')
def get_artists():
    return json.dumps()

@app.route('/cards/<card_id>')
def get_card(card_id):
    return json.dumps()

@app.route("/cards")
def get_cards():
    return json.dumps()

@app.route("/power/<power_value>")
def get_power(power_value):
    return json.dumps()

@app.route("/toughness/<toughness_value>")
def get_toughness(toughness_value):
    return json.dumps()

@app.route("/cmc/<cmc_value>")
def get_cmc(cmc_value):
    return json.dumps()

@app.route("/manaCost/<manacost_combo>")
def get_manacost(manacost_combo):
    return json.dumps()

@app.route("/color/<color_value>")
def get_colors(color_value):
    return json.dumps()

@app.route("/color")
def get_color_list():
    return json.dumps()


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: {0} host port'.format(sys.argv[0]))
        print('  Example: {0} perlman.mathcs.carleton.edu 5101'.format(sys.argv[0]))
        exit()

    host = sys.argv[1]
    port = int(sys.argv[2])
    app.run(host=host, port=port, debug=True)
