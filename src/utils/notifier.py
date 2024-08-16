from utils import ExecutableUtil


class Notifier(ExecutableUtil):
    """
    DOCUMENTME
    """
    def __init__(self):
        pass
        # self.server = cfg
        
    def execute(self, *args):
        """
        DOCUMENTME
        """
        self.notify(*args)
        
    def notify(self, mail, lst):
        """
        DOCUMENTME
        """
        # TODO: ImplementMe
        print(f"Send a message:{lst} at email:{mail}")
