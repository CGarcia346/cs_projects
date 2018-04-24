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
            set_row = [id, sets[key]['name'],  sets[key]['releaseDate'],  sets[key]['border'],  sets[key]['cards'],
                       sets[key]['type']]
            writer.writerow(set_row)
            id += 1
    output_file.close()

def save_authors_table_as_csv(authors, csv_file_name):
    output_file = open(csv_file_name, 'w')
    writer = csv.writer(output_file)
    for author in authors:
        author_row = [author['id'], author['last_name'], author['first_name'], author['birth_year'], author['death_year']]
        writer.writerow(author_row)
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


