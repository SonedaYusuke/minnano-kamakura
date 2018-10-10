from flask import Flask, request, abort
import os
from time import sleep
import carousel
import datetime
from spread import vote
import re

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,FlexSendMessage, TextComponent,Base, TemplateSendMessage, URIAction
)

from linebot.http_client import (
    RequestsHttpClient
)



app = Flask(__name__)

line_bot_api = LineBotApi('hRPpuJajfnuKOuky2DiGhTwh6zv2ZdoVlLyAwElbw9DdcGP7uQO+g6V5AAEL+JPW8nG0REuIrIV5v9NE8S+oDIFVOuIcoO4SN7LKXxSIRSHHQxQpEd4uAmLOK31ptpklYM6TgAFsCJ7zq5HKWphWhQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('493cd24ee99ce4828e9e32d634ffcdde')


@app.route("/webhook", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)

    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):

    if event.message.text == '今日のかまくら':
        pass
    elif event.message.text == 'ランキング':
        reply_line_bot(event)
    elif re.match(r'^\d番に投票', event.message.text):
        if event.message.text == "1番に投票":
          vote("A2")
        if event.message.text == "2番に投票":
          vote("B2")
        if event.message.text == "3番に投票":
          vote("C2")
        if event.message.text == "4番に投票":
          vote("D2")
        if event.message.text == "5番に投票":
          vote("E2")
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text = "ご投票ありがとうございます！" + event.message.text + "しました！")
        )
    else:
        line_bot_api.reply_message(
          event.reply_token,
          TextSendMessage(text="申し訳ありません，無効なメッセージが送られました．もう一度お試しください")
        )

def reply_line_bot(event):
    testcontents = carousel.testcontents
    content = TemplateSendMessage.new_from_json_dict(testcontents)

    line_bot_api.reply_message(
        event.reply_token,
        content
    )


if __name__ == "__main__":
    port = int(os.getenv("PORT", 3000))
    app.run(host="0.0.0.0", port=5000)