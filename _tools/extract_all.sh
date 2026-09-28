#!/usr/bin/env bash
# Run extract.py for every row of papers.tsv not yet in the cache (2 at a time).
cd "$(dirname "$0")/.."
grep -v '^#' _tools/papers.tsv | while IFS=$'\t' read -r key url _ _; do
  [ -f ".cache/docling/$key/figures.md" ] && continue
  echo "$key $url"
done | xargs -P 2 -L 1 bash -c 'uv run _tools/extract.py "$0" "$1" --max-pages 45 > ".cache/log-$0.txt" 2>&1 && echo "OK $0" || echo "FAIL $0"'
