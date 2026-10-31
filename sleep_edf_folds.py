"""Fixed subject-wise cross-validation splits for Sleep-EDF.

Shared across all preprocessing experiments (EXP-00 to EXP-04).
The 10 final holdout subjects are excluded from cross-validation.
"""

import numpy as np


# Fixed TEST subjects for each fold (proposed by Vicente).
# TRAIN = all remaining development subjects.
FOLDS_68 = {
    "A": [
        "SC400", "SC405", "SC411", "SC417",
        "SC422", "SC428", "SC434", "SC441",
        "SC446", "SC452", "SC458", "SC463",
        "SC471", "SC477",
    ],
    "B": [
        "SC401", "SC406", "SC412", "SC418",
        "SC423", "SC429", "SC435", "SC442",
        "SC447", "SC453", "SC459", "SC465",
        "SC473", "SC481",
    ],
    "C": [
        "SC402", "SC407", "SC413", "SC419",
        "SC425", "SC430", "SC436", "SC443",
        "SC449", "SC454", "SC460", "SC466",
        "SC474", "SC482",
    ],
    "D": [
        "SC403", "SC409", "SC414", "SC420",
        "SC426", "SC431", "SC437", "SC444",
        "SC450", "SC455", "SC461", "SC467",
        "SC475",
    ],
    "E": [
        "SC404", "SC410", "SC415", "SC421",
        "SC427", "SC433", "SC438", "SC445",
        "SC451", "SC457", "SC462", "SC470",
        "SC476",
    ],
}

HOLDOUT_GROUPS = {
    "SC408", "SC416", "SC424", "SC432", "SC440",
    "SC448", "SC456", "SC464", "SC472", "SC480",
}

DEVELOPMENT_GROUPS_68 = sorted(
    subject
    for subjects in FOLDS_68.values()
    for subject in subjects
)

# Validate the shared fold definition.
assert len(FOLDS_68) == 5
assert len(DEVELOPMENT_GROUPS_68) == 68
assert len(set(DEVELOPMENT_GROUPS_68)) == 68
assert not (set(DEVELOPMENT_GROUPS_68) & HOLDOUT_GROUPS)


def fixed_sleep_edf_folds(groups):
    """Yield (train_indices, test_indices) for the five fixed folds.

    groups: one subject ID per epoch, aligned with X and y.
    """
    groups = np.asarray(groups)

    actual = set(groups.tolist())
    expected = set(DEVELOPMENT_GROUPS_68)

    if actual != expected:
        raise ValueError(
            "Dataset subjects do not match the fixed 68-subject split.\n"
            f"Missing: {sorted(expected - actual)}\n"
            f"Unexpected: {sorted(actual - expected)}"
        )

    for fold_name, test_subjects in FOLDS_68.items():
        test_mask = np.isin(groups, test_subjects)

        train_indices = np.flatnonzero(~test_mask)
        test_indices = np.flatnonzero(test_mask)

        yield train_indices, test_indices
