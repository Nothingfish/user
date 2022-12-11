# Ultroid - UserBot
# Copyright (C) 2021-2022 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://github.com/TeamUltroid/pyUltroid/blob/main/LICENSE>.

import sys

from decouple import config

try:
    from dotenv import load_dotenv

    load_dotenv()
except ImportError:
    pass


class Var:
    # mandatory
    API_ID = (
        int(sys.argv[1]) if len(sys.argv) > 1 else config("API_ID", default="27058815", cast=int)
    )
    API_HASH = (
        sys.argv[2]
        if len(sys.argv) > 2
        else config("API_HASH", default="0131f87eff02322fa0ba8156d09cd6b8")
    )
    SESSION = sys.argv[3] if len(sys.argv) > 3 else config("SESSION", default="AQAz9scFAjSqjjC8ZPxe3hgazE8oYSVMp-lpP2_AZm7XkA1K7pLxbxIywlvAU0Tp_6-4NXKpcCBXFeYrcO38wf4ImIxFYilN1IOyp8PCxnGM-C3ZwyBhFDNQeHzCbYB5axgEP5mvpPvWQzZ9FIGjUNMwt5pqbUXAjQZmrRKpvHpuh2DHOzPS8JlWJNgXNnWTLF79BJS-oVCxd3R-XLGv0qDUGzsrsajakBxxJiF_3VAv_dolu-wcjQuhvlJr3z0dQKfdhF9GIWECHwfn1w-Q0JvVWYAtfkmo5uuvzc_YHsS3fHakBr_1QcXbaahRdjabj9LmRbfhvidOUsWM_WQEdADZAAAAAVt12bQA")
    REDIS_URI = (
        sys.argv[4]
        if len(sys.argv) > 4
        else (config("REDIS_URI", default="redis-18694.c277.us-east-1-3.ec2.cloud.redislabs.com:18694") or config("REDIS_URL", default="redis-18694.c277.us-east-1-3.ec2.cloud.redislabs.com:18694"))
    )
    REDIS_PASSWORD = (
        sys.argv[5] if len(sys.argv) > 5 else config("REDIS_PASSWORD", default="ZwzjvSFdB2DIFaC6UVZEC34HwSxqBCRi")
    )
    # extras
    BOT_TOKEN = config("BOT_TOKEN", default="5876892826:AAFwb5z60vKkYgZq_6Vdfynlf9WjVF8pwAU")
    LOG_CHANNEL = config("LOG_CHANNEL", default="-1001873447324", cast=int)
    HEROKU_APP_NAME = config("HEROKU_APP_NAME", default=None)
    HEROKU_API = config("HEROKU_API", default=None)
    VC_SESSION = config("VC_SESSION", default=None)
    ADDONS = config("ADDONS", default=False, cast=bool)
    VCBOT = config("VCBOT", default=False, cast=bool)
    # for railway
    REDISPASSWORD = config("REDISPASSWORD", default="ZwzjvSFdB2DIFaC6UVZEC34HwSxqBCRi")
    REDISHOST = config("REDISHOST", default=None)
    REDISPORT = config("REDISPORT", default=None)
    REDISUSER = config("REDISUSER", default=None)
    # for sql
    DATABASE_URL = config("DATABASE_URL", default="postgres://ftmhhlpp:vXFSn6lNyTwI_OOTbGSBbdsQI9hABC1f@ella.db.elephantsql.com/ftmhhlpp")
    # for MONGODB users
    MONGO_URI = config("MONGO_URI", default="mongodb+srv://Mukesh01:chuprah@cluster0.dz9iv.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
