#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" fill_due.py


"""

import datetime

import common


def main():

    client = common.get_client()
    config = common.get_config()["fill-due"]
    
    now = datetime.datetime.now()
    
    for conf in config:
        bn = conf["board"]
        ln = conf["list"]
        period = conf["period"]
        
        board = common.get_board_by_name(client, bn)
        lst = common.get_list_by_name(board, ln)

        due = now + datetime.timedelta(days=period)

        for card in lst.list_cards():
            if card.due_date != '':
                continue

            card.set_due(due)
    

if __name__ == "__main__":
    main()
