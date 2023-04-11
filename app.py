from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

SLACK_BOT_TOKEN = 'xoxb-5083308509781-5076189038295-lhRP7k2VMA5sPU3pkVBbf2jE'
SLACK_APP_TOKEN = 'xapp-1-A0531937FRP-5093235726116-4858d81f4812053564cfd64a9e89c62d70ee1b47bc2bd8e2d8054f3c46c0004f'

app = App(token=SLACK_BOT_TOKEN, name='JokeBot')

@app.event("app_home_opened")
def say_hello(message, say):
    say("Hello User")


def main():
    handler = SocketModeHandler(app, SLACK_APP_TOKEN)
    handler.start


if __name__ == "main":
    main()
