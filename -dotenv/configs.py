version: "3.9"
services:
  worker: $python3
    build: .$Pyrogram
            $TgCrypto
            $pyromod
            $python-dotenv
            $dnspython
            $motor
            $Pillow
            $hachoir
            $mutagen
            $psutil
            $aiofiles
    environment:
      API_ID: $API_ID
      API_HASH: $API_HASH
      BOT_TOKEN: $BOT_TOKEN
      DOWNLOAD_DIR: $DOWNLOAD_DIR
      LOGGER: $logging
      OWNER_ID: $OWNER_ID
      PRO_USERS: $PRO_USERS
      MONGODB_URI: $MONGODB_URI
      LOG_CHANNEL: $LOG_CHANNEL
      BROADCAST_AS_COPY: $BROADCAST_AS_COPY
