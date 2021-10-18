import os

from sys import path
path.append("..")
import config.config as cf

def play_sound(sound_file):
    """Play a sound from the program's /assets/audio directory

    parameters
        sound_file - name of the sound file to play in /assets/audio"""

    if sound_file:
        program_directory = os.path.dirname(__file__)
        sound_file = os.path.join(program_directory, "../assets/audio/", sound_file)

        # Use sox to play sound
        os.system(f"mpv {sound_file} --volume={cf.sound_volume} > /dev/null 2>&1 &")
