# 2014-PiSound

This is the section of the codebase that ran on the raspberry pi. Communication was done through the ruggeduinos GPIO pins, through a current control circuit, and into the Pi's GPIO pins.

At certain points of the robots strategy process, the robot would send commands to the Pi, causing it to play sound out the speakers [on the side of the robot](https://flic.kr/p/sjyMiS).

The robot side of the code can be found [here](https://github.com/SR-CLY/2014/blob/master/sound.py).

## Problems
1 thing we forgot to take into account, was that the arena had it's own speaker equipment, that was far bigger than our robot let alone our speakers. It was almost impossible to hear anything, but that didnt stop us getting some weird looks during practice!

__Note__: Sound files are not included in this repo.
