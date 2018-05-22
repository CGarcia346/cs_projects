#!/usr/bin/env python3
'''
    website.py
'''
import sys
import flask

app = flask.Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/')
def get_main_page():
    ''' This is the only route intended for human users '''
    global api_port
    return flask.render_template('main.html', api_port=api_port)

@app.route('/sets')
def get_sets_page():
    global api_port
    return flask.render_template('sets.html', api_port=api_port)

@app.route("/artists")
def get_artists_page():
    global api_port
    return flask.render_template('artists.html', api_port=api_port)

@app.route('/random')
def get_random():
    global api_port
    return flask.render_template('random.html', api_port=api_port)

@app.route('/cards')
def get_card():
    global api_port
    return flask.render_template('cards.html', api_port=api_port)

@app.route('/advancedsearch')
def get_advanced():
    global api_port
    return flask.render_template('advancedsearch.html', api_port=api_port)

@app.route('/set')
def get_set():
    global api_port
    return flask.render_template('set_data.html', api_port=api_port)

@app.route('/card')
def get_a_card():
    global api_port
    return flask.render_template('card_data.html', api_port=api_port)

@app.route('/artist')
def get_artist():
    global api_port
    return flask.render_template('artist_data.html', api_port=api_port)

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print('Usage: {0} host port api-port'.format(sys.argv[0]), file=sys.stderr)
        exit()

    host = sys.argv[1]
    port = sys.argv[2]
    api_port = sys.argv[3]
    app.run(host=host, port=port)
