import { subtitles } from './voice-generator/subtitles.js'
import { textToSpeech } from './voice-generator/text-to-speech.js'

textToSpeech(subtitles()).then((data) => {
  console.log(data)
})