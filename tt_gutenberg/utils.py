import pandas as pd
'''
def load_gutenberg_data():
    # loading dataset
    url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/refs/heads/main/data/2025/2025-06-03/gutenberg_authors.csv"
    df = pd.read_csv(url)
    return df
'''

# loading dataset
AUTHORS_URL   = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/refs/heads/main/data/2025/2025-06-03/gutenberg_authors.csv"
LANGUAGES_URL = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/refs/heads/main/data/2025/2025-06-03/gutenberg_languages.csv"
METADATA_URL  = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/refs/heads/main/data/2025/2025-06-03/gutenberg_metadata.csv"

def load_gutenberg_authors():
    return pd.read_csv(AUTHORS_URL)

def load_gutenberg_languages():
    return pd.read_csv(LANGUAGES_URL)

def load_gutenberg_metadata():
    return pd.read_csv(METADATA_URL)

def load_gutenberg_for_plot():
    """
    產生含 author、birthdate、language 的資料：
    languages ⟶(gutenberg_id)⟶ metadata ⟶(gutenberg_author_id)⟶ authors
    """
    a = load_gutenberg_authors()    # has: gutenberg_author_id, author, birthdate, alias...
    l = load_gutenberg_languages()  # has: gutenberg_id, language
    m = load_gutenberg_metadata()   # has: gutenberg_id, gutenberg_author_id, author, language

    # get authors' ID from the book
    lm = l.merge(m[["gutenberg_id", "gutenberg_author_id"]], on="gutenberg_id", how="left")

    # get author, birthdate
    out = lm.merge(a[["gutenberg_author_id", "author", "birthdate"]], on="gutenberg_author_id", how="left")

    # clean
    out["author"] = out["author"].astype(str).str.strip()
    out["language"] = out["language"].astype(str).str.strip()

    return out

def load_gutenberg_data():
    """Back-compat for authors.py：回傳 authors 表（含 author/alias/birthdate）。"""
    return load_gutenberg_authors()