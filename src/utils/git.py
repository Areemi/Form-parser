import subprocess
import os

from utils import ExecutableUtil


class Git(ExecutableUtil):
    """Класс для взаимодействия с Git."""

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
        """Записывает данные в файл words.in.

        Args:
            data (str): Данные для записи в файл.
        """

        data_path = os.path.join(self.form_parser_path, 'words.in')
        self.data = data.split()
        with open(data_path, 'a') as file:
            for word in self.data:
                file.write(word + '\n')

    def commit(self) -> None:
        """Коммитит и пушит файл в репозиторий, используя скрипт commit.sh."""
        script_fpath = os.path.join(self.form_parser_path, 'commit.sh')
        try:
            subprocess.run(['bash', script_fpath], input=data.encode(), check=True)
        except subprocess.CalledProcessError as e:
            print(f"Ошибка при выполнении скрипта commit.sh: {e}")
