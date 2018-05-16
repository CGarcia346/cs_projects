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
import math
import psycopg2
import config
import random

app = flask.Flask(__name__)

# Who needs a database when you can just hard-code some actors and movies?
def get_connection():
    
    connection = None
    try:
        connection = psycopg2.connect(database=config.database,
                                      user=config.user,
                                      password=config.password)
    except Exception as e:
        print(e, file=sys.stderr)
    return connection

def get_select_query_results(connection, query, parameters=None):

    cursor = connection.cursor()
    if parameters is not None:
        cursor.execute(query, parameters)
    else:
        cursor.execute(query)
    return cursor

@app.after_request
def set_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

sets = []

connection = get_connection()
cursor = connection.cursor()
query = 'SELECT set_id, name, release_date, border FROM sets'
cursor.execute(query)

for row in cursor:
    new_dict = {}
    new_dict["id"] = row[0]
    new_dict['name'] = row[1]
    new_dict['releaseDate'] = row[2]
    new_dict['border'] = row[3]
    sets.append(new_dict)

cards = []
query = 'SELECT card_id, set_id, name, card_set_number, colors, colorIdentity, manacost, cmc, type, types, subtypes, text, power, toughness, flavor, artist FROM cards'

cursor.execute(query)

for row in cursor:
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
query = 'SELECT artist_id, name, sets, cards FROM artists'
cursor.execute(query)

for row in cursor:
    new_dict = {}
    new_dict['artist_id'] = row[0]
    new_dict['name'] = row[1]
    new_dict['sets'] = row[2]
    new_dict['cards'] = row[3]
    artists.append(new_dict)

power_list = []
query = 'SELECT power, card_id, name FROM power'
cursor.execute(query)

for row in cursor:
    new_dict = {}
    new_dict["power"] = row[0]
    new_dict["card_id"] = row[1]
    new_dict["name"] = row[2]
    power_list.append(new_dict)

toughness_list = []
query = 'SELECT toughness, card_id, name FROM toughness'
cursor.execute(query)

for row in cursor:
    new_dict = {}
    new_dict["toughness"] = row[0]
    new_dict["card_id"] = row[1]
    new_dict["name"] = row[2]
    toughness_list.append(new_dict)

cmc_list = []
query = 'SELECT cmc, card_id, name FROM cmc'
cursor.execute(query)

for row in cursor:
        new_dict = {}
        new_dict["cmc"] = row[0]
        new_dict["card_id"] = row[1]
        new_dict["name"] = row[2]
        cmc_list.append(new_dict)

color_to_id = {}
id_to_color = {}
query = 'SELECT color_id, color FROM color'
cursor.execute(query)

new_dict = {}
other_dict = {}
for row in cursor:
    new_dict[row[1]] = row[0]
    other_dict[row[0]] = row[1]
color_to_id = new_dict.copy()
id_to_color = other_dict.copy()

color_amount_list = []
query = 'SELECT color_id, color, card_id, name FROM colors'
cursor.execute(query)

for row in cursor:
    new_dict = {}
    new_dict["color_id"] = row[0]
    new_dict["color"] = row[1]
    new_dict["card_id"] = row[2]
    new_dict["name"] = row[3]
    color_amount_list.append(new_dict)

card_manacost = []
query = 'SELECT card_id, color_id, amount FROM manacost'
cursor.execute(query)

for row in cursor:
    new_dict = {}
    new_dict['card_id'] = row[0]
    new_dict['color_id'] = row[1]
    new_dict['manacost'] = row[2]
    card_manacost.append(new_dict)

connection.close()

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
    set_id = set_id

    for set in sets:
        if (set['id'] == set_id) or (set['name'] == set_id):
            set_dictionary = set.copy()
            set_id = set['id']
            break

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
    set = flask.request.args.get('set', type= str)
    card = flask.request.args.get('card', type = str)

    for artist in artists:
        if artist_id is not None and artist_id != artist['artist_id']:
            continue
        if name is not None and name.lower().replace(" ", "") not in artist['name'].lower().replace(" ", ""):
            continue
        if set is not None and set not in artist['sets']:
            continue
        if card is not None and card not in artist['cards']:
            continue
        artist_list.append(artist)

    return json.dumps(artist_list)

@app.route('/artist/<artist_id>')
def get_artist(artist_id):

    temp_list = []
    for artist in artists:
        if (artist['artist_id'] == artist_id) or (artist_id.lower().replace(" ", "") in artist['name'].lower().replace(" ","")):
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
    types = flask.request.args.get('types')
    subtypes = flask.request.args.get('subtypes')
    colors = flask.request.args.get('colors')
    artist = flask.request.args.get('artist')

    for card in cards:
        if card_id is not None and card_id != card['card_id']:
            continue
        if name is not None and name.lower().replace(" ", "") not in card['name'].lower().replace(" ", ""):
            continue
        if set_id is not None and set_id != card['set_id']:
            continue
        if colors is not None and colors not in card['colors']:
            continue
        if Type is not None and Type.lower().replace(" ", '') not in card['type'].lower().replace(" ",""):
            continue
        if types is not None and types.lower().replace(" ", '') not in card['types'].lower().replace(" ",""):
            continue
        if subtypes is not None and subtypes.lower().replace(" ", '') not in card['subtypes'].lower().replace(" ",""):
            continue
        if artist is not None and artist.lower().replace(" ", "") not in card['artist'].lower().replace(" ", ""):
            continue
        card_list.append(card)

    return json.dumps(card_list)

@app.route("/power/<power_value>")
def get_power(power_value):

    temp_list = []
    for card in power_list:
        old = power_value
        new = float(power_value)
        if new - math.floor(new) > 0:
            a_string = str(int(math.floor(new)))
            if a_string == "0":
                a_string = ""
            a_string = a_string + "½"
            power_value = a_string

        if card['power'] == power_value:
            temp_list.append(card['name'])

        power_value = old

    return json.dumps(temp_list)

@app.route("/toughness/<toughness_value>")
def get_toughness(toughness_value):

    temp_list = []
    for card in toughness_list:
        old = toughness_value
        new = float(toughness_value)
        if new - math.floor(new) > 0:
            a_string = str(int(math.floor(new)))
            if a_string == "0":
                a_string = ""
            a_string = a_string + "½"
            toughness_value = a_string

        if card['toughness'] == toughness_value:
            temp_list.append(card['name'])

        toughness_value = old

    return json.dumps(temp_list)

@app.route("/cmc/<cmc_value>")
def get_cmc(cmc_value):

    temp_list = []

    for card in cmc_list:
        if card['name'] == "Little Girl" and float(cmc_value) == 0.5:
            temp_list.append(card['name'])
            break

        if card['cmc'] == cmc_value:
            temp_list.append(card['name'])
    return json.dumps(temp_list)


@app.route("/manacost/<manacost_combo>")
def get_manacost(manacost_combo):

    translated = []
    cardswv = []
    hasX = False
    littleT = False
    amountc = 0
    amountw = 0
    amountu = 0
    amountb = 0
    amountr = 0
    amountg = 0
    amountn = ""
    
    for value in manacost_combo:
        
        if value == "h":
            cardswv.append("Little Girl")
            littleT = True
            break

        elif value == "C":
            type = "colorless"
            amountc += 1

        elif value == "W":
            type = "white"
            amountw += 1

        elif value == "U":
            type = 'blue'
            amountu += 1

        elif value == "B":
            type = "black"
            amountb += 1

        elif value == "R":
            type = 'red'
            amountr += 1

        elif value == "G":
            type = "green"
            amountg += 1

        else:
            type = "generic"
            amountn = amountn + value
            if value == "X":
                hasX = True

        if color_to_id[type] not in translated:

            translated.append(color_to_id[type])

    if hasX is True:
        amountn = amountn.replace("X", "")

    try:
        amountn = int(amountn)
    except:
        print(hasX)

    cur_id = "0"
    manacost_truth = True

    fulfill = []

    for manacost in card_manacost:

        if littleT:
            break

        prev_id = cur_id
        cur_id = manacost['card_id']
        try:
            cur_amount = int(manacost['manacost'])

        except:
            cur_amount = None

        if ((cur_id == prev_id) and (manacost_truth is False)):
            continue

        if cur_id != prev_id:
            if ((manacost_truth is True) and (set(fulfill) == set(translated))):
                for card in cards:
                    if card['card_id'] == prev_id:
                        a_card = card
                cardswv.append(a_card['name'])
            manacost_truth = True
            fulfill = []
        
        if (manacost['color_id'] in translated) and (manacost_truth is True):
            color_of_card = id_to_color[manacost['color_id']]

            if color_of_card == "colorless":
                wanted_amount = amountc
            elif color_of_card == "white":
                wanted_amount = amountw
            elif color_of_card == "blue":
                wanted_amount = amountu
            elif color_of_card == "black":
                wanted_amount = amountb
            elif color_of_card == "red":
                wanted_amount = amountr
            elif color_of_card == "green":
                wanted_amount = amountg
            elif color_of_card == "generic":
                if hasX:
                    wanted_amount = None
                else:
                    wanted_amount = amountn

            fulfill.append(manacost['color_id'])
            
            if cur_amount == wanted_amount:
                manacost_truth = True
            else:
                manacost_truth = False

        else:
            manacost_truth = False

    return json.dumps(cardswv)

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
    return json.dumps(translated)

@app.route("/color")
def get_color_list():
    return json.dumps(color_to_id)
@app.route("/random")
def get_random():
    limit = len(cards) - 1
    card = random.randint(0, limit)
    randomcard = cards[card]
    return json.dumps(randomcard)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: {0} host port'.format(sys.argv[0]))
        print('  Example: {0} perlman.mathcs.carleton.edu 5101'.format(sys.argv[0]))
        exit()

    host = sys.argv[1]
    port = int(sys.argv[2])
    app.run(host=host, port=port, debug=True)
