import os
import uuid
from transferchain import utils
from transferchain import exceptions
from transferchain.crypt import bip39
from transferchain.datastructures import Config
from transferchain.wallet import create_wallet, get_wallet_info


def create_config():
    user_id = int(os.environ.get('TRANSFERCHAIN_USER_ID', 0))

    if not user_id:
        raise exceptions.ValidationError("config error: invalid user id")

    api_token = os.environ.get('TRANSFERCHAIN_API_TOKEN')
    api_secret = os.environ.get('TRANSFERCHAIN_API_SECRET')

    if api_token == "" or api_secret == "":
        raise exceptions.ValidationError(
            "config error: invalid api token or api secret")
    conf = Config(api_token=api_token, api_secret=api_secret,
                  db_path=os.getcwd())

    wallet_uuid = os.environ.get('TRANSFERCHAIN_WALLET_UUID')
    if not wallet_uuid:
        wallet_uuid = str(uuid.uuid4())
        result = create_wallet(conf, user_id, wallet_uuid)
        if result.success is False:
            raise exceptions.ValidationError(result.error_message)
        wallet_id = result.wallet_id
    else:
        if not utils.is_valid_uuid(wallet_uuid):
            raise exceptions.ValidationError('invalid wallet uuid')
        wallet_info = get_wallet_info(conf, wallet_uuid)
        wallet_id = wallet_info['wallet_id']

    mnemonics = os.environ.get('TRANSFERCHAIN_MNEMONICS', '')
    if not mnemonics or len(mnemonics.split('')) != 24:
        mnemonics = bip39.create_mnomonics()

    return conf._replace(
        user_id=user_id,
        wallet_uuid=wallet_uuid,
        wallet_id=wallet_id,
        mnemonics=mnemonics)
