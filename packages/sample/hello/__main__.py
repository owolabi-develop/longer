from slack_sdk import WebClient
#logging.basicConfig(level=logging.DEBUG)
from slack_sdk.errors import SlackApiError
def main(args):
      name = args.get("name", "stranger")
      greeting = "Hello " + name + "!"
      print(greeting)
      return {"body": greeting}
