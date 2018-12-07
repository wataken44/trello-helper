#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" add_periodical_task.py


"""

import datetime
import argparse

import common

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--force", action="store_true")
    args = parser.parse_args()

    now = datetime.datetime.now()

    client = common.get_client()
    config = common.get_config()["add-periodical-task"]
    
    for task in config:
        add_periodical_task(client, task, now, args.force)

def add_periodical_task(client, task, now, force):

    period = task["period"]
    at_arr = task["at"]
    title = replace_date(task["title"], now)
    board_name = task["board"]
    list_name = task["list"]

    if period == "month":
        if (force == False) and (now.day not in at_arr):
            return
    elif period == "week":
        if (force == False) and (now.isoweekday() not in at_arr):
            return
        
    board = common.get_board_by_name(client, board_name)
    lst = common.get_list_by_name(board, list_name)
    card = common.get_card_by_name(lst, title)

    if card:
        return

    card = lst.add_card(title)
    due = None
    if period == "month":
        dy = now.year
        dm = now.month + 1
        if dm == 13:
            dy = dy + 1
            dm = 1
        
        due = datetime.datetime(dy, dm, 1, 18, 0, 0) - datetime.timedelta(days=1)
    elif period == "week":
        due = now + datetime.timedelta(days=7)
        
    card.set_due(due)
        
    
def replace_date(title, now):

    title = title.replace("%month%", str(now.month))
    title = title.replace("%day%", str(now.day))

    return title
        
if __name__ == "__main__":
    main()
