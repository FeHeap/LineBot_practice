# -*- coding = utf-8 -*-
# @Time: 2021/8/13 上午 06:04
# @Software: PyCharm

from app import line_bot_api, handler

from linebot.models import MessageEvent, TextMessage, TextSendMessage
from app import forms_camp

@handler.add(MessageEvent, message=TextMessage)
def Reply(event):
    print("user_id:",event.source.user_id)
    if event.source.user_id == 'U2a11299ffe4f96bec2317e639f5d7bfa':
        command = str.strip(event.message.text)
        if command[0:2] == '表單':
            command = str.strip(command[2:])
            if command in forms_camp.date_to_link:
                message_to_client = '今日的簽到表單\n' + forms_camp.date_to_link[command]
                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text=message_to_client)
                )