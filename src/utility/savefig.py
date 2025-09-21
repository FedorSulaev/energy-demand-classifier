from pathlib import Path
import matplotlib.pyplot as plt

# Create figures directory
fig_dir = Path("outputs/figures")
fig_dir.mkdir(parents=True, exist_ok=True)

def savefig(name, dpi=300, tight=True):
    """
    Save the current matplotlib figure to the figures folder.
    
    Args:
        name (str): filename without extension (e.g., 'class_distribution')
        dpi (int): resolution in dots per inch (default=300)
        tight (bool): apply tight_layout before saving
    """
    path = fig_dir / f"{name}.png"
    if tight:
        plt.tight_layout()
    plt.savefig(path, dpi=dpi, bbox_inches="tight")
    print(f"Figure saved: {path}")