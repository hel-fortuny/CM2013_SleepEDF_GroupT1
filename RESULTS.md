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

**Current comparison budget:** 3 of at most 12 configurations evaluated: B0, F1 and F2. The earlier three-subject pilot remains separate. There are nine remaining configurations within the declared budget.


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

## Decision log

| Module | Current choice | Rationale | Alternatives tested so far |
|---|---|---|---|
| Loading | Eight fixed development subjects, both nights, persistent data and parsed cache | Establish a common comparison cohort; three-subject pilot retained separately | Cohort expansion only; not a pipeline comparison |
| Preprocessing | Supplied default, unchanged | Preserve the original reference | None |
| Features | F2: 11 original features plus 5 relative EEG powers, 16 total | Highest current mean subject kappa and macro-F1; 6/8 subjects improve vs F1; accept the documented N1 loss vs F1 while retaining improvement over B0 | B0, F1 and F2 evaluated and inspected; F2 adopted for development |
| Feature selection / classification | Supplied defaults, fitted within folds by the harness | Measure baseline behavior before selecting alternatives | None |
| Inference / reporting | Eight-subject LOSO aggregate, paired and class reports recorded for all three; F2 row-normalized confusion figure inspected; exact numerical/night exports pending | Compare alternatives on identical subjects and report both gains and losses | B0/F1/F2 inspected; exact report archive remains to be confirmed |

## Revisions

On 2026-10-22 the provisional **F1 relative-only band-power choice was revisited and replaced with F2 combined absolute/relative powers** after the predeclared F2 experiment and diagnostic review. Before F2, F1 was preferred to B0 because its mean subject kappa and macro-F1 were slightly higher and its subject spread lower. F2 then raised mean subject kappa from 0.828 (SD 0.054) to 0.837 (SD 0.052), and pooled macro-F1 from 0.758 to 0.762, with paired gains in 6/8 subjects. N1 F1 fell from 0.368 to 0.354, while N2, N3 and REM improved versus F1; the overall gain was judged worth this trade-off for the declared metrics. All numbers refer to the same eight-subject development cohort. This records an actual provisional choice changed after a later result; the team's final choice remains open.

## Contributions recorded so far

| Iteration | Person | Observed work | Review |
|---|---|---|---|
| 1 | Vicente Soares | Set up the Colab copy and persistent data folder; executed synthetic and real baseline cells; supplied metrics, class counts, confusion matrix and source revision. Setup and log preparation were assisted by ChatGPT. | Peer review not yet recorded. |
| 2 / inspection | Vicente Soares | Executed diagnostic plots for three development participants, expanded the cohort to eight subjects, reran the unchanged baseline and supplied its metrics. Setup, interpretation and log preparation were assisted by ChatGPT. | Peer review not yet recorded. |
| 3 (F1) | Vicente Soares | Executed the predeclared relative-band-power comparison and supplied aggregate metrics, paired subject kappas and both per-class reports. Code, interpretation and log preparation were assisted by ChatGPT. | Peer review not yet recorded. |
| 4 (F2) | Vicente Soares | Executed the predeclared combined absolute/relative feature comparison and supplied the confirmed 16-feature count, aggregate scores, paired subject table, class report and confusion figure. Code, interpretation and log preparation were assisted by ChatGPT. | Peer review not yet recorded. |

Contributions from other team members will be added when their actual work is documented.

## Next steps and missing evidence

- Save the executed notebook and this log in the team repository and record the team commit.
- Export numerical confusion matrices and exact prediction arrays for B0, F1 and F2, plus per-record night reports. Rounded paired and per-class panels are now recorded above; current runtime versions are also recorded.
- Add versioned caching for slow per-recording steps before repeated experiments.
- Keep the declared eight-subject cohort and maximum 12-configuration budget fixed during comparisons; record any justified protocol revision before implementing it.
- Consolidate F2 as a reusable feature extractor for the next controlled comparisons. Preserve exact reports and the current executed notebook first; numerical exports and the integration checkpoint have not yet been confirmed. Record future hypotheses before later comparisons.
- A revised provisional feature decision is documented above. Final team pipeline selection, EXPECTED_SCORE.md registration and final hold-out inference are still future stages.

