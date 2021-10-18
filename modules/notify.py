import os

def broadcast(text_head, text_body=None, icon=None):
    """Broadcast a message warning to the user with notify-send.

    parameters
      text_head - The title of the notification
      text-body - The body of the notification
      icon - The icon to display"""

    # Get the file for the icons
    if icon:
        program_directory = os.path.dirname(__file__)
        icon_file = os.path.join(program_directory, "../assets/icons/", icon)
    else:
        icon_file = None

    os.system(f'notify-send "{text_head}" "{text_body}" --icon={icon_file}')
