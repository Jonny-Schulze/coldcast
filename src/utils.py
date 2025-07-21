### plotting functions
import matplotlib.pyplot as plt
import seaborn as sns

def plot_nan_heatmap(df, sort=None):
    """Plots a heatmap of NaN values, optionally sorting by a column."""
    plt.figure(figsize=(10, 8))
    if sort:
        df = df.sort_values(sort)
    sns.heatmap(df.isnull(), cbar=False)
    plt.show()

def plot_timeline(data, date, target, hue=None, log=False):
    """Plots a timeline lineplot with optional hue grouping."""
    plt.figure(figsize=(14, 7))
    sns.lineplot(data=data, x=date, y=target, hue=hue, palette='colorblind')
    plt.xlabel(date, fontsize=12)
    plt.ylabel(target, fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)
    if log:
        plt.yscale('log')
    plt.tight_layout()
    plt.show()