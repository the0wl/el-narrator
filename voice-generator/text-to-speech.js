import axios from 'axios'
import fs from 'fs-extra'
import { env } from './env/index.js'

const method = "POST"

const url = env.TTS_ENDPOINT

const filename = env.OUTPUT_PATH + 'my-narrator.mp3'

const headers = {
  Accept: "audio/mpeg",
  "xi-api-key": env.API_KEY,
  "Content-Type": "application/json",
}

const responseType = "stream"

export const textToSpeech = async (subtitles) => {
  const data = {
    text: subtitles,
    model_id: env.MODEL_ID,
  }

  const response = await axios({ method, url, data, headers, responseType })

  response.data.pipe(fs.createWriteStream(filename))

  return "The narrator audio file has been generated." 
}