# -*- coding = utf-8 -*-
# @Time: 2021/8/13 上午 06:04
# @Software: PyCharm

from app import line_bot_api, handler

from linebot.models import MessageEvent, TextMessage, TextSendMessage

@handler.add(MessageEvent, message=TextMessage)
def echo(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text)
    )