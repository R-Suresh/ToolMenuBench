# Reproducibility Notes

This document describes the public reproducibility package for **ToolMenuBench: Benchmarking Tool-Menu Filtering Strategies for Reliable and Efficient LLM Agents**.

The goal of this repository is to provide clean, arXiv-compatible code and curated artifacts for reproducing the ToolMenuBench experiments. It is not intended to be a dump of raw internal run traces or cloud execution logs.

## Benchmark scope

ToolMenuBench evaluates how tool-menu construction affects multi-step LLM-agent behavior.

The benchmark varies:

- tool-menu size
- distractor type
- state-dependent task structure
- risk exposure
- filtering method
- model backend

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

Current core layout:

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

Target public artifact layout:

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

## What should be included

The public release should include:

- benchmark runner or experiment script
- analysis script
- plotting script
- sanitized benchmark task definitions
- sanitized tool registry
- curated task-level metrics CSVs
- aggregate summary CSVs
- paper-style figures
- LaTeX tables, if available
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
- raw JSONL traces unless carefully inspected and sanitized
- local EC2 shell history
- personal notes
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

## Public artifact policy

For public release, prefer curated and derived files such as:

```text
results/*.csv
tables/*.tex
figures/*.png
reproducibility/run_config_main.json
reproducibility/environment.md
```

Do not upload by default:

```text
raw_traces.jsonl
toolmenubench_raw_traces.jsonl
results_*/
*.log
.aws/
.env
*.pem
*.key
```

## Sanitizing run artifacts

Before uploading any artifact generated on EC2 or through Bedrock, inspect it for:

- Request IDs
- Account IDs
- ARNs
- access keys
- session tokens
- local file paths
- hostnames
- IP addresses
- raw prompts
- raw model completions
- provider response metadata
- timestamps that reveal internal execution details
- review or submission metadata

For the public reproducibility package, prefer task metrics, summary CSVs, figures, and tables over raw JSONL traces.

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

It includes reproducibility notes, environment documentation, citation metadata, and curated artifacts if available.

Raw traces, raw model outputs, cloud logs, and credentials are intentionally excluded.
```
