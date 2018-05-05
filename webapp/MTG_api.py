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
import csv

app = flask.Flask(__name__)

# Who needs a database when you can just hard-code some actors and movies?

sets = []
with open('MTG_sets_table.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        new_dict = {}
        new_dict["id"] = row[0]
        new_dict['name'] = row[1]
        new_dict['releaseDate'] = row[2]
        new_dict['border'] = row[3]
        sets.append(new_dict)

card_list = []
with open('MTG_cards_table.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        new_dict={}
        new_dict['card_id'] = row[0]
        new_dict['set_id'] = row[1]
        new_dict['name'] = row[2]
        new_dict['cards_set_number'] = row[3]
        new_dict['colors'] = row[4]
        new_dict['colorIdentity'] = row[5]
        new_dict['manaCost'] = row[6]
        new_dict['cmc']= row[7]
        new_dict['type']= row[8]
        new_dict['types']= row[9]
        new_dict['subtypes']= row[10]
        new_dict['text']= row[11]
        new_dict['power']= row[12]
        new_dict['toughness']= row[13]
        new_dict['flavor']= row[14]
        new_dict['artist']= row[15]
        card_list.append(new_dict)

@app.route('/')
def hello():
    return 'Welcome to the world of MAGIC THE GATHERING (use a tiny elf voice when reading this)'

@app.route('/sets')
def get_sets():

    sets_list = []
    id = flask.request.args.get('id')
    name = flask.request.args.get('name')
    release_date = flask.request.args.get('releaseDate', type= str)
    border = flask.request.args.get('border', type = str)
    for set in sets:
        if id is not None and id != set['id']:
            continue
        if name is not None and name != set['name']:
            continue
        if release_date is not None and release_date != set['releaseDate']:
            continue
        if border is not None and border != set['border']:
            continue
        sets_list.append(set)

    return json.dumps(sets_list)

@app.route('/set/<set_id>')
def get_set(set_id):
    ''' Returns the first matching actor, or an empty dictionary if there's no match. '''
    set_dictionary = {}
    for set in sets:
        if set['id'] == set_id:
            set_dictionary = set.copy()
            temp_list = []
            for card in card_list:
                if card['set_id'] == set_id:
                    temp_list.append(card)
            set_dictionary['cards'] = temp_list
            print(sets)
            break
    return json.dumps(set_dictionary)

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
