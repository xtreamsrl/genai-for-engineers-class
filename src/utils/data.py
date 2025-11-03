from typing import Literal

import polars as pl
import requests
from PIL import Image
from haystack import Document


def _get_data_base_url() -> str:
    return "https://github.com/xtreamsrl/genai-for-engineers-class/raw/feat/update-notebooks/data"


def get_image_dataset() -> list[Image.Image]:
    n_pictures = 3
    categories = ["cat", "car"]
    image_names = [
        f"{category}{i + 1}.jpeg" for category in categories for i in range(n_pictures)
    ]
    urls = [f"{_get_data_base_url()}/images/{image_name}" for image_name in image_names]
    images = [Image.open(requests.get(url, stream=True).raw) for url in urls]
    return images


def get_dataset(dataset: Literal["movies", "sentences"] = "movies") -> pl.DataFrame:
    url = f"{_get_data_base_url()}/{dataset}.parquet"
    return pl.read_parquet(url)


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
