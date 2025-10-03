import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from .utils import load_gutenberg_for_plot  #

__all__ = ["plot_translations"]

def _to_century_floor(birthdate):
    if pd.isna(birthdate):
        return None
    try:
        return (int(birthdate) // 100) * 100
    except Exception:
        return None

def plot_translations(over: str = "birth_century"):
    if over != "birth_century":
        raise ValueError("Only over='birth_century' is supported.")

    df = load_gutenberg_for_plot()

    required = {"author", "birthdate", "language"}
    missing = required - set(df.columns)
    if missing:
        raise KeyError(f"Missing required columns: {missing}")

    # birth_century
    df = df.dropna(subset=["author", "birthdate", "language"]).copy()
    df["birth_century"] = df["birthdate"].apply(_to_century_floor)

    # different languages
    per_author = (df.dropna(subset=["birth_century"])
                    .drop_duplicates(subset=["author", "language"])
                    .groupby(["author", "birth_century"])["language"]
                    .nunique()
                    .reset_index(name="n_langs"))

    plt.figure(figsize=(10, 5))
    ax = sns.barplot(
        data=per_author.sort_values("birth_century"),
        x="birth_century",
        y="n_langs",
        estimator="mean",
        ci=95
    )
    ax.set_xlabel("Birth Century")
    ax.set_ylabel("Average number of languages per author")
    ax.set_title("Average Translations per Author by Birth Century (95% CI)")
    ax.set_xticklabels([int(t.get_text()) for t in ax.get_xticklabels()])
    plt.tight_layout()
    plt.show()
