# Reproducibility Notes

This document describes the public reproducibility package for **ToolMenuBench: Benchmarking Tool-Menu Filtering Strategies for Reliable and Efficient LLM Agents**.

The goal of this repository is to provide clean, arXiv-compatible code and curated artifacts for reproducing the validated public ToolMenuBench artifact release. It is not intended to be a dump of raw internal run traces or cloud execution logs.

## Public artifact scope

This public package contains the validated 30-task distractor benchmark artifacts:

- 7 distractor conditions
- 7 model backends
- 6 filtering methods
- 3 menu sizes
- 30 benchmark tasks
- 26,460 total task-level rows

The uploaded artifacts support the validated 30-task distractor benchmark. They do not contain a separate 102-task artifact package.

## Benchmark scope

ToolMenuBench evaluates how tool-menu construction affects multi-step LLM-agent behavior.

The benchmark reports:

- task success
- wrong-tool calls
- premature actions
- visible tool count
- risky-tool exposure
- token usage
- model/method-level summaries
- distractor-condition summaries

## Repository layout

```text
.
├── README.md
├── README_PUBLIC_PACKAGE.md
├── REPRODUCIBILITY.md
├── SANITIZATION_REPORT.md
├── MANIFEST.csv
├── CITATION.cff
├── LICENSE
├── requirements.txt
├── .gitignore
├── code/
│   ├── toolmenubench_runner.py
│   ├── analyze_toolmenubench.py
│   ├── plot_toolmenubench_results.py
│   └── README_RUN.md
├── scripts/
│   ├── run_smoke.sh
│   ├── run_full_first_pass.sh
│   └── run_one_distractor_mix.sh
├── results/
│   ├── toolmenubench_task_metrics_all_distractors.csv
│   ├── summary_by_method.csv
│   ├── summary_by_distractor_method.csv
│   ├── summary_by_menu_method.csv
│   ├── summary_by_model_method.csv
│   ├── summary_by_model_distractor_method.csv
│   ├── summary_by_model_menu_method.csv
│   └── task_metrics_by_distractor/
│       ├── toolmenubench_task_metrics_mixed.csv
│       ├── toolmenubench_task_metrics_schema_compatible.csv
│       ├── toolmenubench_task_metrics_risky.csv
│       ├── toolmenubench_task_metrics_cross_domain.csv
│       ├── toolmenubench_task_metrics_semantic.csv
│       ├── toolmenubench_task_metrics_near_duplicate.csv
│       └── toolmenubench_task_metrics_premature.csv
├── figures/
│   ├── success_by_method.png
│   ├── tokens_by_method.png
│   ├── success_vs_menu_size.png
│   └── tokens_vs_menu_size.png
├── tables/
│   ├── main_results_table.tex
│   ├── menu_scaling_table.tex
│   └── model_method_table.tex
└── reproducibility/
    ├── run_config_main.json
    ├── run_config_public_results.json
    └── environment.md
```

## What is included

The public release includes:

- benchmark runner code
- analysis script
- plotting script
- curated task-level metrics CSVs
- per-distractor task-level metrics CSVs
- aggregate summary CSVs
- paper-style figures
- LaTeX tables
- package manifest
- sanitization report
- reproducibility notes
- environment documentation
- citation metadata

## What is intentionally excluded

The repository should not include unsanitized raw traces or cloud execution logs.

Excluded artifacts include:

- AWS credentials
- `.env` files
- PEM/key files
- Bedrock request IDs
- raw Bedrock/API response metadata
- raw model completions
- raw JSONL traces
- local EC2 shell history
- personal notes
- backup files
- review-submission metadata
- any double-blind review information

## Environment setup

Install dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
```

The original experiments used Amazon Bedrock through `boto3`. Configure AWS credentials outside the repository.

Example environment variables:

```bash
export AWS_REGION=us-east-1
export AWS_DEFAULT_REGION=us-east-1
```

## Public result artifacts

The main public task-level file is:

```text
results/toolmenubench_task_metrics_all_distractors.csv
```

Per-distractor task-level metrics are stored under:

```text
results/task_metrics_by_distractor/
```

Aggregate summaries are provided as:

```text
results/summary_by_method.csv
results/summary_by_distractor_method.csv
results/summary_by_menu_method.csv
results/summary_by_model_method.csv
results/summary_by_model_distractor_method.csv
results/summary_by_model_menu_method.csv
```

The public task-metrics CSVs intentionally remove the original `final_state` column because some failure rows contained raw provider metadata or raw model text. Raw JSONL traces are excluded.

## Sanitization

See:

```text
SANITIZATION_REPORT.md
MANIFEST.csv
```

The package manifest records file sizes and SHA-256 hashes for the public artifact package.

## Suggested validation checklist before release

Before tagging a release, check that the repository does not contain sensitive or raw files.

Files that should not be tracked include:

```text
.pem
.key
.env
raw_traces
*_raw_traces.jsonl
.aws
.log
.bak
._*
```

Search tracked files for common secrets or metadata patterns before release.

## Release target

Recommended release tag:

```text
v1.0-arxiv
```

Recommended release title:

```text
v1.0-arxiv: Reproducibility package for ToolMenuBench
```

Recommended release description:

```text
This release contains the public reproducibility package for the arXiv version of ToolMenuBench: Benchmarking Tool-Menu Filtering Strategies for Reliable and Efficient LLM Agents.

It includes runner code, analysis scripts, curated task-level metrics, aggregate summaries, figures, tables, reproducibility notes, environment documentation, citation metadata, a manifest, and a sanitization report.

Raw traces, raw model outputs, cloud logs, and credentials are intentionally excluded.
```
