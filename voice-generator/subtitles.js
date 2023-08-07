import fs from 'fs-extra'

const readScriptFile = () => {
  if (process.argv[2]) {
    return fs.readFileSync(process.argv[2], 'utf8')
  } else {
    throw new Error('The text file path parameter must be provided')
  }
}

export const getSubtitles = () => {
  const data = readScriptFile()

  // Remove all text outside `subtitles` to `/subtitles` area
  const rawSubtitles = data.split('subtitles\r\n')[1].split('\\subtitles')[0].split('\r\n')
  
  // Remove empty line last position
  rawSubtitles.pop()
  
  // Remove timestamp
  const subtitlesText = rawSubtitles.map(x => x.substr(29)).join('\n')

  return subtitlesText
}

const getSRTSubtitles = () => {
  return subtitlesText = data.match(/^(?!\d).+/gm)
}