# Results log — Sleep-EDF, Team T1

**Track:** sleep_edf  
**Split unit:** subject  
**Primary metric:** Cohen's kappa  
**Evaluation mode:** new-subject  
**Team:** Vicente Soares, Helena Fortuny, Dalya Yousif

## Iteration log

| # | Date | What changed and why | Primary metric with spread | Better than previous? | Decision | Code revision |
|---|---|---|---|---|---|---|
| 1 | 2026-10-22 | Ran the supplied baseline on real Sleep-EDF recordings from three subjects, without changing preprocessing, features or classification, to establish an initial reference. | Mean subject kappa 0.720 (SD 0.119; range 0.589–0.822; 3 subjects / 3 LOSO folds). | Initial real-data baseline. | Retain as the reference for this three-subject cohort; establish a larger development cohort before substantive model selection. | Course source: `5949b723bbd34d172f072446dfcb802ef54b49f7`. Team notebook/log commit has not yet been recorded. |

The code revision above identifies the instructor's source used in Colab. It is not the team's experiment commit. Add the team commit after saving the executed notebook and this log in the team repository.

## Iteration 1 — initial real-data baseline

### Purpose and run provenance

- Executed by Vicente in Google Colab on 2026-10-22.
- Notebook: a personal copy of `notebooks/track_sleep_edf.ipynb`.
- Course repository: https://github.com/farhad-abtahi/CM2013
- Course revision: [5949b723bbd34d172f072446dfcb802ef54b49f7](https://github.com/farhad-abtahi/CM2013/tree/5949b723bbd34d172f072446dfcb802ef54b49f7).
- A synthetic smoke test was completed before this run; synthetic results are excluded from the real-data comparison.
- Goal: establish the unchanged real-data baseline and inspect class and subject variability.
- No numerical performance prediction was recorded in this log before this initial run.
- Values below are transcribed from the supplied Colab outputs, rounded to the precision printed by the notebook.

### Data and loading

- Dataset: Sleep-EDF Expanded, version 1.0.0, Sleep-Cassette recordings.
- Download source: PhysioNet's official AWS mirror, selected by the course downloader.
- Requested subject indices: `[0, 1, 2]`.
- Loaded subjects: `SC400`, `SC401`, `SC402`.
- Recordings: 6, with both nights from each subject.
- Epoch duration: 30 seconds; default target sampling rate: 100 Hz.
- Label mapping uses the supplied loader: old stages 3 and 4 are combined as N3; Movement/Unknown epochs are excluded.
- No additional Wake cropping or epoch exclusion was introduced by the team.
- Total retained epochs: **16,688**.
- Features per epoch: **11**.
- `track.assert_no_holdout(recs)` ran successfully.
- This run contains only the three development subjects above; no hold-out prediction or scoring operation is part of this logged work.

| Subject | PSG record IDs |
|---|---|
| SC400 | SC4001E0, SC4002E0 |
| SC401 | SC4011E0, SC4012E0 |
| SC402 | SC4021E0, SC4022E0 |

| Reference stage | Epochs | Share, as printed |
|---|---:|---:|
| W | 11,340 | 68.0% |
| N1 | 596 | 3.6% |
| N2 | 2,792 | 16.7% |
| N3 | 932 | 5.6% |
| REM | 1,028 | 6.2% |

Percentages are rounded and may not sum to exactly 100%.

### Pipeline and validation

- Data mode: `USE_REAL = True`.
- Track construction: `track = SleepEDFTrack()`, with no custom configuration.
- Dataset construction: `X, y, groups = track.build_dataset(recs)`.
- Evaluation: `rep = track.evaluate(X, y, groups)`.
- Preprocessing and the 11 supplied features were unchanged. The default preprocessing is identity, and the default spectral estimator is Welch.
- The supplied classifier and feature-selection settings were retained as the reference; no alternative configuration has been evaluated on this real-data cohort.
- Protocol: leave-one-subject-out (LOSO), 3 folds. Each fold trains on two subjects and evaluates on the third.
- Both nights of a subject stay in the same fold. The evaluation harness checks subject separation and fits selection/classifier steps within each training fold.
- No team-added learned transformation was fitted across all recordings.
- Raw data are kept under `/content/drive/MyDrive/CM2013_data/train`.
- `load_cached()` was used for parsed recordings. Separate preprocessing/feature caches have not yet been configured.

### Results

| Metric | Value | Aggregation |
|---|---:|---|
| Cohen's kappa | 0.729 | Pooled out-of-fold predictions |
| Macro-F1 | 0.622 | Pooled out-of-fold predictions |
| Accuracy | 0.868 | Pooled out-of-fold predictions |
| Mean Cohen's kappa | 0.720 | Unweighted mean across the 3 held-out subjects |
| SD of Cohen's kappa | 0.119 | Across the 3 held-out subjects |
| Minimum Cohen's kappa | 0.589 | Lowest subject score |
| Maximum Cohen's kappa | 0.822 | Highest subject score |

The pooled kappa (0.729) and the mean subject kappa (0.720) use different aggregations and must not be interchanged. In this three-fold LOSO run, each fold corresponds to one held-out subject.

Exact harness summary:

```text
mean cohens_kappa 0.720 (sd 0.119, range 0.589-0.822 across 3 subjects)
```

The row-normalized confusion matrix was inspected in the notebook. The following recalls are approximate readings of its rounded diagonal, not exact exported per-class statistics:

| Reference stage | Approximate recall |
|---|---:|
| W | 97% |
| N1 | 20% |
| N2 | 91% |
| N3 | 34% |
| REM | 54% |

Observed errors in the rounded matrix:
- N1: approximately 34% predicted as W and 34% as N2.
- N3: approximately 35% predicted as W and 31% as N2.
- REM: approximately 39% predicted as N2.

### Interpretation and decision

Wake represents about 68% of the epochs; predicting W for every epoch would therefore achieve about 68% accuracy. The baseline's 86.8% accuracy should be read alongside kappa, macro-F1 and per-stage recall. Performance is much stronger on W and N2 than on N1 and N3 in this cohort.

This is an initial reference on only three subjects. It does not establish performance across the wider Sleep-EDF population. Class imbalance is an observed property; it has not been demonstrated to be the sole cause of the class errors.

**Decision:** preserve this baseline and its cohort for traceability. Set the development cohort and comparison plan before testing model changes. A run on a larger cohort must receive a separate log entry; compare alternatives with a baseline evaluated on that same cohort.

## Decision log

| Module | Current choice | Rationale | Alternatives tested so far |
|---|---|---|---|
| Loading | Three real subjects, both nights, persistent data and parsed cache | Initial check of the real-data pipeline and subject grouping | None |
| Preprocessing | Supplied default, unchanged | Preserve the original reference | None |
| Features | Supplied 11-feature set, unchanged | Preserve the original reference | None |
| Feature selection / classification | Supplied defaults, fitted within folds by the harness | Measure baseline behavior before selecting alternatives | None |
| Inference / reporting | LOSO out-of-fold predictions; pooled metrics and subject spread; row-normalized confusion matrix | Examine class errors and variability between subjects | None |

## Revisions

No earlier modeling decision has yet been revised following a later result. Record a genuine revision, its triggering observation and its measured effect when one occurs.

## Contributions recorded so far

| Iteration | Person | Observed work | Review |
|---|---|---|---|
| 1 | Vicente Soares | Set up the Colab copy and persistent data folder; executed synthetic and real baseline cells; supplied metrics, class counts, confusion matrix and source revision. Setup and log preparation were assisted by ChatGPT. | Peer review not yet recorded. |

Contributions from other team members will be added when their actual work is documented.

## Next steps and missing evidence

- Save the executed notebook and this log in the team repository and record the team commit.
- Capture the runtime dependency versions and export exact per-subject/per-class results and the numerical confusion matrix.
- Add versioned caching for slow per-recording steps before repeated experiments.
- Define the development cohort and either a separate development set or a fixed comparison budget before testing alternatives.
- Record future hypotheses before running each comparison.
- Final pipeline selection, a genuine revised decision, EXPECTED_SCORE.md registration and final hold-out inference are still future stages.





## Experiment: C1_68_crop30_fixed_AE

**Date:** 2026-11-12

**Configuration**
- Subjects: 68
- Wake cropping: 30 minutes
- Validation: 5 fixed subject-wise folds (A-E)

**Results**

| Metric | Value |
|---|---:|
| Accuracy | 0.866 |
| Cohen's kappa | 0.724 |
| Macro-F1 | 0.657 |
| Balanced accuracy | 0.643 |
| Mean fold kappa | 0.724 |
| SD fold kappa | 0.022 |

**Kappa by fold**

- Fold A: 0.745
- Fold B: 0.689
- Fold C: 0.725
- Fold D: 0.726
- Fold E: 0.737

**Saved outputs**
- `experiments\C2_68_crop30_fixed_AE.json`
- `experiments\C2_68_crop30_fixed_AE_confusion.png`
- Five fold JSON reports (A-E)

---



## Experiment: C3_68_crop30_fixed_AE

**Date:** 2026-11-13

**Configuration**
- Subjects: 68
- Wake cropping: 30 minutes
- Validation: 5 fixed subject-wise folds (A-E)

**Results**

| Metric | Value |
|---|---:|
| Accuracy | 0.866 |
| Cohen's kappa | 0.724 |
| Macro-F1 | 0.659 |
| Balanced accuracy | 0.647 |
| Mean fold kappa | 0.724 |
| SD fold kappa | 0.022 |

**Kappa by fold**

- Fold A: 0.747
- Fold B: 0.692
- Fold C: 0.720
- Fold D: 0.722
- Fold E: 0.742

**Saved outputs**
- `experiments\C3_68_crop30_fixed_AE.json`
- `experiments\C3_68_crop30_fixed_AE_confusion.png`
- Five fold JSON reports (A-E)

---



## Experiment: C4_68_crop30_LP40_fixed_AE

**Date:** 2026-11-13

**Configuration**
- Subjects: 68
- Wake cropping: 30 minutes
- Validation: 5 fixed subject-wise folds (A-E)

**Results**

| Metric | Value |
|---|---:|
| Accuracy | 0.866 |
| Cohen's kappa | 0.724 |
| Macro-F1 | 0.660 |
| Balanced accuracy | 0.649 |
| Mean fold kappa | 0.725 |
| SD fold kappa | 0.022 |

**Kappa by fold**

- Fold A: 0.744
- Fold B: 0.691
- Fold C: 0.719
- Fold D: 0.724
- Fold E: 0.744

**Saved outputs**
- `experiments\C4_68_crop30_LP40_fixed_AE.json`
- `experiments\C4_68_crop30_LP40_fixed_AE_confusion.png`
- Five fold JSON reports (A-E)

---



## Experiment: C5_68_crop30_LP40_balanced_subsample_fixed_AE

**Date:** 2026-11-13

**Configuration**
- Subjects: 68
- Wake cropping: 30 minutes
- Validation: 5 fixed subject-wise folds (A-E)

**Results**

| Metric | Value |
|---|---:|
| Accuracy | 0.866 |
| Cohen's kappa | 0.724 |
| Macro-F1 | 0.660 |
| Balanced accuracy | 0.649 |
| Mean fold kappa | 0.724 |
| SD fold kappa | 0.022 |

**Kappa by fold**

- Fold A: 0.744
- Fold B: 0.691
- Fold C: 0.719
- Fold D: 0.724
- Fold E: 0.744

**Saved outputs**
- `experiments\C5_68_crop30_LP40_balanced_subsample_fixed_AE.json`
- `experiments\C5_68_crop30_LP40_balanced_subsample_fixed_AE_confusion.png`
- Five fold JSON reports (A-E)

---



## Experiment: C6_68_crop30_LP40_no_balance_fixed_AE

**Date:** 2026-11-13

**Configuration**
- Subjects: 68
- Wake cropping: 30 minutes
- Validation: 5 fixed subject-wise folds (A-E)

**Results**

| Metric | Value |
|---|---:|
| Accuracy | 0.866 |
| Cohen's kappa | 0.725 |
| Macro-F1 | 0.665 |
| Balanced accuracy | 0.658 |
| Mean fold kappa | 0.726 |
| SD fold kappa | 0.019 |

**Kappa by fold**

- Fold A: 0.743
- Fold B: 0.695
- Fold C: 0.724
- Fold D: 0.726
- Fold E: 0.742

**Saved outputs**
- `experiments\C6_68_crop30_LP40_no_balance_fixed_AE.json`
- `experiments\C6_68_crop30_LP40_no_balance_fixed_AE_confusion.png`
- Five fold JSON reports (A-E)

---



## Experiment: C7_68_crop30_LP40_14features_no_balance_fixed_AE

**Date:** 2026-11-13

**Configuration**
- Subjects: 68
- Wake cropping: 30 minutes
- Validation: 5 fixed subject-wise folds (A-E)

**Results**

| Metric | Value |
|---|---:|
| Accuracy | 0.867 |
| Cohen's kappa | 0.727 |
| Macro-F1 | 0.665 |
| Balanced accuracy | 0.658 |
| Mean fold kappa | 0.728 |
| SD fold kappa | 0.024 |

**Kappa by fold**

- Fold A: 0.745
- Fold B: 0.689
- Fold C: 0.728
- Fold D: 0.727
- Fold E: 0.750

**Saved outputs**
- `experiments\C7_68_crop30_LP40_14features_no_balance_fixed_AE.json`
- `experiments\C7_68_crop30_LP40_14features_no_balance_fixed_AE_confusion.png`
- Five fold JSON reports (A-E)

---



## Experiment: C8_68_crop30_LP40_relativebands_no_balance_fixed_AE

**Date:** 2026-11-13

**Configuration**
- Subjects: 68
- Wake cropping: 30 minutes
- Validation: 5 fixed subject-wise folds (A-E)

**Results**

| Metric | Value |
|---|---:|
| Accuracy | 0.870 |
| Cohen's kappa | 0.733 |
| Macro-F1 | 0.670 |
| Balanced accuracy | 0.664 |
| Mean fold kappa | 0.733 |
| SD fold kappa | 0.024 |

**Kappa by fold**

- Fold A: 0.756
- Fold B: 0.696
- Fold C: 0.731
- Fold D: 0.730
- Fold E: 0.753

**Saved outputs**
- `experiments\C8_68_crop30_LP40_relativebands_no_balance_fixed_AE.json`
- `experiments\C8_68_crop30_LP40_relativebands_no_balance_fixed_AE_confusion.png`
- Five fold JSON reports (A-E)

---



## Experiment: C9_68_crop30_LP40_relative_no_activity_no_balance_fixed_AE

**Date:** 2026-11-13

**Configuration**
- Subjects: 68
- Wake cropping: 30 minutes
- Validation: 5 fixed subject-wise folds (A-E)

**Results**

| Metric | Value |
|---|---:|
| Accuracy | 0.857 |
| Cohen's kappa | 0.706 |
| Macro-F1 | 0.627 |
| Balanced accuracy | 0.619 |
| Mean fold kappa | 0.707 |
| SD fold kappa | 0.030 |

**Kappa by fold**

- Fold A: 0.739
- Fold B: 0.667
- Fold C: 0.692
- Fold D: 0.703
- Fold E: 0.732

**Saved outputs**
- `experiments\C9_68_crop30_LP40_relative_no_activity_no_balance_fixed_AE.json`
- `experiments\C9_68_crop30_LP40_relative_no_activity_no_balance_fixed_AE_confusion.png`
- Five fold JSON reports (A-E)

---



## Experiment: C10_68_crop30_LP40_relative_no_entropy_no_balance_fixed_AE

**Date:** 2026-11-13

**Configuration**
- Subjects: 68
- Wake cropping: 30 minutes
- Validation: 5 fixed subject-wise folds (A-E)

**Results**

| Metric | Value |
|---|---:|
| Accuracy | 0.867 |
| Cohen's kappa | 0.728 |
| Macro-F1 | 0.667 |
| Balanced accuracy | 0.662 |
| Mean fold kappa | 0.729 |
| SD fold kappa | 0.022 |

**Kappa by fold**

- Fold A: 0.750
- Fold B: 0.692
- Fold C: 0.731
- Fold D: 0.727
- Fold E: 0.743

**Saved outputs**
- `experiments\C10_68_crop30_LP40_relative_no_entropy_no_balance_fixed_AE.json`
- `experiments\C10_68_crop30_LP40_relative_no_entropy_no_balance_fixed_AE_confusion.png`
- Five fold JSON reports (A-E)

---



## Experiment: C11_68_crop30_selectiveLP40_absolute_balanced_fixed_AE

**Date:** 2026-11-17

**Configuration**
- Subjects: 68
- Wake cropping: 30 minutes
- Validation: 5 fixed subject-wise folds (A-E)

**Results**

| Metric | Value |
|---|---:|
| Accuracy | 0.871 |
| Cohen's kappa | 0.734 |
| Macro-F1 | 0.667 |
| Balanced accuracy | 0.656 |
| Mean fold kappa | 0.735 |
| SD fold kappa | 0.024 |

**Kappa by fold**

- Fold A: 0.754
- Fold B: 0.696
- Fold C: 0.734
- Fold D: 0.736
- Fold E: 0.755

**Saved outputs**
- `experiments\C11_68_crop30_selectiveLP40_absolute_balanced_fixed_AE.json`
- `experiments\C11_68_crop30_selectiveLP40_absolute_balanced_fixed_AE_confusion.png`
- Five fold JSON reports (A-E)

---



## Experiment: C11b_68_crop30_selectiveLP40_absolute_no_balance_fixed_AE

**Date:** 2026-11-17

**Configuration**
- Subjects: 68
- Wake cropping: 30 minutes
- Validation: 5 fixed subject-wise folds (A-E)

**Results**

| Metric | Value |
|---|---:|
| Accuracy | 0.871 |
| Cohen's kappa | 0.735 |
| Macro-F1 | 0.670 |
| Balanced accuracy | 0.663 |
| Mean fold kappa | 0.735 |
| SD fold kappa | 0.023 |

**Kappa by fold**

- Fold A: 0.755
- Fold B: 0.698
- Fold C: 0.735
- Fold D: 0.734
- Fold E: 0.753

**Saved outputs**
- `experiments\C11b_68_crop30_selectiveLP40_absolute_no_balance_fixed_AE.json`
- `experiments\C11b_68_crop30_selectiveLP40_absolute_no_balance_fixed_AE_confusion.png`
- Five fold JSON reports (A-E)

---



## Experiment: C12_68_crop30_selectiveLP40_relative_prev1_no_balance_fixed_AE

**Date:** 2026-11-17

**Configuration**
- Subjects: 68
- Wake cropping: 30 minutes
- Validation: 5 fixed subject-wise folds (A-E)

**Results**

| Metric | Value |
|---|---:|
| Accuracy | 0.881 |
| Cohen's kappa | 0.754 |
| Macro-F1 | 0.692 |
| Balanced accuracy | 0.682 |
| Mean fold kappa | 0.755 |
| SD fold kappa | 0.026 |

**Kappa by fold**

- Fold A: 0.780
- Fold B: 0.717
- Fold C: 0.754
- Fold D: 0.745
- Fold E: 0.777

**Saved outputs**
- `experiments\C12_68_crop30_selectiveLP40_relative_prev1_no_balance_fixed_AE.json`
- `experiments\C12_68_crop30_selectiveLP40_relative_prev1_no_balance_fixed_AE_confusion.png`
- Five fold JSON reports (A-E)

---



## Experiment: C13_68_crop30_selectiveLP40_relative_prev1next1_no_balance_fixed_AE

**Date:** 2026-11-17

**Configuration**
- Subjects: 68
- Wake cropping: 30 minutes
- Validation: 5 fixed subject-wise folds (A-E)

**Results**

| Metric | Value |
|---|---:|
| Accuracy | 0.882 |
| Cohen's kappa | 0.757 |
| Macro-F1 | 0.694 |
| Balanced accuracy | 0.684 |
| Mean fold kappa | 0.757 |
| SD fold kappa | 0.026 |

**Kappa by fold**

- Fold A: 0.785
- Fold B: 0.724
- Fold C: 0.754
- Fold D: 0.743
- Fold E: 0.782

**Saved outputs**
- `experiments\C13_68_crop30_selectiveLP40_relative_prev1next1_no_balance_fixed_AE.json`
- `experiments\C13_68_crop30_selectiveLP40_relative_prev1next1_no_balance_fixed_AE_confusion.png`
- Five fold JSON reports (A-E)

---



## Experiment: C14_68_crop30_selectiveLP40_relative_recnorm_prev1_no_balance_fixed_AE

**Date:** 2026-11-19

**Configuration**
- Subjects: 68
- Wake cropping: 30 minutes
- Validation: 5 fixed subject-wise folds (A-E)

**Results**

| Metric | Value |
|---|---:|
| Accuracy | 0.877 |
| Cohen's kappa | 0.745 |
| Macro-F1 | 0.664 |
| Balanced accuracy | 0.649 |
| Mean fold kappa | 0.745 |
| SD fold kappa | 0.012 |

**Kappa by fold**

- Fold A: 0.749
- Fold B: 0.729
- Fold C: 0.743
- Fold D: 0.742
- Fold E: 0.763

**Saved outputs**
- `experiments\C14_68_crop30_selectiveLP40_relative_recnorm_prev1_no_balance_fixed_AE.json`
- `experiments\C14_68_crop30_selectiveLP40_relative_recnorm_prev1_no_balance_fixed_AE_confusion.png`
- Five fold JSON reports (A-E)

---



## Experiment: C15_68_crop30_selectiveLP40_relative_prev1_hmm_no_balance_fixed_AE

**Date:** 2026-11-19

**Configuration**
- Subjects: 68
- Wake cropping: 30 minutes
- Validation: 5 fixed subject-wise folds (A-E)

**Results**

| Metric | Value |
|---|---:|
| Accuracy | 0.857 |
| Cohen's kappa | 0.723 |
| Macro-F1 | 0.689 |
| Balanced accuracy | 0.743 |
| Mean fold kappa | 0.723 |
| SD fold kappa | 0.016 |

**Kappa by fold**

- Fold A: 0.721
- Fold B: 0.705
- Fold C: 0.718
- Fold D: 0.720
- Fold E: 0.750

**Saved outputs**
- `experiments\C15_68_crop30_selectiveLP40_relative_prev1_hmm_no_balance_fixed_AE.json`
- `experiments\C15_68_crop30_selectiveLP40_relative_prev1_hmm_no_balance_fixed_AE_confusion.png`
- Five fold JSON reports (A-E)

---

