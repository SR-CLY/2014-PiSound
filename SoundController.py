HARD_CODE = False #Hard Coding Test without Robot! (cycles through all sounds)

print "Program Started" 
import vlc, time
try:
    import RPi.GPIO as GPIO
    print "GPIO Version: " + GPIO.VERSION
except: 
    print"Error Importing GPIO Library."
pins = [17,21,22]
readpinNum = 4
sounds = { #Dictionary entery for decoding binary
    '000': False, #Stops the currant playback when envoked
    '001': 'R2D2.mp3',
    '010': 'Radar.mp3',
    '011': 'Valkyries.mp3',
    '100': 'DialUp.mp3',
    '101': 'Dixie.mp3',
    '110': 'NyanCat.mp3',
    '111': 'SuperMarioTheme.mp3'
}
modePin = 10

def playSound(sound, player):
    """Plays Sound File"""
    print "Playing: " + sound 
    player.set_mrl(sound)
    player.play()

def getFromPi(pins):
    """ Decodes the input from GPIO and returns as Binary String"""
    binary = ""
    for pin in pins:
        inpin = GPIO.input(pin)
        if inpin:
            binary +="1"
        else:
            binary += "0"
    print "Code Detected: " + binary
    return binary

def stopSound(player):
    """Stops the Playback of sound and resets MRL"""
    print "Stopping Playback"
    player.stop()
    player.set_mrl('')
    print ""

def playStartupSound(player):
    """Plays the default sound for robot startup"""
    print "Playing Start Sound"
    player.set_mrl('Beep.mp3')
    player.play()
    
def playSingleSound(player):
    print "Playing Single Sound!"
    player.set_mrl('Circus.mp3')
    player.play()

instance= vlc.Instance(['--play-and-exit'])
player=instance.media_player_new()
print "VLC Configured."
if not HARD_CODE:
    print "Configuring GPIO..."
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(readpinNum, GPIO.IN)
    GPIO.setup(modePin, GPIO.IN)
    for pin in pins: #set up the pins
        GPIO.setup(pin, GPIO.IN)
    playStartupSound(player)
    print "Waiting for start command..."
    while not GPIO.input(readpinNum):
        pass
    if GPIO.input(modePin):
        playSingleSound(player)
        while True:
            pass
    else:
        print "Now Scanning for Pin Input...\n"
        while True: #Main Checking Loop
            readpin = False
            while not readpin:
                readpin = GPIO.input(readpinNum)
            print "Found"
            binary = getFromPi(pins)
            fileName = sounds[binary]
            if not fileName:
                stopSound(player)
            else:
                playSound(fileName, player)
            time.sleep(0.2)
elif HARD_CODE:
    print "Hard Coding Mode Enabled!\n"
    soundlist = ["R2D2.mp3", "Radar.mp3", "Valkyries.mp3", "Beep.mp3", "Dixie.mp3", "SuperMarioTheme.mp3", "NyanCat.mp3"]
    for sound in soundlist:
        playSound(sound, player)
        time.sleep(7)
        stopSound(player)
        time.sleep(0.1)
    print "Hard Coding Complete"
