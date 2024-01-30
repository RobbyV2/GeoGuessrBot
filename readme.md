# GeoGuessr Selenium Discord Bot

Let's you create lobbies for people to play, in a discord bot!

## Setup

- Clone the repository.
- Create an env with `python -m venv env` or with py launcher, and enable it.
- Rename `config.json.example` to `config.json`, fill in the values.
- - Admins are the discord user id's.
- - gg = GeoGuessr.
- Run `pip install -r requirements.txt`
- Run `python main.py`, and it should run!

If there are any errors, try removing headless mode in `getCode.py` and debug from there.
