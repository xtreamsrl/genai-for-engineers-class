# GenAI for Engineers Class

Code and material for the class "Introduction to GenAI for Engineers"

## 🚀 Let's get started!

**#** | **name**                                                                             | **open in**
:-----: |:-------------------------------------------------------------------------------------| :-------:
1 | [Explore Tokens](./notebooks/01-embeddings.ipynb)                                    | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/xtreamsrl/genai-for-engineers-class/blob/main/notebooks/01-tokenization.ipynb)          
2 | [Explore Embeddings](./notebooks/01-embeddings.ipynb)                                | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/xtreamsrl/genai-for-engineers-class/blob/main/notebooks/02-embeddings.ipynb)          
3 | [What are Vector Databases?](./notebooks/02-vector_databases.ipynb)                  | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/xtreamsrl/genai-for-engineers-class/blob/main/notebooks/03-vector-databases.ipynb) 
4 | [Diffusion Models](./notebooks/03-rag_from_scratch.ipynb)                            | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/xtreamsrl/genai-for-engineers-class/blob/main/notebooks/04-stable-diffusion.ipynb) 
5 | [Video Models](./notebooks/03-rag_from_scratch.ipynb)                                | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/xtreamsrl/genai-for-engineers-class/blob/main/notebooks/05-veo.ipynb) 
6 | [RAG From Scratch](./notebooks/03-rag_from_scratch.ipynb)                            | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/xtreamsrl/genai-for-engineers-class/blob/main/notebooks/06-rag-from-scratch.ipynb) 
7 | [Haystack Basics](./notebooks/04-haystack_basics.ipynb)                              | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/xtreamsrl/genai-for-engineers-class/blob/main/notebooks/07-haystack-basics.ipynb) 
8 | [Haystack RAG](./notebooks/05-haystack_rag.ipynb)                                    | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/xtreamsrl/genai-for-engineers-class/blob/main/notebooks/08-haystack-rag.ipynb) 
9 | [Guardrails](./notebooks/06-guardrails.ipynb)                                        | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/xtreamsrl/genai-for-engineers-class/blob/main/notebooks/09-guardrails.ipynb) 
10 | [Observability](./notebooks/07-observability.ipynb)                                  | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/xtreamsrl/genai-for-engineers-class/blob/main/notebooks/10-observability.ipynb) 
11 | [Function Calling](./notebooks/08-function_calling.ipynb)                            | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/xtreamsrl/genai-for-engineers-class/blob/main/notebooks/11-function-calling.ipynb) 
12 | [Agents](./notebooks/09-agents.ipynb)                                                | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/xtreamsrl/genai-for-engineers-class/blob/main/notebooks/12-agents.ipynb) 
13 | [Agents for Income Statement Analysis](./notebooks/10-agents_income_statement.ipynb) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/xtreamsrl/genai-for-engineers-class/blob/main/notebooks/13-agents-income-statement.ipynb) 


## 🥂 How to contribute

> [!NOTE]
> The project uses Python 3.12 for compatibility with Colab.

1. Install uv, following the official docs: https://docs.astral.sh/uv/getting-started/installation/

2. Run:

```bash
uv sync --all-groups
```

3. It is highly recommended to use `nbstripout` to avoid pushing the output of jupyter notebooks.
   Install it with:

```bash
pre-commit install
```

## 🤗 Authors
This class was created by the AI team at [xtream](https://xtreamers.io), with contributions from:
- [Emanuele Fabbiani](https://www.linkedin.com/in/emanuelefabbiani/)
- [Luca Baggi](https://www.linkedin.com/in/lucabaggi/)
- [Gabriele Orlandi](https://www.linkedin.com/in/gabri-o/)
- [Fabio Lipreri](https://www.linkedin.com/in/fabiolipreri/)
- [Marta Peroni](https://www.linkedin.com/in/peroni-marta-19145499/)
- [Carlo Piccinin](https://www.linkedin.com/in/carlo-piccinin-399a0869/)

## 🔍 Spotted in...
The material in this repository was used in classes and seminars taught at:

- [Catholic University of Milan](https://www.unicatt.it/), 2025
- [Lavazza](https://www.lavazza.it), 2025
- [Fabrick](https://www.fabrick.com/), 2025
- [Atlante](https://atlante.energy/), 2025
- [CRIF](https://www.crif.it/), 2024 & 2025
- [Talent Garden](https://talentgarden.com/), 2025
- [Zuccari](https://www.zuccari.com/), 2025
- [TWIN Agency](https://twin.services/en/), 2024
- [WeRoad](https://www.weroad.it/), 2024
- [Banca CF+](https://www.bancacfplus.it/), 2023
- [Boolean Dataweek](https://boolean.careers/), 2023

And was the base for the 10+ talks and workshops, including:

- Embeddings, Transformers, RLHF: Three Key Ideas to Understand ChatGPT, [AI Conf](https://www.aiconf.it/), 2024, Milan, Italy
- How to Build Your Own GPT, [AMLD](https://appliedmldays.org/), 2024, Lausanne, Switzerland
- Embeddings, Transformers, RLHF: Three Key Ideas to Understand ChatGPT, [PyCon IT](https://2024.pycon.it/en), 2024, Florence, Italy
- Beyond ChatGPT: RAG and Fine-Tuning, University of Pavia, 2024, Pavia, Italy
- Embeddings, Transformers, RLHF: Three Key Ideas to Understand ChatGPT, [BI Digital](https://bidigital.it/), 2023, Biella, Italy
- Embeddings, Transformers, RLHF: Three Key Ideas to Understand ChatGPT, [SIIAM](https://www.siiam.it/en) Congress, 2023, Rome, Italy
