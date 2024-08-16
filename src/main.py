from settings import Settings
from conveyor import Conveyor
from utils.parser import Parser
from utils.validator import Validator
from utils.notifier import Notifier


def main():
    settings = Settings('config.json')
    conveyor = Conveyor()
    parser = Parser()
    validator = Validator()
    notifier = Notifier()

    email = settings.cfg.get("email")
    words = parser.parse(settings.cfg.get("words"))

    valid_words = [validator.validate(word) for word in words]

    if valid_words:
        conveyor.add_task(lambda: notifier.notify(email, valid_words))

    conveyor.run()


if __name__ == "__main__":
    main()
