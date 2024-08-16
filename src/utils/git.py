import subprocess
import os

from utils import ExecutableUtil


class Git(ExecutableUtil):
    """A class for interacting with Git."""

    def __init__(self):
        utils_path = os.path.dirname(os.path.abspath(__file__))
        src_path = os.path.dirname(utils_path)
        self.form_parser_path = os.path.dirname(src_path)
        self.data = []

    def execute(self, *args):
        """Сalls the method add and commit"""
        self.add(*args)
        self.commit()

    def add(self, data: str) -> None:
        """Writes data to the words.in file.

        Args:
            data (str): Данные для записи в файл.
        """

        data_path = os.path.join(self.form_parser_path, 'words.in')
        self.data = data.split()
        with open(data_path, 'a') as file:
            for word in self.data:
                file.write(word + '\n')

    def commit(self) -> None:
        """Commit and push the file to the repository using the commit.sh script."""
        script_fpath = os.path.join(self.form_parser_path, 'commit.sh')
        try:
            subprocess.run(['bash', script_fpath], input=data.encode(), check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error while executing the commit.sh script: {e}")
