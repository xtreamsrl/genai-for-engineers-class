import numpy as np
import polars as pl
import umap


def add_sentences(data: pl.DataFrame, sentences: list[str], *, encoder) -> pl.DataFrame:
    new_sentences_df = pl.DataFrame(
        {
            "sentence": sentences,
            "field": "MINE",
        }
    )

    all_sentences = pl.concat([new_sentences_df, data])

    encodings = encoder.encode(all_sentences["sentence"].to_list())

    reduced_encodings = reduce_dimensions(encodings)

    return add_umap_to_dataset(all_sentences, reduced_encodings)


def reduce_dimensions(vectors: np.array) -> np.array:
    return umap.UMAP(random_state=42, n_jobs=1).fit_transform(vectors)


def add_umap_to_dataset(data: pl.DataFrame, reduced_vectors: np.array) -> pl.DataFrame:
    return data.with_columns(
        reduced=reduced_vectors.tolist(),
        x=reduced_vectors[:, 0],
        y=reduced_vectors[:, 1],
    )
