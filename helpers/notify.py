import os

def broadcast(text_head, text_body=None, icon=None):
    """Broadcast a message warning to the user with notify-send.

    parameters
      text_head - The title of the notification
      text-body - The body of the notification
      icon - The icon to display"""

    program_directory = os.path.dirname(__file__)
    icon_file = os.path.join(program_directory, "../assets/", icon)

    os.system(f'notify-send "{text_head}" "{text_body}" --icon={icon_file}')