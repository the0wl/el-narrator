from moviepy.editor import (
  VideoFileClip,
  AudioFileClip,
  afx,
  concatenate_videoclips,
  CompositeVideoClip,
  CompositeAudioClip
  )
from subtitles import subtitles
from settings import settings

subs = subtitles()

# Create sounds (narration, musics, ...)

narrator = AudioFileClip("build/audio/my-narrator.mp3").fx(afx.volumex, 0.3)
background_music = AudioFileClip("assets/music/Empty mind.mp3").subclip(1, 9).fx(afx.volumex, 0.015)

# Create video clips

clip1 = VideoFileClip("assets/video/Transito.mp4").subclip(1, 4)
clip2 = VideoFileClip("assets/video/Evolução.mp4").subclip(1, 6)

# Combine and compose final video file

combined = concatenate_videoclips([clip1, clip2])
combined.audio = CompositeAudioClip([narrator, background_music])

width, height, subtitle_h = settings()

compose = CompositeVideoClip(size=(width, height), clips=[combined, subs.set_position(('center', subtitle_h))])
compose.write_videofile("build/video.mp4")