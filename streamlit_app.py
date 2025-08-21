import streamlit as st
import numpy as np
import pandas as pd
import sqlalchemy
from db import get_engine
from sqlalchemy import text

engine = get_engine()

# Test the connection

def fetch_data(query: str) -> pd.DataFrame:
    with engine.connect() as conn:
        result = conn.execute(text(query))
        rows = result.fetchall()
        columns = result.keys()
    return pd.DataFrame(rows, columns=columns)

# --- Streamlit UI ---
st.title("Supabase Data Viewer")

# Example usage
df = fetch_data("SELECT * FROM source_data")
st.dataframe(df)