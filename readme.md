pdfReaderProject/
│── app.py                      # Flask entry point (create & run app) <br>
│── config.py                   # Configs (API keys, DB URI, etc.) <br>
│── requirements.txt <br>
│── .env                        # Secrets (Mongo URI, API key) <br>
│── README.md <br>
<br>
├── backend/                     # Core backend logic <br>
│   ├── __init__.py <br>
│   ├── routes/                  # Flask route handlers <br>
│   │   ├── __init__.py <br>
│   │   ├── chat_routes.py       # Ask anything / chatbot endpoints <br>
│   │   ├── db_routes.py         # Database query endpoints <br>
│   │   └── extract_routes.py    # Text extraction endpoints <br>
│   │ <br>
│   ├── services/                # Business logic layer <br>
│   │   ├── __init__.py <br>
 |   |   ├── RAG/ <br>
|   |   |   ├──__init__.py <br>
|   |   |   ├──files_services.py <br>
|   |   |   └──vector_embeddings/py <br>
│   │   ├── chatbot_service.py   # Handles embeddings + LLM context <br>
│   │   ├── db_service.py        # Mongo/Postgres queries <br>
│   │   └── extract_service.py   # File parsing, text extraction <br>
│   │ <br>
│   ├── utils/                   # Helper functions <br>
│   │   ├── __init__.py <br>
│   │   ├── embedding_utils.py   # Vector DB, similarity search <br>
│   │   ├── file_utils.py        # Upload, save, delete <br>
│   │   └── text_utils.py        # Cleaning, formatting text <br>
│   │ <br>
│   └── models/                  # For ORM or schema definitions <br>
│       ├── __init__.py <br>
│       ├── mongo_models.py      # MongoDB collections (if used) <br>
│       └── sql_models.py        # SQLAlchemy models (if used) <br>
<br>
├── vector_store/                # Persistent storage for embeddings <br>
│   └── index/                   # FAISS / Chroma DB files <br>
 <br>
├── uploads/                     # User-uploaded files <br>
│   ├── pdfs/ <br>
│   ├── docs/ <br>
│   └── txt/ <br>
 <br>
├── frontend/                    # Optional (if you add UI later) <br>
│   ├── static/                  # CSS, JS <br>
│   ├── templates/               # HTML (if Flask Jinja2) <br>
│   └── react-app/               # (if you choose React instead) <br>


