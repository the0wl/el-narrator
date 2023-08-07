import { getSubtitles } from './voice-generator/subtitles.js'
import { textToSpeech } from './voice-generator/text-to-speech.js'

const subtitles = getSubtitles()

console.log(subtitles)

//textToSpeech(subtitles).then((data) => {
//  console.log(data)
//})