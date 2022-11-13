# How to use the music listener

This is a python script that opens up two tabs and plays the music link in them and then closes after a few minutes

# Music Player
music_player.py is the core file, and you can set up a cron job to run this hourly

music_player_tester.py is a test file for you to make sure your dependencies work without sleep times

music_player_manual.py is a file to let you set the number of times you want the sleep cycle to go

Music_player.ipynb is a jupyter notebook to play around with this and Selenium

# python basic how to
cd into this directory
python music_player_tester.py

whenever it spits out an error saying cannot import X, just use "pip install X"
then try it again

# Cron jobs
If you're really hardcore, you can set this up to run every hour, minute, second, day, etc...
you do this using Cron

1. find your python path:
 in terminal type:
python
import sys
print(sys.executable)

copy the resulting path down

2. find your file path
navigate to your file, and use 'pwd'

copy the resulting path down, add /music_player.py

3. become root
$ sudo -s

4. edit crontab
$ EDITOR=/usr/bin/nano crontab -u mborrus -e

5. refer to this for how often you want it to repeat:
https://devhints.io/cron

6. create one line such as this:

1 * * * * /Users/mborrus/opt/anaconda3/bin/python /Users/mborrus/Desktop/Music/music_player.py

this would run the first minute of every hourly

use ctrl X to get about

7. to stop it running use  EDITOR=/usr/bin/nano crontab -u mborrus -e and delete the string
