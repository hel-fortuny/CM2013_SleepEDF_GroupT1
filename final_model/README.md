# Final model registration package

Repository: https://github.com/hel-fortuny/CM2013_SleepEDF_GroupT1
Target branch: `vincent`.

This package contains the supplied final weights, their original JSON records,
and a byte-for-byte copy of the supplied Colab notebook. The notebook was not
edited. MODEL_MANIFEST.json records file digests and the local integrity checks.
The GitHub connector returned 404, so no remote commit has been created.

## Commit 1: freeze the model

Extract this ZIP. Add the `final_model/` directory to branch `vincent` in the
existing team repository, keeping the existing repository files and history.
Commit it, for example with the message:
`Freeze final CNN1 F2 Transformer5 model and weights`.

Copy the full 40-character SHA of this model commit. The notebook's original
Drive DATA path is retained. The weights in this package are exact copies of
the weights already used by that notebook. The notebook needs the development
caches for its historical checks; those data caches are not included here.

## Commit 2: register the expected score

Open `registration/EXPECTED_SCORE.template.md`. Replace the single
`REPLACE_WITH_FULL_40_CHARACTER_MODEL_COMMIT_SHA` placeholder with the SHA
from commit 1. Save the completed file as `EXPECTED_SCORE.md` at the repository
root and commit it on `vincent`. If an EXPECTED_SCORE.md already exists, inspect
it before updating it. Do not insert the professor's course revision as the
final model SHA.

The template reports kappa 0.7787 ± 0.0174 across the five participant folds.
The unfilled template itself is not a completed registration. Verify that the
completed EXPECTED_SCORE.md and both commits are visible in GitHub before
performing hold-out prediction.

## Results record

Append/adapt `registration/RESULTS_FINAL_MODEL_SNIPPET.md` into the existing
team RESULTS.md without deleting the experiment history or classmates' work.
The package does not replace or consolidate the other team members' results.

## After registration

Keep all training switches False. The existing notebook definitions in 6.4
and 6.5 reload the frozen pipeline and provide FusionSleepEDFTrack68, which
uses the official write_submission method and preserves original epoch times.
Hold-out execution should call those frozen definitions on the published
hold-out recordings. Verify coverage of every eligible epoch, including Wake.
The final hold-out execution call and its registration check still need to be
prepared; this package does not generate predictions.csv.

Do not crop the hold-out using expert labels. Optional hold-out metrics must
be computed from the one frozen prediction set, with no subsequent tuning.

The other team members' notebooks can remain on their own branches, linked
from the team README/RESULTS. They are not required to load this final model.
