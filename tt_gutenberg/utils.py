import pandas as pd

def load_gutenberg_data():
    # loading dataset
    url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/refs/heads/main/data/2025/2025-06-03/gutenberg_authors.csv"
    df = pd.read_csv(url)
    return df
