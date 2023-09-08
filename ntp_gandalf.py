import vlc
import datetime
from time import ctime
import time
import ntplib
c = ntplib.NTPClient()


import time

# creating vlc media player object
media_player = vlc.MediaPlayer()

# media object
vlc.libvlc_media_list_player_set_playback_mode(media_player, 2)
media = vlc.Media("HD Epic Sax Gandalf.mp4")

#make the media loop
media.add_option(":input-repeat=1")



# setting media to the media player
media_player.set_media(media)
# it should loop



# start playing video
media_player.play()
media_player.set_pause(1)
approx_time = response = c.request('europe.pool.ntp.org', version=3).tx_time
approx_time_sys_time = time.time()
while True:
    try:
        response = c.request('europe.pool.ntp.org', version=3)
    except Exception:
        print("bad_connection")
        approx_time = approx_time + (time.time() - approx_time_sys_time)
        approx_time_sys_time = time.time()
    else:
        approx_time = response.tx_time
        approx_time_sys_time = time.time()

    print(ctime(response.tx_time))
    START="2023-09-08 12:15:00"


    start_time = (datetime.datetime(2023, 9,8, 12, 27,30) - datetime.datetime(1970,1,1)).total_seconds()
    print("start", start_time)
    # get the difference between the two times
    # and convert it to seconds
    diff = (start_time - response.tx_time) - 2* 60 * 60
    print(diff)
    if diff < 10:
        time.sleep(diff)
        break

# play the video again seemless
while True:
    media_player.play()
