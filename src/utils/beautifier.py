from utils import ExecutableUtil


class Beautifier(ExecutableUtil):
    """Class for string processing that removes extra spaces and dots."""

    def execute(self, *args):
        """Сalls the method beautify"""
        self.beautify(*args)

    def beautify(word: str) -> str:
        """Removes extra spaces and dots at the beginning and end of a word.

        Args:
            word (str): Original word.

        Returns:
            str: Processed word without extra spaces or dots.
        """
        return word.strip('. ')
