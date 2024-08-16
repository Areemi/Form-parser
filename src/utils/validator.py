from utils import ExecutableUtil
import re


class Validator(ExecutableUtil):
    """
    DOCUMENTME
    """
    def execute(self, *args):
        """
        DOCUMENTME
        """
        self.validate(*args)
    
    def validate(self, word):
        """
        DOCUMENTME
        """
        if len(word) <= 3:
            return False
        if not re.match(r'^[a-zA-Z0-9.]+$', word):
            return False
        if '..' in word:
            return False
        return True
