import { getSubtitles } from './src/text-input.js'
import { textToSpeech } from './src/text-to-speech.js'

const subtitles = getSubtitles()

textToSpeech(subtitles).then((data) => {
  console.log(data)
})