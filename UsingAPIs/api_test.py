#!/usr/bin/env python3
'''
    api_test.py
    Carlos Garcia & Joey Cook-Gallardo, 13 April 2018

    An example for CS 257 Software Design. How to retrieve results
    from an HTTP-based API, parse the results (JSON in this case),
    and manage the potential errors.
'''

import sys
import argparse
import json
import urllib.request

def get_Pokemon(gen, gen_num):
    '''

    '''

    base_url = 'http://pokeapi.co/api/v2/{0}/{1}/'
    url = base_url.format(gen, gen_num)
    request = urllib.request.Request(url)
    request.add_header("User-Agent", "Garco")
    data_from_server = urllib.request.urlopen(request).read()
    string_from_server = data_from_server.decode('utf-8')
    generation_list = json.loads(string_from_server)

    result_list = []
    pokemon_species = generation_list['pokemon_species']
    count = 0
    for pokemon_list_dictionary in pokemon_species:
        count+= 1
        pokemon = pokemon_list_dictionary['name']

        id_url = pokemon_list_dictionary['url']
        request_id = urllib.request.Request(id_url)
        request_id.add_header("User-Agent", "Garco")
        data_extend = urllib.request.urlopen(request_id).read()
        string_extend = data_extend.decode('utf-8')
        pokemon_entry = json.loads(string_extend)
        id_num = pokemon_entry['id']
        str_num = str(id_num)
        print("received id: " + str_num + " and appended to " + pokemon + " || collected total: " + str(count))
        poke_data = (pokemon, id_num)
        result_list.append(poke_data)

    print(result_list)
    return result_list

def main(args):
    if args.action == 'generation':
        pokedex = get_Pokemon(args.action, args.gen_num)
        '''
        for root_word in root_words:
            root = root_word['root']
            part_of_speech = root_word['partofspeech']
            print('{0} [{1}]'.format(root, part_of_speech))

    elif args.action == 'conjugate':
        conjugations = get_conjugations(args.word, args.language)
        for conjugation in conjugations:
            text = conjugation['text']
            tense = conjugation['tense']
            person = conjugation['person']
            number = conjugation['number']
            print('{0} [{1} {2} {3}]'.format(text, tense, person, number))
            '''

if __name__ == '__main__':
    # When I use argparse to parse my command line, I usually
    # put the argparse setup here in the global code, and then
    # call a function called main to do the actual work of
    # the program.
    parser = argparse.ArgumentParser(description='Get word info from the Ultralingua API')

    parser.add_argument('action',
                        metavar='action',
                        help='action to perform on the word ("gen" or "entry")',
                        choices=['generation', 'entry'])
    '''
    parser.add_argument('language',
                        metavar='language',
                        help='the language as a 3-character ISO code',
                        choices=['eng', 'fra', 'spa', 'deu', 'ita', 'por'])
                        '''
    parser.add_argument('gen_num', help='the word you want to act on')

    args = parser.parse_args()
    main(args)