# -*- coding = utf-8 -*-
# @Time: 2021/8/13 上午 06:02
# @Software: PyCharm

from flask import Flask
from linebot import LineBotApi, WebhookHandler

app = Flask(__name__)

import configparser
config = configparser.ConfigParser()
config.read('config.ini')
line_bot_api = LineBotApi(config.get('line-bot', 'channel_access_token'))
handler = WebhookHandler(config.get('line-bot', 'channel_secret'))

from app import routes, models_for_line