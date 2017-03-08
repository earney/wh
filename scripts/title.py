#!/usr/bin/env python3

from moviepy.editor import *


_png=ImageClip("../images/wiregrass_title.png")
_zoom=_png.resize(lambda t: 1+0.1*t)\
          .set_position(('center', 'center'))\
          .set_duration(5)

_audio = AudioFileClip("../audio/Night_Sounds_-_Crickets-Lisa_Redfern-591005346.wav")

_zoom1 = CompositeVideoClip([_zoom])
_zoom1=_zoom1.set_audio(_audio).set_duration(5)
_zoom1.write_videofile("../videos/wiregrass_title.mp4", fps=30)
