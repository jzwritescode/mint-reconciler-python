from src.commands.InterfaceCommand import InterfaceCommand
from src.service.PandasDataLoader import PandasDataLoader


class MintDataLoader(InterfaceCommand):

    def __init__(self, file_path: str = "", data_context: object = None):
        self.pandas_data_loader = PandasDataLoader(file_path)
        self.data_frame = data_context

    def run(self):
        """ Loads data from CSV file to dataframe
        @precondition:  File must be in mint.com CSV format
        @return: None
        """
        self.pandas_data_loader.create_data_frame_from_file()
