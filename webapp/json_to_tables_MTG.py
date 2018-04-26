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
            set_row = [id, sets[key]['name'],  sets[key]['releaseDate'],  sets[key]['border'],  sets[key]['cards']]
            writer.writerow(set_row)
            id += 1
    output_file.close()

def save_cards_table_as_csv(sets, csv_file_name):
    output_file = open(csv_file_name, 'w')
    writer = csv.writer(output_file)
    ban = ["promo", "duel deck", "reprint", "box", "from the vault", "premium deck", "starter", "masters", "masterpiece"]
    id = 0
    card_id = 0
    for key in sets:
        if (sets[key]['type'] not in ban):
            cards = sets[key]['cards']
            for card in cards:

                card_set_num = None

                if "number" in card:
                    card_set_num = card['number']

                set_row = [id, card_id, card_set_num, card['artist'], card['name'], card['type'], card['cmc']]

                if "types" in card:
                    set_row.append(card['types'])
                else:
                    set_row.append(None)
                if "manaCost" in card:
                    set_row.append(card['manaCost'])
                else:
                    set_row.append(None)

                if "subtypes" in card:
                    set_row.append(card['subtypes'])
                else:
                    set_row.append(None)
                if "colors" in card:
                    set_row.append(card['colors'])
                else:
                    set_row.append(None)
                if "text" in card:
                    set_row.append(card['text'])
                else:
                    set_row.append(None)
                if "colorIdentity" in card:
                    set_row.append(card['colorIdentity'])
                else:
                    set_row.append(None)
                if "flavor" in card:
                    set_row.append(card['flavor'])
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

                card_id += 1
                writer.writerow(set_row)
            id += 1
    output_file.close()

def save_artist_table_as_csv(sets, csv_file_name):
    output_file = open(csv_file_name, 'w')
    writer = csv.writer(output_file)
    ban = ["promo", "duel deck", "reprint", "box", "from the vault", "premium deck", "starter", "masters", "masterpiece"]
    id = 0
    card_id = 0
    artists = []
    for key in sets:
        if (sets[key]['type'] not in ban):
            cards = sets[key]['cards']
            for card in cards:
                if card["artist"] not in artists:
                    artists.append(card["artist"])
                artistID = artists.index(card['artist'])
                set_row = [id, artistID, card_id, card["artist"], card["name"]]
                writer.writerow(set_row)
                card_id+=1
            id += 1
    output_file.close()


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
    save_sets_table_as_csv(data, 'sets_table.csv')
    save_cards_table_as_csv(data, 'cards_table.csv')
    save_artist_table_as_csv(data, 'artists_table.csv')

