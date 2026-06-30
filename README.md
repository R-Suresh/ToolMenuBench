# ToolMenuBench

ToolMenuBench is a benchmark for evaluating tool-menu construction strategies in multi-step LLM agents. It studies how the visible tool menu affects reliability, efficiency, and safety-relevant risk exposure.

ToolMenuBench reports both filter-level and downstream agent metrics, including visible-tool count, risky-tool exposure, task success, wrong-tool calls, premature actions, and token usage.

## Paper

**ToolMenuBench: Benchmarking Tool-Menu Filtering Strategies for Reliable and Efficient LLM Agents**

arXiv: `2606.15508`

## Public artifact scope

This repository contains the validated public 30-task distractor benchmark artifact release:

- 7 distractor conditions
- 7 model backends
- 6 filtering methods
- 3 menu sizes
- 30 benchmark tasks
- 26,460 task-level rows

The uploaded public artifacts support the validated 30-task distractor benchmark. They do not contain a separate 102-task artifact package.

## Repository contents

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

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
```

The original experiments were run in a Linux/EC2 environment using Amazon Bedrock through `boto3`. Configure AWS credentials outside this repository.

Example region configuration:

```bash
export AWS_REGION=us-east-1
export AWS_DEFAULT_REGION=us-east-1
```

## Public results

The main public task-level file is:

```text
results/toolmenubench_task_metrics_all_distractors.csv
```

The per-distractor task-level metrics are under:

```text
results/task_metrics_by_distractor/
```

Aggregate summaries are provided under:

```text
results/summary_by_method.csv
results/summary_by_distractor_method.csv
results/summary_by_menu_method.csv
results/summary_by_model_method.csv
results/summary_by_model_distractor_method.csv
results/summary_by_model_menu_method.csv
```

The public task-metrics CSVs intentionally remove the original `final_state` column because some failure rows contained raw provider metadata or raw model text. Raw JSONL traces are excluded.

## Public artifact policy

This repository is intended to contain clean reproducibility code and curated artifacts only.

Do not upload:

- AWS credentials or `.env` files
- PEM/key files
- raw Bedrock request metadata
- raw model completions
- raw JSONL traces
- local EC2 shell history
- local cloud logs
- backup files
- review-submission metadata

For public release, prefer curated CSV summaries, derived metrics, generated figures, and sanitized benchmark definitions over raw traces.

## License

This repository is released under the MIT License.
