import json
import collections
from unidecode import unidecode

from conf import DATASET_ORIGINAL_PATH

def load_dataset():
    with open(DATASET_ORIGINAL_PATH, encoding="utf-8") as file:
        dataset = json.load(file)
        return dataset

dataset = load_dataset()
