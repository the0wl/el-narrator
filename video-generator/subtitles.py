from moviepy.editor import (TextClip)
from moviepy.video.tools.subtitles import SubtitlesClip

import os
import re
import time

def subtitles(filename):
  if not isinstance(filename, str):
    raise Exception("The `filename` parameter must be a string")
  
  generator = lambda txt : TextClip(
    txt, 
    font='Arial', 
    fontsize=40, 
    color='white', 
    stroke_width=1.5, 
    bg_color='black'
  )
  
  _, extension = os.path.splitext(filename)
  
  if extension == '.srt':
    subs = get_srt_subs(filename)
  else :
    subs = get_subs(filename)
  
  return SubtitlesClip(subs, generator)
  
def get_srt_subs(filename):
  SUBS_REGEX = '([0-9]{2}:[0-9]{2}:[0-9]{2},[0-9]{2}.{5}[0-9]{2}:[0-9]{2}:[0-9]{2},[0-9]{2})\n(.+)?'
  data = ''
  
  with open(filename, "r", encoding='utf-8') as f:
    lines = f.readlines()
    data = ''.join(lines)
  
  subsArray = re.findall(SUBS_REGEX, data)
    
  subs = []

  for sub in subsArray:
      subs.append(((str_to_sec(sub[0][0:8]), str_to_sec(sub[0][16:-3])), str(sub[1])))
 
  #falta uma legenda vazia
      
  return subs
  
def get_subs(filename):
  return []

def str_to_sec(text):
  time_obj = time.strptime(text, '%H:%M:%S')
  return float((time_obj.tm_min * 60) + (time_obj.tm_sec))