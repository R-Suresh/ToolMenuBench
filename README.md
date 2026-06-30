# ToolMenuBench

ToolMenuBench is a benchmark for evaluating tool-menu construction strategies in multi-step LLM agents. It studies how the visible tool menu affects reliability, efficiency, and safety-relevant risk exposure.

The benchmark varies:

- tool-menu size
- distractor type
- state-dependent task structure
- risk exposure
- filtering method
- model backend

ToolMenuBench reports both filter-level and downstream agent metrics, including visible-tool count, risky-tool exposure, task success, wrong-tool calls, premature actions, and token usage.

## Paper

**ToolMenuBench: Benchmarking Tool-Menu Filtering Strategies for Reliable and Efficient LLM Agents**

arXiv: `2606.15508`

## Repository contents

```text
.
├── README.md
├── REPRODUCIBILITY.md
├── CITATION.cff
├── LICENSE
├── requirements.txt
├── .gitignore
└── reproducibility/
    ├── run_config_main.json
    └── environment.md
```

Curated public artifacts should be added under these folders once available:

```text
code/
data/
results/
tables/
figures/
```

## Expected public artifact layout

```text
code/
  toolmenubench_runner.py
  analyze_results.py
  plot_results.py

data/
  tasks_102.json
  tool_registry_100.json

results/
  toolmenubench_task_metrics.csv
  summary_by_method.csv
  summary_by_menu_method.csv
  summary_by_distractor_method.csv
  summary_by_model_method.csv

tables/
  summary_by_method.tex

figures/
  success_by_method.png
  wrong_tool_calls_by_method.png
  premature_actions_by_method.png
  risky_tool_exposure_by_method.png
  token_usage_by_method.png
```

The exact artifact names may differ depending on the final curated export, but raw traces and cloud logs should not be uploaded publicly.

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
- review-submission metadata

For public release, prefer curated CSV summaries, derived metrics, generated figures, and sanitized benchmark definitions over raw traces.

## License

This repository is released under the MIT License.
