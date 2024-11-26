# mini-rag

This is a minimal implementation of the RAG model for question answering.

## Requirements

- Python 3.8 or later

#### Install Python using MiniConda

1) Download and install MiniConda from [here](https://docs.anaconda.com/free/miniconda/#quick-command-line-install)
2) Create a new environment using the following command:

```bash
$ conda create -n mini-rag python=3.8
```

3) Activate the environment:

```bash
$ conda activate mini-rag
```

### (Optional) Setup you command line interface for better readability

```bash
export PS1="\[\033[01;32m\]\u@\h:\w\n\[\033[00m\]\$ "
```

## Installation

### Install the required packages

```bash
$ pip install -r requirements.txt
```

### Setup the environment variables

```bash
$ cp .env.example .env
```

# Run Docker Compose services

```bash
$ cd docker
$ cd .env.example .env
```

- Update `.env` with your credentials

```bash
$ cd docker
$ sudo docker compose up -d
```

Set your environment variables in the `.env` file. Like `OPENAI_API_KEY` value.

## Run FastAPI server
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 5000
```

## POSTMAN Collection

Downlaod the POSTMAN Collection from [/assets/mini-rag-app.postman_collection.json](/assets/mini-rag-app.postman_collection.json)
