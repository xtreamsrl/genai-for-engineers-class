import numpy as np
import pandas as pd
import umap


def add_sentences(data: pd.DataFrame, sentences: list[str], *, encoder) -> pd.DataFrame:
    new_sentences = pd.DataFrame(
        {
            "sentence": sentences,
            "field": "MINE",
        }
    )

    all_sentences = pd.concat([data, new_sentences], ignore_index=True).reset_index(
        drop=True
    )

    encodings = encoder.encode(all_sentences["sentence"])

    reduced_encodings = reduce_dimensions(encodings)

    return add_umap_to_dataset(all_sentences, reduced_encodings)


def reduce_dimensions(vectors: np.array) -> np.array:
    return umap.UMAP().fit_transform(vectors)


def add_umap_to_dataset(data: pd.DataFrame, reduced_vectors: np.array) -> pd.DataFrame:
    return data.assign(
        reduced=reduced_vectors.tolist(),
        x=reduced_vectors[:, 0],
        y=reduced_vectors[:, 1],
    )
