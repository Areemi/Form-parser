import json
import os


class Settings:
    """Class to load and manage configuration settings."""
    
    def __init__(self, file):
        """Initialize with the path to the configuration file."""
        src_path = os.path.dirname(os.path.abspath(__file__)) # Путь к папке с файлом
        form_parser_path = os.path.dirname(src_path)
        data_dpath = os.path.join(form_parser_path, file)

        """if not os.path.exists(folder_path):  # Если пути не существует создаем его
            os.makedirs(folder_path)

        with open(directory_folder, 'w') as file:  # Открываем фаил и пишем
            file.write("этот текст создан автоматически")"""
        self.cfg = self.load_config(data_dpath)

    def load_config(self, cfg):
        """Load configuration from a JSON file."""
        with open(cfg, 'r') as f:
            return json.load(f)
