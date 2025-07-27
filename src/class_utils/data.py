from typing import Literal

import polars as pl
from haystack import Document


def get_dataset(dataset: Literal["movies", "sentences"] = "movies") -> pl.DataFrame:
    base_url = "https://github.com/xtreamsrl/genai-for-engineers-class/raw/main/data"
    return pl.read_parquet(f"{base_url}/{dataset}.parquet")


def get_movie_dataset_as_documents(sample: int | None = 1000) -> list[Document]:
    movie_df = get_dataset("movies")
    if sample is not None:
        movie_df = movie_df.sample(sample, seed=42)
    documents = [
        Document(
            id=movie["id"],
            content=f"title: {movie['title']} \noverview: {movie['overview']}",
            meta={
                "title": movie["title"],
                "release_date": movie["release_date"],
            },
        )
        for movie in movie_df.to_dicts()
    ]
    return documents
