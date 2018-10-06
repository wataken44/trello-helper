#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" common.py


"""


import codecs
import json
import os
import sys

from trello import TrelloClient

_config = None
_client = None

def load_config():
    global _config

    fn = os.path.dirname(__file__) + "/config.json"
    fp = codecs.open(fn, 'r', 'utf-8')
    _config = json.load(fp)
    fp.close()

def get_config():
    global _config

    if _config is None:
        load_config()
    
    return _config

def get_client():
    global _client
    secret = get_config()["secret"]

    if _client is None:
        _client = TrelloClient(
            api_key=secret["api_key"],
            api_secret=secret["api_secret"],
            token=secret["token"],
        )

    return _client

def get_board_by_name(client, name):
    for board in client.list_boards():
        if board.name == name:
            return board
    
    return None

def get_list_by_name(board, name):
    for lst in board.list_lists():
        if lst.name == name:
            return lst

    return None

def get_card_by_name(lst, name):
    for card in lst.list_cards():
        if card.name == name:
            return card

    return None
