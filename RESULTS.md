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
| 2 (B0) | 2026-10-22 | Expanded the development cohort to eight subjects and reran the unchanged supplied baseline before testing alternatives. | Mean subject kappa 0.824 (SD 0.068; range 0.710–0.896; 8 subjects / 8 LOSO folds). | Not a controlled improvement over iteration 1: the cohort and training-set size changed. | Use as the reference for the fixed eight-subject comparison cohort. | Course source: `5949b723bbd34d172f072446dfcb802ef54b49f7`; personal notebook / team commit not yet recorded. |
| 3 (F1) | 2026-10-22 | Replaced only the five absolute EEG band powers with per-epoch relative powers; retained the other six features and all evaluation settings. | Mean subject kappa 0.828 (SD 0.054; range 0.730–0.885; same 8 subjects / 8 LOSO folds). | Small observed gain vs B0: mean subject kappa +0.004; pooled macro-F1 +0.007, from rounded reported values. | Prefer F1 provisionally after paired/class inspection; keep the B0 reference and document the participant/REM trade-offs. | Course source unchanged; feature transformation supplied in the Colab cell; personal experiment commit not yet recorded. |
| 4 (F2) | 2026-10-22 | Kept the 11 original features and appended only the five per-epoch relative EEG band powers, producing 16 features; same eight-subject evaluation and classifier configuration. | Mean subject kappa 0.837 (SD 0.052; range 0.758–0.897; 8 subjects / 8 LOSO folds). | Highest reported aggregate scores so far: mean subject kappa +0.009 and pooled macro-F1 +0.004 vs F1, from printed values. | Adopt F2 as the development working reference after paired/class/confusion inspection; retain the N1 trade-off. | Course source unchanged; combined-feature construction in Colab; personal experiment commit not yet recorded. |
| 5 (C1) | 2026-10-27 | Cropped training nights to the first–last sleep-labelled epoch plus 30 minutes on each side; retained F2's 16 features and RF. Each held-out subject was evaluated on all original epochs. | Mean subject kappa 0.813 (SD 0.051; range 0.714–0.878; same 8 subjects / 8 LOSO folds). | Lower primary metric than F2 by 0.024; N1 F1 improves from 0.354 to 0.391, while pooled macro-F1 falls from 0.762 to 0.758. | Do not replace F2 with C1 under the declared primary metric. Preserve the minority-recall gains and precision/Wake trade-offs. | Course source unchanged; custom training-only crop/LOSO cell executed in Colab; personal experiment commit not yet recorded. |
| 6 (P1) | 2026-10-27 | Added EEG-only Butterworth low-pass (single-pass order 4, Wn=35 Hz, forward-backward SOS, odd padding per epoch); recomputed F2's 16 features, retaining all epochs, the same LOSO folds and classifier. | Mean subject kappa 0.833 (SD 0.054; range 0.749–0.895; same 8 subjects / 8 LOSO folds). | Small observed loss vs F2: mean subject kappa -0.004 and pooled macro-F1 -0.005; seven subjects worsen and one improves. | Retain F2 after aggregate, class, paired subject and confusion review; P1 increases the displayed N1-to-W confusion. | Course source unchanged; reusable feature helper, versioned per-recording caches and P1 evaluation executed in Colab; P1 JSON save confirmed; personal experiment commit not yet recorded. |

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

## Iteration 2 (B0) — fixed eight-subject development baseline

This is Vicente's individual development attempt, to be discussed with the team. The team's final pipeline has not been selected.

### Cohort and comparison plan

Before testing any modeling alternative, the development cohort was fixed to subject indices `[0, 1, 2, 3, 4, 5, 6, 7]` and the comparison budget to at most **12 configurations, including this baseline**. This choice was stated in the Colab instructions before the eight-subject baseline was evaluated; a repository commit recording the plan is still pending. The earlier three-subject run remains a pilot and is outside this comparison budget.

- Subjects: `SC400`, `SC401`, `SC402`, `SC403`, `SC404`, `SC405`, `SC406`, `SC407`.
- Recordings: **16**, two nights per subject, confirmed by the loader output.
- Retained epochs: **44,303**.
- Features: **11**.
- Protocol: **8-fold leave-one-subject-out**, split unit **subject**, evaluation mode **new-subject**. Each fold trains on seven subjects; both nights of the remaining subject are evaluated together.
- Data mode: real Sleep-EDF data; persistent folder `/content/drive/MyDrive/CM2013_data/train`.
- Parsed-record cache reported by Colab: `_cache_SleepEDFTrack_c036dc141386.pkl`.
- Label mapping, epoch inclusion and sampling rate follow the unchanged course loader. No additional cropping was introduced.
- None of these subjects belongs to the published hold-out set. No hold-out prediction or scoring is included in this development run.

### Unchanged pipeline and provenance

- Course revision: `5949b723bbd34d172f072446dfcb802ef54b49f7`.
- Configuration: `BASELINE_CONFIG = {}`; supplied defaults.
- Preprocessing: identity.
- Features: five absolute EEG band powers (delta 0.5–4, theta 4–8, alpha 8–11, sigma 11–16, beta 16–30 Hz), three EEG Hjorth parameters, EEG spectral entropy, EOG movement and EMG RMS.
- Band-power estimator: the supplied Welch implementation, with `nperseg=min(epoch_length, 256)`; the diagnostic plots' 8-second Welch windows did not alter model features.
- Classifier: supplied pipeline with `StandardScaler` followed by a 200-tree random forest, `class_weight="balanced"`, seed 0.
- The scaler and classifier are fitted inside each training fold by the evaluator. No learned transform is fitted to the combined development cohort.
- Evaluation code: `X8, y8, groups8 = track.build_dataset(recs)` and `rep8 = track.evaluate(X8, y8, groups8)`.
- Feature matrix `X8` is available in the active Colab runtime for reuse; a separate persistent preprocessing/feature cache is not yet implemented.

Runtime versions printed in the same Colab workflow before this run:

```json
{"imbalanced-learn": "0.14.2", "matplotlib": "3.10.0", "mne": "1.13.2", "numpy": "2.1.3", "python": "3.13.16", "scikit-learn": "1.6.1", "scipy": "1.16.3"}
```

These are not retrospectively assigned to the earlier three-subject run, whose runtime was not captured at execution.

### Reported results

The following rounded values were supplied by Vicente from the executed Colab cell on 2026-10-22. They were not independently recomputed here.

| Metric | Value | Aggregation |
|---|---:|---|
| Mean Cohen's kappa | **0.824** | Unweighted across 8 held-out subjects / LOSO folds |
| SD of Cohen's kappa | **0.068** | Across the same 8 subjects |
| Minimum Cohen's kappa | 0.710 | Lowest subject score |
| Maximum Cohen's kappa | 0.896 | Highest subject score |
| Cohen's kappa | 0.825 | Pooled out-of-fold predictions |
| Macro-F1 | 0.751 | Pooled out-of-fold predictions |
| Accuracy | 0.917 | Pooled out-of-fold predictions |

Exact printed summary:

```text
mean cohens_kappa 0.824 (sd 0.068, range 0.710-0.896 across 8 subjects)
```

The eight-subject class counts, per-class reports and paired subject scores were subsequently supplied for B0 and F1 (see iteration 3). Numerical confusion matrices are still pending. The earlier pilot's 68% Wake share and rounded confusion matrix must not be copied to this cohort.

### Interpretation and decision

The score is higher than in the three-subject pilot, but both the evaluated cohort and the number of training subjects per fold changed. This is **not evidence of a pipeline improvement**. Alternatives will be compared against B0 using these same eight subjects, epochs, folds and evaluation settings.

**Decision:** retain B0 as the fixed-cohort reference. No modeling alternative has yet been evaluated. The limited development cohort and repeated comparisons still limit the strength of generalization claims; the reserved hold-out remains untouched.

## Development inspection — observations before the first feature experiment

One deterministic example per available stage was plotted for each of `SC4001E0`, `SC4011E0` and `SC4021E0`: the middle retained epoch of that stage, EEG Fpz-Cz, at 100 Hz. The diagnostic showed raw time traces and Welch PSDs with 8-second windows, 50% overlap and no added filtering.

- The displayed N3 epochs have prominent slow activity. Low-frequency power cannot automatically be treated as unwanted drift.
- Amplitudes and spectral shapes vary between the displayed epochs and participants.
- In `SC4021E0`, both the N1 and N2 examples show a peak near 15 Hz; a single peak is not a reliable standalone stage rule.
- These are illustrative epochs from three nights, not a comprehensive artifact or powerline-noise assessment of all 16 recordings. No filter was selected on this evidence alone.

## Iteration 3 (F1) — relative EEG band powers

**Status: executed by Vicente; aggregate metrics, paired subject scores and per-class reports supplied. F1 selected as a provisional working reference after inspection.**

Replace the five absolute EEG band-power features with relative powers, keeping the other six features, Welch settings, epochs, subject folds, seed, scaling and classifier unchanged. The feature count stays at 11.

For each epoch independently:

`relative_power[band] = absolute_power[band] / sum(absolute_power[delta, theta, alpha, sigma, beta])`

The denominator covers 0.5–30 Hz under the supplied band definitions. If all five powers are zero, encode all five relative powers as zero. Reject non-finite or negative input powers. The transformation uses neither labels nor statistics from other epochs or participants; the learned scaler continues to be fitted inside each training fold.

**Directional prediction recorded before this comparison:** relative powers may improve mean subject kappa and macro-F1 by reducing dependence on absolute EEG amplitude. They may also lose useful absolute-power information, so improvement is uncertain. The illustrative plots motivate the hypothesis; they do not establish its mechanism.

Use the existing `X8` matrix to derive this candidate without downloading, parsing or recomputing the original features. Keep `X8` unchanged. Compare the subject-level results in paired form and inspect the per-class panel before deciding whether to retain F1; a small change in the pooled score alone will not establish a benefit. Future inference must implement the same feature transformation as training if this candidate is selected.

### Reported F1 results and comparison with B0

Vicente supplied the following Colab output on 2026-10-22 after executing the predeclared relative-power comparison. This records the reported run, not a separate rerun. The same `y8` and `groups8` were reused with `X8_rel`; all 44,303 epochs and 11 feature columns remain represented.

| Metric | B0: absolute powers | F1: relative powers | Difference from printed values |
|---|---:|---:|---:|
| Mean subject kappa | 0.824 | **0.828** | +0.004 |
| SD of subject kappa | 0.068 | **0.054** | -0.014 |
| Minimum subject kappa | 0.710 | 0.730 | +0.020 |
| Maximum subject kappa | 0.896 | 0.885 | -0.011 |
| Pooled kappa | 0.825 | **0.829** | +0.004 |
| Pooled macro-F1 | 0.751 | **0.758** | +0.007 |
| Pooled accuracy | 0.917 | 0.918 | +0.001 |

Exact printed summary:

```text
mean cohens_kappa 0.828 (sd 0.054, range 0.730-0.885 across 8 subjects)
```

**Interpretation:** mean subject kappa and pooled macro-F1 moved in the predicted direction, with a small absolute gain. The between-subject SD is lower in this cohort. This SD describes variation between the evaluated participants; it is not a confidence interval for the gain. The extrema above are cohort extrema and do not identify which participants improved or worsened.

The paired and per-class inspection below locates the gains and losses. No significance claim or established physiological mechanism is made. The comparisons reuse the same development cohort, so later tuning must remain within the declared budget and be interpreted as development evidence.

**Decision after the inspection below:** use F1 as a provisional working reference because mean subject kappa and pooled macro-F1 improve slightly with lower observed subject dispersion. Preserve B0 and explicitly retain the REM and participant-specific losses in the record. This is a development choice, not a demonstrated population-level advantage or a final pipeline selection.

**Budget at the end of F1:** 2 of at most 12 configurations evaluated on the fixed cohort: B0 and F1. The three-subject pilot remains outside that budget. At that stage, no earlier model-selection decision had yet been revised after a later experiment.

### Paired subject and per-class inspection of B0 versus F1

On 2026-10-22 Vicente supplied the following tables from the existing out-of-fold predictions. This inspection did not fit another model or consume another comparison configuration.

| Subject | B0 kappa | F1 kappa | F1 minus B0, as printed |
|---|---:|---:|---:|
| SC400 | 0.885 | 0.878 | -0.007 |
| SC401 | 0.860 | 0.853 | -0.007 |
| SC402 | 0.810 | 0.816 | +0.006 |
| SC403 | 0.879 | 0.885 | +0.005 |
| SC404 | 0.803 | 0.807 | +0.004 |
| SC405 | 0.749 | 0.786 | +0.037 |
| SC406 | 0.896 | 0.870 | -0.026 |
| SC407 | 0.710 | 0.730 | +0.019 |

Scores and differences were rounded independently by the Colab display. The differences are transcribed as reported and must not be recalculated by subtracting the rounded endpoints; this explains the apparent mismatch in rows such as SC403 and SC407.

**Participant interpretation:** 5 of 8 participants improved and 3 worsened. The largest reported gain is SC405 (+0.037); the largest loss is SC406 (-0.026). The two lowest B0 scores, SC407 and SC405, both improve, while the highest B0 score, SC406, decreases. The effect is heterogeneous.

The per-class reports pool out-of-fold predictions over all eight subjects. The same class support applies to B0 and F1:

| Stage | Epochs | Share of the cohort |
|---|---:|---:|
| W | 30,588 | 69.04% |
| N1 | 1,482 | 3.35% |
| N2 | 7,263 | 16.39% |
| N3 | 2,165 | 4.89% |
| REM | 2,805 | 6.33% |

**B0 — original absolute powers**

| Stage | Precision | Recall | F1 | Support |
|---|---:|---:|---:|---:|
| W | 0.957 | 0.981 | 0.969 | 30,588 |
| N1 | 0.483 | 0.252 | 0.331 | 1,482 |
| N2 | 0.862 | 0.873 | 0.868 | 7,263 |
| N3 | 0.862 | 0.738 | 0.795 | 2,165 |
| REM | 0.774 | 0.817 | 0.795 | 2,805 |

**F1 — relative powers**

| Stage | Precision | Recall | F1 | Support |
|---|---:|---:|---:|---:|
| W | 0.960 | 0.981 | 0.970 | 30,588 |
| N1 | 0.530 | 0.281 | 0.368 | 1,482 |
| N2 | 0.853 | 0.882 | 0.867 | 7,263 |
| N3 | 0.850 | 0.746 | 0.795 | 2,165 |
| REM | 0.780 | 0.800 | 0.790 | 2,805 |

| Report aggregate | B0 precision | B0 recall | B0 F1 | F1 precision | F1 recall | F1 F1 |
|---|---:|---:|---:|---:|---:|---:|
| Macro average | 0.787 | 0.732 | 0.751 | 0.795 | 0.738 | 0.758 |
| Support-weighted average | 0.909 | 0.917 | 0.911 | 0.912 | 0.918 | 0.913 |

**Class interpretation:** the clearest F1 gain is N1, from 0.331 to 0.368. Its recall rises from 0.252 to 0.281 (2.9 percentage points), but most N1 epochs are still missed. REM F1 decreases from 0.795 to 0.790, with recall falling from 0.817 to 0.800. N2 F1 changes from 0.868 to 0.867; N3 F1 stays at 0.795 at the reported precision; Wake F1 rises from 0.969 to 0.970. Thus the macro-F1 gain is mainly associated with N1 and is not uniform across stages.

The new cohort has approximately 69.04% Wake epochs, rather than the pilot's 68.0%. Read accuracy alongside kappa, macro-F1 and the class report. Numerical confusion matrices and per-record night reports remain to be exported.

## Iteration 4 (F2) — absolute plus relative EEG band powers

**Status: executed; aggregate metrics, paired subject scores, class report and row-normalized confusion matrix inspected. F2 adopted as the development working reference.**

**Motivation:** F1 improves the mean metrics and N1 performance but loses ground for REM and some participants. The five relative-power features remove the magnitude of the original five band powers, although the retained Hjorth activity and other features still contain amplitude information. The observed losses do not prove that power normalization caused them through loss of amplitude information.

**Construction:** keep all 11 B0 columns and append only the five relative-power columns from F1, producing **16 features**. Do not append all 11 F1 columns, which would duplicate the other six features. Name the added columns `eeg_delta_relative`, `eeg_theta_relative`, `eeg_alpha_relative`, `eeg_sigma_relative` and `eeg_beta_relative`.

**Directional prediction recorded before this run:** complementary absolute and relative descriptions may preserve the N1 benefit while recovering some of the REM or participant-specific losses. Redundancy and the extra feature dimensions may instead hurt performance; a gain is uncertain.

**Controls:** same 44,303 epochs, eight subjects, labels, subject folds, seed, preprocessing and supplied scaler/random-forest configuration. The learned scaler and classifier remain fitted inside each training fold. This comparison changes the feature representation and dimension. Reuse `X8` and the five band columns of `X8_rel`; no new spectral extraction or data download is needed. Keep both existing matrices and reports unchanged.

Compare F2 against both F1 (the provisional working reference) and B0. Continue to assess mean subject kappa, its spread and pooled macro-F1, with paired/class inspection before making a firm decision. If selected for later inference, this same 16-column construction must be implemented in the track's feature extractor with aligned feature names.

### Reported F2 results

Vicente supplied these aggregate outputs from the executed Colab cell on 2026-10-22. The cell confirmed **16 features** and evaluated `X8_comb` with the same `y8` and `groups8`. No additional run was performed here.

| Metric | B0: absolute | F1: relative | F2: combined |
|---|---:|---:|---:|
| Mean subject kappa | 0.824 | 0.828 | **0.837** |
| SD of subject kappa | 0.068 | 0.054 | **0.052** |
| Minimum subject kappa | 0.710 | 0.730 | 0.758 |
| Maximum subject kappa | 0.896 | 0.885 | 0.897 |
| Pooled kappa | 0.825 | 0.829 | **0.837** |
| Pooled macro-F1 | 0.751 | 0.758 | **0.762** |
| Pooled accuracy | 0.917 | 0.918 | 0.922 |

Exact printed summary:

```text
mean cohens_kappa 0.837 (sd 0.052, range 0.758-0.897 across 8 subjects)
```

**Aggregate comparison:** from the reported rounded values, mean subject kappa increases by 0.009 versus F1 and 0.013 versus B0. Pooled macro-F1 increases by 0.004 versus F1 and 0.011 versus B0. Subject SD is slightly lower than F1, and the cohort minimum rises from 0.730 to 0.758; the paired inspection below identifies SC407 as the lowest-scoring participant for F2.

**Interpretation:** the combined representation currently leads the aggregate development metrics. This is consistent with the broad hypothesis that both representations can help the finite classifier. The relative powers are deterministic functions of the absolute powers; they provide a different representation of the same signal information. These scores do not establish a physiological mechanism or generalization to the full population. The subsequent class report below shows partial retention of the N1 gain and recovery of most of the REM loss relative to B0.

**Decision after the inspection below:** adopt F2 as the development working reference. It has the highest mean subject kappa and pooled macro-F1 of the three configurations, improves 6/8 subjects versus F1, and improves N2/N3/REM F1 versus F1. Accept and record the smaller N1 F1 relative to F1 (0.354 versus 0.368), while noting it remains above B0 (0.331). Preserve B0 and F1 for traceability. This is a development choice on eight subjects, not final pipeline selection or a significance claim.

**Budget at the end of F2:** 3 of at most 12 configurations evaluated: B0, F1 and F2. The earlier three-subject pilot remains separate. Nine configurations remained at this checkpoint; see C1 below for the current count.


### Paired subject and class inspection of F2

Vicente supplied the following diagnostics on 2026-10-22 from the existing F2 predictions. They do not constitute another model fit or comparison configuration.

| Subject | F1 kappa | F2 kappa | F2 minus F1, as printed |
|---|---:|---:|---:|
| SC400 | 0.878 | 0.883 | +0.005 |
| SC401 | 0.853 | 0.861 | +0.008 |
| SC402 | 0.816 | 0.819 | +0.003 |
| SC403 | 0.885 | 0.887 | +0.002 |
| SC404 | 0.807 | 0.806 | -0.001 |
| SC405 | 0.786 | 0.781 | -0.005 |
| SC406 | 0.870 | 0.897 | +0.027 |
| SC407 | 0.730 | 0.758 | +0.029 |

Scores and differences are transcribed at their independently rounded display precision. In particular, the reported SC407 difference is +0.029 even though subtraction of the rounded endpoints gives +0.028.

**Participant interpretation:** F2 improves 6 of 8 participants versus F1. The largest reported gains are SC407 (+0.029) and SC406 (+0.027). SC404 (-0.001) and SC405 (-0.005) worsen. SC405 nevertheless remains above its original B0 score (0.781 versus 0.749). Gains are heterogeneous and the observed between-subject SD is not an uncertainty interval for the difference.

**F2 pooled class report**

| Stage | Precision | Recall | F1 | Support |
|---|---:|---:|---:|---:|
| W | 0.961 | 0.984 | 0.972 | 30,588 |
| N1 | 0.511 | 0.271 | 0.354 | 1,482 |
| N2 | 0.872 | 0.884 | 0.878 | 7,263 |
| N3 | 0.874 | 0.760 | 0.813 | 2,165 |
| REM | 0.773 | 0.816 | 0.794 | 2,805 |

| Aggregate | Precision | Recall | F1 | Support |
|---|---:|---:|---:|---:|
| Macro average | 0.798 | 0.743 | 0.762 | 44,303 |
| Support-weighted average | 0.915 | 0.922 | 0.917 | 44,303 |

Pooled accuracy is 0.922.

**Class trade-offs versus F1:** N1 F1 falls from 0.368 to 0.354 and recall from 0.281 to 0.271. N2 F1 improves from 0.867 to 0.878; N3 from 0.795 to 0.813; REM from 0.790 to 0.794; Wake from 0.970 to 0.972. The hypothesis is only partly supported: F2 retains some of the N1 benefit over B0, rather than all of F1's gain, and almost recovers B0 REM F1 (0.794 versus 0.795).

**Row-normalized F2 confusion matrix, as displayed in the supplied figure**

Rows are reference stages; columns are predictions in the order shown. These are the figure's values rounded to two decimals, not exact numerical matrix exports.

| Real / predicted | W | N1 | N2 | N3 | REM |
|---|---:|---:|---:|---:|---:|
| W | 0.98 | 0.00 | 0.01 | 0.00 | 0.00 |
| N1 | 0.40 | 0.27 | 0.15 | 0.00 | 0.17 |
| N2 | 0.03 | 0.02 | 0.88 | 0.02 | 0.04 |
| N3 | 0.10 | 0.00 | 0.14 | 0.76 | 0.00 |
| REM | 0.05 | 0.05 | 0.08 | 0.00 | 0.82 |

Rounding may prevent displayed rows from summing to 1, and 0.00 does not establish zero errors. The three-decimal class-report recalls above are more precise than the diagonal read from the figure. Main residual error: approximately 40% of actual N1 is predicted as Wake, 17% as REM and 15% as N2. N3 is confused mainly with N2 (approximately 14%) and Wake (10%). These are descriptive error patterns, not established causes.

**Working choice:** use F2 for the next controlled development comparisons. First preserve exact out-of-fold reports and the current executed notebook; then consolidate the feature construction into a reusable extractor and add versioned per-recording caches before slower processing/feature experiments. Downloaded data and cache files remain outside git.

## Team discussion and preservation checkpoint — 2026-10-27

Vicente reported the team's first direction-setting meeting. Each member will develop an individual preprocessing/filtering/feature strategy before discussing the attempts together. Subject-level cross-validation and the instructor's ten fixed hold-out subjects remain the shared evaluation discipline. The team discussed signal-quality inspection by sampling recordings, the exclusion of Movement/Unknown by the loader, Wake imbalance, a possible training crop and possible minority resampling. These are discussion items, not claims that filtering or synthetic augmentation has been implemented. Direct comparisons between members require a common cohort and evaluation protocol.

Vicente supplied the successful Colab save message for /content/drive/MyDrive/CM2013_data/experiments/features_B0_F1_F2.json. The uploaded executed notebook capstone_viggy(1).ipynb also contains this save output and the B0/F1/F2 cells and results. This confirms the reported export operation; the JSON bytes have not been uploaded here for independent numerical inspection. It does not confirm a team repository commit. That notebook snapshot predates the later label-audit and C1 cells executed through the conversation; save the current Colab notebook to preserve those additions.

## Development label audit — before C1, 2026-10-27

The following diagnostics use only SC400–SC407. They summarize reference labels and do not fit another classifier or consume another comparison configuration. The existing eight-subject counts remain W 30,588; N1 1,482; N2 7,263; N3 2,165; REM 2,805; total 44,303.

### Per-subject stage percentages

Transcribed from Vicente's displayed table, rounded to one decimal. Each subject combines both nights; rounding may prevent rows from summing to exactly 100%.

| Subject | W (%) | N1 (%) | N2 (%) | N3 (%) | REM (%) |
|---|---:|---:|---:|---:|---:|
| SC400 | 70.9 | 2.1 | 11.4 | 9.4 | 6.2 |
| SC401 | 65.1 | 3.6 | 21.6 | 3.6 | 6.1 |
| SC402 | 68.0 | 5.0 | 17.0 | 3.8 | 6.2 |
| SC403 | 71.4 | 1.9 | 15.9 | 3.4 | 7.3 |
| SC404 | 61.7 | 5.7 | 21.2 | 2.7 | 8.7 |
| SC405 | 73.1 | 2.9 | 15.1 | 4.5 | 4.5 |
| SC406 | 72.8 | 2.6 | 14.7 | 4.7 | 5.2 |
| SC407 | 69.2 | 3.1 | 14.2 | 6.9 | 6.6 |

Wake is the majority for every subject (61.7–73.1%); N1 is uncommon for every subject (1.9–5.7%). Imbalance is shared across the cohort. These proportions alone do not establish the cause of N1 errors or identify signal artifacts. The existing classifier already uses class_weight="balanced", fitted separately in each training fold.

### Where the Wake epochs occur

For each night, locate the first and last retained epoch labelled N1/N2/N3/REM. Count Wake before the first, after the last, and between them. Minutes below sum retained 30-second epochs after Movement/Unknown exclusion; they are not reconstructed elapsed EDF timestamps or independently measured lights-off times. No epochs were removed by this diagnostic.

| Recording | Total W (min) | Initial W (min) | Final W (min) | W between sleep endpoints (min) |
|---|---:|---:|---:|---:|
| SC4001E0 | 998.5 | 510.5 | 454.0 | 34.0 |
| SC4002E0 | 942.5 | 434.5 | 476.5 | 31.5 |
| SC4011E0 | 928.0 | 359.0 | 550.5 | 18.5 |
| SC4012E0 | 912.0 | 321.5 | 569.5 | 21.0 |
| SC4021E0 | 953.5 | 364.5 | 585.0 | 4.0 |
| SC4022E0 | 935.5 | 378.5 | 554.5 | 2.5 |
| SC4031E0 | 1004.0 | 435.5 | 558.5 | 10.0 |
| SC4032E0 | 978.5 | 460.5 | 510.0 | 8.0 |
| SC4041E0 | 767.0 | 406.0 | 321.0 | 40.0 |
| SC4042E0 | 886.5 | 537.0 | 317.0 | 32.5 |
| SC4051E0 | 1129.0 | 644.5 | 440.5 | 44.0 |
| SC4052E0 | 890.0 | 540.5 | 298.5 | 51.0 |
| SC4061E0 | 1034.5 | 467.5 | 556.0 | 11.0 |
| SC4062E0 | 1003.5 | 423.5 | 543.5 | 36.5 |
| SC4071E0 | 979.0 | 466.5 | 510.5 | 2.0 |
| SC4072E0 | 952.0 | 320.0 | 488.5 | 143.5 |

Summing these displayed half-minute values gives 15,294 minutes of Wake: 14,804 at the two ends and 490 between the first/last sleep-labelled epochs. Thus 96.8% of retained Wake duration lies at the ends. A first-to-last sleep window with 30 retained minutes on either side would retain 16,615 epochs across the eight-subject pool, including all 13,715 sleep epochs and 2,900 Wake epochs (17.45% of the cropped pool), removing 27,688 Wake epochs. These are arithmetic summaries of the audit, not a changed evaluation set. Each actual C1 fold crops only its seven training subjects.

## Iteration 5 (C1) — training-only sleep-window crop, 30-minute margins

**Status: executed by Vicente on 2026-10-27; aggregate/spread, full class report and paired subject scores supplied; C1 JSON save confirmed. F2 remains the development working reference. Direct C1 confusion-matrix inspection remains pending.**

### Predeclared hypothesis and controls

The label audit motivated testing whether reducing long Wake stretches in training would improve recognition of minority stages. The stated risk was worse Wake recognition. The margin was fixed at 30 minutes before viewing C1 results; no margin search has been run. This is a training-sample selection experiment. Signal filtering and feature extraction are unchanged.

- Same eight development subjects, both nights; none belongs to the published hold-out set.
- Features: unchanged F2 matrix X8_comb, 16 columns; original features plus five relative EEG powers.
- Same default StandardScaler → RF with 200 trees, balanced class weights and seed 0; a fresh pipeline is fitted in every fold.
- Eight-fold LeaveOneGroupOut on subjects. Both nights of each subject remain together.
- Within each fold, reference labels are used to locate the crop endpoints only for training subjects. Keep the first-to-last sleep-labelled interval plus 30 minutes on either side, clamped to the recording boundaries. Preserve any Wake within that interval.
- The loaded arrays contain only retained epochs, so the margin is 60 retained epochs at 30 seconds each. Exact elapsed-time margins would require original timestamps; that change has not been implemented.
- The test indices remain complete: all 44,303 original development epochs receive out-of-fold predictions. Test/hold-out labels are not used to determine an inference crop.
- The Colab cell checked feature/label/group alignment before fitting. Its custom LOSO loop applies the mask only to training indices, predicts the full held-out subject and uses the course _make_report helper to retain the same metric/spread schema.
- No new synthetic samples, learned feature selection, signal filters or hold-out operations are introduced.

Reported training sizes, in the LOSO subject order:

| Fold | Held-out subject | Training epochs after crop |
|---|---|---:|
| 1 | SC400 | 14,647 |
| 2 | SC401 | 14,326 |
| 3 | SC402 | 14,581 |
| 4 | SC403 | 14,752 |
| 5 | SC404 | 14,180 |
| 6 | SC405 | 14,697 |
| 7 | SC406 | 14,756 |
| 8 | SC407 | 14,366 |

Their sum is 116,305 = 7 × 16,615, consistent with every cropped subject appearing in seven training folds. This is an arithmetic consistency check; the models were run in Vicente's Colab, not rerun here.

### Reported C1 results

All values below are transcribed from the supplied outputs at three-decimal precision. Differences use those rounded values.

| Metric | F2: full training | C1: cropped training | C1 minus F2 |
|---|---:|---:|---:|
| Mean subject kappa | 0.837 | 0.813 | -0.024 |
| SD of subject kappa | 0.052 | 0.051 | -0.001 |
| Minimum subject kappa | 0.758 | 0.714 | -0.044 |
| Maximum subject kappa | 0.897 | 0.878 | -0.019 |
| Pooled kappa | 0.837 | 0.813 | -0.024 |
| Pooled macro-F1 | 0.762 | 0.758 | -0.004 |
| Pooled accuracy | 0.922 | 0.906 | -0.016 |

C1 pooled balanced accuracy is 0.771. F2's exact balanced-accuracy value has not been supplied separately; its displayed macro-average recall was 0.743. Balanced accuracy gives equal weight to stage recalls, whereas macro-F1 also depends on stage precision.

Exact printed C1 summary:

~~~text
mean cohens_kappa 0.813 (sd 0.051, range 0.714-0.878 across 8 subjects)
~~~

**C1 pooled class report, on the complete evaluation set**

| Stage | Precision | Recall | F1 | Support |
|---|---:|---:|---:|---:|
| W | 0.976 | 0.949 | 0.962 | 30,588 |
| N1 | 0.407 | 0.377 | 0.391 | 1,482 |
| N2 | 0.833 | 0.894 | 0.863 | 7,263 |
| N3 | 0.768 | 0.814 | 0.790 | 2,165 |
| REM | 0.744 | 0.824 | 0.782 | 2,805 |

| Aggregate | Precision | Recall | F1 | Support |
|---|---:|---:|---:|---:|
| Macro average | 0.746 | 0.771 | 0.758 | 44,303 |
| Support-weighted average | 0.909 | 0.906 | 0.907 | 44,303 |

Pooled accuracy is 0.906.

### Interpretation and decision

The predicted minority-recall benefit is partly observed. N1 recall rises from 0.271 to 0.377 (+10.6 percentage points) and N1 F1 from 0.354 to 0.391 (+0.037). Its precision falls from 0.511 to 0.407, so more actual N1 is detected alongside more false N1 predictions. N3 recall rises from 0.760 to 0.814 (+5.4 points), but its precision falls from 0.874 to 0.768 and F1 from 0.813 to 0.790. Higher recall alone is therefore not sufficient evidence of a better stage classifier.

Recall rises for every sleep stage and falls for Wake (0.984 → 0.949, -3.5 points). Precision falls for every sleep stage and rises for Wake. This pattern is consistent with a shift toward predicting sleep stages more often after the training selection changes; the confusion matrix is needed to locate specific changed errors. N1 is the only stage whose F1 improves; Wake, N2, N3 and REM F1 all decrease. Class weighting remains enabled in both runs, with weights recomputed from the training data provided to each fold.

Mean subject kappa falls by 0.024 and pooled macro-F1 by 0.004 on the same complete evaluation set. The similar between-subject SD is not a confidence interval for the difference, and the new extrema do not identify paired individual changes. No significance claim is made.

**Decision:** retain F2 as the working reference under the predeclared primary metric; do not adopt C1 as an overall improvement. Preserve C1 as the first fixed-cohort alternative that underperforms on both primary mean kappa and pooled macro-F1, with a useful N1 trade-off. This result does not establish that every cropping strategy fails. Do not replace the complete evaluation set with a cropped test set to obtain a more favourable comparison. The paired inspection below confirms losses for six of eight subjects. The exact-report save is now confirmed; preserve the updated executed notebook as well. C1 confusion inspection can use these existing saved predictions without retraining.

### Paired subject inspection and C1 export confirmation

Vicente supplied the following table and the successful save message on 2026-10-27. These steps reused the existing predictions and did not fit another model or consume a comparison configuration.

| Subject | F2 kappa | C1 kappa | C1 minus F2, as printed |
|---|---:|---:|---:|
| SC400 | 0.883 | 0.878 | -0.006 |
| SC401 | 0.861 | 0.791 | -0.070 |
| SC402 | 0.819 | 0.803 | -0.016 |
| SC403 | 0.887 | 0.862 | -0.025 |
| SC404 | 0.806 | 0.813 | +0.007 |
| SC405 | 0.781 | 0.714 | -0.067 |
| SC406 | 0.897 | 0.842 | -0.055 |
| SC407 | 0.758 | 0.801 | +0.042 |

Scores and differences were rounded independently from the full-precision values in Colab. Preserve the displayed differences rather than subtracting the rounded endpoints; SC400 and SC407 illustrate this distinction.

**Participant interpretation:** two subjects improve (SC404 and SC407) and six worsen. The largest losses are SC401 (-0.070), SC405 (-0.067) and SC406 (-0.055). The largest gain is SC407 (+0.042), which had the lowest F2 kappa; C1's lowest score instead belongs to SC405 (0.714). The effect is heterogeneous and does not support treating the aggregate loss as the effect of just one unusual participant. No significance claim is made. **The working decision remains F2.**

Confirmed Colab output: Guardado: /content/drive/MyDrive/CM2013_data/experiments/C1_crop30.json. The export cell includes the course revision, runtime versions, baseline configuration, 16 feature names, 30-minute margin, training-only crop scope, complete-epoch evaluation scope and full C1 report with predictions. The JSON bytes have not been uploaded here for independent inspection. This confirms the reported save operation, not a team repository commit.

**Current comparison budget (updated after P1):** 5 of at most 12 configurations evaluated: B0, F1, F2, C1 and P1. Seven remain. The three-subject pilot and label/quality diagnostics remain outside this count. The team's final pipeline, final-model commit and EXPECTED_SCORE.md registration remain future work.

## EEG quality screening and targeted inspection — 2026-10-27

These diagnostics use the same 16 development nights, SC400–SC407. They do not fit a classifier or consume another comparison configuration. At this diagnostic checkpoint, no automatic epoch rejection, quality-based crop or new signal filter had been applied to a classification run. The subsequent P1 filtering experiment is recorded separately below.

### Complete-epoch finite/constant checks and amplitude distribution

For every loaded EEG Fpz-Cz epoch, check whether all samples are finite, whether the complete epoch is exactly constant, and its peak-to-peak amplitude (maximum minus minimum), converted from volts to microvolts for reporting. P50/P95 are percentiles across finite epochs within each recording. These are descriptive quality-screening statistics, not fitted rejection thresholds. An epoch with a constant subsegment can still pass the complete-epoch constant check.

| Recording | Epochs | Epochs with NaN/Inf | Completely constant epochs | P50 peak-to-peak (uV) | P95 (uV) | Maximum (uV) |
|---|---:|---:|---:|---:|---:|---:|
| SC4001E0 | 2650 | 0 | 0 | 182.9 | 248.7 | 353.1 |
| SC4002E0 | 2829 | 0 | 0 | 217.1 | 302.7 | 397.4 |
| SC4011E0 | 2802 | 0 | 0 | 200.5 | 288.3 | 383.4 |
| SC4012E0 | 2848 | 0 | 0 | 176.1 | 304.0 | 381.0 |
| SC4021E0 | 2804 | 0 | 0 | 123.1 | 191.4 | 340.2 |
| SC4022E0 | 2755 | 0 | 0 | 197.4 | 288.1 | 383.0 |
| SC4031E0 | 2820 | 0 | 0 | 140.3 | 209.9 | 333.2 |
| SC4032E0 | 2732 | 0 | 0 | 207.2 | 280.4 | 388.6 |
| SC4041E0 | 2569 | 0 | 0 | 177.6 | 291.3 | 386.0 |
| SC4042E0 | 2788 | 0 | 0 | 221.3 | 325.1 | 396.0 |
| SC4051E0 | 2722 | 0 | 0 | 265.0 | 345.9 | 362.0 |
| SC4052E0 | 2804 | 0 | 0 | 204.7 | 340.3 | 360.0 |
| SC4061E0 | 2770 | 0 | 0 | 317.3 | 390.0 | 390.0 |
| SC4062E0 | 2830 | 0 | 0 | 144.0 | 210.3 | 294.1 |
| SC4071E0 | 2810 | 0 | 0 | 134.3 | 203.8 | 320.6 |
| SC4072E0 | 2770 | 0 | 0 | 201.3 | 314.2 | 361.0 |

Values are transcribed at the supplied one-decimal precision. All 44,303 EEG epochs pass these two basic integrity checks; this does not establish that they are artifact-free. SC4061E0 has the largest median amplitude and equal displayed P95/maximum (390 uV), motivating a targeted inspection. Large amplitude alone is not an artifact diagnosis; sleep physiology, cross-contamination and measurement failure require different interpretations.

### Two selected SC4061E0 epochs

Select the epoch whose peak-to-peak amplitude is nearest the within-night median, plus the first epoch attaining the maximum. Display each full 30-second EEG epoch, a 2-second zoom around its largest excursion from its median, and diagnostic Welch PSD (8-second Hann windows, 50% overlap, constant detrending, density scaling, frequency range up to 50 Hz at fs=100 Hz). These plotting settings do not alter the model features, which still use their original estimator settings.

Vicente supplied the figure image(20261027-170320).png and these printed values:

| Selection | Retained epoch index | Reference stage | Minimum (uV) | Maximum (uV) | Displayed peak-to-peak (uV) |
|---|---:|---|---:|---:|---:|
| Nearest median amplitude | 134 | W | -170.286 | 146.952 | 317.2 |
| Maximum amplitude | 4 | W | -194.000 | 196.000 | 390.0 |

The selected observed epoch need not equal the interpolated P50 statistic; the different displayed precision is also retained. Indices refer to the retained loader arrays, not original EDF sample indices.

**Visual observations:** epoch 4 contains a prominent interval of fast irregular high-amplitude activity at approximately 15–18 seconds, with broader high-frequency power than the median-amplitude example. This is suspicious for contamination, but its physiological or instrumental origin has not been confirmed with the other channels. The median-amplitude example has strong low-frequency content. Neither of these two PSDs shows a dominant isolated 50-Hz peak; this does not establish the absence of powerline interference throughout the cohort. The displayed zoom does not by itself establish a long, unambiguous flat plateau at the measurement limit.

### EDF calibration limits and per-stage contact counts in SC4061E0

The technical EDF header was read directly, without downloading or reloading all signal samples. Reported EEG Fpz-Cz physical limits are **-194.0 to 196.0 uV**, matching the extrema in epoch 4. The prefilter text is **HP:0.5Hz LP:100Hz [enhanced cassette BW]**. This is acquisition metadata, not a new digital filtering setting: the loaded EEG is at 100 Hz and the represented frequency range ends at 50 Hz. The declaration alone does not establish an ideal anti-alias response.

The diagnostic counts samples within half of one digital quantization step of either declared physical limit, using the EDF digital range to calculate the step and converting units to match the loaded volts. An epoch is flagged if at least one sample meets this condition. No epoch is removed. Numeric digital-min/max values were used by the cell but not printed in the supplied output.

| Stage | Epochs | Epochs contacting either limit (%) | Samples at the limits (%) |
|---|---:|---:|---:|
| W | 2069 | 42.436 | 0.185 |
| N1 | 56 | 3.571 | 0.005 |
| N2 | 407 | 0.246 | 0.001 |
| N3 | 136 | 0.735 | 0.001 |
| REM | 102 | 0.000 | 0.000 |

These are rounded percentages supplied by Vicente. Contact is concentrated in Wake in this night. A flag in 42.436% of Wake epochs coexists with only 0.185% of Wake samples at a limit: it is not evidence that 42.436% of the Wake duration is unusable. Merely touching a limit does not establish the extent or cause of clipping; consecutive rail runs and additional waveforms would further characterize severity. These findings apply to this night, not automatically to the other 15 recordings.

**Quality-handling decision at this checkpoint:** preserve the integrity flags and all original evaluation epochs. Do not automatically reject an entire 30-second epoch because one sample touches a limit. Filtering cannot reconstruct a peak lost to genuine saturation; quality flags must not be erased by a smoother-looking output. There is no quality-based exclusion rule or added quality feature in the classifier yet.

### Planned P1 candidate — EEG-only low-pass, before any score is observed

This subsection preserves the P1 plan stated before its real-signal preview or model score. At that earlier checkpoint the fixed-cohort comparison count was four. Execution and results were supplied later on the same day and are recorded in Iteration 6 below.

- Motivation: the inspected suspicious Wake burst contains fast broadband activity. Test whether suppressing the upper represented frequencies improves the EEG descriptors while retaining most of the 0.5–30 Hz band-power range. The burst's source remains unconfirmed; useful Wake information may also be attenuated.
- Candidate: Butterworth low-pass, single-pass order 4, design Wn=35 Hz, fs=100 Hz, second-order sections, forward-backward application with odd padding. No new high-pass or notch is proposed. The EDF already declares an acquisition high-pass at 0.5 Hz, and the inspected examples do not motivate an automatic 50-Hz notch.
- Forward-backward filtering squares the single-pass magnitude response; 35 Hz is therefore about -6.02 dB after both passes, not the composite -3 dB point. Zero phase does not guarantee preserved waveform morphology.
- A local analytical frequency-response check (SciPy 1.17.0, separate from the Colab experiment environment) verified about -0.494 dB at 30 Hz, -6.021 dB at 35 Hz and -31.497 dB at 40 Hz, with less than 0.51 dB attenuation through 30 Hz and more than 30 dB from 40 Hz at fs=100 Hz. This is a filter-design check, not a real-data model result.
- Implementation plan: introduce PREPROCESS_VERSION=1 and explicit cutoff/order settings; return a new filtered EEG array without modifying the loaded recordings. Apply along each epoch's sample axis so separated retained epochs are not concatenated across excluded gaps; edge transients remain a limitation to inspect.
- Preview a suspicious W epoch and a deterministic N3 example with before/after time traces and PSDs before recomputing features. The filtered output is a processing candidate, not a recovered clean reference.
- For the later model comparison, retain all 44,303 evaluation epochs, the same 8 subject folds, F2's 16 feature definitions and the same scaler/RF settings. Recompute all EEG-dependent descriptors and relative powers consistently; leave EOG and EMG unchanged. Fit the scaler/classifier only within each training fold. Keep F2 as the working reference until the complete metric/spread panel supports a change.
- First integrate the feature construction into a reusable extractor and add versioned per-recording caches before the full P1 evaluation. Filter preview and analytical checks do not consume a model-comparison configuration.

Supporting sources: course book sections 8.2 (printed pp. 103–105, quality screening and saturated data) and 9.5 (pp. 119–120, forward-backward filtering and edge effects); official EDF specification https://www.edfplus.info/specs/edf.html; SciPy butter and sosfiltfilt documentation https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.butter.html and https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.sosfiltfilt.html. The course source and Colab runtime versions for the actual classification experiments remain those recorded earlier.

## Iteration 6 (P1) — EEG-only 35-Hz low-pass with F2 features

### Preview, implementation and checks

Executed by Vicente in Colab on 2026-10-27 after the plan above. The real-signal preview figure, image(20261027-172344).png, shows the suspicious W epoch 4 and a deterministic N3 example (retained epoch 1262) from SC4061E0, with time-domain zooms and before/after PSDs. The filter suppresses upper-frequency power, with close PSD overlap below 30 Hz; the N3 waveform is nearly unchanged in the displayed window. The W burst partly remains. These observations are limited to the displayed examples and do not establish artifact recovery or improved classification.

- Preprocessing: PREPROCESS_VERSION=1; PREPROCESS_SETTINGS={"cutoff_hz":35.0,"order":4}. EEG-only scipy.signal.butter(..., btype="lowpass", fs=rec.fs, output="sos") followed by sosfiltfilt(..., axis=-1, padtype="odd") on each retained epoch. No added high-pass, notch, crop or quality-based rejection. Loaded recordings remain unchanged; filtered arrays are placed in replacement Recording objects.
- Reusable helper extrair_features_viggy(rec) extracts the original 11 course features and appends the same five relative EEG powers as F2, using a zero-safe sum of the five bands. It checks that powers are finite and nonnegative. Before filtering, the helper matches X8_comb for the first recording at rtol=1e-12, atol=0, and its feature names match the 16 F2 names. This is a first-record parity check, not an independent all-record extractor test.
- Per-recording preprocessing and feature caches use adapter.cached under /content/drive/MyDrive/CM2013_data/cache/viggy, outside the repository. FEATURE_VERSION=1. Input identity hashes the actual EEG/EOG/EMG arrays including shape and dtype, with record ID and sampling rate. The preprocessing key includes its version, settings and NumPy/SciPy runtime versions. The feature key includes the preceding preprocessing key, feature version, pinned course revision, effective feature configuration and names. Classifier settings are excluded. Code changes require the corresponding version to be bumped.
- Feature-cache hits can bypass loading the larger preprocessing result. Changing the classifier reuses both cached stages; changing feature code/version reuses preprocessing; changing preprocessing invalidates both. No fitted scaler, feature selector, class resampling or model is cached across folds. Cache files remain outside git.
- Vicente supplied 16 successful preprocessing-cache messages and 16 feature-cache messages, each computed and saved, followed by the confirmations below. The feature matrix has shape (44303, 16). Labels and groups remain aligned to the original records; EOG/EMG feature columns match F2 at rtol=1e-12, atol=0. The evaluation cell also checks that the full P1 feature matrix is finite.

```text
Extrator F2 confirmado na primeira gravação.
P1: 44303 épocas | 16 features | 8 participantes
Labels, grupos, EOG e EMG confirmados.
```

The helper makes feature construction reusable within the current notebook. The original track adapter's default training/inference path still describes 11 features; integrating the selected 16-feature implementation consistently into final training and hold-out inference remains future work.

### Evaluation and reported results

Evaluation call: rep8_p1 = track.evaluate(X8_p1, y8, groups8, cfg=BASELINE_CONFIG). The same fixed SC400–SC407 cohort, all 44,303 epochs, eight subject-wise LOSO folds, seed-0 200-tree balanced random forest and fold-fitted StandardScaler are retained. Both nights of each test subject remain together. This compares P1 directly with F2; the C1 training crop is not combined with P1. No hold-out subject is used.

| Metric | F2: no additional LPF | P1: EEG LPF 35 Hz | P1 minus F2 |
|---|---:|---:|---:|
| Mean subject kappa | 0.837 | 0.833 | -0.004 |
| Subject kappa SD | 0.052 | 0.054 | +0.002 |
| Subject kappa minimum | 0.758 | 0.749 | -0.009 |
| Subject kappa maximum | 0.897 | 0.895 | -0.002 |
| Pooled kappa | 0.837 | 0.833 | -0.004 |
| Pooled macro-F1 | 0.762 | 0.757 | -0.005 |
| Pooled accuracy | 0.922 | 0.920 | -0.002 |

Differences here are descriptive subtractions of the rounded displayed values. The minimum/maximum comparisons do not establish that the same subject occupies each endpoint. P1 pooled balanced accuracy is **0.738**. F2's printed macro recall is 0.743, but an independently printed full-precision F2 balanced-accuracy value has not been supplied here. The full panel and spreads can be retained from each exact report export; only kappa spread is transcribed in the supplied console summary.

Exact summaries supplied:

```text
F2 — sem LPF adicional: mean cohens_kappa 0.837 (sd 0.052, range 0.758-0.897 across 8 subjects)
P1 — LPF de 35 Hz: mean cohens_kappa 0.833 (sd 0.054, range 0.749-0.895 across 8 subjects)
```

| Stage | P1 precision | P1 recall | P1 F1 | Support | F2 F1 | P1 minus F2 F1 |
|---|---:|---:|---:|---:|---:|---:|
| W | 0.959 | 0.984 | 0.971 | 30588 | 0.972 | -0.001 |
| N1 | 0.488 | 0.252 | 0.332 | 1482 | 0.354 | -0.022 |
| N2 | 0.869 | 0.877 | 0.873 | 7263 | 0.878 | -0.005 |
| N3 | 0.872 | 0.764 | 0.815 | 2165 | 0.813 | +0.002 |
| REM | 0.778 | 0.815 | 0.796 | 2805 | 0.794 | +0.002 |
| Macro average | 0.793 | 0.738 | 0.757 | 44303 | 0.762 | -0.005 |
| Weighted average | 0.913 | 0.920 | 0.915 | 44303 | 0.917 | -0.002 |

P1 accuracy is 0.920 on 44,303 epochs. Values preserve the three-decimal console precision; no exact confusion counts are inferred from the rounded class metrics.

**Interpretation and decision:** P1 has a small observed loss in the declared primary mean subject kappa, a slightly larger subject SD, and lower pooled macro-F1 and accuracy than F2. N1 shows the largest displayed class-F1 loss (-0.022); N3 and REM each gain 0.002. The fact that the filter attenuated upper-frequency activity in the preview did not translate into better aggregate classification under this configuration. These results do not identify the cause of the loss or establish statistical significance. **Retain F2 with no additional LPF as the working reference.** Paired subject differences and direct confusion inspection were subsequently supplied below using the existing out-of-fold predictions.

### Paired subject comparison and exact-report save confirmation

Vicente supplied the following Colab table and successful save message on 2026-10-27. These diagnostics reuse the existing out-of-fold predictions; the comparison count remains five of twelve.

| Subject | F2 kappa | P1 kappa | P1 minus F2, as printed |
|---|---:|---:|---:|
| SC400 | 0.883 | 0.880 | -0.004 |
| SC401 | 0.861 | 0.856 | -0.004 |
| SC402 | 0.819 | 0.815 | -0.004 |
| SC403 | 0.887 | 0.884 | -0.003 |
| SC404 | 0.806 | 0.799 | -0.007 |
| SC405 | 0.781 | 0.784 | +0.002 |
| SC406 | 0.897 | 0.895 | -0.002 |
| SC407 | 0.758 | 0.749 | -0.009 |

Scores and differences were independently rounded from full-precision Colab values. Preserve the supplied differences: subtracting the rounded endpoints would give a different last digit for SC400, SC401 and SC405.

**Paired interpretation:** seven of eight participants have a lower kappa with P1; only SC405 improves, by a printed 0.002. The largest losses are SC407 (-0.009) and SC404 (-0.007). SC407 remains the lowest-scoring participant and SC406 remains the highest. The observed aggregate decline is accompanied by small declines across most participants; the table supports retaining F2, without establishing a population effect or a mechanism for the loss. No additional configurations were trained for this review.

Confirmed Colab output:

```text
Guardado: /content/drive/MyDrive/CM2013_data/experiments/P1_lowpass35.json
```

The supplied export cell stores experiment ID, course revision, runtime versions, baseline configuration, preprocessing version/settings/application, feature version and names, complete-epoch evaluation scope, no-training-crop flag, record/subject/epoch manifest and the complete P1 report including out-of-fold predictions. The successful save is confirmed by Vicente's output; the JSON bytes have not been uploaded here for independent inspection. The latest executed notebook upload and corresponding personal/team repository commit remain unconfirmed. No hold-out predictions have been made.

### Direct confusion inspection

Vicente supplied image(20261027-181326).png on 2026-10-27. It compares F2 and P1 using row-normalized out-of-fold confusion matrices with a common 0–1 color scale. Rows are true stages; columns are predicted stages, ordered W, N1, N2, N3, REM. Values in the figure are rounded to two decimals. This diagnostic does not fit another model or consume a configuration.

| True stage | Predicted W | Predicted N1 | Predicted N2 | Predicted N3 | Predicted REM |
|---|---:|---:|---:|---:|---:|
| W, P1 | 0.98 | 0.00 | 0.01 | 0.00 | 0.00 |
| N1, P1 | 0.42 | 0.25 | 0.16 | 0.00 | 0.17 |
| N2, P1 | 0.04 | 0.02 | 0.88 | 0.02 | 0.05 |
| N3, P1 | 0.10 | 0.00 | 0.13 | 0.76 | 0.00 |
| REM, P1 | 0.05 | 0.05 | 0.08 | 0.00 | 0.81 |

The F2 matrix agrees with the earlier recorded F2 figure. Its N1 row is [0.40, 0.27, 0.15, 0.00, 0.17], compared with P1 [0.42, 0.25, 0.16, 0.00, 0.17]. Thus the displayed proportion of N1 predicted as W rises from about 40% to 42%, while correct N1 classification falls from about 27% to 25%; the proportion predicted as N2 rises from about 15% to 16%. These are marginal row comparisons, not a paired tracing of individual epochs between prediction categories.

Other visible changes are small: N2-to-W and N2-to-REM each rise by about one displayed percentage point; N3-to-N2 falls by about one. Two-decimal rounding can hide differences or exaggerate their apparent size at a boundary. In particular, the REM diagonals 0.82 and 0.81 coexist with the three-decimal recalls 0.816 and 0.815. Rounded rows need not sum to exactly one, and a displayed 0.00 does not establish zero errors. Exact counts remain in the saved reports.

**Decision after confusion review:** retain F2. N1 remains the largest class weakness; this particular added low-pass does not improve its recognition. The figure does not establish why the filter changed predictions or prove that all filtering is unhelpful.

## Next candidate M1 — classifier comparison, specified before evaluation

Proposed on 2026-10-27 after completing the P1 review; **not yet executed or scored** at this checkpoint. The comparison count remains five of twelve until execution.

- Question: with F2's fixed 16 descriptors, how does a regularized linear classifier compare with the current random forest? This compares model families and their class trade-offs without changing signal processing or the cohort.
- Keep X8_comb, all 44,303 epochs, no added LPF, no training crop, the same SC400–SC407 groups and eight LOSO folds. Reuse the computed feature matrix; do not recompute features or use hold-out data.
- Candidate: sklearn Pipeline(StandardScaler(), LogisticRegression(C=1.0, penalty="l2", solver="lbfgs", class_weight="balanced", max_iter=2000)). Other defaults follow the recorded scikit-learn 1.6.1 runtime. With five classes, lbfgs uses multinomial logistic loss. No C sweep or hyperparameter selection is part of this candidate.
- Pass this pipeline as clf to track.evaluate(..., cfg=BASELINE_CONFIG). The evaluator clones it per fold, so scaling, balanced class weights and model coefficients are fitted only using that fold's training subjects. RF's existing class weighting remains balanced as before.
- Retain F2's RF result as the working reference until the complete M1 panel, subject spread and paired/class inspection support a change. Report convergence warnings if any; numerical convergence must be resolved before interpreting the candidate's score.
- Method reference checked against the matching installed version: https://scikit-learn.org/1.6/modules/generated/sklearn.linear_model.LogisticRegression.html.

## Decision log

| Module | Current choice | Rationale | Alternatives tested so far |
|---|---|---|---|
| Loading | Eight fixed development subjects, both nights, persistent data and parsed cache | Establish a common comparison cohort; three-subject pilot retained separately | Cohort expansion only; not a pipeline comparison |
| Preprocessing / filtering | No additional LPF, as in F2 | P1 lowers mean subject kappa from 0.837 to 0.833 and macro-F1 from 0.762 to 0.757; preserve the QC evidence and quality flags | P1: EEG-only 35-Hz Butterworth low-pass, order 4, forward-backward SOS; previewed and evaluated, not adopted |
| Training epoch selection | All retained epochs, as in F2 | C1 improves N1 F1 but lowers the declared primary mean kappa and pooled macro-F1 on the complete evaluation set | C1: first–last sleep plus 30-minute margins in training only; not adopted |
| Features | F2: 11 original features plus 5 relative EEG powers, 16 total | Highest current mean subject kappa and macro-F1; 6/8 subjects improve vs F1; accept the documented N1 loss vs F1 while retaining improvement over B0 | B0, F1 and F2 evaluated and inspected; F2 adopted for development |
| Feature selection / classification | Current reference: supplied scaler and balanced RF, fitted within folds | Keep F2 while preparing a controlled model-family comparison | No alternative classifier evaluated yet; M1 logistic regression is specified above before execution |
| Inference / reporting | Complete-epoch eight-subject LOSO retained for B0/F1/F2/C1/P1; P1 aggregate, class, paired subject and confusion results recorded | Preserve evaluation coverage while comparing strategies and report gains as well as losses; final 16-feature training/inference integration remains pending | B0/F1/F2, C1 and P1 JSON saves confirmed; direct C1 confusion inspection, per-record night reporting and independent JSON inspection pending |

## Revisions

On 2026-10-22 the provisional **F1 relative-only band-power choice was revisited and replaced with F2 combined absolute/relative powers** after the predeclared F2 experiment and diagnostic review. Before F2, F1 was preferred to B0 because its mean subject kappa and macro-F1 were slightly higher and its subject spread lower. F2 then raised mean subject kappa from 0.828 (SD 0.054) to 0.837 (SD 0.052), and pooled macro-F1 from 0.758 to 0.762, with paired gains in 6/8 subjects. N1 F1 fell from 0.368 to 0.354, while N2, N3 and REM improved versus F1; the overall gain was judged worth this trade-off for the declared metrics. All numbers refer to the same eight-subject development cohort. This records an actual provisional choice changed after a later result; the team's final choice remains open.

## Contributions recorded so far

| Iteration | Person | Observed work | Review |
|---|---|---|---|
| 1 | Vicente Soares | Set up the Colab copy and persistent data folder; executed synthetic and real baseline cells; supplied metrics, class counts, confusion matrix and source revision. Setup and log preparation were assisted by ChatGPT. | Peer review not yet recorded. |
| 2 / inspection | Vicente Soares | Executed diagnostic plots for three development participants, expanded the cohort to eight subjects, reran the unchanged baseline and supplied its metrics. Setup, interpretation and log preparation were assisted by ChatGPT. | Peer review not yet recorded. |
| 3 (F1) | Vicente Soares | Executed the predeclared relative-band-power comparison and supplied aggregate metrics, paired subject kappas and both per-class reports. Code, interpretation and log preparation were assisted by ChatGPT. | Peer review not yet recorded. |
| 4 (F2) | Vicente Soares | Executed the predeclared combined absolute/relative feature comparison and supplied the confirmed 16-feature count, aggregate scores, paired subject table, class report and confusion figure. Code, interpretation and log preparation were assisted by ChatGPT. | Peer review not yet recorded. |
| 5 (C1) / label audit | Vicente Soares | Reported the team's direction-setting meeting; confirmed the B0/F1/F2 and C1 JSON saves; supplied per-subject stage proportions and per-night Wake endpoint counts; executed the predeclared training-only crop and supplied fold sizes, aggregate/spread, class and paired subject reports. Code, arithmetic, interpretation and log preparation were assisted by ChatGPT. | Strategy discussion occurred; peer review of C1 results not yet recorded. |
| QC after C1 | Vicente Soares | Executed EEG finite/constant and amplitude screening across all 16 nights; supplied SC4061E0 median/maximum-epoch figure and extrema; read EDF calibration/prefilter metadata and supplied per-stage rail-contact percentages. Code and interpretation were assisted by ChatGPT; the candidate filter's analytical response was checked separately, not as a Colab model run. | No peer review of these QC findings recorded yet. |
| 6 (P1) / caching | Vicente Soares | Executed the W/N3 low-pass preview, reusable F2 feature-helper checks, versioned per-recording preprocessing/features caches and eight-subject P1 evaluation; supplied cache-save confirmations, aggregate metrics with kappa spread, per-stage report, paired subject table, successful P1 JSON save message and side-by-side F2/P1 confusion matrices. Code, interpretation and log preparation were assisted by ChatGPT. | Peer review of P1 results not yet recorded. |

Contributions from other team members will be added when their actual work is documented.

## Next steps and missing evidence

- Save the executed notebook and this log in the team repository and record the team commit.
- B0/F1/F2, C1 and P1 exact-report JSON saves are confirmed in Colab; C1/F2 and P1/F2 paired subject comparisons are recorded. Preserve the updated executed notebook and record the actual experiment commit.
- P1/F2 confusion inspection is now recorded, including increased N1-to-W confusion. Direct C1 confusion inspection, per-record night reports and independent inspection of exported JSON files remain pending; use existing predictions.
- Next evaluate the predeclared M1 logistic-regression pipeline on X8_comb with the same eight subject folds, then save and inspect its full report before selecting another classifier or changing features. M1 has not yet been scored.
- Versioned per-recording preprocessing/features caching is now implemented and its first writes confirmed for all 16 nights. Keep data/cache files outside git and bump the relevant version whenever processing or feature code changes.
- Keep the declared eight-subject cohort and maximum 12-configuration budget fixed during comparisons; five configurations have been evaluated and seven remain. Record any justified protocol revision before implementing it.
- A reusable 16-feature helper is implemented and checked against F2 on the first recording. Integrate the selected processing/features consistently into final training, inference and feature names; the original track adapter's default inference still uses 11 features. Keep no additional LPF as the current working choice after P1.
- Cohort EEG amplitude/integrity screening, targeted SC4061E0 waveform/header inspection and the W/N3 LPF preview are recorded. Inspect further nights where needed, preserving quality flags. No automatic rejection rule has been chosen, and a filtered trace must not be treated as proof of recovered clipped data.
- A revised provisional feature decision is documented above. Final team pipeline selection, EXPECTED_SCORE.md registration and final hold-out inference are still future stages.

