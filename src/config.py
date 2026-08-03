import json
from pathlib import Path


class Config:

    def __init__(self, root: Path):

        self.root = root

        self.settings = self.load_json(
            root / "config" / "settings.json"
        )

        self.mapping = self.load_json(
            root / "config" / "mapping.json"
        )

    def load_json(self, path):

        with open(path, encoding="utf8") as file:
            return json.load(file)

    @property
    def create_backup(self):
        return self.settings["create_backup"]

    @property
    def overwrite_output(self):
        return self.settings["overwrite_output"]

    @property
    def pretty_json(self):
        return self.settings["pretty_json"]

    @property
    def mapping_rules(self):
        return self.mapping
