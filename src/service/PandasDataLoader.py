import os

import pandas as pd
from varname import nameof

from src.config.CONSTANTS import VALID_FILE_TYPES, VALID_READER_ENGINE

class PandasDataLoader:
    def __init__(self, file_path: str = "", *, file_type: str = ""):

        self.data_frame = None

        # attempt to parse out file
        # TODO:  Do I need to take into account file_path == "" and file_type != ""
        if file_path != "" and file_type == "":
            self.file_path, self.file_type = os.path.splitext(file_path)
        else:
            self.file_path = file_path
            self.file_type = file_type

    def create_data_frame_from_file(self):
        match self.select_pandas_import_engine():
            case "read_csv":
                self.data_frame = self.create_data_frame_csv()
            case "read_excel":
                self.data_frame = self.create_data_frame_excel()
            case _:
                raise FileNotFoundError("Invalid file name")

    def none_value_check(self, variable):
        variable_name = nameof(variable)
        if variable is None:
            raise TypeError(f"Variable: {variable_name} is {variable}")

    def empty_value_check(self, variable):
        variable_name = nameof(variable)
        if variable == "":
            raise AttributeError(f"Variable: {variable_name} is {variable}")

    def is_valid_file_type(self) -> bool:
        success = True
        variable = self.file_type
        self.none_value_check(variable)
        self.empty_value_check(variable)
        # should be True
        return success

    def is_valid_file_path(self):
        success = True
        variable = self.file_path
        self.none_value_check(variable)
        self.empty_value_check(variable)
        # should be True
        return success

    def valid_file_type(self) -> bool:
        """
        Checks to see if extension is in the list
        @return: True if valid; False otherwise
        """
        return self.file_type in VALID_FILE_TYPES

    def select_pandas_import_engine(self):
        for key, value in VALID_READER_ENGINE.items():
            if self.file_type in value:
                return key
        
        # default:  return empty string
        return ""

    def create_data_frame_excel(self):
        return pd.read_excel(f"{self.file_path}{self.file_type}")

    def create_data_frame_csv(self):
        return pd.read_csv(f"{self.file_path}{self.file_type}")
