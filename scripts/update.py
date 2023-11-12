import json
import logging
from multiprocessing import Pool
from pathlib import Path
from urllib.request import urlopen

BASE_DIR = Path(__file__).resolve().parent.parent
PLUGINS_DIR = BASE_DIR / 'plugins'

BASE_URL = 'https://codeberg.org/micro-plugins/plugin-channel/raw/branch/main/plugins/{}.json'


def get_channels():
    with open(BASE_DIR / 'PLUGINS.json') as file:
        return json.load(file)


def get_plugin(url):
    with urlopen(url) as response:
        return json.load(response)


def write_json(plugin, name):
    with open(name, 'w') as file:
        json.dump(plugin, file, ensure_ascii=False, indent=4, sort_keys=True)


def update_plugin(url):
    logging.debug(f'{url=}')
    try:
        plugin = get_plugin(url)
        name = plugin[0]["Name"]
        write_json(plugin, PLUGINS_DIR / f'{name}.json')
        return BASE_URL.format(name)
    except Exception as exc:
        logging.error(f'{url=} {exc=}')


pool = Pool(16)
results = pool.map(update_plugin, get_channels())
pool.close()
pool.join()

write_json(sorted(filter(None, results)), BASE_DIR / 'channel.json')
