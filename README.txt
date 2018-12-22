# slackify

Slackify notifies a specified channel with a specified message. The channel, url, and message can either be specified on the command line or from a configuration plist. Slackify is intended to be used from the command line to enable notification of a finished process.

# How to use:

`slackify.py -c "#general" -m "This is my custom message."`

# Example:

`echo hello; slackify.py -c "#general" -m "The echo command finished."`

Slackify requires the `management_tools` module, so it has been included for convenience.
