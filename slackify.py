#!/usr/bin/python

from management_tools.slack import IncomingWebhooksSender as IWS
import socket
import subprocess
import sys
import re
import plistlib
import re
import argparse
import os

def main():
    parser = argparse.ArgumentParser(description='Send Slack notifications.')
    parser.add_argument('-c', '--channel', nargs=1, help='the Slack channel')
    parser.add_argument('-m', '--message', nargs=1, help='the slack message')
    parser.add_argument('-u', '--url', nargs=1, help='the slack url')

    args = parser.parse_args()

    if args.channel:
        channel = args.channel[0]
    else:
        channel = slack_data['channel']

    if args.message:
        message = args.message[0]
    else:
        message = slack_data['message']

    if args.url:
        url = args.url[0]
    else:
        url = slack_data['url']

    current_ip = socket.gethostbyname(socket.gethostname())
    bot = IWS(url, bot_name=current_ip, channel=channel)

    cmd = ['hostname']
    hostname_output = subprocess.check_output(cmd)
    hostname = re.split("\.", hostname_output)[0]
    bot.send_message("Notification for {0}: {1}".format(hostname, message))
    print("Slackify message sent.")

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    slack_plist = os.path.join(script_dir, "public/slack_config.plist")
    slack_data = plistlib.readPlist(slack_plist)
    main()
