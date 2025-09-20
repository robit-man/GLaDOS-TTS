# GLaDOS Text To Speech

## [Click here for a rapid deployment of a fine tuned ONNX model and piper implementation!](https://github.com/robit-man/piper-tts-service)
![Alt text](https://upload.wikimedia.org/wikipedia/en/b/bf/Glados.png "GLaDOS")

This project employs pitch correction over text to speech comperable to GLaDOS from Portal

To use with an existing project with tts output:

`from speak import speak`

`quote = "Despite Your Violent Behavior, The Only Thing You’ve Managed To Break So Far Is My Heart."`

`speak(quote)`


to test out of the box:

clone project
`git clone https://github.com/robit-man/GLaDOS-TTS/`

enter directory
`cd GLaDOS-TTS`

install requirements
`pip3 install -r requirements`

run test script
`python3 test.py`

