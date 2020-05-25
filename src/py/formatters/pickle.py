import pickle
import json

from .base import BaseFormatter


class PickleFormatter(BaseFormatter):

    read_only = False

    decode_format = "json"

    def decode(self, value):
        self.read_only = self.__class__.read_only
        return json.dumps(pickle.loads(value), ensure_ascii=False)

    def encode(self, value):
        return pickle.dumps(json.loads(value))
