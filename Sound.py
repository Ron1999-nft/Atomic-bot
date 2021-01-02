from playsound import playsound
import keyboard, time

def playing_sound_repeatedly(): # -> loop
    t_end = time.time() + 60
    while time.time() < t_end:
        playsound('Computer-beep-beeping-1-www.FesliyanStudios.com.mp3')  # play the sound
