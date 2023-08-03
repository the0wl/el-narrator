import { config } from 'dotenv'
import { z } from 'zod'

config()

const envSchema = z.object({
  TTS_ENDPOINT: z.string(),
  API_KEY: z.string(),
  OUTPUT_PATH: z.string().default('build/audio/'),
  MODEL_ID: z.string().default('eleven_multilingual_v1'),
})

const _env = envSchema.safeParse(process.env)

if (_env.success === false) {
  console.error('⚠ Invalid environment variables', _env.error.format())

  throw new Error('Invalid environment variables')
}

export const env = _env.data