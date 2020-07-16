from flask import Flask
from flask import render_template
from flask import request, send_file

blackjack_site = Flask(__name__)
blackjack_site.run(host='0.0.0.0', port='8888')


@blackjack_site.route('/')
def hubsite_index():
    return render_template('index.html', settings=settings, version=version)


@blackjack_site.route('/devices/')
@blackjack_site.route('/devices/<guid>')
def hubsite_spots(guid=None):
    return render_template('devices.html', guid=guid, settings=settings, version=version)


@blackjack_site.route('/metadata/')
@blackjack_site.route('/metadata/<guid>')
def hubsite_spots_metadata(guid=None):
    if guid is None:
        metadata_json = json.dumps(database.get_metadata())
    else:
        metadata_json = json.dumps(database.get_metadata(guid=guid))
    return metadata_json