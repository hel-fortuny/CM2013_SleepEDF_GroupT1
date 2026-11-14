
# Results Log — Sleep-EDF, Dalya Yousif

**Track:** sleep_edf  
**Contributor:** Dalya Yousif  
**Split unit:** Subject  
**Primary metric:** Cohen's kappa  
**Evaluation mode:** New-subject classification  
**Development cohort:** 68 subjects, 133 recordings  
**Validation:** 5 fixed subject-wise folds (A–E)  
**Independent holdout:** 10 subjects — not evaluated  

## Iteration Log

| # | Experiment | What changed and why | Primary metric with spread | Better than baseline? | Decision |

| # | Experiment | What changed and why | Primary metric with spread | Better than baseline? | Decision |
|---|---|---|---|---|---|
| 1 | TC1+C1 Baseline | Reference configuration with 33 features. | Mean κ 0.750198 (SD 0.025996; 5 folds). | Reference | Retain as baseline. |
| 2 | N1 Transition Bridge | Corrected isolated N2 predictions between N1 predictions; 213 epochs modified. | Mean κ 0.750266 (SD 0.025928; 5 folds). | Marginal increase | Do not adopt without further validation. |
| 3 | Relative Temporal Delta | Added five relative temporal EEG features (38 total). | Mean κ 0.749594 (SD 0.025869; 5 folds). | No | Retain baseline. |
| 4 | N1 Weighting x1.5 | Increased N1 sample weights during training. | Mean κ 0.749608 (SD 0.026687; 5 folds). | No | Retain baseline. |
| 5 | YASA Spindle Features | Added four spindle features from Fpz-Cz EEG (37 total). | Mean κ 0.749236 (SD 0.025973; 5 folds). | No | Retain baseline. |


## Experimental Setup

### Purpose and run provenance

- Contributor: Dalya Yousif.
- Objective: Investigate targeted approaches to improve N1 classification.
- Reference configuration: TC1+C1 baseline.
- Experiments: N1 Transition Bridge, Relative Temporal Delta, N1 Weighting x1.5, and YASA Spindle Features.
- Evaluation results were reconstructed from saved predictions and experiment artifacts.
- Full model training was not rerun using the cleaned notebooks.

### Data and loading

- Dataset: Sleep-EDF Expanded.
- Development cohort: 68 subjects, 133 recordings.
- Evaluated epochs: 360,621.
- Sleep stages: W, N1, N2, N3, REM.
- Independent 10-subject holdout: Not evaluated.

### Pipeline and validation

- Validation: Five fixed subject-wise folds (A–E).
- Both recordings of each subject remain within the same fold.
- Baseline feature count: 33.
- Classifier: Random Forest.
- Primary metric: Cohen's kappa.
- Additional metrics: Accuracy, Macro-F1, Balanced Accuracy, N1 Precision, N1 Recall, and N1 F1.

### Metric aggregation

- **Pooled metrics:** Calculated from all out-of-fold predictions combined.
- **Fold mean:** Unweighted average of the five fold-level metrics.
- **SD:** Sample standard deviation across the five folds (`ddof=1`).
- Pooled metrics and fold means are reported separately because they are not mathematically equivalent.



## Results — Targeted N1 Experiments

### Pooled out-of-fold performance

| Experiment | Cohen's κ | Accuracy | Macro-F1 | N1 Recall | N1 F1 |
|---|---:|---:|---:|---:|---:|
| TC1+C1 Baseline | 0.749713 | 0.878706 | 0.688077 | 0.225765 | 0.282346 |
| N1 Transition Bridge | 0.749783 | 0.878723 | 0.688705 | 0.229737 | 0.285189 |
| Relative Temporal Delta | 0.749107 | 0.878454 | 0.687657 | 0.224926 | 0.282632 |
| N1 Weighting x1.5 | 0.749103 | 0.878468 | 0.686622 | 0.216871 | 0.276120 |
| YASA Spindle Features | 0.748767 | 0.878188 | 0.687821 | 0.227499 | 0.283415 |

### Fold-level performance (Mean ± SD)

| Experiment | Cohen's κ | N1 Recall |
|---|---|---|
| TC1+C1 Baseline | 0.750198 ± 0.025996 | 0.226681 ± 0.048401 |
| N1 Transition Bridge | 0.750266 ± 0.025928 | 0.230687 ± 0.050190 |
| Relative Temporal Delta | 0.749594 ± 0.025869 | 0.225836 ± 0.045295 |
| N1 Weighting x1.5 | 0.749608 ± 0.026687 | 0.217523 ± 0.050368 |
| YASA Spindle Features | 0.749236 ± 0.025973 | 0.228642 ± 0.047893 |

### Interpretation and decision

The N1 Transition Bridge produced the highest N1 recall, but its improvement over the baseline was small (+0.397 percentage points in pooled recall).

YASA spindle features produced a smaller increase (+0.173 percentage points).

Relative Temporal Delta and additional N1 weighting did not improve pooled N1 recall.

None of the four modifications demonstrated a substantial improvement in N1 classification. The TC1+C1 baseline was retained as the preferred configuration.

These comparisons are descriptive; no formal statistical significance testing was performed.



## Earlier Exploratory Experiments

### Wavelet Denoising and Filtering

**Purpose:** Investigate whether signal preprocessing improves sleep-stage classification while preserving physiologically important EEG features.

**Dataset:** Initial exploratory subset of 8 recordings (22,240 epochs).

**Methods:** Compared raw EEG features with selective wavelet denoising.

| Metric | Raw EEG | Selective Wavelet |
|---|---:|---:|
| Accuracy | 0.904 | 0.900 |
| Cohen's kappa | 0.809 | 0.800 |
| Macro-F1 | 0.746 | 0.741 |

**Interpretation:** Selective wavelet denoising did not improve classification performance on this exploratory subset.

**Decision:** No evidence from this experiment justified adopting selective wavelet denoising as the default preprocessing method.

**Limitation:** These exploratory results are not directly comparable with the later 68-subject experiments because the evaluated datasets and experimental configurations differ.
