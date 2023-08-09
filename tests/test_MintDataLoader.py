from src.commands.MintDataLoader import MintDataLoader
from src.config.CONSTANTS import EXPECTED_TO_PASS, FAIL, PASS
from tests.AssertionMessageHandler import AssertionMessageHandler


class TestMintDataLoader:
    def setup_class(self):
        self.csv_file = "data/file.csv"
        self.excel_file = "data/file.xlsx"
        self.invalid_file_ext = "data/file.exe"
        # going linux style here
        self.invalid_file_no_ext = "data/file"

    def test_run_csv_pass(self):
        message = "test_run_csv_pass"
        result = EXPECTED_TO_PASS
        try:
            test_object = MintDataLoader(self.csv_file)
            test_object.run()
        except FileNotFoundError:
            result = FAIL
            message = f"{message} - FileNotFoundError"
        except ValueError:
            result = FAIL
            message = f"{message} - ValueError"
        except AttributeError:
            result = FAIL
            message = f"{message} - AttributeError"
        AssertionMessageHandler(message, result)

    def test_run_excel_pass(self):
        message = "test_run_excel_pass"
        result = EXPECTED_TO_PASS
        try:
            test_object = MintDataLoader(self.csv_file)
            test_object.run()
            message = f"{message} - No Issue"
            result = PASS
        except FileNotFoundError:
            result = FAIL
            message = f"{message} - FileNotFoundError"
        except ValueError:
            result = FAIL
            message = f"{message} - ValueError"
        except AttributeError:
            result = FAIL
            message = f"{message} - AttributeError"
        AssertionMessageHandler(message, result)

    def test_run_fail_file_ext(self):
        message = "test_run_fail_file_ext"
        result = EXPECTED_TO_PASS
        try:
            test_object = MintDataLoader(self.invalid_file_ext)
            test_object.run()
            message = f"{message} - No Issue"
            result = FAIL
        except FileNotFoundError:
            result = PASS
            message = f"{message} - FileNotFoundError"
        except ValueError:
            result = PASS
            message = f"{message} - ValueError"
        except AttributeError:
            result = PASS
            message = f"{message} - AttributeError"
        AssertionMessageHandler(message, result)

    def test_run_fail_file_no_ext(self):
        message = "test_run_fail_file_no_ext"
        result = EXPECTED_TO_PASS
        try:
            test_object = MintDataLoader(self.invalid_file_no_ext)
            test_object.run()
            message = f"{message} - No Issue"
            result = FAIL
        except FileNotFoundError:
            result = PASS
            message = f"{message} - FileNotFoundError"
        except ValueError:
            result = PASS
            message = f"{message} - ValueError"
        except AttributeError:
            result = PASS
            message = f"{message} - AttributeError"
        AssertionMessageHandler(message, result)
