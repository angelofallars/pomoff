import os

def play_sound(sound_file):
    """Play a sound from the program's /assets/audio directory

    parameters
        sound_file - name of the sound file to play in /assets/audio"""

    program_directory = os.path.dirname(__file__)
    sound_file = os.path.join(program_directory, "../assets/audio/", sound_file)

    # Use sox to play sound
    os.system(f"play -v 4 {sound_file} > /dev/null 2>&1 &")
