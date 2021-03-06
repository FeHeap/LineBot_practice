# -*- coding = utf-8 -*-
# @Time: 2021/8/13 上午 06:04
# @Software: PyCharm

from app import app, handler
from flask import request, abort, render_template
from linebot.exceptions import InvalidSignatureError

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/callback', methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'