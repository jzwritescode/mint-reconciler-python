import pandas as pd


class FinancialRecord(object):
    """
    Hold record from a given institution
    """
    _key = ""
    _file = ""
    _records = pd.DataFrame()
    _headers = ""

    def __init__(self, key: str, file: str, records: pd.DataFrame):
        """
        Constructor
        @param key: Institution Key
        @param file: file being imported
        @param records: list of records
        """
        _key = key
        _file = file
        _records = records
