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
        int(sys.argv[1]) if len(sys.argv) > 1 else config("API_ID", default=16401923, cast=int)
    )
    API_HASH = (
        sys.argv[2]
        if len(sys.argv) > 2
        else config("API_HASH", default=3faea4a96156fd1768b180d0aeacf099)
    )
    SESSION = sys.argv[3] if len(sys.argv) > 3 else config("SESSION", default=AQF1e-YAfF6Wo3VmyyPK8uDHFGn8XZ0kif19NHbwvwrepTLESUgqQExcY6LU3csCsAi30MR3oNuEBh4ms3XVqs-9QjSgsIxAV2WCQuriMG74ggqpZ8Vz5dm13jYylaPFg9n8xSVRPgi2B4S5bMyy2iNG9xIvHOr-MZvKZ1b9SHQBOpeWXxEo2z-vdGosV5lEc2IIczogPE9G9NTCfN6cim1I7DLeY3vzialuI431O-9EiH5cLf9s4aAkgn4d6YR13GHrbNh9Igr9-Ruzx3TI6nrx51LPysIk9oqdRLtUnsERcfV6YQkMDwO7RY7gbJDdNy0_FQBAzxHhoA1oBsEP1_Ovk4jJ0gAAAAFeutgvAA)
    REDIS_URI = (
        sys.argv[4]
        if len(sys.argv) > 4
        else (config("REDIS_URI", default=redis-18694.c277.us-east-1-3.ec2.cloud.redislabs.com:18694) or config("REDIS_URL", default=redis-18694.c277.us-east-1-3.ec2.cloud.redislabs.com:18694))
    )
    REDIS_PASSWORD = (
        sys.argv[5] if len(sys.argv) > 5 else config("REDIS_PASSWORD", default=ZwzjvSFdB2DIFaC6UVZEC34HwSxqBCRi)
    )
    # extras
    BOT_TOKEN = config("BOT_TOKEN", default=None)
    LOG_CHANNEL = config("LOG_CHANNEL", default=0, cast=int)
    HEROKU_APP_NAME = config("HEROKU_APP_NAME", default=None)
    HEROKU_API = config("HEROKU_API", default=None)
    VC_SESSION = config("VC_SESSION", default=None)
    ADDONS = config("ADDONS", default=False, cast=bool)
    VCBOT = config("VCBOT", default=False, cast=bool)
    # for railway
    REDISPASSWORD = config("REDISPASSWORD", default=None)
    REDISHOST = config("REDISHOST", default=None)
    REDISPORT = config("REDISPORT", default=None)
    REDISUSER = config("REDISUSER", default=None)
    # for sql
    DATABASE_URL = config("DATABASE_URL", default=None)
    # for MONGODB users
    MONGO_URI = config("MONGO_URI", default=None)
