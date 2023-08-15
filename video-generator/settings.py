import sys

def settings():
  width = int(sys.argv[2])
  height = int(sys.argv[3])
  subtitle_h = int(sys.argv[3]) - 100
  
  return width, height, subtitle_h