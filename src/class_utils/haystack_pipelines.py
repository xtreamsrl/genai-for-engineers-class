from haystack import Pipeline
from haystack.components.builders import PromptBuilder
from haystack.components.embedders import (
    SentenceTransformersDocumentEmbedder,
    SentenceTransformersTextEmbedder,
)
from haystack.components.generators import OpenAIGenerator
from haystack.components.retrievers import InMemoryEmbeddingRetriever
from haystack.components.writers import DocumentWriter
from haystack.document_stores.types import DocumentStore
from haystack_integrations.components.retrievers.qdrant import QdrantEmbeddingRetriever


def build_indexing_pipline(
    document_store: DocumentStore,
    embedding_model: str = "sentence-transformers/all-MiniLM-L6-v2",
) -> Pipeline:
    pipe = Pipeline()
    pipe.add_component(
        instance=SentenceTransformersDocumentEmbedder(model=embedding_model),
        name="doc_embedder",
    )
    pipe.add_component(
        instance=DocumentWriter(document_store=document_store), name="doc_writer"
    )
    pipe.connect("doc_embedder.documents", "doc_writer.documents")
    return pipe


def build_openai_rag_pipeline(
    retriever: InMemoryEmbeddingRetriever | QdrantEmbeddingRetriever,
    prompt_template: str,
    embedding_model: str = "sentence-transformers/all-MiniLM-L6-v2",
    openai_model: str = "gpt-3.5-turbo",
) -> Pipeline:
    pipe = build_prompt_building_pipeline(retriever, prompt_template, embedding_model)
    pipe.add_component("llm", OpenAIGenerator(model=openai_model))
    pipe.connect("prompt_builder", "llm")
    return pipe


def build_prompt_building_pipeline(
    retriever: InMemoryEmbeddingRetriever | QdrantEmbeddingRetriever,
    prompt_template: str,
    embedding_model: str = "sentence-transformers/all-MiniLM-L6-v2",
) -> Pipeline:
    pipe = Pipeline()
    pipe.add_component(
        "embedder", SentenceTransformersTextEmbedder(model=embedding_model)
    )
    pipe.add_component("retriever", retriever)
    pipe.add_component(
        "prompt_builder",
        PromptBuilder(template=prompt_template, required_variables="*"),
    )

    pipe.connect("embedder.embedding", "retriever.query_embedding")
    pipe.connect("retriever", "prompt_builder.documents")
    return pipe
