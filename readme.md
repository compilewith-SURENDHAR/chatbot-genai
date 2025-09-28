pdfReaderProject/
│── app.py                      # Flask entry point (create & run app)
│── config.py                   # Configs (API keys, DB URI, etc.)
│── requirements.txt
│── .env                        # Secrets (Mongo URI, API key)
│── README.md

├── backend/                     # Core backend logic
│   ├── __init__.py
│   ├── routes/                  # Flask route handlers
│   │   ├── __init__.py
│   │   ├── chat_routes.py       # Ask anything / chatbot endpoints
│   │   ├── db_routes.py         # Database query endpoints
│   │   └── extract_routes.py    # Text extraction endpoints
│   │
│   ├── services/                # Business logic layer
│   │   ├── __init__.py
|   |   ├── RAG/
|   |   |   ├──__init__.py
|   |   |   ├──files_services.py
|   |   |   └──vector_embeddings/py
│   │   ├── chatbot_service.py   # Handles embeddings + LLM context
│   │   ├── db_service.py        # Mongo/Postgres queries
│   │   └── extract_service.py   # File parsing, text extraction
│   │
│   ├── utils/                   # Helper functions
│   │   ├── __init__.py
│   │   ├── embedding_utils.py   # Vector DB, similarity search
│   │   ├── file_utils.py        # Upload, save, delete
│   │   └── text_utils.py        # Cleaning, formatting text
│   │
│   └── models/                  # For ORM or schema definitions
│       ├── __init__.py
│       ├── mongo_models.py      # MongoDB collections (if used)
│       └── sql_models.py        # SQLAlchemy models (if used)

├── vector_store/                # Persistent storage for embeddings
│   └── index/                   # FAISS / Chroma DB files

├── uploads/                     # User-uploaded files
│   ├── pdfs/
│   ├── docs/
│   └── txt/

├── frontend/                    # Optional (if you add UI later)
│   ├── static/                  # CSS, JS
│   ├── templates/               # HTML (if Flask Jinja2)
│   └── react-app/               # (if you choose React instead)

└── tests/                       # Unit & integration tests
    ├── __init__.py
    ├── test_chatbot.py
    ├── test_db.py
    └── test_extract.py
