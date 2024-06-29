from typing import Literal

import pandas as pd
from haystack import Document

BASE_URL = "https://github.com/xtreamsrl/genai-for-engineers-class/raw/main/data"


def get_dataset(dataset: Literal["movies", "sentences"] = "movies") -> pd.DataFrame:
    return pd.read_parquet(f"{BASE_URL}/{dataset}.parquet")


def get_movie_dataset_as_documents(sample: int | None = 1000) -> list[Document]:
    movie_df = get_dataset("movies")
    if sample is not None:
        movie_df = movie_df.sample(sample, random_state=42)
    documents = [
        Document(
            id=movie["id"],
            content=f'title: {movie["title"]} \noverview: {movie["overview"]}',
            meta={
                "title": movie["title"],
                "release_date": movie["release_date"],
            },
        )
        for movie in movie_df.to_dict(orient="records")
    ]
    return documents
