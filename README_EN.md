# Discord EEW Bot

![PEP8 Test](https://github.com/Hipro-Official/Discord-Weather-Bot/workflows/PEP8%20Test/badge.svg)
![license](https://img.shields.io/badge/license-GPL--3.0-green)
![version](https://img.shields.io/badge/version-1.0.0-blue)
<br>

![image](./picture/EEW.png)

日本語をご所望の場合, [README.md](./README.md)をご参照ください。

This is the inventory page of the Discord EEW Bot. This Discord EEW Bot only notifies you of the earthquake early warning in Japan. <br>

## Specification

Discord EEW Bot uses Heroku. The configuration is as follows.
![image](picture/Component.png)

### Features
The Discord EEW Bot has the following features.
1. In the event of an earthquake with an intensity of 5 or more on the Richter scale, it will be delivered via Embed.

### Usage (code)
Config/config.py contains the URL of the API and the names of the environment variables that you have registered with Heroku. <br>
If the URL of the API has changed, please edit this file if you want to use a different environment variable name. <br>
Please refer to [here](https://devcenter.heroku.com/articles/config-vars#using-the-heroku-dashboard) for information on how to register Heroku environment variables. <br>.

### API
|#|API name|URL|
|:-:|:-|:-|
|1|緊急地震速報 JSON API (Ver.Beta)|https://api.iedred7584.com/eew/|

When using the APIs, please comply with the restrictions of each API provider.<br>

### Note
You are free to modify the code, but if you modify all or part of the code in this Bot, please insert the following information as your license.
```
Code provided by Hipro
https://github.com/Hipro-Official
```

Hipro cannot be held responsible for any changes to the code in the files except for [config.py](Config/config.py)in this bot.<br>
If you have any problems, please issue a voucher in Issue.

### License
GNU GENERAL PUBLIC LICENSE v3.0