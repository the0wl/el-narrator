from moviepy.editor import (
  VideoFileClip,
  AudioFileClip,
  afx,
  concatenate_videoclips,
  CompositeVideoClip,
  CompositeAudioClip
  )
from moviepy.video.tools.subtitles import SubtitlesClip
from subtitles import subtitles

#subtitles = subtitles('assets/subtitle/example.srt')
subtitles = subtitles('script/main.msv')

# Create sounds (narration, musics, ...)

narrator = AudioFileClip("build/audio/my-narrator.mp3").fx(afx.volumex, 0.3)
background_music = AudioFileClip("assets/music/Empty mind.mp3").fx(afx.volumex, 0.015)

# Create video clips

clip1 = VideoFileClip("assets/video/Transito.mp4").subclip(1, 4)
clip2 = VideoFileClip("assets/video/Evolução.mp4").subclip(1, 5)

# Combine and compose final video file

combined = concatenate_videoclips([clip1, clip2])
combined.audio = CompositeAudioClip([narrator, background_music])

compose = CompositeVideoClip(size=(1920, 1080), clips=[combined, subtitles.set_position(('center', 980))])
compose.write_videofile("build/video.mp4")