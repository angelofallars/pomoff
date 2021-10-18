import os

def broadcast(text_head, text_body):
    """Broadcast a message warning to the user with notify-send.

    parameters
      text_head - The title of the notification
      text-body - The body of the notification"""

    os.system(f'notify-send "{text_head}" "{text_body}"')
