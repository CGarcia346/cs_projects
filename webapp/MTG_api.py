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

cards = []
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
        cards.append(new_dict)

artists = []
with open('MTG_artists_table.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        new_dict = {}
        new_dict['artist_id'] = row[0]
        new_dict['name'] = row[1]
        new_dict['sets'] = row[2]
        new_dict['cards'] = row[3]
        artists.append(new_dict)

power_list = []
with open('MTG_power_table.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        new_dict = {}
        new_dict["power"] = row[0]
        new_dict["card_id"] = row[1]
        new_dict["name"] = row[2]
        power_list.append(new_dict)

toughness_list = []
with open('MTG_toughness_table.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        new_dict = {}
        new_dict["toughness"] = row[0]
        new_dict["card_id"] = row[1]
        new_dict["name"] = row[2]
        toughness_list.append(new_dict)

cmc_list = []
with open('MTG_cmc_table.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        new_dict = {}
        new_dict["cmc"] = row[0]
        new_dict["card_id"] = row[1]
        new_dict["name"] = row[2]
        cmc_list.append(new_dict)

color_list = []
with open('color.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        new_dict = {}
        new_dict["color_id"] = row[0]
        new_dict["color"] = row[1]
        color_list.append(new_dict)

color_amount_list = []
with open('MTG_color_table.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        new_dict = {}
        new_dict["color_id"] = row[0]
        new_dict["color"] = row[1]
        new_dict["card_id"] = row[2]
        new_dict["name"] = row[3]
        color_amount_list.append(new_dict)

@app.route('/')
def hello():
    return 'Welcome to the world of MAGIC THE GATHERING (use a tiny elf voice when reading this)'


@app.route('/sets')
def get_sets():

    sets_list = []
    set_id = flask.request.args.get('set_id')
    name = flask.request.args.get('name')
    release_date = flask.request.args.get('releaseDate', type= str)
    border = flask.request.args.get('border', type = str)
    for set in sets:
        if set_id is not None and set_id != set['id']:
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
    set_dictionary = {}
    for set in sets:
        if set['id'] == set_id:
            set_dictionary = set.copy()

    set_dictionary['cards'] = []

    for card in cards:
        if card['set_id'] == set_id:
            set_dictionary['cards'].append(card)

    return json.dumps(set_dictionary)


@app.route('/artists')
def get_artists():
    artist_list = []
    artist_id = flask.request.args.get('artist_id')
    name = flask.request.args.get('name')
    sets = flask.request.args.get('sets', type= str)
    cards = flask.request.args.get('cards', type = str)

    for artist in artists:
        if artist_id is not None and artist_id != artist['artist_id']:
            continue
        if name is not None and name != artist['name']:
            continue
        if sets is not None and sets not in artist['sets']:
            continue
        if cards is not None and cards not in artist['cards']:
            continue
        artist_list.append(artist)

    return json.dumps(artist_list)

@app.route('/artists/<artist_id>')
def get_artist(artist_id):
    temp_list = []
    for artist in artists:
        if artist['artist_id'] == artist_id:
            temp_list.append(artist)

    return json.dumps(temp_list)

@app.route('/cards/<card_id>')
def get_card(card_id):
    acard = []
    for card in card_list:
        if card['card_id'] == card_id:
            acard.append(card)
    return json.dumps(acard)

@app.route("/cards")
def get_cards():

    card_list = []
    card_id = flask.request.args.get('card_id')
    name = flask.request.args.get('name')
    set_id = flask.request.args.get('set_id', type= str)
    Type = flask.request.args.get('type', type = str)
    colors = flask.request.args.get('colors')
    artist = flask.request.args.get('artist')

    for card in cards:
        if card_id is not None and card_id != card['card_id']:
            continue
        if name is not None and name != card['name']:
            continue
        if set_id is not None and set_id != card['set_id']:
            continue
        if colors is not None and colors not in card['colors']:
            continue
        if Type is not None and Type.lower().replace(" ", '') != card['type'].lower().replace(" ",""):
            continue
        if artist is not None and artist.lower().replace(" ", "") not in card['artist'].lower().replace(" ", ""):
            continue
        card_list.append(card)

    return json.dumps(card_list)

@app.route("/power/<power_value>")
def get_power(power_value):
    temp_list = []
    for card in power_list:
        if card['power'] == power_value:
            temp_list.append(card['name'])
    return json.dumps(temp_list)

@app.route("/toughness/<toughness_value>")
def get_toughness(toughness_value):
    temp_list = []
    for card in toughness_list:
        if card['toughness'] == toughness_value:
            temp_list.append(card['name'])
    return json.dumps(temp_list)

@app.route("/cmc/<cmc_value>")
def get_cmc(cmc_value):
    temp_list = []
    for card in cmc_list:
        if card['cmc'] == cmc_value:
            temp_list.append(card['name'])
    return json.dumps(temp_list)

'''
This is incomplete
'''
@app.route("/manaCost/<manacost_combo>")
def get_manacost(manacost_combo):
    return json.dumps()

@app.route("/color/<color_value>")
def get_colors(color_value):

    color_copy = color_amount_list.copy()
    if "_" in color_value:
        color_value = color_value.split("_")
    else:
        color_value = [color_value]

    while color_value:
        temp_list = []
        for card in color_copy:

            card_colors = card['color']

            if color_value[0] in card_colors:
                temp_list.append(card)

        color_value.pop(0)
        color_copy = temp_list

    final_list = []
    for card in color_copy:
        final_list.append(card['name'])
    return json.dumps(final_list)

@app.route("/color")
def get_color_list():
    return json.dumps(color_list)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: {0} host port'.format(sys.argv[0]))
        print('  Example: {0} perlman.mathcs.carleton.edu 5101'.format(sys.argv[0]))
        exit()

    host = sys.argv[1]
    port = int(sys.argv[2])
    app.run(host=host, port=port, debug=True)
