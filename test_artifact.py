import unittest

from analyze import load_scores, summarize


class ArtifactTest(unittest.TestCase):
    def test_headline_result_is_computed_from_rows(self):
        scores = load_scores()
        ranking = dict(summarize(scores))
        self.assertAlmostEqual(ranking["rep1"], 76.954907, places=6)
        self.assertAlmostEqual(ranking["ablate_raw_cost"], 75.346577, places=6)
        self.assertTrue(
            all(
                scores["rep1"][model] > scores["ablate_raw_cost"][model]
                for model in scores["rep1"]
            )
        )

if __name__ == "__main__":
    unittest.main()
