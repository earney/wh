#!/usr/bin/env python3

from moviepy.editor import *
import os
import re # to parse this file to make the credits


W, H = 1280, 720 # dimensions of the final video

# These very useful functions resize the clips to
# the dimensions of the final video

VideoFileClip.reW = lambda clip :  clip.resize(width=W)
VideoFileClip.reH = lambda clip :  clip.resize(height=H)

def zoom_example():
   _map=ImageClip("../images/us_wiregrass_map.png")\
    .resize(height=H*4)\
    .resize(lambda t: 1+0.1*t)\
    .set_position(('right', 'bottom'))\
    .set_duration(7)
    #.set_position(('center', 'center'))

   _video = CompositeVideoClip([_map]).resize(width=W)

   _video.to_videofile("../videos/zoom_map.mp4", fps=30)

zoom_example()
