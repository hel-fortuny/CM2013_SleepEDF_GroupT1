# Targeted N1 Improvement Experiments — Sleep-EDF

**Contributor:** Dalya  
**Project:** CM2013 Sleep-EDF Capstone  
**Status:** Completed — exploratory experiments

## Objective

The TC1+C1 configuration was selected as the reference baseline based on its strong overall classification performance (Cohen's κ = 0.749713). However, N1 recall remained low (22.58%).

Four experiments investigated whether targeted modifications could improve N1 detection without compromising overall performance.

## Experimental Setup

- Dataset: Sleep-EDF Expanded
- Development set: 68 subjects, 133 recordings, 360,621 epochs
- Validation: Five fixed subject-wise folds (A–E)
- Classifier: Random Forest, 200 trees, balanced class weighting
- Baseline: 33 TC1+C1 features, 30-minute training-only wake cropping
- Independent 10-subject holdout: Not used

## Experiments

**1. N1 Transition Bridge**

Applied a rule-based correction to isolated N2 predictions between consecutive N1 predictions. Modified 213 epochs without retraining.

**2. Relative Temporal Delta**

Added five current-minus-previous relative EEG band-power features, increasing the feature count from 33 to 38.

**3. N1 Weighting ×1.5**

Applied additional 1.5× sample weighting to N1 training epochs.

**4. YASA Spindle Features**

Added four spindle features extracted from Fpz-Cz EEG using YASA: count, mean duration, amplitude, and frequency. Total: 37 features.

## Results

| Configuration | Cohen's κ | Accuracy | Macro-F1 | N1 Recall | N1 F1 |
|---|---:|---:|---:|---:|---:|
| TC1+C1 Baseline | 0.749713 | 0.878706 | 0.688077 | 0.225765 | 0.282346 |
| N1 Transition Bridge | 0.749783 | 0.878723 | 0.688705 | 0.229737 | 0.285189 |
| Relative Temporal Delta | 0.749107 | 0.878454 | 0.687657 | 0.224926 | 0.282632 |
| N1 Weighting ×1.5 | 0.749103 | 0.878468 | 0.686622 | 0.216871 | 0.276120 |
| YASA Spindle Features | 0.748767 | 0.878188 | 0.687821 | 0.227499 | 0.283415 |

## Interpretation

The N1 Transition Bridge produced the largest N1 recall increase (+0.40 percentage points), but the improvement was marginal.

Relative Temporal Delta and N1 weighting did not improve N1 recall. YASA spindle features slightly increased N1 recall (+0.17 percentage points), while overall performance decreased slightly.

None of the modifications demonstrated a substantial improvement. TC1+C1 was therefore retained as the preferred configuration.

## Notebooks

- [N1 experiments](notebooks/Dalya_N1_Experiments_Clean_v1.ipynb)
- [YASA experiment](notebooks/Dalya_YASA_Full_AE_Clean_v3.ipynb)

## Reproducibility

The notebooks use saved predictions and experiment artifacts stored in Google Drive to reproduce evaluation metrics and confusion matrices.

The saved YASA predictions were verified across all five folds and 360,621 epochs, reproducing the original global metrics within a tolerance of 1e-5.

**Limitations:**
- Full model training has not been independently rerun from scratch using these cleaned notebooks.
- The original experiment artifacts and dataset are required for complete reproduction.
- No independent holdout evaluation or formal significance testing was performed for these modifications.
- The N1 Transition Bridge is an exploratory heuristic, not an AASM scoring rule.

## Outcome

All four experiments were documented and compared against the same TC1+C1 baseline. Their results informed the decision to retain the baseline and highlighted the continuing difficulty of N1 classification.