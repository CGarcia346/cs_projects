#!/usr/bin/env python3
'''
    api_test.py
    Carlos Garcia & Joey Cook-Gallardo, 15 April 2018
    An api that allows its user to search for the pokemon in a generation or the entry of a pokemon
'''

import sys
import argparse
import json
import urllib.request
import math

def get_Pokedex(gen, searchable):
    '''
        searches for and prints out a list of all the pokemon in a generation
        parameter: generation, specifies that the user is searching for the pokemon within a generation
        parameter: searches for the specific number of the generation
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
        count += 1
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
    '''
       organizes the list of pokemon/id tuples
       parameter: list of tuples, tuple contains a pokemon and its id number
    '''
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
    '''
       searches for and prints out the entry of a pokemon
       parameter: pokemonSpecies, specifies that the user is searching for a pokemon entry
       parameter: entry, the pokemon the user wants the entry of
   '''

    base_url = 'http://pokeapi.co/api/v2/{0}/{1}/'
    url = base_url.format(pokemonSpecies, entry)
    request = urllib.request.Request(url)
    request.add_header("User-Agent", "Garco")
    data_from_server = urllib.request.urlopen(request).read()
    string_from_server = data_from_server.decode('utf-8')
    pokemon_info = json.loads(string_from_server)
    pokemon_data = []

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

    types = []
    type_dictionary = pokemon_info['types']

    for type_dictionaries in type_dictionary:
        type = type_dictionaries['type']['name']
        types.append(type)

    pokemon_data.append(pokemon_name)
    pokemon_data.append(stats)
    pokemon_data.append(abilities)
    pokemon_data.append(types)
    return pokemon_data

def main(args):
    '''
       interprets input and runs methods based off the input
    '''
    check_searchable = [1,2,3,4,5,6,7]

    if args.action == 'generation':

        try:
            pokedex = get_Pokedex(args.action, args.searchable)

        except:
            can_search = False
            while(not can_search):
                print("Invalid search, Try Again! Maybe a valid number entry(1-7) will work")
                args.searchable = input()
                try:
                    pokedex = get_Pokedex(args.action, args.searchable)
                    can_search = True
                except:
                    can_search = False



        print("=======================================================================================================")
        print("Pokemon list in order")
        for pokemon in pokedex:
            print(str(pokemon[0]) + "-" + pokemon[1])

    elif args.action == 'entry':

        try:
            pokemon_info = get_Pokemon('pokemon', args.searchable)

        except:
            can_search = False
            while(not can_search):
                print("Invalid search, Try Again! Maybe a valid number entry(1-802) or proper name will work")
                args.searchable = input()
                try:
                    pokemon_info = get_Pokemon('pokemon', args.searchable)
                    can_search = True
                except:
                    can_search = False

        name = pokemon_info[0]
        print("\n \t" + name[0].upper() + name[1:] + ":")

        stat_list = pokemon_info[1]
        print("\t \t Stats-")
        for stat in stat_list:
            print("\t \t \t" + stat[0] + ": " + str(stat[1]))
        print()

        ability_list= pokemon_info[2]
        print("\t \t Abilities-")
        for ability in ability_list:
            print("\t \t \t" + ability)
        print()

        type_list = pokemon_info[3]
        print("\t \t Type: ")
        for type in type_list:
            print("\t \t \t" + type)
        print()

if __name__ == '__main__':
    '''
       input from the user and provides information about how to use the api to the user
    '''
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