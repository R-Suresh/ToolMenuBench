# Sanitization Report

No sensitive/provider metadata patterns were found in the public result CSV artifacts.

The public task-metrics CSVs exclude the original `final_state` column because some failure rows in the raw exports contained provider metadata or raw model text. Raw JSONL traces, logs, backup files, and Mac metadata files are not included in this public package.
