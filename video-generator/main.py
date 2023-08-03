from moviepy.editor import (
  VideoFileClip,
  AudioFileClip,
  TextClip,
  afx,
  concatenate_videoclips,
  CompositeVideoClip,
  CompositeAudioClip
  )
from moviepy.video.tools.subtitles import SubtitlesClip
from subtitles import subtitles

# Generates subtitles based on text file
#with open("assets/script/example.txt", "r", encoding="utf-8") as f:
#  lines = f.readlines()
#  data = ''.join(lines)

#tmpSubsText = data.split('subtitles\n')[1]
#subsArray = tmpSubsText.split('\\subtitles')[0].split('\n')
#subsArray.pop()

#subs = []

#for sub in subsArray:
#  subs.append(((float(sub[1:4]), float(sub[6:9])), str(sub[10:])))

#generator = lambda txt : TextClip(txt.encode(encoding = 'UTF-8', errors = 'strict'), font='Arial', fontsize=40, color='white', stroke_width=1.5, bg_color='black')
#subtitles = SubtitlesClip(subs, generator)

subtitles = subtitles('assets/script/example.srt')

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