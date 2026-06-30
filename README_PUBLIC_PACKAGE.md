# ToolMenuBench Public Artifact Package

This package contains a curated public artifact layout for **ToolMenuBench: Benchmarking Tool-Menu Filtering Strategies for Reliable and Efficient LLM Agents**.

## Scope

This public package contains the validated 30-task distractor benchmark artifacts:

- 7 distractor conditions
- 7 model backends
- 6 filtering methods
- 3 menu sizes
- 30 benchmark tasks
- 26,460 total task-level rows

The uploaded artifacts available here support the 30-task validated distractor benchmark. They do not contain a separate 102-task artifact package.

## Layout

```text
code/
  toolmenubench_runner.py
  analyze_toolmenubench.py
  plot_toolmenubench_results.py
  README_RUN.md

scripts/
  run_smoke.sh
  run_full_first_pass.sh
  run_one_distractor_mix.sh

results/
  toolmenubench_task_metrics_all_distractors.csv
  summary_by_method.csv
  summary_by_distractor_method.csv
  summary_by_menu_method.csv
  summary_by_model_method.csv
  summary_by_model_distractor_method.csv
  summary_by_model_menu_method.csv
  task_metrics_by_distractor/
    toolmenubench_task_metrics_mixed.csv
    toolmenubench_task_metrics_schema_compatible.csv
    toolmenubench_task_metrics_risky.csv
    toolmenubench_task_metrics_cross_domain.csv
    toolmenubench_task_metrics_semantic.csv
    toolmenubench_task_metrics_near_duplicate.csv
    toolmenubench_task_metrics_premature.csv

figures/
  success_by_method.png
  tokens_by_method.png
  success_vs_menu_size.png
  tokens_vs_menu_size.png

tables/
  main_results_table.tex
  menu_scaling_table.tex
  model_method_table.tex

reproducibility/
  run_config_public_results.json
  environment.md
```

## Sanitization

The public task-metrics CSVs intentionally remove the `final_state` column because some failure rows contained raw provider metadata or raw model text. Raw JSONL traces are excluded.

Do not upload these files publicly:

```text
toolmenubench_raw_traces.jsonl
raw_traces.jsonl
*.log
*.bak
._*
*.zip
```

## Recommended GitHub placement

Copy these package folders into the repository root:

```text
code/
scripts/
results/
figures/
tables/
reproducibility/
README_PUBLIC_PACKAGE.md
requirements.txt
```

Then update `README.md` and `REPRODUCIBILITY.md` to describe the released public artifacts as validated 30-task runs.
