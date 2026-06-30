import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

out = Path("results_full_7models/figures")
out.mkdir(exist_ok=True)

by_method = pd.read_csv("results_full_7models/summary_by_method.csv")
by_menu = pd.read_csv("results_full_7models/summary_by_menu_method.csv")

# Success by method
plt.figure(figsize=(8, 4.5))
plt.bar(by_method["method"], by_method["success"])
plt.ylabel("Task success")
plt.xlabel("Filtering method")
plt.xticks(rotation=35, ha="right")
plt.tight_layout()
plt.savefig(out / "success_by_method.png", dpi=200)
plt.close()

# Tokens by method
plt.figure(figsize=(8, 4.5))
plt.bar(by_method["method"], by_method["tokens"])
plt.ylabel("Average tokens per task")
plt.xlabel("Filtering method")
plt.xticks(rotation=35, ha="right")
plt.tight_layout()
plt.savefig(out / "tokens_by_method.png", dpi=200)
plt.close()

# Success vs menu size
plt.figure(figsize=(8, 4.5))
for method, g in by_menu.groupby("method"):
    g = g.sort_values("menu_size")
    plt.plot(g["menu_size"], g["success"], marker="o", label=method)
plt.ylabel("Task success")
plt.xlabel("Tool registry size")
plt.legend(fontsize=8)
plt.tight_layout()
plt.savefig(out / "success_vs_menu_size.png", dpi=200)
plt.close()

# Tokens vs menu size
plt.figure(figsize=(8, 4.5))
for method, g in by_menu.groupby("method"):
    g = g.sort_values("menu_size")
    plt.plot(g["menu_size"], g["tokens"], marker="o", label=method)
plt.ylabel("Average tokens per task")
plt.xlabel("Tool registry size")
plt.legend(fontsize=8)
plt.tight_layout()
plt.savefig(out / "tokens_vs_menu_size.png", dpi=200)
plt.close()

print("Wrote figures to", out)
