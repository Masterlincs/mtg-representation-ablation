"""Recompute the headline results from the preserved score table."""

import csv
from collections import defaultdict
from pathlib import Path
from statistics import mean


DATA = Path(__file__).parent / "data" / "key_results.csv"


def load_scores(path: Path = DATA) -> dict[str, dict[str, float]]:
    scores: dict[str, dict[str, float]] = defaultdict(dict)
    with path.open(newline="", encoding="utf-8") as source:
        for row in csv.DictReader(source):
            scores[row["variant"]][row["model"]] = float(row["mechanical_score"])
    return dict(scores)


def summarize(scores: dict[str, dict[str, float]]) -> list[tuple[str, float]]:
    return sorted(
        ((variant, mean(model_scores.values())) for variant, model_scores in scores.items()),
        key=lambda item: item[1],
        reverse=True,
    )


def main() -> None:
    scores = load_scores()
    for variant, score in summarize(scores):
        print(f"{variant:18} {score:8.3f}")

    rep1_deltas = {
        model: scores["rep1"][model] - scores["ablate_raw_cost"][model]
        for model in scores["rep1"]
    }
    print(f"\nrep1 vs raw cost: +{mean(rep1_deltas.values()):.3f} mean points")
    print(
        "per-model range: "
        f"+{min(rep1_deltas.values()):.3f} to +{max(rep1_deltas.values()):.3f}"
    )


if __name__ == "__main__":
    main()

