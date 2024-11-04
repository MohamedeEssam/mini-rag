from helpers.config import get_settings, Settings

class BaseDataModel:

    def __init__(self, db_client: object):
        self.db_client = db_client
        self.pp_settings = get_settings()