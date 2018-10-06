#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" test.py


"""


import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import common

def main():
    client = common.get_client()

    print(len(client.list_boards()))
    print(client.list_boards())

    board = common.get_board_by_name(client, 'home')
    lst = common.get_list_by_name(board, 'task')

    print(lst.list_cards())
    
if __name__ == "__main__":
    main()
