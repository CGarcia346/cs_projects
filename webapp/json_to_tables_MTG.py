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
import json
import csv



def save_sets_table_as_csv(sets, csv_file_name, sortedList):

    output_file = open(csv_file_name, 'w')
    writer = csv.writer(output_file)
    id = 0
    while sortedList:
        for key in sets:
            if sortedList:
                if sets[key]['name'] == sortedList[0]:
                    set_row = [id, sets[key]['name'],  sets[key]['releaseDate'],  sets[key]['border']]
                    writer.writerow(set_row)
                    id += 1
                    sortedList.remove(sortedList[0])


    output_file.close()

def save_cards_table_as_csv(sets, csv_file_name):

    output_file = open(csv_file_name, 'w')
    writer = csv.writer(output_file)
    set_id = 0
    card_id = 0


    for dict in sets:
            cards = dict['cards']

            for card in cards:
                if "number" in card:
                    card_set_num = card['number']
                else:
                    card_set_num = None

                set_row = [card_id, set_id, card['name'], card_set_num]

                if "colors" in card:
                    set_row.append(card['colors'])
                else:
                    set_row.append(None)

                if "colorIdentity" in card:
                    set_row.append(card['colorIdentity'])
                else:
                    set_row.append(None)

                if "manaCost" in card:
                    set_row.append(card['manaCost'])
                else:
                    set_row.append(None)

                set_row.append(card['cmc'])
                set_row.append(card['type'])

                if "types" in card:
                    set_row.append(card['types'])
                else:
                    set_row.append(None)

                if "subtypes" in card:
                    set_row.append(card['subtypes'])
                else:
                    set_row.append(None)

                if "text" in card:
                    set_row.append(card['text'])
                else:
                    set_row.append(None)

                if "power" in card:
                    set_row.append(card['power'])
                else:
                    set_row.append(None)

                if "toughness" in card:
                    set_row.append(card['toughness'])
                else:
                    set_row.append(None)

                if "flavor" in card:
                    set_row.append(card['flavor'])
                else:
                    set_row.append(None)

                set_row.append(card['artist'])

                card_id += 1
                writer.writerow(set_row)

            set_id += 1

    output_file.close()

def save_artist_table_as_csv(sets, csv_file_name):

    output_file = open(csv_file_name, 'w')
    writer = csv.writer(output_file)
    ban = ["promo", "duel deck", "reprint", "box", "from the vault", "premium deck", "starter", "masters", "masterpiece"]
    artist_list = []
    artists = {}
    temp_list = []
    artist_id = 0

    for key in sets:
        if (sets[key]['type'] not in ban):
            cards = sets[key]['cards']

            for card in cards:
                if card["artist"] not in artists:
                    artist_list.append(card['artist'])
                    artists[card["artist"]] = {"id": artist_list.index(card['artist']), 'a_set': [card['name']],
                                               'c_set': [card['name']]}
                else:
                    if sets[key]['name'] not in artists[card['artist']]['a_set']:
                        artists[card["artist"]]['a_set'].append(sets[key]['name'])
                    artists[card["artist"]]['c_set'].append(card['name'])
    for artist in artists:
        temp_list.append(artist)
    temp_list.sort()
    while temp_list:
        for artist in artists:
            if temp_list:
                if artist == temp_list[0]:
                    artists[artist]['id'] = artist_id
                    set_row = [artists[artist]['id'], artist, artists[artist]['a_set'], artists[artist]['c_set']]
                    writer.writerow(set_row)
                    temp_list.remove(temp_list[0])
                    artist_id += 1

    output_file.close()

def save_cmc_table_as_csv(sets, csv_file_name):

    output_file = open(csv_file_name, 'w')
    writer = csv.writer(output_file)
    ban = ["promo", "duel deck", "reprint", "box", "from the vault", "premium deck", "starter", "masters", "masterpiece"]
    card_id = 0

    for dict in sets:

        cards = dict['cards']
        for card in cards:
                set_row = [card["cmc"], card_id, card["name"]]
                writer.writerow(set_row)
                card_id += 1

    output_file.close()

def save_color_table_as_csv(sets, csv_file_name):

    output_file = open(csv_file_name, 'w')
    writer = csv.writer(output_file)
    ban = ["promo", "duel deck", "reprint", "box", "from the vault", "premium deck", "starter", "masters", "masterpiece"]
    card_id = 0
    color_list = []

    for dict in sets:

        cards = dict['cards']

        for card in cards:
                if "colors" in card:

                    if card["colors"] not in color_list:
                        color_list.append(card["colors"])
                        color_id = len(color_list) - 1
                    else:
                        color_id = color_list.index(card["colors"])

                    set_row = [color_id, card["colors"], card_id, card["name"]]

                else:
                    color_id = -1
                    set_row = [color_id, None, card_id, card["name"]]

                writer.writerow(set_row)
                card_id += 1

    output_file.close()

def save_type_table_as_csv(sets, csv_file_name):

    output_file = open(csv_file_name, 'w')
    writer = csv.writer(output_file)
    ban = ["promo", "duel deck", "reprint", "box", "from the vault", "premium deck", "starter", "masters", "masterpiece"]
    card_id = 0
    type_list = []

    for dict in sets:

        cards = dict['cards']

        for card in cards:

                if card["type"] not in type_list:
                    type_list.append(card["type"])
                    type_id = len(type_list) - 1
                else:
                    type_id = type_list.index(card["type"])

                set_row = [type_id, card["type"], card_id, card["name"]]
                writer.writerow(set_row)
                card_id += 1

    output_file.close()

def save_power_table_as_csv(sets, csv_file_name):

    output_file = open(csv_file_name, 'w')
    writer = csv.writer(output_file)
    ban = ["promo", "duel deck", "reprint", "box", "from the vault", "premium deck", "starter", "masters", "masterpiece"]
    card_id = 0

    for dict in sets:

        cards = dict['cards']

        for card in cards:

            if 'power' in card:
                set_row = [card["power"], card_id, card["name"]]
                writer.writerow(set_row)

            card_id += 1

    output_file.close()

def save_toughness_table_as_csv(sets, csv_file_name):

    output_file = open(csv_file_name, 'w')
    writer = csv.writer(output_file)
    ban = ["promo", "duel deck", "reprint", "box", "from the vault", "premium deck", "starter", "masters", "masterpiece"]
    card_id = 0

    for dict in sets:

        cards = dict['cards']

        for card in cards:

            if 'toughness' in card:
                set_row = [card["toughness"], card_id, card["name"]]
                writer.writerow(set_row)

            card_id += 1

    output_file.close()

def save_manacost_table(sets, csv_file_name):

    output_file = open(csv_file_name, 'w')
    writer = csv.writer(output_file)
    ban = ["promo", "duel deck", "reprint", "box", "from the vault", "premium deck", "starter", "masters", "masterpiece"]
    card_id = 0

    for dict in sets:

        cards = dict['cards']

        for card in cards:
                if 'manaCost' in card:
                    manaCost = card['manaCost']

                    if "/" in manaCost:

                        while "/" in manaCost:
                            i= manaCost.index('/')
                            if manaCost[i+1] == "P":
                                manaCost = manaCost[:i] + manaCost[i+3:]
                            else:
                                manaCost = manaCost[:i] + "}{" + manaCost[i+1:]

                    if "C" in manaCost:
                        amount = 0
                        while "C" in manaCost:
                            i = manaCost.index('C')
                            manaCost = manaCost[:i-1] + manaCost[i+2:]
                            amount += 1
                            set_row = [card_id, 0, amount]
                            writer.writerow(set_row)

                    if "hw" in manaCost:
                        amount = 0.5
                        set_row = [card_id, 1, amount]
                        writer.writerow(set_row)
                        manaCost = ""

                    if "W" in manaCost:
                        amount = 0
                        while "W" in manaCost:
                            i = manaCost.index('W')
                            manaCost = manaCost[:i-1] + manaCost[i+2:]
                            amount += 1
                        set_row = [card_id, 1, amount]
                        writer.writerow(set_row)

                    if "U" in manaCost:
                        amount = 0
                        while "U" in manaCost:
                            i = manaCost.index('U')
                            manaCost = manaCost[:i-1] + manaCost[i+2:]
                            amount += 1
                        set_row = [card_id, 2, amount]
                        writer.writerow(set_row)

                    if "B" in manaCost:
                        amount = 0
                        while "B" in manaCost:
                            i = manaCost.index('B')
                            manaCost = manaCost[:i-1] + manaCost[i+2:]
                            amount += 1
                        set_row = [card_id, 3, amount]
                        writer.writerow(set_row)

                    if "R" in manaCost:
                        amount = 0
                        while "R" in manaCost:
                            i = manaCost.index('R')
                            manaCost = manaCost[:i-1] + manaCost[i+2:]
                            amount += 1
                        set_row = [card_id, 4, amount]
                        writer.writerow(set_row)

                    if "G" in manaCost:
                        amount = 0
                        while "G" in manaCost:
                            i = manaCost.index('G')
                            manaCost = manaCost[:i-1] + manaCost[i+2:]
                            amount += 1
                        set_row = [card_id, 5, amount]
                        writer.writerow(set_row)

                    if manaCost:
                        for omit in ["X", "{", "}"]:
                            if omit in manaCost:
                                manaCost = manaCost.replace(omit, "")
                        set_row = [card_id, 6, manaCost]
                        writer.writerow(set_row)

                card_id += 1

    output_file.close()

def create_color_table():

    output_file = open("color.csv", 'w')
    writer = csv.writer(output_file)

    set_row = [0, "colorless"]
    writer.writerow(set_row)

    set_row = [1, "white"]
    writer.writerow(set_row)

    set_row = [2, "blue"]
    writer.writerow(set_row)

    set_row = [3, "black"]
    writer.writerow(set_row)

    set_row = [4, "red"]
    writer.writerow(set_row)

    set_row = [5, "green"]
    writer.writerow(set_row)

    set_row = [6, "generic"]
    writer.writerow(set_row)

def save_linking_table_as_csv(books, authors, csv_file_name):
    ''' Exercise for the reader. Roughly, you might do this like so:
        
        Open a csv writer
        Build a dictionary mapping (author name) --> (author id)
        for book in books:
            for author_name in book['authors']:
                author_id = ...
                table_row = [book['id'], author_id]
                writer.writerow(table_row)
    '''
    pass
def sortList(data, csv_file_name):
    ban = ["promo", "duel deck", "reprint", "box", "from the vault", "premium deck", "starter", "masters", "masterpiece"]
    temp_list = []
    for key in data:
        if (data[key]['type'] not in ban):
            temp_list.append(data[key]['name'])
    temp_list.sort()
    return temp_list

def sortDics(data, csv_file_name):
    ban = ["promo", "duel deck", "reprint", "box", "from the vault", "premium deck", "starter", "masters", "masterpiece"]
    temp_list = []
    sortedList = []
    for key in data:
        if (data[key]['type'] not in ban):
            temp_list.append(data[key]['name'])
    temp_list.sort()

    while temp_list:
        for key in data:
            if temp_list:
                if temp_list[0] == data[key]['name']:
                    sortedList.append(data[key])
                    temp_list.remove(temp_list[0])
    return sortedList

if __name__ == '__main__':
    # Turn JSON string into Python objects
    data = json.loads(open('AllSets.json').read())

    sortedList = sortList(data, 'MTG_sets_table.csv')
    dicList = sortDics(data, 'MTG_sets_table.csv')

    # Save the tables
    save_sets_table_as_csv(data, 'MTG_sets_table.csv', sortedList)
    save_cards_table_as_csv(dicList, 'MTG_cards_table.csv')
    save_artist_table_as_csv(data, 'MTG_artists_table.csv')
    save_cmc_table_as_csv(dicList, 'MTG_cmc_table.csv')
    save_power_table_as_csv(dicList, 'MTG_power_table.csv')
    save_toughness_table_as_csv(dicList, 'MTG_toughness_table.csv')
    save_color_table_as_csv(dicList, 'MTG_color_table.csv')
    save_type_table_as_csv(dicList, 'MTG_type_table.csv')
    save_manacost_table(dicList, 'MTG_manacost_table.csv')
    create_color_table()
