import pytest

from src.config.CONSTANTS import *
from src.service.PandasDataLoader import PandasDataLoader
from tests.AssertionMessageHandler import AssertionMessageHandler


class TestPandasDataLoader:

    def setup_class(self):
        self.valid_path_constructor = PandasDataLoader(file_path="data/file", file_type=".csv")
        self.valid_type_constructor = PandasDataLoader(file_path="data/file", file_type=".csv")

    def test_constructor_throws_type_error_for_none_file_path(self):
        result = EXPECTED_TO_FAIL
        test_object = None
        try:
            test_object = PandasDataLoader(file_path=None, file_type=None)
            test_object.none_value_check(test_object.file_path)
        except TypeError:
            result = PASS
        AssertionMessageHandler("file_path throws NoneType exception", result)

    def test_constructor_throws_type_error_for_none_file_type(self):
        result = EXPECTED_TO_FAIL
        test_object = None
        try:
            test_object = PandasDataLoader(file_path=None, file_type=None)
            test_object.none_value_check(test_object.file_type)
        except TypeError:
            result = PASS
        AssertionMessageHandler("file_type throws NoneType exception", result)

    def test_constructor_throws_attribute_error_exception_for_empty_file_path(self):
        result = EXPECTED_TO_FAIL
        test_object = None
        try:
            test_object = PandasDataLoader(file_path="", file_type="csv")
            test_object.empty_value_check(test_object.file_path)
        except AttributeError:
            result = PASS
        AssertionMessageHandler("file_path throws AttributeError exception", result)

    def test_constructor_throws_attribute_error_for_empty_file_type(self):
        result = EXPECTED_TO_FAIL
        test_object = None
        try:
            test_object = PandasDataLoader(file_path="", file_type="")
            test_object.empty_value_check(test_object.file_type)
        except AttributeError:
            result = PASS
        AssertionMessageHandler("file_type throws AttributeError exception", result)

    def test_constructor_valid_file_path(self):
        result = EXPECTED_TO_PASS
        try:
            test_object = PandasDataLoader(file_path="data/file.csv", file_type="csv")
            test_object.empty_value_check(test_object.file_path)
        except AttributeError:
            result = FAIL
        AssertionMessageHandler("file_type throws AttributeError exception", result)

    def test_valid_file_type_from_path_constructor(self):
        result = EXPECTED_TO_PASS
        try:
            test_object = PandasDataLoader(file_path="data/file.csv")
            success = test_object.is_valid_file_path()
        except AttributeError:
            result = FAIL
        AssertionMessageHandler("file_path throws AttributeError exception", result)

    def test_valid_file_path(self):
        result = EXPECTED_TO_PASS
        message = "VALID file_path"
        try:
            # setup here because exception may happen
            test_object = PandasDataLoader(file_path="data/file.csv")
            success = test_object.is_valid_file_path()
        except TypeError:
            result = FAIL
            message = "TypeError with file_path"
        except AttributeError:
            result = FAIL
            message = "AttributeError with file_path"
        AssertionMessageHandler(message, result)

    def test_invalid_file_path(self):
        result = EXPECTED_TO_FAIL
        message = "INVALID file_path"
        try:
            # setup here because exception may happen
            test_object = PandasDataLoader(file_type="")
            success = test_object.is_valid_file_path()
        except TypeError:
            result = PASS
            message = "TypeError with file_path"
        except AttributeError:
            result = PASS
            message = "AttributeError with file_path"
        AssertionMessageHandler(message, result)

    def test_valid_file_types(self):
        """
        Checks valid file type
        @precondition - file should have extension
        @return: None
        """
        result = EXPECTED_TO_PASS
        test_object = PandasDataLoader(file_path="data/file.csv")
        result = test_object.valid_file_type()
        AssertionMessageHandler(f"File type check {test_object.file_path}", not result)

    def test_select_pandas_import_method_excel(self):
        result = EXPECTED_TO_PASS
        expected_value = "read_excel"
        test_object = PandasDataLoader(file_path="data/file.xlsx")
        method = test_object.select_pandas_import_engine()
        result = method == expected_value
        AssertionMessageHandler(f"Engine Check {test_object.file_type}", not result)

    def test_select_pandas_import_method_csv(self):
        result = EXPECTED_TO_PASS
        expected_value = "read_csv"
        test_object = PandasDataLoader(file_path="data/file.csv")
        method = test_object.select_pandas_import_engine()
        result = method == expected_value
        AssertionMessageHandler(f"Engine Check {test_object.file_type}", not result)

    def test_select_pandas_import_method_invalid(self):
        expected_value = ""
        test_object = PandasDataLoader(file_path="data/file.exe")
        method = test_object.select_pandas_import_engine()
        result = method == expected_value
        AssertionMessageHandler(f"Engine Check {test_object.file_type}", not result)

    def test_create_dataframe_from_file(self):
        test_object = PandasDataLoader(file_path="data/file.csv")
        test_object.data_frame = test_object.create_data_frame_from_file()

    def test_create_data_frame_csv(self):
        test_object = PandasDataLoader(file_path="data/file.csv")
        df = test_object.create_data_frame_csv()
        result = (len(df) > 0)
        AssertionMessageHandler("Create from CSV", not result)

    def test_create_dataframe_excel(self):
        test_object = PandasDataLoader(file_path="data/file.xlsx")
        df = test_object.create_data_frame_excel()
        result = (len(df) > 0)
        AssertionMessageHandler("Create from EXCEL", not result)
