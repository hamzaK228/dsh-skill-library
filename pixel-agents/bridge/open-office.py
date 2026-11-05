#!/usr/bin/python3
import pathlib, webbrowser, urllib.parse
secret=(pathlib.Path.home()/'.config/pixel-agents-codex/token').read_text().strip()
webbrowser.open('http://127.0.0.1:4312/?token='+urllib.parse.quote(secret))
