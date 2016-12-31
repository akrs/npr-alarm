import import xml.etree.ElementTree as ET

import requests, pychromecast

def get_xml():
    """
    Gets the podcast description as an XML tree
    """
    r = requests.get('https://www.npr.org/rss/podcast.php?id=500005')
    return ET.fromstring(r.text)

def get_url_and_type(xml):
    """
    Gets the URL of the audio file, and it's type
    """
    attr = xml.find('channel').find('item').find('enclosure').attrib
    return attr['url'], attr['type']

def cast(url, mime, device_name='Andrew\'s room'):
    chromecasts = pychromecast.get_chromecasts()
    cast = next(cc for cc in chromecasts if cc.device.friendly_name == device_name)
    cast.wait()
    cast.media_controller.play_media(url, mime)

def main():
    xml = get_xml()
    url, mime = get_url_and_type(xml)
    cast(url, mime)

if __name__ == '__main__':
    main()