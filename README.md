# 📘 Learn Mistral — Practical AI Workshops

Welcome to the official repository for **_Learn Mistral_** book published by Packt, a hands-on, workshop-driven guide to mastering open-source large language models (LLMs). This repo supports the book's chapters (2–11) and contains code, datasets, configs, and deployment files for practical experimentation.

📍 **Repo URL**: [https://github.com/PacktPublishing/Learn-Mistral](https://github.com/PacktPublishing/Learn-Mistral)

---

## 📂 Repository Structure

Each chapter has its own subfolder (e.g., `Chapter-3`, `Chapter-5`) and includes self-contained workshop materials. Below is a breakdown by chapter:

---

### `Chapter-2` – **Model Setup Examples**
- Folders: `7b`, `mistral-nemo`, `mistral-small`
- Each contains: `emoji.modelfile` — Sample model definitions or tokenizer configs for Mistral variants.

---

### `Chapter-3` – **Softmax and Visualization**
- `ch03_plot_pie_chart.py`: Visualize categorical distributions.
- `ch03_softmax_workshop.py`: Simulates softmax behavior with step-by-step logic.

---

### `Chapter-4` – **Embeddings in Action**
- `ch04_embeddings.ipynb`: Compute and compare vector embeddings using popular libraries.

---

### `Chapter-5` – **Fine-Tuning and Evaluation**
- `ch05_ws1_*.py/.ipynb`: Loan prediction pipeline with and without Weights & Biases (W&B).
- `ch05_ws1_loaners-repayment-data.csv`: Dataset for workshop 1.
- `ch05_ws2_mistral_finetune_7b.ipynb`: Fine-tune Mistral 7B.
- `ch05-mistarl-7b-train-config.yaml`, `*-validation-config.yaml`: Configuration files for model training & validation.

---

### `Chapter-6` – **Retrieval-Augmented Generation (RAG)**
> All notebooks use either ChromaDB or Pinecone for retrieval backend:

- `Ch06_WS1`: Basic RAG
- `Ch06_WS2`: Multi-query RAG
- `Ch06_WS3`: Chain-of-thought and decomposition
- `Ch06_WS4`: Step-back prompting and generalization

---

### `Chapter-7` – **Codestral App Deployment**
- `main.py`: Web backend using Codestral models.
- `config.json`: Application config.
- `templates/joke.html`: Frontend template for joke generation.

---

### `Chapter-8` – **Secure & Vulnerable Code Patterns**
- `JdbcServlet.java`: Java with unsafe JDBC.
- `too-permissive.terraform`: Example of misconfigured infrastructure as code.
- `vulnerable.php`: PHP with common security flaws.

---

### `Chapter-10` – **Cloud LLM Invocation**
- `requirements.txt`: Required Python packages.
- `ws10_step01_list_models.py`: Lists cloud-available models.
- `ws10_step02_call_model.py`: Calls/invokes selected models via API.

---

### `Chapter-11` – **Dockerized Local LLM Deployment**
- `docker-compose-*.yml`: Run models like Mistral 7B, 8B, and Bloom locally via Docker.
- `ch11_ws_step3_*.py`: Scripts to test and interact with deployed models.

---

## 🚀 How to Use

```bash
git clone https://github.com/PacktPublishing/Learn-Mistral.git
cd Learn-Mistral/Chapter-5
python ch05_ws1_loaners_predict.py
```

Or open `.ipynb` notebooks directly in JupyterLab or VSCode.

---

## 🧰 Requirements

Dependencies vary by chapter. Most workshops use:
- `transformers`, `torch`, `faiss`, `langchain`, `pinecone-client`
- For fine-tuning: `wandb`, `peft`
- Deployment: `docker`, `uvicorn`, `fastapi`

Refer to `requirements.txt` (where present) or the first cell of each notebook.

---

## 📬 Contributing

Pull requests and issues are welcome. If you have improvements, bug reports, or suggestions for new workshops — open an issue or PR!
