# GLaDOS Text To Speech
![Alt text](https://upload.wikimedia.org/wikipedia/en/b/bf/Glados.png "GLaDOS")

This project employs pitch correction to text to speech comperable to GLaDOS from Portal

Use librosa < 0.6.*

To use with an existing project with tts output:

`from speak import speak`

`quote = "Despite Your Violent Behavior, The Only Thing You’ve Managed To Break So Far Is My Heart."`

`speak(quote)`


to test without out of the box:

`git clone https://github.com/robit-man/GLaDOS-TTS/`

`cd GLaDOS-TTS`

`pip3 install -r requirements`

`python3 test.py`

