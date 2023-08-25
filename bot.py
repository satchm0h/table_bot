import os
import logging
import yaml

from webex_bot.webex_bot import WebexBot
from table_command import TableCommand


log = logging.getLogger(__name__)


# Support a YAML config file that looks like this:
#   webex_email: <YOUR CCE ID>@cisco.com
#   webex_token: <YOUR WEBEX TOKEN HERE>

CONFIG_FILE_LOCATION = "~/.table_bot.yml"

def parse_yaml_config(config_file_path):
    if not os.path.isfile(config_file_path):
        log.warn(f"Config file '{config_file_path}' not found.")
        return None

    config_dict = None
    with open(config_file_path, 'r') as file:
        try:
            config_dict = yaml.load(file, Loader=yaml.FullLoader)
            print(config_dict)
        except yaml.YAMLError as exc:
            log.warning("Error reading config file: "+ exc)
            return None
    return config_dict


# Gather our required inputs
config = parse_yaml_config(os.path.expanduser(CONFIG_FILE_LOCATION))
if config is None:
    config = dict();

log.info(config);

webex_email = os.getenv('WEBEX_EMAIL')
if webex_email is not None:
    config['webex_email'] = webex_email

access_token = os.getenv('WEBEX_TEAMS_ACCESS_TOKEN')
if access_token is not None:
    config['webex_token'] = access_token


# Make sure we have everything we need
if config.get('webex_email') is None:
    log.error(f"The webex email is not found in the config file {CONFIG_FILE_LOCATION} or the environment var WEBEX_EMAIL")
    exit(3);

if config.get('webex_token') is None:
    log.error(f"The webex token is not found in the config file {CONFIG_FILE_LOCATION} or the environment var WEBEX_TEAMS_ACCESS_TOKEN")
    exit(1);

# Create a Bot Object
bot = WebexBot(teams_bot_token=config['webex_token'],
               approved_users=[config['webex_email']],
               bot_name="Table Bot",
               include_demo_commands=False)

# Instatiate the table command
bot.add_command(TableCommand())

bot.run()
