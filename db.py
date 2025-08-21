import streamlit as st
import sqlalchemy

@st.cache_resource  # zajistí, že se spojení vytvoří jen jednou a bude sdílené
def get_engine():
        # Supabase connection
    from sqlalchemy import create_engine
        # from sqlalchemy.pool import NullPool
    from dotenv import load_dotenv
    import os

    # Load environment variables from .env
    load_dotenv()

    # Fetch variables
    USER = os.getenv("user")
    PASSWORD = os.getenv("password")
    HOST = os.getenv("host")
    PORT = os.getenv("port")
    DBNAME = os.getenv("dbname")

    # Construct the SQLAlchemy connection string
    DATABASE_URL = f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DBNAME}?sslmode=require"

    # Create the SQLAlchemy engine
    engine = create_engine(DATABASE_URL)
    # If using Transaction Pooler or Session Pooler, we want to ensure we disable SQLAlchemy client side pooling -
    # https://docs.sqlalchemy.org/en/20/core/pooling.html#switching-pool-implementations
    # engine = create_engine(DATABASE_URL, poolclass=NullPool)
    return engine
