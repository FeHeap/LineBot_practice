# -*- coding = utf-8 -*-
# @Time: 2021/8/13 上午 06:04
# @Software: PyCharm

from app import line_bot_api, handler

from linebot.models import MessageEvent, TextMessage, TextSendMessage
from app import camp

@handler.add(MessageEvent, message=TextMessage)
def Reply(event):
    print("user_id:",event.source.user_id)
    command = str.strip(event.message.text)

    if event.source.user_id == 'U2a11299ffe4f96bec2317e639f5d7bfa' or event.source.user_id == 'U4a033bb7c0bf8c6fa94c5d2735676d47':
        if command[0:2] == '表單':
            command = str.strip(command[2:])
            if command in camp.date_to_link:
                message_to_client = f'今日({command})的簽到表單\n' + camp.date_to_link[command]
                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(text=message_to_client)
                )

    if command in camp.others:
        message_to_client = camp.others[command]
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=message_to_client)
        )
