import requests
import json
import time
import random

# ANSI escape code for green color
GREEN = "\033[92m"
RESET_COLOR = "\033[0m" 
   
def send_message(message, channel_id, authorization):
    header = {
        "Authorization": authorization,
        "Content-Type": "application/json",
        #"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",
    }

    data = {
        "content": message,
        "nonce": str(random.randrange(0, 100000000000000000)),
        "tts": False,
    }

    discord_url = f"https://discord.com/api/v9/channels/{channel_id}/messages"

    try:
        res = requests.post(url=discord_url, headers=header, json=data)
       #print(res.status_code)
       #print(res.content)
        res_json = res.json()
        res_json = res.json()
        print(f"{GREEN}Message sent!{RESET_COLOR} ID: {res_json['id']}, Content: {res_json['content']}{RESET_COLOR}")
        return res_json
    except Exception as e:
        print(f"Error sending message: {e}")
        return none
def chat(channel_id, authorization, message_file, num_messages, line_delay, message_interval):
    with open(message_file) as fin:
        lines = fin.readlines()

    for _ in range(num_messages) if num_messages > 0 else itertools.count():
        for line in lines:
            send_message(line.strip(), channel_id, authorization)
            time.sleep(line_delay)

        if num_messages > 0:
            time.sleep(message_interval)

def main():
    channel_id = "channel_id" #Replace with the Discord channel ID where you want to send messages
    authorization = "Auth_Token" #Replace this with your Authentication Token
    message_file = "Chat.txt"
    num_messages = 1  # Replace with the number of messages you want to send (0 for infinite loop)
    line_delay = 5  # Replace with the delay between lines (in seconds)
    message_interval = 5  # Replace with the interval between messages (in seconds)

    try:
        chat(channel_id, authorization, message_file, num_messages, line_delay, message_interval)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
    