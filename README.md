<center>

<h1>my-short-video</h1>

<p>Gerador de vídeos curtos narrados</p>

</center>

<br>

# Introdução

A ferramenta aceita aúdios, legendas e vídeos, com o intuito de gerar vídeos curtos para postagens em plataformas de terceiros. No estado atual da aplicação os recursos serão consumidos localmente, porém no futuro será possível vincular com servidores remotos.

## Recursos

Dentro das pastas `/music`, `/subtitle`, `/video` devem ser populados com os recursos que você deseja utilizar nos vídeos gerados.

Os recursos são utilizados por meio do arquivo localizado na pasta `/script/main.msv`. Dentro do arquivo é necessário criar uma seção para utilizar cada tipo de recurso. Abaixo temos um exemplo da composição do arquivo `.msv`.

```
narrator
** Controles (volume, efeito, ...) **
/narrator

musics
** Definir audios e controles para eles (corte, volume, efeito, ...) **
/musics

videos
** Definir vídeos e controles para eles (corte, volume, efeito, ...) **
/videos

subtitles
** Legendas do vídeo final **
** Pode apontar um arquivo no formato .srt também **
\subtitles
```

## Execução

Dentro do arquivo `package.json` temos os seguintes scripts: `setup`, `text-to-speech`, `generate-video`, `dev`.

- **setup:** instala os pacotes necessários para a execução da aplicação.
- **text-to-speech:** executa a transformação das suas legendas em um aúdio.
- **generate-video:** executa a criação do vídeo final.
- **dev**: executa os comandos **text-to-speech** e **generate-video** em sequencia.

Exemplo:

```shell
npm run setup
npm run dev
```

## Narração

Esta seção reune algumas informações importantes para que a narração gerada tenha uma qualidade aceitável e agradável ao telespectador.

### Pronúncia

Algumas palavras podem ter uma pronúncia estranha ou errada. Portanto, é importante revisar o texto alterando as partes necessárias, se está buscando uma qualidade maior. Exemplo:

```
Olá, bem vindo ao canal Teste. Este conteúdo está sendo narrado pela ferramenta elnarrator.io
```

Pode ser alterado para:

```
Olá, bem vindo ao canal Teste. Este conteúdo está sendo narrado pela ferramenta el narraitor ponto aio
```

### Datas

A narração não lida bem com datas. Exemplo:

  ```
    16/06/2023
    16 de Junho de 2023
  ```

Para isso seria necessário fazer ajustes manuais para:

```
  Dezesseis de junho de dois mil e vinte e três
```
