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

const getSubtitles = (data) => {
  const rawSubtitles = data.split('subtitles\r\n')[1].split('\\subtitles')[0].split('\r\n').join('\n')
  
  return rawSubtitles.match(/^(?!\d).+/gm).join('\n')
}

const getSRTSubtitles = (data) => {
  return data.match(/^(?!\d).+/gm).join('\n')
}