# ToolMenuBench EC2/Bedrock Starter

This starter package runs a first ToolMenuBench experiment set on an EC2 instance using Amazon Bedrock.

## Files

- `toolmenubench_runner.py` — main experiment runner.
- `analyze_toolmenubench.py` — summary script.
- `requirements.txt` — dependencies.
- `run_smoke.sh` — tiny test run.
- `run_full_first_pass.sh` — first real run.

## Outputs

The runner writes:

```text
results/toolmenubench_task_metrics.csv
results/toolmenubench_raw_traces.jsonl
```

The analyzer writes:

```text
results/summary_by_method.csv
results/summary_by_menu_method.csv
results/summary_by_distractor_method.csv
results/summary_by_model_method.csv
```

## Safety

Do not commit AWS credentials, `.env` files, PEM keys, raw logs with private data, or local machine paths.
