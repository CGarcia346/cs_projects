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
import math

def get_Pokedex(gen, searchable):
    '''

    '''

    base_url = 'http://pokeapi.co/api/v2/{0}/{1}/'
    url = base_url.format(gen, searchable)
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
        poke_data = (id_num, pokemon)
        result_list.append(poke_data)
        print("received id: " + str_num + " and appended to " + pokemon + " || collected total: " + str(count) +
              "|| progress complete: " + str(int((len(result_list) / len(pokemon_species))*100)) + "%")

    final_list = createOrder(result_list)
    return final_list

def createOrder(list_of_tuples):

    ordered_list = []

    while len(list_of_tuples) != 0:

        i = 0
        index = 0
        lowest = float("inf")

        for aTuple in list_of_tuples:
            if aTuple[0] < lowest:
                lowest = aTuple[0]
                index = i
                i += 1

            else:
                i += 1

        ordered_list.append(list_of_tuples.pop(index))

    return ordered_list

def get_Pokemon(pokemonSpecies, entry):

    base_url = 'http://pokeapi.co/api/v2/{0}/{1}/'
    url = base_url.format(pokemonSpecies, entry)
    request = urllib.request.Request(url)
    request.add_header("User-Agent", "Garco")
    data_from_server = urllib.request.urlopen(request).read()
    string_from_server = data_from_server.decode('utf-8')
    pokemon_info = json.loads(string_from_server)

    pokemon_data = []
    '''
    name, stats
    '''
    pokemon_name = pokemon_info['name']
    stat_list_dictionary = pokemon_info['stats']
    stats = []
    for stat_dictionary in stat_list_dictionary:
        stat_inner_list = stat_dictionary['stat']
        name = stat_inner_list['name']
        base_stat = stat_dictionary['base_stat']
        stat_tuple = (name, base_stat)
        stats.append(stat_tuple)

    abilities = []
    abilities_dictionary = pokemon_info['abilities']

    for list_dictionaries in abilities_dictionary:
        ability = list_dictionaries['ability']['name']
        abilities.append(ability)

    pokemon_data.append(pokemon_name)
    pokemon_data.append(stats)
    pokemon_data.append(abilities)
    print(pokemon_data)
    return pokemon_data

def main(args):
    if args.action == 'generation':
        pokedex = get_Pokedex(args.action, args.searchable)
        print("=======================================================================================================")
        print("Pokemon list in order")
        for pokemon in pokedex:
            print(str(pokemon[0]) + "-" + pokemon[1])

    elif args.action == 'entry':
        pokemon_info = get_Pokemon("pokemon", args.searchable)

if __name__ == '__main__':
    # When I use argparse to parse my command line, I usually
    # put the argparse setup here in the global code, and then
    # call a function called main to do the actual work of
    # the program.
    parser = argparse.ArgumentParser(description='Get Pokemon data from pokeapi.co')

    parser.add_argument('action',
                        metavar='action',
                        help='action to perform on the word ("generation" or "entry")',
                        choices=['generation', 'entry'])

    parser.add_argument('searchable',
                        metavar = 'searchable',
                        help='for generation: numbers(1-7) || for Pokedex entry: numbers(1-802) or name of a Pokemon')

    args = parser.parse_args()
    main(args)