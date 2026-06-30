#!/usr/bin/env bash
set -euo pipefail

export AWS_REGION="${AWS_REGION:-us-east-1}"
export AWS_DEFAULT_REGION="${AWS_DEFAULT_REGION:-us-east-1}"
export BEDROCK_MODEL_IDS="${BEDROCK_MODEL_IDS:-amazon.nova-lite-v1:0,amazon.nova-pro-v1:0,anthropic.claude-3-haiku-20240307-v1:0,anthropic.claude-3-sonnet-20240229-v1:0}"

python3 toolmenubench_runner.py \
  --mode full \
  --task-limit 30 \
  --menu-sizes 25,100,250 \
  --distractor-mix mixed \
  --outdir results

python3 analyze_toolmenubench.py --input results/toolmenubench_task_metrics.csv --outdir results
