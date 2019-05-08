""" __init__.py for sqlfluff """

import configparser
import pkg_resources


# Get the current version
config = configparser.ConfigParser()
config.read_file(open(pkg_resources.resource_filename('sqlfluff', 'config.ini')))

__version__ = config.get('sqlfluff', 'version')
