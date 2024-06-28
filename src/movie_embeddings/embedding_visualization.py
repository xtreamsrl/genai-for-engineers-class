import pandas as pd
import plotly
import plotly.express as px


def plot_movies(data: pd.DataFrame) -> plotly.graph_objs.Figure:
    fig = (
        px.scatter(
            data,
            x="x",
            y="y",
            color="genre",
            height=512,
            hover_name="genre",
            hover_data={
                "overview": False,
                "title": True,
                "x": False,
                "y": False,
            },
        )
        .update_layout(
            title_text="Which genres are close together?",
            template="plotly_white",
        )
        .update_traces(textposition="top center", marker=dict(size=5))
    )

    return fig


def plot_sentences(sentences: pd.DataFrame) -> plotly.graph_objs.Figure:
    sentences["short_sentence"] = sentences["sentence"].str.slice(0, 20) + "..."

    fig = (
        px.scatter(
            sentences,
            x="x",
            y="y",
            text="short_sentence",
            color="field",
            height=512,
            hover_name="field",
            hover_data={
                "sentence": True,
                "x": False,
                "y": False,
                "field": False,
                "short_sentence": False,
            },
        )
        .update_layout(
            title_text="Which vectors are close together?",
            template="plotly_white",
        )
        .update_traces(textposition="top center", marker=dict(size=15))
    )

    return fig
