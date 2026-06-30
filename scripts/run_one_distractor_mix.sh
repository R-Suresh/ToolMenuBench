#!/usr/bin/env bash
set -o pipefail

MIX="$1"

cd "$(dirname "$0")/../code"
if [ -d ../.venv ]; then
  source ../.venv/bin/activate
elif [ -d .venv ]; then
  source .venv/bin/activate
fi

export AWS_REGION=us-east-1
export AWS_DEFAULT_REGION=us-east-1

mkdir -p ../results_run

export BEDROCK_MODEL_IDS="us.anthropic.claude-opus-4-8,us.anthropic.claude-sonnet-4-6,us.anthropic.claude-haiku-4-5-20251001-v1:0,openai.gpt-oss-120b-1:0,us.amazon.nova-premier-v1:0,us.amazon.nova-2-lite-v1:0,us.amazon.nova-2-pro-preview-20251202-v1:0"

echo "============================================================"
echo "Running distractor mix: $MIX"
echo "Started at: $(date)"
echo "============================================================"

python3 toolmenubench_runner.py \
  --mode full \
  --task-limit 30 \
  --menu-sizes 25,100,250 \
  --distractor-mix "$MIX" \
  --outdir "../results_run/results_distractor_full_${MIX}" \
  2>&1 | tee "../results_run/results_distractor_full_${MIX}_run.log"

RUN_STATUS=${PIPESTATUS[0]}

echo "Runner exit status for $MIX: $RUN_STATUS"
echo "Analyzing $MIX at: $(date)"

python3 analyze_toolmenubench.py \
  --input "../results_run/results_distractor_full_${MIX}/toolmenubench_task_metrics.csv" \
  --outdir "../results_run/results_distractor_full_${MIX}" \
  2>&1 | tee -a "../results_run/results_distractor_full_${MIX}_run.log"

echo "Finished distractor mix: $MIX"
echo "Finished at: $(date)"
