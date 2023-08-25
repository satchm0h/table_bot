# Table Webex Bot

This is an example webex bot that just outputs an ASCII formatted text table. 

This repo can be used to scaffold a very basic webex bot that leverages the awesome [webex_bot](https://github.com/fbradyirl/webex_bot) python framework that leverages the web sockets Webex API.
## Configuration

### Environment Variables

```sh
export WEBEX_TEAMS_ACCESS_TOKEN=XXX
export WEBEX_EMAIL=<your email>
```
### Config File

As an alternative to definfing the environment variables you can instead
define a YAML config file at `~/.table_bot.yml` with the following contents

```yaml
webex_email: <YOUR EMAIL ADDRESS HERE>
webex_token: <YOUR WEBEX TOKEN HERE>

```
## Running the Bot

### Install Dependencues

```sh
# Recommended to first create and use a virtual environment before running the following:
pip install -r requirements.txt
```

### Run the script

```
python3 bot.py
```

