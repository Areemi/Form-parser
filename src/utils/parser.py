from utils import ExecutableUtil


class Parser(ExecutableUtil):
    """
    DOCUMENTME
    """
    def execute(self, *args):
        """
        DOCUMENTME
        """
        self.parse(*args)

    @staticmethod
    def parse(data):
        """
        DOCUMENTME
        """
        return data.split()
