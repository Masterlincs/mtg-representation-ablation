# MTG embedding representation ablation

Results from the representation-ablation part of a larger MTG embeddings project. The main project is still a heavy work in progress.

## Result

18 representations were tested over 32,151 cards. Five embedding models completed every variant.

| Representation | Mean score |
| --- | ---: |
| Oracle text only | 70.920 |
| Labelled, expanded prose | 66.767 |
| Raw mana cost + oracle text | 75.347 |
| Raw cost + stats + keywords + oracle text (`rep1`) | 76.955 |

Compact MTG notation performed best on this benchmark. `rep1` beat the previous best representation on all five overlapping models by 1.18–1.96 points.

## Verify

```bash
python analyze.py
python -m unittest
```

The repo contains the reported scores and code to recompute the headline comparison. It does not contain the card corpus, model weights, embeddings, or the full experiment pipeline.

## Limitations

- The same benchmark was used to choose and report `rep1`.
- The metric weights were chosen manually.
- The verbose formatter joined adjacent expanded mana symbols without spaces, weakening that comparison.
- Two registered models failed during the original ablation, leaving five complete models.
- There is no held-out human-rated evaluation.

The result is benchmark-specific. The next useful test is a frozen comparison on a human-rated similarity set.
