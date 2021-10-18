import os

def play_sound(sound_file):
    """Play a sound from the program's /sound directory

    parameters
        sound_file - name of the sound file to play in /sound"""

    program_directory = os.path.dirname(__file__)
    sound_file = os.path.join(program_directory, "../sound/", sound_file)

    # Use sox to play sound
    os.system(f"play -v 4 {sound_file} > /dev/null 2>&1 &")
