from playsound import playsound
import keyboard

def playing_sound_repeatedly(): # -> loop
    print('Press C to exit the sound')
    while True:
        # python file\PLay beep sound\ is edited from path file
        playsound('Computer-beep-beeping-1-www.FesliyanStudios.com.mp3') # play the sound
        if keyboard.is_pressed('c'):
            print('C has been pressed, programme will be existed')
            exit()