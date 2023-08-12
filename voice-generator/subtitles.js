import fs from 'fs-extra'

const readScriptFile = () => {
  if (!process.argv[2])
    throw new Error('The text file path parameter must be provided')
  
  return [process.argv[2].split('.')[1], fs.readFileSync(process.argv[2], 'utf8')]
}

export const subtitles = () => {
  const [extension, data] = readScriptFile()
  return (extension === 'srt') ? getSRTSubtitles(data) : getSubtitles(data)
}

// Given the whole text from a '.msv' file:
// - Remove all text outside `subtitles` to `/subtitles` area
// - Remove empty line last position
// - Remove timestamp

const getSubtitles = (data) => {
  const rawSubtitles = data.split('subtitles\r\n')[1].split('\\subtitles')[0].split('\r\n')
  rawSubtitles.pop()
  const subtitlesText = rawSubtitles.map(x => x.substr(29)).join('\n')

  return subtitlesText
}

// Given the whole text from a '.srt' file:
// - Remove timestamp
const getSRTSubtitles = (data) => {
  return data.match(/^(?!\d).+/gm).join('\n')
}