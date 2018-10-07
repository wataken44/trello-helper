trello helper
========================

[Trello](https://trello.com) に標準だとできなかったりプラグインが有償だったりする機能を足すやつ

* 定期的なタスク登録
* 期限設定のないタスクに期限設定

## requirement

* python3
* cron

## install

install

    $ git clone https://github.com/wataken44/trello-helper
    $ pip install -r trello-helper/requirements.txt

config

    $ cd trello-helper/trello_helper/
    $ vi config.json

config.json sample

    {
      "secret": {
        "api_key": "<trello api key>",
        "api_secret": "<trello api secret>",
        "token": "<trello token>"
      },
      "add-periodical-task": [
        {
          "period" : "week",                           // "week" or "month" 
          "at": [1],                                   // if period == "week", 1: Mon, 2: Tue, ... 7: Sun 
          "title": "(%month%/%day%) send weekly report",
          "board": "work",                             // trello board title
          "list": "task"                               // trello list title
        },
        {
          "period" : "month",
          "at": [1],                                   // if period == "month", calendar day
          "title": "(%month%) send monthly report",
          "board": "home",
          "list": "task"
        }
      ],
      "fill-due": [
        {
          "board": "home",
          "list": "task",
          "period": 14                                 // if empty due, set due at today + 14 day
        }
      ]
    }
    

## usage

定期的なタスク登録

    $ python3 add_periodical_task.py

期限設定のないタスクに期限設定

    $ python3 fill_due.py
