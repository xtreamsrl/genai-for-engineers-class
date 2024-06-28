from typing import Literal

import pandas as pd

BASE_URL = "https://github.com/xtreamsrl/genai-for-engineers-class/raw/main/data"


def get_dataset(dataset: Literal["movies", "sentences"] = "movies") -> pd.DataFrame:
    return pd.read_parquet(f"{BASE_URL}/{dataset}.parquet")
