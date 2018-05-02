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

def save_sets_table_as_csv(sets, csv_file_name):

    output_file = open(csv_file_name, 'w')
    writer = csv.writer(output_file)
    ban = ["promo", "duel deck", "reprint", "box", "from the vault", "premium deck", "starter", "masters", "masterpiece"]
    id = 0

    for key in sets:

        if (sets[key]['type'] not in ban):
            set_row = [id, sets[key]['name'],  sets[key]['releaseDate'],  sets[key]['border']]
            writer.writerow(set_row)
            id += 1

    output_file.close()

def save_cards_table_as_csv(sets, csv_file_name):

    output_file = open(csv_file_name, 'w')
    writer = csv.writer(output_file)
    ban = ["promo", "duel deck", "reprint", "box", "from the vault", "premium deck", "starter", "masters", "masterpiece"]
    set_id = 0
    card_id = 0

    for key in sets:

        if (sets[key]['type'] not in ban):
            cards = sets[key]['cards']

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
    artists = []

    for key in sets:
        if (sets[key]['type'] not in ban):
            cards = sets[key]['cards']

            for card in cards:
                if card["artist"] not in artists:
                    artists.append(card["artist"])

                artistID = artists.index(card['artist'])
                set_row = [artistID, card["artist"], sets[key]['name'], card["name"]]
                writer.writerow(set_row)

    output_file.close()

def save_cmc_table_as_csv(sets, csv_file_name):

    output_file = open(csv_file_name, 'w')
    writer = csv.writer(output_file)
    ban = ["promo", "duel deck", "reprint", "box", "from the vault", "premium deck", "starter", "masters", "masterpiece"]
    card_id = 0

    for key in sets:

        if sets[key]['type'] not in ban:
            cards = sets[key]['cards']

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

    for key in sets:

        if sets[key]['type'] not in ban:
            cards = sets[key]['cards']

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

    for key in sets:
        if sets[key]['type'] not in ban:
            cards = sets[key]['cards']

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

    for key in sets:

        if sets[key]['type'] not in ban:
            cards = sets[key]['cards']

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

    for key in sets:

        if sets[key]['type'] not in ban:
            cards = sets[key]['cards']

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

    for key in sets:

        if sets[key]['type'] not in ban:
            cards = sets[key]['cards']
            for card in cards:
                if 'manaCost' in card:
                    manaCost = card['manaCost']

                    if "C" in manaCost:
                        amount = 0
                        while "C" in manaCost:
                            i = manaCost.index('C')
                            manaCost = manaCost[:i-1] + manaCost[i+2:]
                            amount += 1
                            set_row = [card_id, 0, amount]
                            writer.writerow(set_row)

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

if __name__ == '__main__':
    # Turn JSON string into Python objects
    data = json.loads(open('AllSets.json').read())

    # Save the tables
    save_sets_table_as_csv(data, 'MTG_sets_table.csv')
    save_cards_table_as_csv(data, 'MTG_cards_table.csv')
    save_artist_table_as_csv(data, 'MTG_artists_table.csv')
    save_cmc_table_as_csv(data, 'MTG_cmc_table.csv')
    save_power_table_as_csv(data, 'MTG_power_table.csv')
    save_toughness_table_as_csv(data, 'MTG_toughness_table.csv')
    save_color_table_as_csv(data, 'MTG_color_table.csv')
    save_type_table_as_csv(data, 'MTG_type_table.csv')
    save_manacost_table(data, 'MTG_manacost_table.csv')
