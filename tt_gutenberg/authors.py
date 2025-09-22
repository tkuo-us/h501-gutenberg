from .utils import load_gutenberg_data

def list_authors(by_languages=True, alias=True):
    df = load_gutenberg_data()

    if alias:
        col = "alias"
    else:
        col = "author"

    counts = df.groupby(col).size().reset_index(name="count")

    # many -> less
    counts = counts.sort_values("count", ascending=False)

    # return
    return counts[col].tolist()
