from argparse import ArgumentParser
import os


class Parser(ArgumentParser):
    def __init__(self):
        super(Parser,self).__init__()

    # register and parse command line arguments
    def get_args(self):
        self.add_argument("file_path", type=self._valid_file_path, help="path of graph file")
        self.add_argument("start_node", type=str, help="source node to of the graph route")
        self.add_argument("end_node", type=str, help="destination node of the graph route")
        return self.parse_args()

    @staticmethod
    def _valid_file_path(path):
        """
        check if the file path is valid if path provided is a valid
        param value: location on filesystem
        return: absolute location on filesystem
        """
        abs_path = os.path.abspath(path)
        if not os.path.exists(abs_path):
            raise OSError
        return abs_path