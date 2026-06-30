#!/usr/bin/env python3
import argparse
from pathlib import Path
import pandas as pd


def summarize(df, group_cols):
    return (
        df.groupby(group_cols)
        .agg(
            runs=("task_id", "count"),
            success=("success", "mean"),
            wrong=("wrong_tool_count", "mean"),
            premature=("premature_action_count", "mean"),
            tools_per_step=("avg_tools_per_step", "mean"),
            gold_exp=("gold_exposure_rate", "mean"),
            no_visible=("no_visible_rate", "mean"),
            risky_visible=("risky_visible_count", "mean"),
            unauthorized_risky=("unauthorized_risky_visible_count", "mean"),
            tokens=("total_tokens", "mean"),
            steps=("steps", "mean"),
        )
        .reset_index()
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="results/toolmenubench_task_metrics.csv")
    parser.add_argument("--outdir", default="results")
    args = parser.parse_args()

    outdir = Path(args.outdir)
    outdir.mkdir(exist_ok=True)
    df = pd.read_csv(args.input)

    outputs = {
        "summary_by_method.csv": summarize(df, ["method"]),
        "summary_by_menu_method.csv": summarize(df, ["menu_size", "method"]),
        "summary_by_distractor_method.csv": summarize(df, ["distractor_mix", "method"]),
        "summary_by_model_method.csv": summarize(df, ["model", "method"]),
    }

    for name, table in outputs.items():
        path = outdir / name
        table.to_csv(path, index=False)
        print(f"Wrote {path}")

    print("\n=== Summary by method ===")
    print(outputs["summary_by_method.csv"].to_string(index=False))


if __name__ == "__main__":
    main()
