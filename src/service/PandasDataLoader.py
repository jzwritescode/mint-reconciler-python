import os

import pandas as pd
from varname import nameof

from src.config.CONSTANTS import VALID_FILE_TYPES, VALID_READER_ENGINE


class PandasDataLoader:
    def __init__(self, file_path: str = "", *, file_type: str = ""):
        """
        Constructor
        @param file_path: path to file, including file name
        @param file_type: file extension.
        """

        self.data_frame = None

        # attempt to parse out file
        # TODO:  Do I need to take into account file_path == "" and file_type != ""
        if file_path != "" and file_type == "":
            self.file_path, self.file_type = os.path.splitext(file_path)
        else:
            self.file_path = file_path
            self.file_type = file_type

    def create_data_frame_from_file(self):
        """
        Creates dataframe based on file type.
        @return: Nothing
        """
        # run initial file check
        if not self.is_valid_file_path():
            raise FileNotFoundError("Valid File Check: Invalid file name.")

        if self.is_valid_file_type():
            match self.select_pandas_import_engine():
                case "read_csv":
                    self.data_frame = self.create_data_frame_csv()
                case "read_excel":
                    self.data_frame = self.create_data_frame_excel()
                case _:
                    raise FileNotFoundError("Import Engine Process: Invalid file name")
        else:
            raise ValueError("Invalid file type.")

    def none_value_check(self, variable):
        """
        Checks if None is set for a given variable
        @param variable: Variable to be checked
        @return: Nothing.  Exception gets thrown if there's an issue
        """
        variable_name = nameof(variable)
        if variable is None:
            raise TypeError(f"Variable: {variable_name} is {variable}")

    def empty_value_check(self, variable):
        """
        Checks if a variable is an empty string.
        @param variable: Variable to be checked
        @return: Nothing.  Exception gets thrown if there's an issue
        """
        variable_name = nameof(variable)
        if variable == "":
            raise AttributeError(f"Variable: {variable_name} is {variable}")

    def is_valid_file_type(self) -> bool:
        """
        Checks if file type is valid.

        @return: True if valid...This is the only value
        that gets returned because an exception will be
        raised for a "False" condition.
        """
        success = True
        variable = self.file_type
        self.none_value_check(variable)
        self.empty_value_check(variable)
        # should be True
        return success

    def is_valid_file_path(self):
        """
        Checks if file path is valid.

        @return: True if valid...This is the only value
        that gets returned because an exception will be
        raised for a "False" condition.
        """
        success = True
        variable = self.file_path
        self.none_value_check(variable)
        self.empty_value_check(variable)
        # should be True
        return success

    def valid_file_type(self) -> bool:
        """
        Checks to see if extension is in the list.

        @return: True if valid; False otherwise
        """
        return self.file_type in VALID_FILE_TYPES

    def select_pandas_import_engine(self) -> str:
        """
        Determines which import engine (read_csv, read_excel)
        will be used
        @return: String with engine type. Blank if nothing found.
        """
        for key, value in VALID_READER_ENGINE.items():
            if self.file_type in value:
                return key
        
        # default:  return empty string
        return ""

    def create_data_frame_excel(self) -> pd.DataFrame:
        """
        Create dataframe from Excel file.
        @precondition:  All checks for valid file name/type passed.
        @return: Creates dataframe
        """
        return pd.read_excel(f"{self.file_path}{self.file_type}")

    def create_data_frame_csv(self) -> pd.DataFrame:
        """
        Create dataframe from CSV file.
        @precondition:  All checks for valid file name/type passed.
        @return: Creates dataframe
        """
        return pd.read_csv(f"{self.file_path}{self.file_type}")
