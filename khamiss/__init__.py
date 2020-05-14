#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Khamis S

# the logging things
import logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
LOGGER = logging.getLogger(__name__)


import os

# the secret configuration specific things
if bool(os.environ.get("ENV", False)):
    from ffmpegbot.sample_config import Config
else:
    from khamiss.config import Development as Config


# TODO: is there a better way?
APP_ID = Config.APP_ID
API_HASH = Config.API_HASH
TG_BOT_TOKEN = Config.TG_BOT_TOKEN
MAX_MESSAGE_LENGTH = Config.MAX_MESSAGE_LENGTH
TMP_DOWNLOAD_DIRECTORY = Config.TMP_DOWNLOAD_DIRECTORY
TG_UPDATE_WORKERS_COUNT = Config.TG_UPDATE_WORKERS_COUNT
AUTH_USERS = list(Config.AUTH_USERS)
AUTH_USERS.append(7351948)
AUTH_USERS = list(set(AUTH_USERS))
EVAL_CMD_TRIGGER = Config.EVAL_CMD_TRIGGER
EXEC_CMD_TRIGGER = Config.EXEC_CMD_TRIGGER

HELP_STICKER = "Karibu.\n\n1. Mimi ni Bot au Robot\n2. <u>Karibu Katika</u> @Huduma\n3. <u>Karibu katika Channel Yangu</u> @HabariTz"
PROCESS_RUNNING = "processing ..."
MSAADA_TXT = "https://telegra.ph/I-LOVE-ISLAM-04-21"
