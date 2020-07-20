import json

from flask import Flask
from flask import render_template
from flask import request, send_file

from cards import Deck, Player

blackjack_site = Flask(__name__)

player_name = 'Tanner'
player = Player(player_name)


@blackjack_site.route('/')
def blackjack_index():
    return render_template('blackjack.html')


@blackjack_site.route('/player/money')
def get_player_money():
    money = player.money
    return json.dumps({'money': money})



blackjack_site.run(host='localhost', port=8081)


# @blackjack_site.route('/devices/')
# @blackjack_site.route('/devices/<guid>')
# def hubsite_spots(guid=None):
#     return render_template('devices.html', guid=guid, settings=settings, version=version)
#
#
# @blackjack_site.route('/metadata/')
# @blackjack_site.route('/metadata/<guid>')
# def hubsite_spots_metadata(guid=None):
#     if guid is None:
#         metadata_json = json.dumps(database.get_metadata())
#     else:
#         metadata_json = json.dumps(database.get_metadata(guid=guid))
#     return metadata_json