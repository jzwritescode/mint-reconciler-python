import os

import pandas as pd
from varname import nameof


def non_value_check(file_path):
    pass


class PandasDataLoader:
    def __init__(self, file_path: str = "", *, file_type: str = ""):
        self.file_path = file_path
        self.file_type = file_type

        # attempt to parse out file
        if file_type != "":
            self.file_path, self.file_type = os.path.splitext(file_path)

    def create_dataframe_from_file(self) -> pd.DataFrame:
        pass

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
