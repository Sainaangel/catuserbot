from sample_config import Config


class Development(Config):
    # get this values from the my.telegram.org
    APP_ID = 6296490
    API_HASH = "24385183c93a98ae4155c25d9f5f64b2"
    # the name to display in your alive message
    ALIVE_NAME = "⏤͟͞ ＦＬムＳＨ三[🇮🇳]e"
    # create any PostgreSQL database (i recommend to use elephantsql) and paste that link here
    DB_URI = "mongodb+srv://pankajsain:pankaj9024@cluster0.fdc33h6.mongodb.net/?retryWrites=true&w=majority"
    # After cloning the repo and installing requirements do python3 stringsetup.py an fill that value with this
    STRING_SESSION = "1BJWap1sBu1WDNirSFt2zhK2dhSC6-p2lYSd_wM4uv1vwgUWEliHrqbLBOdMKI0dEm0ZfuXOFFtCB9R1kQSrZSn1aqNiqG-3pD-vljRbJJ8HSYTIHoA-JP0FLJkBZMrmj4juRid2VUG6yaR7m7P_dxcMgCtzghZgeb_AWS8SleFnXFj-73P8Hnv0a2BfaBd9DsfyzaeXvG-QzQNhZGgl_Aceq3v_9sWhBegg10XmdLtmOwy3Wo4OgaCONDeZExE26Vxi40QlZEm0bFGK_3rbSAmogrNl_Sr8qPQA376HNV4sbL62u2wXBPSpRYL-w4E5W55Oi3IiNYk0JKxJHs62z_ZpHfiS_6QI="
    # create a new bot in @botfather and fill the following vales with bottoken
    TG_BOT_TOKEN = "6080251945:AAFPZ-5EA-GpbWG1KuPd0ET2J_ehDzQ1PUs"
    # create a private group and a rose bot to it and type /id and paste that id here (replace that -100 with that group id)
    PRIVATE_GROUP_BOT_API_ID = -1001647004968
    # command handler
    COMMAND_HAND_LER = "!"
    # command hanler for sudo
    SUDO_COMMAND_HAND_LER = "."
    # External plugins repo
    EXTERNAL_REPO = "https://github.com/TgCatUB/CatPlugins"
    # if you need badcat plugins set "True"
    BADCAT = "true"
