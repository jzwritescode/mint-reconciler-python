import pytest

from src.config.CONSTANTS import *
from src.service.PandasDataLoader import PandasDataLoader
from tests.AssertionMessageHandler import AssertionMessageHandler


class TestPandasDataLoader:

    def setup_class(self):
        self.valid_path_constructor = PandasDataLoader(file_path="/path/to/file.csv", file_type="csv")
        self.valid_type_constructor = PandasDataLoader(file_path="/path/to/file.csv", file_type="csv")

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
            test_object = PandasDataLoader(file_path="/path/to/file.csv", file_type="")
            test_object.empty_value_check(test_object.file_type)
        except AttributeError:
            result = PASS
        AssertionMessageHandler("file_type throws AttributeError exception", result)

    def test_constructor_valid_file_path(self):
        result = EXPECTED_TO_PASS
        try:
            test_object = PandasDataLoader(file_path="/path/to/file.csv", file_type="csv")
            test_object.empty_value_check(test_object.file_path)
        except AttributeError:
            result = FAIL
        AssertionMessageHandler("file_type throws AttributeError exception", result)

    def test_valid_file_type_from_path_constructor(self):
        result = EXPECTED_TO_PASS
        try:
            test_object = PandasDataLoader(file_path="/path/to/file.csv")
            success = test_object.is_valid_file_path()
        except AttributeError:
            result = FAIL
        AssertionMessageHandler("file_path throws AttributeError exception", result)

    def test_valid_file_path(self):
        result = EXPECTED_TO_PASS
        message = "VALID file_path"
        try:
            # setup here because exception may happen
            test_object = PandasDataLoader(file_path="/path/to/file.csv")
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
        # filename, file_extension = os.path.splitext('/path/to/somefile.ext')
        # expected_pass = self.check_file_type()
        AssertionMessageHandler(TEST_NOT_IMPLEMENTED, FAIL)

    def test_create_dataframe_from_file(self):
        AssertionMessageHandler(TEST_NOT_IMPLEMENTED, FAIL)
