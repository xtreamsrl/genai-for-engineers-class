# GenAI for Engineers Class

Code and material for the class "Introduction to GenAI for Engineers"

## 🚀 Let's get started!

**#** | **name**                                                            | **open in**
:-----: |:--------------------------------------------------------------------| :-------:
1 | [Explore Embeddings](./notebooks/01-embeddings.ipynb)               | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/xtreamsrl/genai-for-engineers-class/blob/main/notebooks/01-embeddings.ipynb)          
2 | [What are Vector Databases?](./notebooks/02-vector_databases.ipynb) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/xtreamsrl/genai-for-engineers-class/blob/main/notebooks/02-vector_databases.ipynb) 
3 | [RAG From Scratch](./notebooks/03-rag_from_scratch.ipynb)           | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/xtreamsrl/genai-for-engineers-class/blob/main/notebooks/03-rag_from_scratch.ipynb) 
4 | [Haystack Basics](./notebooks/04-haystack_basics.ipynb)             | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/xtreamsrl/genai-for-engineers-class/blob/main/notebooks/04-haystack_basics.ipynb) 
5 | [Haystack RAG](./notebooks/05-haystack_rag.ipynb)                   | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/xtreamsrl/genai-for-engineers-class/blob/main/notebooks/05-haystack_rag.ipynb) 
6 | [Guardrails](./notebooks/06-guardrails.ipynb)                       | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/xtreamsrl/genai-for-engineers-class/blob/main/notebooks/06-guardrails.ipynb) 
7 | [Guardrails](./notebooks/07-observability.ipynb)                    | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/xtreamsrl/genai-for-engineers-class/blob/main/notebooks/07-observability.ipynb) 


## 🎓 A bit of theory

The slides for this class are available on [Canva](https://www.canva.com/design/DAGI8YciVf0/nqo2qMxGM-q4_itr72_clw/edit?utm_content=DAGI8YciVf0&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton), kindly powered by [xtream](https://xtreamers.io).


## 🤗 How to contribute

> [!NOTE]
> The project uses Python 3.10 for compatibility with Colab.

1. Install Poetry, following the official docs: https://python-poetry.org/docs/#installation

2. Run:

```bash
poetry install
```

3. It is highly recommended to use `nbstripout` to avoid pushing the output of jupyter notebooks.
   Install it with:

```bash
pre-commit install
```