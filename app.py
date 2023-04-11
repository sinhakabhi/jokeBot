from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

SLACK_BOT_TOKEN = 'SLACK_BOT_TOKEN'
SLACK_APP_TOKEN = 'SLACK_APP_TOKEN'

app = App(token=SLACK_BOT_TOKEN, name='JokeBot')

@app.event("app_home_opened")
def say_hello(message, say):
    say("Hello User")


def main():
    handler = SocketModeHandler(app, SLACK_APP_TOKEN)
    handler.start


if __name__ == "main":
    main()
