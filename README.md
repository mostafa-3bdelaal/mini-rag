# mini-rag

This is a minimal implementation of the RAG model for question answering.

## Requirements

- Python 3.8 or later

### Install Dependencies

```bash
sudo apt update
sudo apt install libpq-dev gcc python3-dev
```

### Install Python using MiniConda

1. Download and install MiniConda from [here](https://docs.anaconda.com/free/miniconda/#quick-command-line-install).

2. Create a new environment using the following command:

```bash
conda create -n mini-rag python=3.11
```

3. Activate the environment:

```bash
conda activate mini-rag
```

### (Optional) Setup your command line interface for better readability

```bash
export PS1="\\[\033[01;32m\\]\u@\h:\w\n\\[\033[00m\\]\\$ "
```


## Installation

### Install the required packages

```bash
pip install -r requirements.txt
```

### Setup the environment variables

```bash
cp .env.example .env
```

Set your environment variables in the `.env` file, such as the `OPENAI_API_KEY` value.

## Run Docker Compose Services

```bash
cd docker
cp .env.example .env
```

Update the Docker `.env` file with your MongoDB credentials and other required settings.

```bash
sudo docker compose up -d
```

### Important: MongoDB Configuration

Before running the FastAPI server, make sure to update the `MONGODB_URL` in your application's `.env` file.

Replace `admin:admin` with the actual MongoDB username and password configured in `docker/.env`.

For example:

```env
MONGODB_URL="mongodb://your_username:your_password@localhost:27007/?authSource=admin"
MONGODB_DATABASE="mini-rag"
```

**Note:**

- Replace `your_username` and `your_password` with your actual MongoDB credentials.
- Make sure the port (`27007`) matches your Docker port mapping.
- `authSource=admin` is required when authenticating with the MongoDB root user.
- The application's `.env` file and `docker/.env` are two separate files. Updating `docker/.env` does not automatically update the application's `MONGODB_URL`.
- Never commit your actual passwords or API keys to GitHub.

## Run the FastAPI server

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 5000
```

## POSTMAN Collection

Download the POSTMAN collection from [/assets/mini-rag-app.postman_collection.json](/assets/mini-rag-app.postman_collection.json).
