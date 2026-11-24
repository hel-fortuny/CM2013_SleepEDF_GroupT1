# Results log — Sleep-EDF, Team T1

**Track:** sleep_edf  
**Split unit:** subject  
**Primary metric:** Cohen's kappa  
**Evaluation mode:** new-subject  
**Team:** Vicente Soares, Helena Fortuny, Dalya Yousif  
**Last updated:** 2026-11-19

## Current checkpoint — 2026-11-19

Vicente has completed **19 configurations on the 68-subject development cohort**. The exploratory phase was reopened for two specific team suggestions: Dalya's handcrafted/CNN feature fusion and Helena's signal-to-image CNN2D pipeline. Both have now been evaluated. **CNN64 + F2 → Transformer5** has the highest observed mean fold kappa and pooled Macro-F1; the final team model remains undecided.

| Phase | Evaluation | Current reference or candidate |
|---|---|---|
| Earlier exploration | SC400–SC407; eight subject-wise LOSO folds | F2 on the eight-subject cohort |
| Engineered features | 68 subjects / 133 recordings; fixed subject folds A–E | F2 for single-epoch comparisons; TC1 for controlled temporal comparisons; **TC1 + sigma: 0.755 ± 0.018** |
| Learned EEG features | Same subjects, recordings, test epochs and A–E folds | **CNN + Transformer5: 0.774 ± 0.018**; CNN + LSTM5: 0.766 ± 0.033; single-epoch CNN2D was below CNN1D |
| Hybrid CNN + handcrafted features | Same five-epoch past-only windows as Transformer5; F2 includes EEG, EOG and EMG descriptors | **CNN64 + F2 → Transformer5: 0.779 ± 0.017**, pooled Macro-F1 **0.754** |
| EEG foundation model | Same development data; CBraMod frozen | Logistic regression: **0.6376 ± 0.0246**; MLP64: **0.6366 ± 0.0315**. Neither is shortlisted. |

- **Common evaluation:** 360,621 retained epochs, including Wake, with one out-of-fold prediction per epoch. Folds are split by subject. The ten reserved holdout subjects remain unused.
- **Clearest controlled context result:** keeping the CNN and LSTM architecture fixed, adding up to four prior epochs improved kappa in all five folds (mean gain **+0.0370**) and raised N1 F1 from 0.3872 to 0.4548. Switching the five-epoch head from LSTM to Transformer gave a smaller mean gain (**+0.0078**), mainly in fold A; fold D worsened.
- **New fusion result:** versus Transformer5, pooled kappa rose **0.774 → 0.779** and Macro-F1 **0.748 → 0.754**, with higher kappas in 4/5 folds. This adds manual EEG/EOG/EMG descriptors and a trainable projection; it does not isolate any single source of the gain. Repeat-seed checks and a direct participant-level comparison against Transformer5 are pending. The printed **50-higher / 18-lower** participant counts compare fusion with **F2**.
- **New spectrogram result:** single-epoch CNN2D gave mean fold kappa **0.692 ± 0.034**, below CNN1D's **0.703 ± 0.035**, with lower kappas in 4/5 folds. Observed fit times were **46.6 versus 12.2 min**. This tested configuration is not adopted; the result does not establish that spectrogram models are generally inferior.
- **Other alternatives:** retain the recorded filtering, crop, sigma, AR and CBraMod trade-offs. TC1 + sigma has the highest observed kappa among Vicente's RF runs. Both pooled CBraMod classifiers remain outside the shortlist.
- **Team evidence:** the original EXP-00–03 table remains separate. Helena's newer C2–C13 results, including C11b, and Dalya's reported runs are recorded below with their evidence limits. They are outside Vicente's 19-configuration count.
- **Export and decision status:** the new scores are transcribed from the supplied Colab outputs and confusion figures, which report saved JSON/PNG files and per-fold checkpoints. The new export bytes have not been independently audited. The final all-68 fit, team model commit, `EXPECTED_SCORE.md` commit and holdout predictions remain pending. The latest instructor rules are recorded below.

### Current 68-subject comparison panel

These are Vicente's runs. All completed rows use the same 68 subjects, 133 recordings, A–E test memberships and complete 360,621-epoch test coverage. Only the two crop configurations reduce training epochs. Pooled scores combine all out-of-fold predictions; the fold mean and sample SD give each fold equal weight.

| Experiment | Features | Mean fold kappa ± sample SD | Pooled kappa | Accuracy | Macro-F1 | Balanced accuracy | N1 recall | N1 F1 | Fit time (min) | Current role |
|---|---|---|---|---|---|---|---|---|---|---|
| B0_68_fixed_AE | 11 | 0.728 ± 0.012 | 0.728 | 0.873 | 0.651 | 0.628 | 0.131 | 0.191 | 35.2 | Original baseline |
| F2_68_fixed_AE | 16 | 0.735 ± 0.017 | 0.735 | 0.876 | 0.659 | 0.638 | 0.135 | 0.195 | 46.3 | Reference for isolated comparisons |
| LP40_68_fixed_AE | 16 | 0.736 ± 0.018 | 0.736 | 0.876 | 0.661 | 0.641 | 0.129 | 0.187 | 44.6 | Tested filter; not adopted |
| C1_68_crop30_fixed_AE | 16 | 0.729 ± 0.024 | 0.729 | 0.868 | 0.666 | 0.653 | 0.195 | 0.241 | 20.0 | Training-selection alternative |
| LR1_68_fixed_AE | 16 | 0.592 ± 0.024 | 0.591 | 0.768 | 0.600 | 0.705 | 0.456 | 0.259 | 2.8 | Classifier alternative; not adopted |
| TC1_68_fixed_AE | 33 | 0.751 ± 0.020 | 0.751 | 0.883 | 0.677 | 0.654 | 0.153 | 0.223 | 35.9 | Engineered temporal reference |
| TC1_C1_68_crop30_fixed_AE | 33 | 0.750 ± 0.026 | 0.750 | 0.879 | 0.688 | 0.672 | 0.226 | 0.282 | 14.5 | Training-crop alternative to TC1 |
| SEL40_68_fixed_AE | 16 | 0.736 ± 0.017 | 0.736 | 0.876 | 0.660 | 0.640 | 0.135 | 0.193 | 26.3 | Selective filter; local gain, not adopted |
| TC1_LP40_68_fixed_AE | 33 | 0.751 ± 0.022 | 0.752 | 0.883 | 0.678 | 0.656 | 0.148 | 0.217 | 65.5 | Full EEG filtering with TC1; not adopted |
| TC1_SIGMA_68_fixed_AE | 34 | 0.755 ± 0.018 | 0.756 | 0.885 | 0.681 | 0.658 | 0.157 | 0.230 | 57.3 | Highest mean kappa among Vicente's Random Forest runs |
| TC1_AR16_68_fixed_AE | 33 | 0.753 ± 0.023 | 0.7532 | 0.8838 | 0.6800 | 0.6565 | 0.1621 | 0.2330 | 66.2 | Alternative spectral estimator; small mixed gain |
| CNN1_68_fixed_AE | 64 learned / 1 epoch | 0.703 ± 0.035 | 0.703 | 0.841 | 0.687 | 0.768 | 0.627 | 0.366 | 12.2 | Single-epoch CNN reference |
| CNN1_LSTM1_68_fixed_AE | 64 learned / 1 epoch | 0.7294 ± 0.0299 | 0.729 | 0.858 | 0.706 | 0.773 | 0.6194 | 0.3872 | 2.8 (head) | Control without previous epochs |
| CNN1_LSTM5_68_fixed_AE | 64 learned / up to 5 epochs | 0.7664 ± 0.0335 | 0.765 | 0.879 | 0.739 | 0.804 | 0.6738 | 0.4548 | 2.9 (head) | Matched recurrent context reference |
| CNN1_TRANSFORMER5_68_fixed_AE | 64 learned / up to 5 epochs | 0.7742 ± 0.0180 | 0.774 | 0.883 | 0.748 | 0.806 | 0.6658 | 0.4527 | 4.8 (head) | Direct five-epoch comparator for fusion |
| CBRAMOD_LR_68_fixed_AE | 200 learned / 1 epoch | 0.6376 ± 0.0246 | 0.637 | 0.803 | 0.622 | 0.702 | 0.4618 | 0.2882 | 50.6 (LR) | Linear evaluation of frozen embeddings; not adopted |
| CBRAMOD_MLP64_68_fixed_AE | 200 learned / 1 epoch | 0.6366 ± 0.0315 | 0.636 | 0.803 | 0.626 | 0.698 | 0.4962 | 0.2991 | 1.0 (MLP) | Nonlinear comparison on the same embeddings; not adopted |
| CNN1_F2_TRANSFORMER5_68_fixed_AE | 64 CNN + 16 F2 / epoch; up to 5 epochs | **0.779 ± 0.017** | **0.779** | **0.886** | **0.754** | **0.811** | **0.695** | **0.464** | 5.2 (projection + head) | Highest observed mean kappa; pending stability checks and team selection |
| CNN2D_68_fixed_AE | 1 × 101 × 57 log-PSD; 64 learned / 1 epoch | 0.692 ± 0.034 | 0.691 | 0.837 | 0.677 | 0.747 | 0.585 | 0.354 | 46.6 (STFT + CNN2D) | Spectrogram pipeline; not adopted after comparison with CNN1D |

Reported precision is preserved. No significance or equivalence test or repeat-seed confirmation has been performed for the two additions. Small observed differences are not proof of superiority; fold SD is not a confidence interval for a paired pipeline difference. Fitting times are observations from separate Colab runs, not a controlled benchmark. **Head-only times exclude the original CNN1 training and feature preparation**; fusion's 5.2 min covers the new 80→64 projection and Transformer. CNN2D's 46.6 min includes per-batch STFT and the full CNN2D fit, while CNN1's 12.2 min covers the original full CNN fit. The shared CBraMod extraction time of 3.9 min is excluded from its classifier fit times; LR ran on CPU and MLP on GPU.

## Iteration log

| # | Date | What changed and why | Primary metric with spread | Better than previous? | Decision | Code revision |
|---|---|---|---|---|---|---|
| 1 | 2026-10-22 | Ran the supplied baseline on real Sleep-EDF recordings from three subjects, without changing preprocessing, features or classification, to establish an initial reference. | Mean subject kappa 0.720 (SD 0.119; range 0.589–0.822; 3 subjects / 3 LOSO folds). | Initial real-data baseline. | Retain as the reference for this three-subject cohort; establish a larger development cohort before substantive model selection. | Course source: `5949b723bbd34d172f072446dfcb802ef54b49f7`. Team notebook/log commit has not yet been recorded. |
| 2 (B0) | 2026-10-22 | Expanded the development cohort to eight subjects and reran the unchanged supplied baseline before testing alternatives. | Mean subject kappa 0.824 (SD 0.068; range 0.710–0.896; 8 subjects / 8 LOSO folds). | Not a controlled improvement over iteration 1: the cohort and training-set size changed. | Use as the reference for the fixed eight-subject comparison cohort. | Course source: `5949b723bbd34d172f072446dfcb802ef54b49f7`; personal notebook / team commit not yet recorded. |
| 3 (F1) | 2026-10-22 | Replaced only the five absolute EEG band powers with per-epoch relative powers; retained the other six features and all evaluation settings. | Mean subject kappa 0.828 (SD 0.054; range 0.730–0.885; same 8 subjects / 8 LOSO folds). | Small observed gain vs B0: mean subject kappa +0.004; pooled macro-F1 +0.007, from rounded reported values. | Prefer F1 provisionally after paired/class inspection; keep the B0 reference and document the participant/REM trade-offs. | Course source unchanged; feature transformation supplied in the Colab cell; personal experiment commit not yet recorded. |
| 4 (F2) | 2026-10-22 | Kept the 11 original features and appended only the five per-epoch relative EEG band powers, producing 16 features; same eight-subject evaluation and classifier configuration. | Mean subject kappa 0.837 (SD 0.052; range 0.758–0.897; 8 subjects / 8 LOSO folds). | Highest reported aggregate scores so far: mean subject kappa +0.009 and pooled macro-F1 +0.004 vs F1, from printed values. | Adopt F2 as the development working reference after paired/class/confusion inspection; retain the N1 trade-off. | Course source unchanged; combined-feature construction in Colab; personal experiment commit not yet recorded. |
| 5 (C1) | 2026-10-27 | Cropped training nights to the first–last sleep-labelled epoch plus 30 minutes on each side; retained F2's 16 features and RF. Each held-out subject was evaluated on all original epochs. | Mean subject kappa 0.813 (SD 0.051; range 0.714–0.878; same 8 subjects / 8 LOSO folds). | Lower primary metric than F2 by 0.024; N1 F1 improves from 0.354 to 0.391, while pooled macro-F1 falls from 0.762 to 0.758. | Do not replace F2 with C1 under the declared primary metric. Preserve the minority-recall gains and precision/Wake trade-offs. | Course source unchanged; custom training-only crop/LOSO cell executed in Colab; personal experiment commit not yet recorded. |
| 6 (P1) | 2026-10-27 | Added EEG-only Butterworth low-pass (single-pass order 4, Wn=35 Hz, forward-backward SOS, odd padding per epoch); recomputed F2's 16 features, retaining all epochs, the same LOSO folds and classifier. | Mean subject kappa 0.833 (SD 0.054; range 0.749–0.895; same 8 subjects / 8 LOSO folds). | Small observed loss vs F2: mean subject kappa -0.004 and pooled macro-F1 -0.005; seven subjects worsen and one improves. | Retain F2 after aggregate, class, paired subject and confusion review; P1 increases the displayed N1-to-W confusion. | Course source unchanged; reusable feature helper, versioned per-recording caches and P1 evaluation executed in Colab; P1 JSON save confirmed; personal experiment commit not yet recorded. |
| 7 (B0_68) | 2026-10-29 | Established the original 11-feature baseline on all 68 development subjects using the explicitly defined A–E folds, complete test recordings and per-recording feature caches. | Mean fold kappa **0.728** (sample SD **0.012**; 5 folds / 68 subjects). Pooled kappa 0.728; macro-F1 0.651. | New-cohort reference; not directly comparable with the earlier eight-subject scores. | Retain as the common A–E baseline for subsequent 68-subject strategies. | Course source unchanged; custom fixed-fold evaluator and executed notebook cells; team experiment commit not yet recorded. |
| 8 (F2_68) | 2026-10-29 | Appended five per-epoch relative EEG powers to the cached original 11 features; same 68 subjects, 360,621 test epochs, A–E folds and classifier settings. | Mean fold kappa **0.735** (sample SD **0.017**; same 5 folds). Pooled kappa 0.735; macro-F1 0.659. | Kappa rises in 5/5 folds; mean gain about 0.007. All five pooled stage F1 scores rise; N1 gain is small. | Adopt F2_68 as the provisional reference for further controlled comparisons; keep B0_68 and inspect signals before choosing filters. | Course source unchanged; F2 feature version 1 and reusable fixed-fold evaluator; per-fold completion logs supplied; consolidated F2 JSON/PNG export subsequently confirmed; team experiment commit not yet recorded. |
| 9 (LP40_68) | 2026-10-29; closure confirmed 2026-10-31 | After spectral inspection, added an EEG-only 40-Hz Butterworth low-pass and recomputed F2's 16 features; same A–E folds, test epochs and RF settings. | Mean fold kappa **0.736** (sample SD **0.018**; 5 folds). Pooled kappa 0.736; macro-F1 0.661. | Small aggregate gain vs F2, but only 3/5 folds and 29/68 subjects improve; N1 F1 falls from 0.195 to 0.187. | **Keep F2_68 as reference.** Preserve LP40 as a justified alternative with mixed results; evaluation, review and export complete. | Course source unchanged; LP40 processing/feature versions 1; 133 feature caches and five fold reports completed; consolidated JSON/PNG saves confirmed; team experiment commit not yet recorded. |
| 10 (C1_68) | 2026-10-31 | Reused F2's 16 features; removed only training Wake outside each recording's first–last sleep interval plus 30-minute original-time margins. Same A–E folds, complete test epochs and RF. | Mean fold kappa **0.729** (sample SD **0.024**; 5 folds). Pooled kappa 0.729; macro-F1 0.666; balanced accuracy 0.653. | Lower primary kappa by about 0.006; higher N1 F1 by 0.046. Kappa rises in 1/5 folds and 36/68 subjects; five fits take 20.0 minutes. | **Keep F2_68 as reference.** Preserve C1's minority-recall/speed gains and precision/Wake trade-offs; review and export complete. | Course source unchanged; selection version 1; original timing/label alignment checked for 133 recordings; five fold reports and consolidated JSON/PNG saves confirmed; team experiment commit not yet recorded. |
| 11 (LR1_68) | 2026-10-31 | Replaced only F2's Random Forest with balanced L2 logistic regression (C=1, lbfgs, max_iter=2000, tol=1e-4). Same 16 features, full epochs and A–E folds. | Mean fold kappa **0.592** (sample SD **0.024**; 5 folds). Pooled kappa 0.591; macro-F1 0.600; balanced accuracy 0.705. | Kappa falls in 5/5 folds and 63/68 subjects. N1 F1 rises to 0.259, but the other four stage F1 scores fall. Five fits take 2.8 minutes. | **Keep F2_68 with Random Forest.** Preserve LR1's speed/recall gains and false-positive costs; review and export complete. | Course source unchanged; same cached F2 matrix; all five fits completed in 147–169 iterations; per-fold and consolidated JSON/PNG saves confirmed; team experiment commit not yet recorded. |
| 12 (TC1_68) | 2026-11-02 | Added one previous consecutive epoch's 16 signal features plus an availability flag to current F2 features; 33 columns, past only, same recording/gap rules, RF and full A–E training/test sets. | Mean fold kappa **0.751** (sample SD **0.020**); pooled kappa 0.751; macro-F1 0.677. | Kappa rises in 5/5 folds and 62/68 subjects versus F2; pooled macro-F1 +0.018. N1 recall/F1 rise to 0.153/0.223. | **Adopt TC1_68 as the individual primary-metric working reference.** Keep F2 for isolated 16-feature comparisons; final team method remains open. | Course SHA unchanged; TC1 feature version 1; original-time adjacency checks; five fold completions and consolidated JSON/PNG saves supplied; team experiment commit not recorded. |
| 13 (TC1_C1_68) | 2026-11-02 | Revisited training-only Wake cropping with TC1's already-built 33-feature context matrix; kept sleep-window margins at 30 minutes and all A–E test epochs. | Mean fold kappa **0.750** (sample SD **0.026**); pooled kappa 0.750; macro-F1 **0.688**. | Primary mean kappa about -0.001 versus TC1, but macro-F1 +0.011, balanced accuracy +0.018 and N1 F1 +0.060 as printed. Kappa rises in 39/68 subjects. | **Keep TC1 as the kappa reference; preserve TC1 + crop as the Macro-F1/N1 alternative.** This is a completed combination, not an assumed sum of earlier effects. | Same course source, TC1 v1 and original-time crop rule; context built before training selection; five fold completions and consolidated JSON/PNG saves supplied; team commit not recorded. |
| 14 (SEL40_68) | 2026-11-02; diagnosis consolidated 2026-11-04 | Applied the existing EEG-only LP40 recipe selectively when the epoch's 48–50 / 0.5–50-Hz power fraction is at least 10%; same F2 16-feature recipe, RF and full A–E sets. | Mean fold kappa **0.736** (sample SD **0.017**); pooled kappa 0.736; macro-F1 0.660. | Global gains versus F2 are about +0.001 kappa and Macro-F1; N1 F1 slightly lower. Selected-epoch kappa/Macro-F1 improve to 0.538/0.515, but five of the ten most-selected nights worsen. | **Do not adopt SEL40 as the reference.** Preserve the local benefits and mixed per-night effects. The later full LP40 + TC1 comparison is separate (iteration 15). | Selection/ratio version 1; 133 ratio records, 25,446 selected epochs and 74 validated LP40 cache reuses; JSON/PNG and later diagnostics-save messages supplied; team commit not recorded. |
| 15 (TC1_LP40_68) | 2026-11-10 | Added the existing EEG-only LP40 to every epoch used by TC1; reused the 133 original LP40 feature caches. Same 33 feature columns, full training/test epochs, RF and A–E folds. | Mean fold kappa **0.751** (sample SD **0.022**; 5 folds); pooled kappa 0.752. | Mean kappa is unchanged at three decimals. Pooled Macro-F1 +0.001; N1 F1 0.223 → 0.217. Fold changes are mixed; five fits took 65.5 min versus 35.9 min for TC1. | **Retain TC1 without LP40.** The filter did not give a clear global benefit in the temporal pipeline. | Same pinned course SHA, TC1 v1 and LP40 v1 caches; five completed folds and consolidated JSON/PNG saves recorded. Team experiment commit not recorded. |
| 16 (TC1 + sigma) | Recorded 2026-11-14 | Added one within-epoch STFT sigma concentration feature to TC1; tested whether short sigma events improve staging and reduce N1–N2 confusion. | Mean fold kappa 0.755 ± 0.018; pooled kappa 0.756; Macro-F1 0.681. | Higher kappa in 5/5 folds and 48/68 subjects versus TC1, but N1 → N2 rose from 29.12% to 29.55%. | Keep as the best observed RF result by mean kappa; retain TC1 as the simpler reference. | STFT v1 notebook cells 5.2–5.6; JSON/PNG saves reported; team experiment commit not recorded. |
| 17 (TC1 + AR16) | Recorded 2026-11-14 | Replaced only the five absolute and five relative band-power features per current/previous epoch with Burg AR(16) estimates; retained the other TC1 features and tested an alternative to Welch. | Mean fold kappa 0.753 ± 0.023; pooled kappa 0.7532; Macro-F1 0.6800. | Pooled kappa +0.0018 versus TC1; mixed folds and 39/68 subjects higher. N1 F1 rose from 0.2227 to 0.2330. | Keep Welch as the spectral reference; preserve AR's class trade-offs. | Burg AR(16) v1 notebook cells 5.7–5.10; JSON/PNG saves reported; team experiment commit not recorded. |
| 18 (CNN1) | 2026-11-14 | Trained a compact 1D CNN on one raw EEG Fpz-Cz epoch to test learned features on the same A–E split. | Mean fold kappa 0.703 ± 0.035; pooled kappa 0.703; Macro-F1 0.687. | Below F2 in kappa by 0.032; N1 recall rose from 0.135 to 0.627, with many more false N1 calls. F2 also uses EOG and EMG. | Retain as the learned single-epoch baseline and source of frozen features for the sequence models. | Notebook cells 5.11–5.14; five CNN checkpoints and JSON/PNG saves reported; team experiment commit not recorded. |
| 19 (CNN + LSTM1) | 2026-11-14 | Trained a separate LSTM head on 64 frozen fold-specific CNN features; gave it only the current epoch to control for changing the prediction head. | Mean fold kappa 0.7294 ± 0.0299; pooled kappa 0.729; Macro-F1 0.706. | Higher than CNN1 in every fold, but mean kappa remains below F2. | Use as the control for the context comparison; this iteration alone does not demonstrate a context gain. | Notebook cells 5.15–5.16; five head checkpoints and JSON/PNG saves reported; team experiment commit not recorded. |
| 20 (CNN + LSTM5) | 2026-11-14 | Used the same frozen CNN, LSTM and training settings as LSTM1 with up to four consecutive earlier epochs; retained shorter sequences at recording starts and gaps. | Mean fold kappa 0.7664 ± 0.0335; pooled kappa 0.765; Macro-F1 0.739. | Mean kappa +0.0370 versus LSTM1; 5/5 folds improve. N1 F1 +0.0676 and fewer false N1 from Wake and N2. | Carry forward as the direct comparator for the Transformer. | Notebook cells 5.15–5.16; five head checkpoints and JSON/PNG saves reported; team experiment commit not recorded. |
| 21 (CNN + Transformer5) | 2026-11-14 | Replaced the LSTM5 head with one Transformer encoder layer, four attention heads and learned relative-to-current positions; same CNN weights, context and training settings. | Mean fold kappa 0.7742 ± 0.0180; pooled kappa 0.774; Macro-F1 0.748. | Mean kappa +0.0078 versus LSTM5; 4/5 folds higher, mainly fold A (+0.035); fold D lower. N1 F1 falls by 0.0021. | Leading development candidate; keep LSTM5 and the RF references for team review. | Notebook cells 5.17–5.18; five head checkpoints and JSON/PNG saves reported; team experiment commit not recorded. |
| 22 (CBraMod + LR) | 2026-11-14 | Averaged the frozen CBraMod patch embeddings, then trained fold-fitted scaling and balanced L2 logistic regression to test whether the representations separate sleep stages with a linear classifier. | Mean fold kappa 0.6376 ± 0.0246; pooled kappa 0.637; Macro-F1 0.622. | Lower kappa in 5/5 folds versus CNN1 (mean delta −0.0656); pooled N1 F1 0.2882 versus 0.3664. | Preserve the completed linear evaluation. Keep Transformer5 as the leading candidate. | Notebook cells 5.19–5.21; upstream code and checkpoint revisions below; five fold reports and consolidated JSON/PNG saves reported; team experiment commit not recorded. |
| 23 (CBraMod + MLP64) | 2026-11-15 | Recovered the exact same 200 frozen embeddings used by LR. Replaced the linear classifier with a 64-unit ReLU MLP to test whether nonlinear classification helps, using the same fold-fitted scaler and class-balancing rule. | Mean fold kappa 0.6366 ± 0.0315; pooled kappa 0.636; Macro-F1 0.626. | Mean fold kappa −0.0010 versus LR (3/5 folds improve); N1 F1 +0.0109. Both CBraMod variants are below CNN1 on mean kappa. | Keep as the last exploratory comparison; neither CBraMod head enters the shortlist. | Notebook cells 5.22–5.23; existing feature cache verified against the LR report; five fold completions and consolidated JSON/PNG saves supplied; team experiment commit not recorded. |
| 24 (CNN64 + F2 + Transformer5) | 2026-11-19 | Tested Dalya's fusion proposal using 64 frozen fold-specific CNN features plus 16 fold-standardized F2 features per epoch; trainable Linear(80,64) and the existing five-epoch Transformer design. | Mean fold kappa 0.779 ± 0.017; pooled kappa 0.779; Macro-F1 0.754. | Pooled kappa +0.005 and Macro-F1 +0.006 vs Transformer5; kappa higher in 4/5 folds. N1 F1 about 0.453 → 0.464; N2 recall about 0.716 → 0.703. | Leading observed candidate, pending paired participant review, stability checks and team selection. The 33-feature TC1 fusion was not tested. | Notebook cells 5.24–5.25; five head fits, saved per-fold scaler statistics and JSON/PNG exports reported; team experiment commit not recorded. |
| 25 (CNN2D) | 2026-11-19 | Tested Helena's spectrogram proposal: full 30-second Fpz-Cz epochs converted to fixed log-PSD STFT matrices; new single-epoch CNN2D trained from scratch with CNN1D's training recipe and folds. | Mean fold kappa 0.692 ± 0.034; pooled kappa 0.691; Macro-F1 0.677. | Pooled kappa −0.012 and Macro-F1 −0.010 vs single-epoch CNN1D; kappa lower in 4/5 folds. Observed fit time 46.6 vs 12.2 min. | Completed, not adopted in this configuration and 12-pass budget. Retain as a negative pipeline result; fusion remains the leading candidate. | Notebook cells 5.26–5.27; PSD/gradient pilot passed; five full CNN2D checkpoints and JSON/PNG exports reported; team experiment commit not recorded. |

Course starter code used in Colab: `5949b723bbd34d172f072446dfcb802ef54b49f7`. Notebook cells and upstream revisions identify implementation evidence; they are not team commits. Add the actual team commit after saving the executed code and this log in the repository.

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

**Eight-subject comparison budget at the P1 checkpoint:** 5 of at most 12 configurations evaluated: B0, F1, F2, C1 and P1. Seven remain. The three-subject pilot and label/quality diagnostics remain outside this count. The team's final pipeline, final-model commit and EXPECTED_SCORE.md registration remain future work.

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

## 68-subject phase — protocol revision, 2026-10-29

### Scope and cohort decision

Following team discussion, work moved from the small exploratory cohort to all **68 available development subjects**, with **133 recordings**. The first eight subjects were a convenient initial subset, not an instructor-required or demonstrably representative sample. Their five completed configurations remain useful exploratory evidence; repeating every earlier configuration on the larger cohort is not automatic.

A new unchanged baseline was evaluated before adopting any eight-subject candidate in this phase. Both B0_68 and F2_68 are newly trained 68-subject cross-validation experiments. No fitted model from the eight-subject phase was transferred.

The earlier at-most-12-configuration plan referred to the fixed eight-subject exploration; five configurations were completed there. **Updated checkpoint, 2026-10-31:** the active 68-subject phase has five completed configurations: B0_68, F2_68, LP40_68, C1_68 and LR1_68. Across both development cohorts, ten cohort/configuration evaluations are recorded, plus the separate pilot. B0/F2 and the training-crop strategy were evaluated on both overlapping cohorts; C1's margin implementation also changed as documented. These are not ten independent methods or holdout results. Five fits for one A–E strategy count as one configuration, not five methods. No replacement numerical comparison budget is retrospectively claimed; record each next candidate before fitting. **Update, 2026-11-04:** TC1_68, TC1_C1_68 and SEL40_68 bring the active phase to eight completed configurations (13 cohort/configuration evaluations across the eight- and 68-subject phases, plus the separate pilot). The five fold fits per strategy are not five different methods; colleagues' unverified-protocol experiments are not included in this count.

### Exact fixed A–E assignment

These are the **test subjects** for each fold. Training uses the other four lists. All nights of one participant remain together. Every development subject is tested exactly once; within each fold the training and test subject sets are disjoint.

| Test fold | Subject IDs |
|---|---|
| A | SC400, SC405, SC411, SC417, SC422, SC428, SC434, SC441, SC446, SC452, SC458, SC463, SC471, SC477 |
| B | SC401, SC406, SC412, SC418, SC423, SC429, SC435, SC442, SC447, SC453, SC459, SC465, SC473, SC481 |
| C | SC402, SC407, SC413, SC419, SC425, SC430, SC436, SC443, SC449, SC454, SC460, SC466, SC474, SC482 |
| D | SC403, SC409, SC414, SC420, SC426, SC431, SC437, SC444, SC450, SC455, SC461, SC467, SC475 |
| E | SC404, SC410, SC415, SC421, SC427, SC433, SC438, SC445, SC451, SC457, SC462, SC470, SC476 |

| Fold | Train subjects | Test subjects | Test recordings | Train epochs | Test epochs |
|---|---|---|---|---|---|
| A | 54 | 14 | 27 | 286,790 | 73,831 |
| B | 54 | 14 | 28 | 285,309 | 75,312 |
| C | 54 | 14 | 26 | 290,405 | 70,216 |
| D | 55 | 13 | 26 | 290,337 | 70,284 |
| E | 55 | 13 | 26 | 289,643 | 70,978 |

The five test-epoch counts sum to **360,621**. The notebook assembled the feature tables and checked the subject set, exclusion of final holdout subjects, feature finiteness, train/test subject separation and exactly-once test coverage. The explicit indices are stored in `SPLITS_68`; they are reused for all controlled comparisons.

The original `track.evaluate` automatically uses LOSO for at most 12 groups and a five-fold `GroupKFold` for larger cohorts. It does not directly accept the selected A–E memberships. The 68-subject runs therefore use a custom loop over `SPLITS_68`, with a new scaler/classifier pipeline in every fold. Calling the original evaluator on the 68 subjects would not by itself guarantee this named assignment.

Final holdout subjects, excluded from these experiments: **SC408, SC416, SC424, SC432, SC440, SC448, SC456, SC464, SC472, SC480**.

### Colleague's earlier five-fold assignment

Vicente supplied a colleague's train/test subject lists produced before A–E was defined. Checking those lists showed the same 68 development subjects, no train/test subject overlap within a fold, one test appearance per subject and no reserved holdout subjects. This verifies the separation in the supplied lists, not every fitting step of the colleague's unseen pipeline.

Their earlier **test** memberships were:

| Earlier fold | Train subjects | Test subjects | Test subject IDs |
|---|---|---|---|
| 1 | 55 | 13 | SC403, SC407, SC415, SC434, SC435, SC438, SC445, SC449, SC454, SC457, SC466, SC467, SC474 |
| 2 | 54 | 14 | SC405, SC409, SC413, SC420, SC425, SC429, SC441, SC442, SC455, SC458, SC465, SC470, SC473, SC482 |
| 3 | 54 | 14 | SC402, SC411, SC412, SC414, SC418, SC421, SC426, SC427, SC430, SC431, SC436, SC437, SC459, SC462 |
| 4 | 55 | 13 | SC401, SC406, SC417, SC433, SC443, SC444, SC446, SC447, SC451, SC453, SC461, SC475, SC477 |
| 5 | 54 | 14 | SC400, SC404, SC410, SC419, SC422, SC423, SC428, SC450, SC452, SC460, SC463, SC471, SC476, SC481 |

These groups differ from A–E and cannot be made equivalent just by renaming fold numbers as letters. For example, SC403 and SC407 are together in earlier fold 1 but are in D and C under A–E. The lists alone do not establish that subjects were randomly shuffled.

Experiments confirmed to use these earlier lists must remain labelled as using the **previous five-fold subject split**. They can be compared within that protocol if test epochs and fitting procedures also match. The later EXP-00–EXP-03 table has not yet been linked to either these lists or A–E; its current fold membership remains **unconfirmed**. Direct comparisons with this log's A–E results require matching actual test-subject memberships and evaluation epochs. Changing only the split can reuse fixed per-recording features; training-fold-fitted steps and models must be fitted again. No colleague result is silently relabelled as A–E in this log.

### Download and persistent-folder checkpoint

- The download was resumed in the existing `/content/drive/MyDrive/CM2013_data/train` folder and completed for 68 subjects and 133 PSG/Hypnogram pairs.
- A read-only inventory found **266 EDF files, 6.151 GiB**, with all 133 matching annotation files and no repeated EDF basenames inside `train`.
- At that pre-feature-preparation checkpoint there were two parsed-record caches (4.090 GiB), 32 existing processing/feature caches (0.996 GiB) and three result JSON files (0.011 GiB). These are historical inventory values, not a new size measurement after the 68-subject runs.
- Dataset EDFs, parsed-record caches, feature caches and result reports have different purposes. No cache/data deletion or migration was part of the continuation.
- The notebook was organised into session setup, archived eight-subject work and the active 68-subject phase. The later 68-subject code was added through successive chat cells; the newly executed notebook has not yet been supplied as a fresh upload.
- No whole-cohort parsed cache was built for this phase. Processing reads one recording at a time.

### Per-recording baseline feature preparation

`preparar_b0_gravacao(psg)` uses a temporary local directory with links to the existing PSG/Hypnogram pair, loads that one night at **100 Hz / 30-second epochs**, and applies the original identity-preprocessing / 11-feature Welch recipe. It returns only the record ID, feature matrix, labels, subject groups and feature names. No EDF copy or full parsed-record array is placed in the new feature cache.

- Cache step: `viggy_b0_features`, under `/content/drive/MyDrive/CM2013_data/cache/viggy`.
- `B0_FEATURE_VERSION = 1`.
- Cache key: feature version, pinned course revision, loading settings, baseline processing/feature recipe, Python/NumPy/SciPy/MNE runtime versions, and each source file's name, byte size and nanosecond modification time.
- The cache is independent of the classifier and validation-fold choice. Changing those does not require repeating the same fixed feature calculations.
- No scaler, learned feature selection, resampling or fitted classifier is cached across folds.
- The first test, SC4001E0 / SC400, produced **2,650 epochs × 11 features** in **75.2 seconds**, saved as `_cache_viggy_b0_features_70271cb6daa7.pkl`.
- In the subsequent 133-record loop, that entry was reused and the other **132** entries were computed and saved. The loop took **112.5 minutes**, excluding the earlier standalone first-record computation.
- Completion: **68 subjects, 133 recordings, 360,621 epochs, 11 features**. The feature tables were concatenated into `X_b0_68`, `y_b0_68`, `groups_b0_68` and `record_ids_b0_68`.
- Feature matrices passed finite-value and alignment checks. These checks are not a raw-signal artifact audit of all 133 nights.

### Common retained-label distribution

| Stage | Epochs | Share |
|---|---|---|
| W | 248,341 | 68.86% |
| N1 | 17,877 | 4.96% |
| N2 | 60,494 | 16.77% |
| N3 | 11,610 | 3.22% |
| REM | 22,299 | 6.18% |

The counts sum to 360,621. The supplied loader merges old stages 3/4 into N3 and excludes Movement/Unknown epochs. Wake is retained throughout evaluation. All five completed 68-subject strategies use exactly these labels and test epochs; C1 changes training selection only.

## Iteration 7 (B0_68) — original baseline on the fixed A–E folds

**Status: all five folds completed; pooled and per-stage results and the confusion figure supplied by Vicente on 2026-10-29.**

### Pipeline, execution and timing

- `X_b0_68.shape == (360621, 11)`; 68 subjects and 133 recordings.
- Original five absolute EEG band powers, three EEG Hjorth parameters, EEG spectral entropy, EOG movement and EMG RMS.
- Supplied Welch feature estimator, identity preprocessing, no added high-pass/low-pass/notch, no training crop and no added feature selection.
- Fresh `StandardScaler → RandomForestClassifier` pipeline per fold: **200 trees, class_weight="balanced", random_state=0**. CPU parallelism was set to `n_jobs=-1`; the other baseline model settings were retained.
- Scaling and class weights/model fitting use only the training subjects. The complete test recordings are predicted; no test-label-derived crop is applied.
- Fold A was timed first and saved. The subsequent loop loaded A and trained B–E, checking saved-result metadata, test indices, true labels and subject groups before reuse.
- Per-fold outputs contain the course revision, runtime metadata, feature version/names, A–E assignment, recording/epoch manifest, model/scaler parameters, train/test subjects, test row indices, timings and full prediction/report arrays.
- Exact runtime versions for this active phase have not been separately transcribed from the JSONs. Do not assign the older Python 3.13.16 runtime block to these runs without checking their saved metadata.

| Fold | Kappa | Macro-F1 | Accuracy | Balanced accuracy | Training min |
|---|---|---|---|---|---|
| A | 0.743 | 0.667 | 0.881 | 0.661 | 6.953 |
| B | 0.716 | 0.642 | 0.861 | 0.629 | 7.104 |
| C | 0.730 | 0.643 | 0.874 | 0.612 | 7.011 |
| D | 0.715 | 0.636 | 0.873 | 0.597 | 7.118 |
| E | 0.737 | 0.658 | 0.874 | 0.633 | 7.025 |

**Reported primary result: mean fold kappa 0.728 ± 0.012**, using the sample SD (`ddof=1`) across the five folds. Total training time is approximately **35.2 minutes**, counting A once. Fold A's initial printed prediction time was 2.2 seconds.

Fold metrics and timings above preserve the supplied three-decimal display precision. The mean/SD came from the unrounded values in Colab; rounding should not be used to invent more precise estimates.

### Pooled out-of-fold panel

All 360,621 epochs were assigned exactly one test prediction in their original row order before the joint report was computed.

| Metric | Pooled value |
|---|---|
| Cohen's kappa | 0.728 |
| Macro-F1 | 0.651 |
| Accuracy | 0.873 |
| Balanced accuracy | 0.628 |

| Stage / aggregate | Precision | Recall | F1 | Support |
|---|---|---|---|---|
| W | 0.937 | 0.980 | 0.958 | 248,341 |
| N1 | 0.352 | 0.131 | 0.191 | 17,877 |
| N2 | 0.751 | 0.809 | 0.779 | 60,494 |
| N3 | 0.828 | 0.667 | 0.739 | 11,610 |
| REM | 0.623 | 0.553 | 0.586 | 22,299 |
| Macro average | 0.698 | 0.628 | 0.651 | 360,621 |
| Support-weighted average | 0.854 | 0.873 | 0.860 | 360,621 |

These pooled metrics are computed from all test predictions together, not by averaging the five printed fold metrics. In particular, mean fold macro-F1 and pooled macro-F1 are different quantities. The course report also retains per-subject panels; no numerical SD across 68 individual subjects was supplied here.

### Confusion inspection

Source: the baseline confusion figure supplied as `image(20261029-144624).png`. Rows are true stages, columns predicted stages, normalized within each true stage. Values below are the figure's three-decimal values.

| True stage | Predicted W | Predicted N1 | Predicted N2 | Predicted N3 | Predicted REM |
|---|---|---|---|---|---|
| W | 0.980 | 0.007 | 0.009 | 0.001 | 0.004 |
| N1 | 0.413 | 0.131 | 0.311 | 0.002 | 0.143 |
| N2 | 0.082 | 0.022 | 0.809 | 0.022 | 0.064 |
| N3 | 0.074 | 0.001 | 0.255 | 0.667 | 0.004 |
| REM | 0.142 | 0.059 | 0.243 | 0.002 | 0.553 |

Rounded rows can differ slightly from a sum of one; the entries are not exact integer counts. No counts are reconstructed by multiplying rounded rates by class supports.

### Interpretation and decision

Wake represents 68.86% of the retained data and has recall 0.980. Accuracy 0.873 therefore needs to be read with macro-F1, balanced accuracy and the stage panel.

N1 is the main weakness: recall 0.131 and F1 0.191; about 41.3% of N1 epochs are predicted as Wake and 31.1% as N2. N3-to-N2 and REM-to-N2 confusions are about 25.5% and 24.3%. N3 has fewer retained examples than N1 but substantially higher recall, illustrating that class frequency alone does not explain the difference. Class weighting was already enabled.

**Decision:** use B0_68 as the fixed A–E reference. Its lower score than the eight-subject baseline is not a controlled change in pipeline quality: the evaluated subjects, training-set sizes and folds differ. No filter, crop or classifier alternative is selected from this baseline matrix alone.

### Output status

- `experiments/B0_68_fixed_AE_fold_A.json`: an explicit successful save path was supplied after the A run.
- `experiments/B0_68_fixed_AE_fold_B.json` through `...fold_E.json`: the supplied loop saves each file before printing the reported completion; all four completion messages were supplied.
- The full pooled report and baseline figure were computed and shown.
- The archived executed notebook records successful saves of `experiments/B0_68_fixed_AE.json` and `experiments/B0_68_fixed_AE_confusion.png`; this resolves the earlier pending save confirmation.
- The exported JSON bytes were not uploaded for independent inspection; reported execution and outputs, rather than a local rerun, are the evidence recorded here.

## Iteration 8 (F2_68) — original plus relative powers on the same A–E folds

**Status: all five folds and pooled/class/confusion diagnostics completed; consolidated JSON/PNG saves subsequently confirmed. F2_68 remains the working reference after the LP40 comparison.**

### Hypothesis and single controlled change

The earlier small-cohort work motivated checking whether relative EEG powers provide useful complementary information alongside the absolute powers on the larger cohort. The same feature strategy is evaluated with newly trained models on the 68 development subjects; this is not reuse of an eight-subject fitted model.

- Start from the cached original matrix `X_b0_68` and preserve all 11 original columns.
- Append five relative powers: delta, theta, alpha, sigma and beta.
- For each epoch, divide each absolute band power by the sum of those five band powers (0.5–30 Hz under the original definitions).
- If the denominator is zero, all five relative values are zero. Reject non-finite or negative input powers.
- No labels, fitted statistics, other epochs or other participants enter this transformation. The scaler is still fitted inside each training fold.
- `F2_FEATURE_VERSION = 1`; `X_f2_68.shape == (360621, 16)`.
- Labels, subject groups, record order, complete test epochs, fixed A–E indices and baseline model/scaler settings remain the same. No signal filter or training crop is added.
- F2 preparation uses the existing feature table; it does not reread EDFs or create another whole-cohort parsed cache. Five new classifier fits are still required.

The reusable `avaliar_experiencia_68` function clones the baseline pipeline per fold, verifies that the test indices match B0_68, saves each result via a temporary file and supports reuse only after checking metadata and prediction alignment. In the supplied F2 execution, all five folds were newly trained.

### Reported fold results

| Fold | Kappa | Macro-F1 | Accuracy | Balanced accuracy | Training min |
|---|---|---|---|---|---|
| A | 0.753 | 0.679 | 0.885 | 0.676 | 9.232 |
| B | 0.718 | 0.647 | 0.862 | 0.636 | 9.083 |
| C | 0.739 | 0.652 | 0.878 | 0.622 | 9.248 |
| D | 0.717 | 0.638 | 0.875 | 0.598 | 9.350 |
| E | 0.748 | 0.673 | 0.879 | 0.653 | 9.364 |

**Reported primary result: mean fold kappa 0.735 ± 0.017**, sample SD across five folds. Total training time is approximately **46.3 minutes**, about **11.1 minutes** more than B0_68 in these runs. This is an observed runtime comparison, not a guaranteed speed ratio on another session or machine.

| Fold | B0_68 kappa | F2_68 kappa | Difference, as printed |
|---|---|---|---|
| A | 0.743 | 0.753 | +0.010 |
| B | 0.716 | 0.718 | +0.002 |
| C | 0.730 | 0.739 | +0.009 |
| D | 0.715 | 0.717 | +0.002 |
| E | 0.737 | 0.748 | +0.011 |

All five folds improve. Gains are larger in A/C/E than B/D, and the observed between-fold SD increases. These paired fold results do not show that every one of the 68 individual participants improves and do not establish statistical significance.

### Pooled metrics and class results

The `juntar_previsoes_68` helper checks fold identities, true labels, subject groups, prediction lengths and exactly-once coverage, then reconstructs the joint report in the original row order. Every original valid epoch, including Wake, remains in the evaluation.

| Metric | B0_68 | F2_68 | Difference from rounded outputs |
|---|---|---|---|
| Mean fold kappa | 0.728 | 0.735 | +0.007 |
| Fold kappa sample SD | 0.012 | 0.017 | +0.005 |
| Pooled kappa | 0.728 | 0.735 | +0.007 |
| Pooled macro-F1 | 0.651 | 0.659 | +0.008 |
| Pooled accuracy | 0.873 | 0.876 | +0.003 |
| Pooled balanced accuracy | 0.628 | 0.638 | +0.010 |
| Total training min, approximate | 35.2 | 46.3 | +11.1 |

| Stage / aggregate | Precision | Recall | F1 | Support |
|---|---|---|---|---|
| W | 0.939 | 0.980 | 0.959 | 248,341 |
| N1 | 0.351 | 0.135 | 0.195 | 17,877 |
| N2 | 0.761 | 0.813 | 0.786 | 60,494 |
| N3 | 0.838 | 0.681 | 0.751 | 11,610 |
| REM | 0.631 | 0.581 | 0.605 | 22,299 |
| Macro average | 0.704 | 0.638 | 0.659 | 360,621 |
| Support-weighted average | 0.857 | 0.876 | 0.863 | 360,621 |

| Stage | Recall B0 | Recall F2 | F1 B0 | F1 F2 | F1 difference, as printed |
|---|---|---|---|---|---|
| W | 0.980 | 0.980 | 0.958 | 0.959 | +0.001 |
| N1 | 0.131 | 0.135 | 0.191 | 0.195 | +0.004 |
| N2 | 0.809 | 0.813 | 0.779 | 0.786 | +0.007 |
| N3 | 0.667 | 0.681 | 0.739 | 0.751 | +0.012 |
| REM | 0.553 | 0.581 | 0.586 | 0.605 | +0.019 |

All five stage F1 scores improve. This does not mean that every class metric rises: N1 precision changes from 0.352 to 0.351, while its recall increases only from 0.131 to 0.135. The larger F1 gains are REM (+0.019) and N3 (+0.012).

### Confusion inspection

Source: `image(20261029-161643).png`, supplied after the pooled F2 report. Same true-row / predicted-column order and common 0–1 colour scale as B0. Values are transcribed at the displayed three-decimal precision.

| True stage | Predicted W | Predicted N1 | Predicted N2 | Predicted N3 | Predicted REM |
|---|---|---|---|---|---|
| W | 0.980 | 0.007 | 0.009 | 0.001 | 0.004 |
| N1 | 0.412 | 0.135 | 0.303 | 0.002 | 0.149 |
| N2 | 0.077 | 0.023 | 0.813 | 0.022 | 0.064 |
| N3 | 0.066 | 0.000 | 0.249 | 0.681 | 0.005 |
| REM | 0.138 | 0.061 | 0.217 | 0.002 | 0.581 |

N1-to-W is almost unchanged (0.413 → 0.412); N1-to-N2 declines (0.311 → 0.303) and N1-to-REM rises (0.143 → 0.149). REM-to-N2 declines from 0.243 to 0.217, alongside improved correct REM recognition (0.553 → 0.581). N3 recall rises from 0.667 to 0.681.

These are comparisons of rounded row proportions, not paired tracing of individual epochs between prediction categories. A displayed 0.000 does not prove that the exact count is zero.

### Decision

**Retain F2_68 as the provisional reference for subsequent 68-subject A–E comparisons.** The primary mean kappa is about 0.007 higher, pooled macro-F1 rises by 0.008 and all five stage F1 values rise, at the cost of extra training time. Keep B0_68 as the unchanged baseline.

N1 remains the main weakness (recall 13.5%, F1 0.195). The matrix does not by itself identify an artifact mechanism or demonstrate that a filter or Wake crop would fix the errors. At the original F2 checkpoint, the next step was signal/spectrum inspection before choosing filters. That inspection and the subsequent LP40 experiment are documented below; no 68-subject training-crop experiment has yet run.

### Output status — updated 2026-10-31

- Individual `experiments/F2_68_fixed_AE_fold_A.json` through `...fold_E.json` were saved before the supplied completion messages.
- The pooled report, stage comparison and confusion figure were computed and shown.
- After the previous log update, Vicente explicitly confirmed:
  - `/content/drive/MyDrive/CM2013_data/experiments/F2_68_fixed_AE.json`
  - `/content/drive/MyDrive/CM2013_data/experiments/F2_68_fixed_AE_confusion.png`
- This supersedes the pending-export status. File saves are confirmed by the Colab messages. The uploaded F2 JSON predictions and confusion counts were subsequently checked in the 2026-11-10 paired review.
- The course reports retain predictions and subject/fold panels. No all-68 final fit, holdout predictions, final-model commit or `EXPECTED_SCORE.md` registration are part of these completed runs.

## 68-subject signal and spectrum inspection — 2026-10-29

### Selection and scope

Before choosing a filter, participants with the lowest, middle and highest F2_68 out-of-fold subject kappas were selected. Subject ID broke ties; the middle position was `n // 2`. The first available record ID for each was inspected.

| Selection | Subject | F2 subject kappa | Selected night | Retained epochs | N1 epochs |
|---|---|---|---|---|---|
| Lowest | SC461 | 0.241 | SC4611E0 | 2,644 | 123 |
| Middle | SC453 | 0.763 | SC4531E0 | 2,602 | 124 |
| Highest | SC414 | 0.905 | SC4141E0 | 2,756 | 29 |

Subject kappas pool each participant's evaluated recordings; they are **not** kappas for the single selected nights. SC461/SC414 are in test fold D; SC453 is in B. These performance-selected diagnostic examples are not a representative sample of all 68 participants or an independent validation set.

One PSG/Hypnogram pair was read at a time through temporary links to the persistent source files. No full-cohort raw array or new EDF copy was created.

### SC4611E0 time traces and checks

- Retained epochs: **2,644**; EEG epochs with NaN/Inf: **0**; fully constant EEG epochs: **0**.
- W/N1 examples were chosen near their within-stage median peak-to-peak amplitudes:

| True stage | Retained epoch index | F2 prediction | Peak-to-peak EEG, µV |
|---|---|---|---|
| W | 1,593 | W | 199.789 |
| N1 | 1,798 | W | 143.024 |

Indices refer to retained epochs after Movement/Unknown exclusion, not uninterrupted elapsed time. N1 showed a conspicuous component near 49–50 Hz; W showed large slower excursions. Neither observation alone identifies an artifact cause or explains the prediction.

Finite/constant checks do not establish artifact-free EEG. No EDF calibration-rail audit was supplied for SC4611E0; the earlier SC4061E0 rail findings describe a different recording.

### Diagnostic spectra and power fractions

EEG was converted from volts to µV for diagnostic plots, with sampling at **100 Hz**. Per-epoch Welch settings: Hann window, `nperseg=800` (8 s), `noverlap=400`, constant detrending and density scaling. The plotted stage curves are pointwise median PSDs, with an overview and a 45–50 Hz zoom.

For each epoch, trapezoidal integration measured power in **48–50 Hz as a percentage of 0.5–50 Hz power**. The table gives the median and P95 of these per-epoch fractions, not the fraction of epochs classified as artifacts.

| Recording | Stage | Epochs | Median 48–50 Hz power, % | P95, % |
|---|---|---|---|---|
| SC4611E0 | W | 1,707 | 1.06 | 16.68 |
| SC4611E0 | N1 | 123 | 48.47 | 90.68 |
| SC4611E0 | N2 | 276 | 44.61 | 88.43 |
| SC4611E0 | N3 | 139 | 29.54 | 80.43 |
| SC4611E0 | REM | 399 | 49.45 | 63.34 |
| SC4531E0 | W | 1,748 | 1.69 | 4.57 |
| SC4531E0 | N1 | 124 | 2.57 | 9.36 |
| SC4531E0 | N2 | 465 | 1.05 | 5.45 |
| SC4531E0 | N3 | 85 | 1.56 | 3.33 |
| SC4531E0 | REM | 180 | 1.59 | 13.41 |
| SC4141E0 | W | 1,939 | 0.87 | 3.22 |
| SC4141E0 | N1 | 29 | 0.50 | 1.00 |
| SC4141E0 | N2 | 404 | 0.11 | 0.42 |
| SC4141E0 | N3 | 151 | 0.04 | 0.10 |
| SC4141E0 | REM | 233 | 0.27 | 0.59 |

These diagnostic Welch settings do not change the original model feature estimator (`nperseg=256`). For example, 48.47% for SC4611E0/N1 describes the median epoch's power fraction; it does not mean 48.47% of N1 epochs were marked bad.

### Interpretation before model training

The near-50-Hz component is prominent in SC4611E0 sleep and much weaker in the other two examples. It is compatible with electrical/mains interference, but its origin, prevalence across all 133 nights and contribution to classification errors were not established.

At 100-Hz sampling, 50 Hz is the Nyquist boundary. A **40-Hz low-pass** was chosen below the observed component and above the five power-feature bands ending at 30 Hz. The candidate was selected before seeing LP40's classification scores.

Supplied diagnostic figures: `image(20261029-165733).png` (time traces), `image(20261029-170803).png` (SC461 spectra), `image(20261029-171322).png` (SC453) and `image(20261029-171332).png` (SC414). These identify the supplied evidence; separate persistent exports of these diagnostic figures were not confirmed.

## Iteration 9 (LP40_68) — EEG-only 40-Hz low-pass with F2 features

**Run/review supplied in the 2026-10-29 session; consolidated export confirmed and closure recorded on 2026-10-31. Evaluation, diagnostics, decision and export are complete. Saving the executed notebook and recording the team experiment commit remain repository actions.**

### Hypothesis and controlled specification

Hypothesis: attenuating the observed high-frequency component before feature extraction might improve subject-independent staging. Starting from F2_68, change only EEG preprocessing and recalculate the same feature recipe.

| Setting | Specification |
|---|---|
| Input | Existing development recordings; EEG in volts; 100 Hz / 30-second epochs |
| Filter | Butterworth low-pass; `Wn=40.0 Hz` |
| Order | 4 per pass |
| Application | Forward/backward `sosfiltfilt`, separately per epoch, `axis=-1` |
| Padding | `padtype="odd"`; default SciPy padding length |
| Channels | EEG filtered; EOG and EMG unchanged |
| Other processing | No added high-pass, notch, rereferencing, rejection, crop or class resampling |
| Features | Original 11 plus five relative EEG powers, 16 total; same Welch feature recipe |
| Relative denominator | Sum of the five power features, independently per epoch; zero output if denominator is zero |
| Classifier | Same 200-tree RF, `class_weight="balanced"`, seed 0, `n_jobs=-1` |
| Scaling | StandardScaler fitted afresh inside each training fold |
| Evaluation | Same 68 subjects, 133 recordings, 360,621 valid test epochs and exact A–E indices |
| Versions | `LP40_PREPROCESS_VERSION=1`; `LP40_FEATURE_VERSION=1`; base/relative feature versions remain 1 |

Forward/backward filtering gives a composite response different from one pass: the per-pass order is 4 and final attenuation at the Butterworth design frequency is approximately 6 dB. The code filters each retained epoch rather than the complete continuous night.

The preview used SC4611E0/N1 retained epoch 1,798, comparing the 10–11 s trace segment and full-epoch PSD before/after processing. The fast near-50-Hz component was strongly attenuated. This checked the filter effect, not classification performance or recovery of artifact-free EEG. Source: `image(20261029-172100).png`.

### Features, caching and preparation completion

`preparar_lp40_gravacao_68(psg)` reads one night, filters EEG, recalculates the original features and appends the five relative powers. It stores only the record ID, small feature table, labels, subject groups and feature names.

- Cache step: `viggy_lp40_features`, under `/content/drive/MyDrive/CM2013_data/cache/viggy`.
- Key: pinned course revision; PSG/Hypnogram names, sizes and modification times; loading settings; Python/NumPy/SciPy/MNE versions; preprocessing version/settings/channel/scope; and original, relative and LP40 feature versions/names.
- Scalers, cross-recording resampling and classifiers are not cached across folds. There is no extra full-cohort filtered raw cache or EDF copy.
- First code-validation entry: **SC4611E0**, **2,644 × 16**, **51.1 s**, saved as `_cache_viggy_lp40_features_8e4c87d8ba0e.pkl`. Labels/groups and unchanged EOG/EMG feature columns were checked against the baseline payload.
- Full loop: **133/133 recordings**, **105.2 minutes**; SC4611E0 reused at position 104, the other 132 entries computed/saved. This loop time excludes the preceding standalone 51.1-second test.
- Final matrix: **`X_lp40_68.shape == (360621, 16)`**, **68 subjects**, **133 recordings**.
- The helper checked finite features, record identity, feature names, dimensions, labels/groups and unchanged EOG/EMG columns. Concatenation checked the original label, subject and record/epoch order against B0/F2.
- SC4611E0 was the first validation example, not the only processed recording. All 133 nights subsequently used the same recipe.

Classifier/fold choices are independent of this fixed feature cache. Processing or feature-code changes require the relevant version/dependency change.

### Five-fold results

Five new fold-fitted pipelines were evaluated with `avaliar_experiencia_68`. Each fold report was saved before its supplied completion message.

| Fold | Kappa | Macro-F1 | Accuracy | Balanced accuracy | Training min |
|---|---|---|---|---|---|
| A | 0.756 | 0.680 | 0.887 | 0.675 | 9.113 |
| B | 0.719 | 0.650 | 0.863 | 0.639 | 8.494 |
| C | 0.736 | 0.650 | 0.876 | 0.623 | 9.202 |
| D | 0.716 | 0.636 | 0.874 | 0.600 | 8.883 |
| E | 0.751 | 0.678 | 0.880 | 0.662 | 8.889 |

**Mean fold kappa: 0.736 ± 0.018**, sample SD (`ddof=1`) across five folds. Total training: **44.6 minutes**. F2's 46.3-minute fit time was slightly longer in these runs; this is not a guaranteed speed ratio, and LP40 also required the additional feature preparation above.

| Fold | F2 kappa | LP40 kappa | Difference, as printed |
|---|---|---|---|
| A | 0.753 | 0.756 | +0.003 |
| B | 0.718 | 0.719 | +0.001 |
| C | 0.739 | 0.736 | -0.003 |
| D | 0.717 | 0.716 | -0.001 |
| E | 0.748 | 0.751 | +0.003 |

Three folds improve and two worsen. The approximately +0.001 difference between printed mean kappas is small and rounded. Fold SD is not a confidence interval for the method difference; no significance claim is made.

### Pooled panel and stage comparison

Predictions were reconstructed in the common original row order with exactly-once coverage checks. All retained Wake and sleep test epochs remain included.

| Metric | F2_68 | LP40_68 |
|---|---|---|
| Mean fold kappa ± sample SD | 0.735 ± 0.017 | 0.736 ± 0.018 |
| Pooled kappa | 0.735 | 0.736 |
| Pooled macro-F1 | 0.659 | 0.661 |
| Pooled accuracy | 0.876 | 0.876 |
| Pooled balanced accuracy | 0.638 | 0.641 |

| Stage / aggregate | LP40 precision | LP40 recall | LP40 F1 | Support |
|---|---|---|---|---|
| W | 0.938 | 0.979 | 0.958 | 248,341 |
| N1 | 0.338 | 0.129 | 0.187 | 17,877 |
| N2 | 0.767 | 0.814 | 0.790 | 60,494 |
| N3 | 0.840 | 0.690 | 0.758 | 11,610 |
| REM | 0.630 | 0.593 | 0.611 | 22,299 |
| Macro average | 0.703 | 0.641 | 0.661 | 360,621 |
| Support-weighted average | 0.857 | 0.876 | 0.864 | 360,621 |

| Stage | F2 recall | LP40 recall | F2 F1 | LP40 F1 | F1 difference, as printed |
|---|---|---|---|---|---|
| W | 0.980 | 0.979 | 0.959 | 0.958 | -0.001 |
| N1 | 0.135 | 0.129 | 0.195 | 0.187 | -0.008 |
| N2 | 0.813 | 0.814 | 0.786 | 0.790 | +0.003 |
| N3 | 0.681 | 0.690 | 0.751 | 0.758 | +0.007 |
| REM | 0.581 | 0.593 | 0.605 | 0.611 | +0.006 |

Differences were calculated before display rounding; they need not equal subtraction of the printed values (notably N2). W/N1 F1 decline while N2/N3/REM improve slightly. The aggregate macro-F1 gain is not a gain for every stage.

### Paired subject inspection

| Previously inspected participant | F2 kappa | LP40 kappa | Difference, as printed |
|---|---|---|---|
| SC461 | 0.241 | 0.271 | +0.030 |
| SC453 | 0.763 | 0.768 | +0.004 |
| SC414 | 0.905 | 0.906 | +0.000 |

Across all **68** participants before rounding: **29 increase, 39 decrease, 0 exactly equal**. SC414's displayed +0.000 is a small positive rounded difference, consistent with no exact ties. SC453's displayed difference is also calculated before rounding.

SC461 improves but its subject kappa remains low. The kappa pools the participant's recordings, whereas the strong spectral component was inspected in SC4611E0. The observations do not prove that the component caused the original errors. Counts of improved/worsened participants omit effect magnitude and do not replace the full metric panel.

### Confusion inspection

Source: `image(20261029-211549).png`, supplied by Vicente. True stages are rows and predictions columns, normalized within each true stage. These are the displayed three-decimal values, not exact integer counts.

| True stage | Predicted W | Predicted N1 | Predicted N2 | Predicted N3 | Predicted REM |
|---|---|---|---|---|---|
| W | 0.979 | 0.006 | 0.010 | 0.000 | 0.004 |
| N1 | 0.413 | 0.129 | 0.302 | 0.002 | 0.154 |
| N2 | 0.077 | 0.023 | 0.814 | 0.022 | 0.064 |
| N3 | 0.061 | 0.000 | 0.244 | 0.690 | 0.006 |
| REM | 0.145 | 0.070 | 0.190 | 0.002 | 0.593 |

A displayed 0.000 does not prove zero errors. Of true N1 epochs, **12.9%** are identified correctly; **41.3%** are called W, **30.2%** N2, **15.4%** REM and **0.2%** N3. N1-to-W is essentially unchanged vs F2 (0.412 to 0.413), while N1 recall falls from 0.135 to 0.129.

N3-to-N2 decreases from 0.249 to 0.244. REM-to-N2 decreases from 0.217 to 0.190 and correct REM recognition rises from 0.581 to 0.593. Small aggregate gains coexist with N1 losses.

Possible explanations remain hypotheses: the five absolute and five relative powers use bands ending at 30 Hz, below the targeted near-50-Hz component, while broader EEG descriptors can still be affected. The inspected spectra also vary between nights. Attenuating one component need not resolve the information limitations behind N1-to-W/N2 confusion; the current observations do not isolate these mechanisms.

### Decision and confirmed exports

**Retain F2_68 as the working reference; do not adopt the LP40 addition for subsequent reference runs at this checkpoint.**

The primary kappa gain is small, fold/subject results are mixed and N1 recall/F1 decline. LP40 remains a justified and reproducible alternative with recorded trade-offs. This is not a claim that LP40 can never help or that the difference is statistically significant.

P1's 35-Hz experiment used eight subjects and LOSO. Its scores cannot isolate the effect of 35 versus 40 Hz against this different 68-subject A–E experiment.

Artifacts under `/content/drive/MyDrive/CM2013_data/experiments`:

| Artifact | Evidence/status |
|---|---|
| `LP40_68_fixed_AE_fold_A.json` through `LP40_68_fixed_AE_fold_E.json` | Evaluation loop saved each report before its supplied completion message. |
| `LP40_68_fixed_AE.json` | Explicit successful save message supplied at the 2026-10-31 closure checkpoint. |
| `LP40_68_fixed_AE_confusion.png` | Explicit successful save message supplied; confusion figure also shown. |

The consolidated-export cell stores shared configuration/runtime, split unit, epoch count, fold metrics, fold mean/sample SD, total fitting time, pooled report/predictions, paired subject comparison and working decision. It saves the row-normalized confusion image separately. The exported bytes have not been independently uploaded/read here; this log uses the supplied execution outputs. No new training was performed to prepare this update.

The run, review, decision and export are closed. Save the actually executed notebook/log and record the team experiment commit to complete repository reproducibility. The course SHA alone does not complete that step. No all-68 final fit or reserved-holdout run has occurred.

## Iteration 10 (C1_68) — training-only sleep-window crop on fixed A–E folds

**Executed and closed: 2026-10-31.** Experiment ID: `C1_68_crop30_fixed_AE`. This evaluates a training-selection strategy on the current 68-subject protocol. It does not combine C1 with LP40.

### Session recovery and preparation checks

A new Colab session first restored the existing data rather than downloading or extracting all features again. The 133 B0 feature caches were loaded in the original recording order saved in the F2 fold reports. The original 11 features and five relative-power columns reconstructed `X_b0_68.shape == (360621, 11)` and `X_f2_68.shape == (360621, 16)`. The recovery checked labels, subject groups, test indices and order against all five saved F2 reports and reconstructed the F2 out-of-fold predictions.

Headers and hypnogram annotations were then read for all 133 PSG recordings, with signal preloading disabled, to recover each retained epoch's original onset and each recording's duration. The stage mapping and 30-second event construction matched the pinned loader; reconstructed retained labels were checked against each cached feature table. The source was checked at 100 Hz with `first_samp == 0`. All 133 timelines were verified.

During this preparation, reading `SC4002E0-PSG.edf` failed with `OSError: [Errno 107] Transport endpoint is not connected`. This indicated an unavailable Drive mount during I/O; it did not demonstrate a corrupt EDF or a feature/model failure. A force-remount recovery was supplied, and the subsequent successful 133-recording verification confirms preparation resumed. Skipping the normal session-setup section was discussed; it is not established as the cause of the mount disconnect. No deletion, duplicate raw-data copy or repeat download was needed for C1.

### Hypothesis and controlled selection rule

The hypothesis was that removing long Wake periods at recording endpoints from training might help sleep-stage recognition, especially N1. Random forest class weights were already `balanced`; the experiment tests an additional change to which real training examples are retained.

Unchanged from F2_68:

- Same 68 subjects, 133 recordings and exact A–E subject memberships.
- Same 16 F2 features, including both absolute and relative EEG powers.
- No additional signal filter; no LP40, notch or feature change.
- Same fold-fitted StandardScaler and 200-tree balanced random forest, seed 0, `n_jobs=-1`; a new clone is fitted in every fold.
- Every test fold retains its complete original valid epochs, including endpoint Wake. In total, each of the 360,621 common test epochs receives one out-of-fold prediction.

For each recording belonging to the current fold's training subjects:

1. Locate the onset of the first epoch labelled N1, N2, N3 or REM, and the endpoint of the last such epoch.
2. Set the permitted start to `max(0, first_sleep_onset - 1800 seconds)`.
3. Set the permitted end to `min(recording_duration, last_sleep_endpoint + 1800 seconds)`. The last sleep endpoint includes its 30-second epoch.
4. Keep complete valid epochs inside that window, with a numerical tolerance of `1e-6` seconds. Keep Wake inside the window, including Wake between sleep bouts.
5. If a training recording has no sleep-labelled epoch, retain all its valid epochs.

This **retains up to 30 minutes before and after sleep**; it does not simply remove the first and last 30 minutes of a recording. Hours of distant endpoint Wake can be removed. Selection uses only the current fold's training labels. Test labels are used for scoring, not to select test epochs or construct model inputs.

The original `SPLITS_68` remains unchanged; `SPLITS_C1_68` holds the selected training indices and copied original test indices. Assertions checked that selected rows are a subset of the original training rows, train/test subjects remain separate, the training subject set remains intact, all test indices remain identical and **only W-labelled training rows were removed**. No synthetic examples were introduced.

**Implementation revision relative to the eight-subject C1:** these margins use original event times in seconds, including gaps left by Movement/Unknown exclusion. The older implementation used 60 retained rows as a nominal 30-minute margin. The two implementations must not be silently described as identical. C1_68 is compared directly with F2_68 under the current common protocol.

Original event-time arrays were held in session memory. The consolidated export records the training windows and their epoch counts; there is no new raw-signal or feature extraction cache for this crop.

### Training quantities before fitting

| Fold | Original training epochs | Retained training epochs | Wake epochs removed | Complete test epochs |
|---|---:|---:|---:|---:|
| A | 286,790 | 138,071 | 148,719 | 73,831 |
| B | 285,309 | 131,053 | 154,256 | 75,312 |
| C | 290,405 | 135,556 | 154,849 | 70,216 |
| D | 290,337 | 137,710 | 152,627 | 70,284 |
| E | 289,643 | 132,394 | 157,249 | 70,978 |

Stage percentages in each training fold, before → after the crop:

| Fold | W (%) | N1 (%) | N2 (%) | N3 (%) | REM (%) |
|---|---|---|---|---|---|
| A | 68.73 → 35.04 | 5.08 → 10.56 | 16.65 → 34.58 | 3.21 → 6.67 | 6.33 → 13.14 |
| B | 68.85 → 32.18 | 4.90 → 10.66 | 17.08 → 37.18 | 2.93 → 6.38 | 6.25 → 13.60 |
| C | 68.96 → 33.51 | 4.98 → 10.67 | 16.81 → 36.00 | 3.17 → 6.78 | 6.08 → 13.03 |
| D | 68.59 → 33.78 | 5.03 → 10.61 | 16.89 → 35.60 | 3.38 → 7.12 | 6.11 → 12.89 |
| E | 69.19 → 32.60 | 4.80 → 10.49 | 16.46 → 36.01 | 3.41 → 7.46 | 6.15 → 13.44 |

The percentages of sleep stages rise because Wake rows were removed, not because extra N1/N2/N3/REM examples were created. Test distributions remain identical to F2.

The selected indices and windows were prepared and reviewed before the five C1 fits. The pipeline was reconstructed from the saved F2 scaler/classifier parameters. The evaluation guarded the loaded NumPy, SciPy and scikit-learn versions against F2's recorded versions; no mismatch blocked the reported run. Current runtime and original feature-cache provenance are recorded separately rather than silently replacing one with the other.

### Five-fold results and timing

| Fold | Cohen's kappa | Macro-F1 | Accuracy | Balanced accuracy | Fit time (min) |
|---|---:|---:|---:|---:|---:|
| A | 0.749 | 0.684 | 0.880 | 0.692 | 4.280 |
| B | 0.689 | 0.640 | 0.842 | 0.638 | 3.731 |
| C | 0.734 | 0.662 | 0.871 | 0.642 | 4.269 |
| D | 0.731 | 0.652 | 0.878 | 0.619 | 3.962 |
| E | 0.744 | 0.686 | 0.872 | 0.671 | 3.759 |

**Mean fold kappa: 0.729 ± 0.024**, using sample SD (`ddof=1`) across five folds. This is not a 68-subject SD or a confidence interval.

**Total fitting time: 20.0 minutes**, versus 46.3 minutes reported for F2's five fits. These are observed Colab timings with different training sizes, not a hardware-controlled benchmark or a guaranteed speed ratio.

| Fold | F2 kappa | C1 kappa | C1 − F2, as printed |
|---|---:|---:|---:|
| A | 0.753 | 0.749 | -0.004 |
| B | 0.718 | 0.689 | -0.029 |
| C | 0.739 | 0.734 | -0.005 |
| D | 0.717 | 0.731 | +0.014 |
| E | 0.748 | 0.744 | -0.004 |

Kappa declines in 4/5 folds and increases in D; the largest printed loss is in B. Fold variability increases from 0.017 to 0.024. Macro-F1 improves in four folds and balanced accuracy in all five. No significance claim is made.

### Pooled metrics and class results

| Pooled out-of-fold metric | F2 | C1 | C1 − F2, as printed |
|---|---:|---:|---:|
| Cohen's kappa | 0.735 | 0.729 | -0.006 |
| Macro-F1 | 0.659 | 0.666 | +0.007 |
| Accuracy | 0.876 | 0.868 | -0.008 |
| Balanced accuracy | 0.638 | 0.653 | +0.015 |

Pooled kappa and mean fold kappa both round to 0.729 for C1 but are different aggregations.

C1's full per-stage report:

| True stage | Precision | Recall | F1 | Support |
|---|---:|---:|---:|---:|
| W | 0.955 | 0.959 | 0.957 | 248,341 |
| N1 | 0.314 | 0.195 | 0.241 | 17,877 |
| N2 | 0.731 | 0.831 | 0.778 | 60,494 |
| N3 | 0.821 | 0.690 | 0.750 | 11,610 |
| REM | 0.614 | 0.590 | 0.602 | 22,299 |
| Macro average | 0.687 | 0.653 | 0.666 | 360,621 |
| Weighted average | 0.860 | 0.868 | 0.863 | 360,621 |

| Stage | F2 recall | C1 recall | F2 F1 | C1 F1 | F1 difference, as printed |
|---|---:|---:|---:|---:|---:|
| W | 0.980 | 0.959 | 0.959 | 0.957 | -0.002 |
| N1 | 0.135 | 0.195 | 0.195 | 0.241 | +0.046 |
| N2 | 0.813 | 0.831 | 0.786 | 0.778 | -0.009 |
| N3 | 0.681 | 0.690 | 0.751 | 0.750 | -0.001 |
| REM | 0.581 | 0.590 | 0.605 | 0.602 | -0.003 |

Differences were calculated before rounding; do not reconstruct them by subtracting only the displayed three-decimal values. N1 is the only stage with improved F1. Its precision falls from 0.351 to 0.314 while its recall rises from 0.135 to 0.195. The macro-F1 gain reflects the N1 improvement outweighing the other stages' F1 losses. Balanced accuracy rises because the mean of class recalls rises; this does not imply higher precision or F1 for every stage.

### Paired participant comparison

Vicente supplied counts calculated **before rounding** from the pooled per-participant reports:

| Change in participant kappa, C1 versus F2 | Participants |
|---|---:|
| Increased | 36 |
| Decreased | 32 |
| Exactly equal | 0 |
| Total | 68 |

A majority with higher subject kappa does not imply a higher mean fold or pooled kappa. The counts omit change magnitude, and participant, fold and pooled aggregations are different. The full participant differences are stored by the consolidated export; a numerical 68-row table has not been supplied in chat. The observed counts do not establish statistical significance.

### Confusion inspection

Source: the side-by-side F2/C1 image supplied by Vicente on 2026-10-31, titled “68 subjects — fixed folds A–E — complete test recordings.” Rows are true stages and columns predictions. The C1 percentages below are transcribed at the figure's displayed precision of **one decimal percentage point**; they are not exact counts.

| True stage | Predicted W (%) | Predicted N1 (%) | Predicted N2 (%) | Predicted N3 (%) | Predicted REM (%) |
|---|---:|---:|---:|---:|---:|
| W | 95.9 | 1.5 | 1.8 | 0.1 | 0.6 |
| N1 | 32.0 | 19.5 | 32.7 | 0.2 | 15.5 |
| N2 | 4.8 | 3.2 | 83.1 | 2.2 | 6.6 |
| N3 | 4.6 | 0.0 | 25.7 | 69.0 | 0.6 |
| REM | 9.7 | 8.2 | 22.8 | 0.2 | 59.0 |

Rounded rows need not sum to exactly 100%; a displayed 0.0% does not prove zero errors.

- Correct N1 recognition rises **13.5% → 19.5%**. N1 called Wake falls **41.2% → 32.0%**, but N1 called N2 rises **30.3% → 32.7%**.
- Correct Wake recognition falls **98.0% → 95.9%**. Wake called N1 rises **0.7% → 1.5%**, and Wake called N2 rises **0.9% → 1.8%**.
- Fewer N2/N3/REM epochs are called Wake, and each of these stages has higher recall. Their precision losses mean their F1 does not improve.

The result is consistent with reduced preference for Wake after changing training selection. It does not show that class imbalance is the only cause of N1 errors. W forms roughly 69% of the unchanged test set, so a modest drop in Wake recall affects many epochs and helps explain the lower accuracy. Kappa must still be read from the computed panel, rather than inferred solely from the Wake proportion.

### Decision and confirmed exports

**Retain F2_68 as the working reference under the declared primary kappa criterion.** C1 improves N1 F1, macro-F1 and balanced accuracy and uses less fitting time, but lowers mean fold kappa and pooled kappa and increases fold spread. Preserve it as an alternative with explicit trade-offs. This is not a universal rejection of training selection or a claim about the unseen holdout.

Artifacts under `/content/drive/MyDrive/CM2013_data/experiments`:

| Artifact | Evidence/status |
|---|---|
| `C1_68_crop30_fixed_AE_fold_A.json` through `C1_68_crop30_fixed_AE_fold_E.json` | Explicit successful save messages supplied for all five folds before completion. |
| `C1_68_crop30_fixed_AE.json` | Explicit successful consolidated-report save message supplied on 2026-10-31. |
| `C1_68_crop30_fixed_AE_confusion.png` | Explicit successful image save message supplied on 2026-10-31; side-by-side confusion figure inspected separately. |

The supplied export cell stores configuration/runtime provenance, split unit, cohort/epoch counts, fold panel and mean/sample SD, total fitting time, training quantities, class distributions, per-recording training windows, pooled out-of-fold report, class report, paired global/stage/participant comparisons and the decision. The per-fold reports retain the exact selected training indices and common full test indices. Saves use a temporary file followed by replacement so the loop can resume from complete reports.

The exported JSON/PNG bytes have not been uploaded and independently inspected here; save status is based on the supplied Colab execution output. No EDF or original cache was overwritten by the crop. The C1 evaluation, review, decision and export are complete; saving the executed notebook/log and recording the team experiment commit remain separate tasks. No all-68 final fit, alternative-classifier run or reserved-holdout prediction has occurred.

## Iteration 11 (LR1_68) — logistic regression with unchanged F2 features

**Executed, reviewed and exported: 2026-10-31.** Experiment ID: `LR1_68_fixed_AE`. This replaces the classifier in the F2 recipe; it does not combine two fitted models or add LP40/cropping.

### Question and controls specified before fitting

The purpose was to compare two classifier families on the same information. Every completed experiment before LR1 had used random forest. Logistic regression provides a simpler alternative and tests whether that alternative gives useful class trade-offs with the existing descriptors. A better score was not assumed in advance.

- Same **68 development subjects, 133 recordings and 360,621 valid epochs**.
- Same **16 F2 features**: 11 original descriptors plus five relative EEG band powers.
- Same exact A–E subject memberships and complete original training/test indices from `SPLITS_68`. Every valid epoch receives one out-of-fold test prediction.
- No additional filter, no Wake crop, no feature selection or synthetic examples.
- Same StandardScaler settings as F2, fitted afresh inside each training fold.
- Only the classifier changes: F2's 200-tree balanced random forest is replaced by logistic regression. The class-weight policy remains `balanced` and is calculated from each training fold's labels.

Candidate specified before running the five fits:

```python
Pipeline([
    ("scale", StandardScaler(**saved_F2_scaler_params)),
    ("clf", LogisticRegression(
        C=1.0,
        penalty="l2",
        solver="lbfgs",
        class_weight="balanced",
        max_iter=2000,
        tol=1e-4,
    )),
])
```

Other estimator defaults are retained and exported by `get_params()`. There is no C sweep or further logistic-regression tuning in LR1. This is a comparison of the stated configurations, not the best possible performance of either model family. The historical eight-subject M1 proposal remains unexecuted; LR1 is a separate experiment on the current 68-subject protocol.

Method reference checked against the course's recorded scikit-learn 1.6.1 API: https://scikit-learn.org/1.6/modules/generated/sklearn.linear_model.LogisticRegression.html. The run records actual loaded Python/NumPy/SciPy/scikit-learn versions and checks matching reference-version keys where available. Exact current versions have not been separately transcribed from the exported JSON here; do not silently assign the older runtime block to LR1.

### Execution, alignment and convergence checks

The first evaluation cell attempted `from tracks.sleep_edf import SleepEDFTrack`, which failed because `tracks` was not importable under this notebook's module arrangement. The error occurred before any fit. The line was replaced with `SleepEDFTrack = type(track_c1_68)`, reusing the already-loaded class, and a separate reporting instance was then created for LR1. No package installation or download was needed to resolve this.

Before training, the cell checked feature finiteness, the subject/recording counts, complete train/test coverage, subject separation, and exact test-index/label/group agreement with all five saved F2 fold reports. It uses a new cloned scaler/classifier pipeline per fold; it does not call the original evaluator's automatic partitioning.

The saved-result metadata includes a SHA-256 fingerprint of the feature matrix, labels, groups and recording IDs, with shapes/dtypes included in the hash input. It also records feature names, recipe, estimator/scaler settings and runtime. Existing reports are reused only after matching metadata, exact training/test indices, true labels, groups and prediction lengths. A result is retained in RAM before its atomic temporary-file/replacement save, allowing recovery from a Drive write failure without immediately refitting.

A `ConvergenceWarning` is treated as an error, and reaching `max_iter` also stops the cell before accepting the fold's report. **All five folds completed**, using 147–169 solver iterations, below the 2,000-iteration cap. The cap is a maximum budget, not a required number of training iterations. The reported results therefore do not reflect an ignored convergence warning.

F2's existing feature matrix was reused. No new EDF reads, signal preprocessing or per-recording feature caches were required for this classifier comparison.

### Five-fold results and timing

| Fold | Cohen's kappa | Macro-F1 | Accuracy | Balanced accuracy | Fit time (min) | Solver iterations |
|---|---:|---:|---:|---:|---:|---:|
| A | 0.596 | 0.584 | 0.776 | 0.710 | 0.734 | 163 |
| B | 0.550 | 0.576 | 0.735 | 0.682 | 0.513 | 165 |
| C | 0.598 | 0.625 | 0.766 | 0.723 | 0.532 | 159 |
| D | 0.608 | 0.622 | 0.795 | 0.684 | 0.483 | 147 |
| E | 0.606 | 0.607 | 0.772 | 0.728 | 0.528 | 169 |

**Mean fold kappa: 0.592 ± 0.024**, sample SD (`ddof=1`) across the five folds. This is not a 68-subject SD or a confidence interval.

**Total fitting time: 2.8 minutes**, compared with the previously reported 46.3 minutes for F2's five random-forest fits. These are observed Colab timings, not a controlled hardware benchmark or a guarantee for another session. Both comparisons use prepared features; the values are fitting times, not download/feature-extraction times.

| Fold | F2 kappa | LR1 kappa | LR1 − F2, as printed |
|---|---:|---:|---:|
| A | 0.753 | 0.596 | -0.157 |
| B | 0.718 | 0.550 | -0.168 |
| C | 0.739 | 0.598 | -0.141 |
| D | 0.717 | 0.608 | -0.109 |
| E | 0.748 | 0.606 | -0.142 |

Kappa, macro-F1 and accuracy decline in **all five folds**; balanced accuracy increases in all five. The primary mean fold kappa is approximately 0.143 lower than F2, from rounded means. Fold kappa SD rises from 0.017 to 0.024. No significance claim is made.

### Pooled out-of-fold metrics

The diagnostic cell rebuilt both F2 and LR1 predictions in original row order, checking fold indices, labels, groups, allowed predicted labels and exactly-once test coverage before computing the pooled reports.

| Pooled metric | F2 | LR1 | LR1 − F2, as printed |
|---|---:|---:|---:|
| Cohen's kappa | 0.735 | 0.591 | -0.144 |
| Macro-F1 | 0.659 | 0.600 | -0.059 |
| Accuracy | 0.876 | 0.768 | -0.108 |
| Balanced accuracy | 0.638 | 0.705 | +0.067 |

LR1's **pooled kappa 0.591** and **mean fold kappa 0.592** are different aggregations, not inconsistent reports of one quantity. Pooled metrics use all test predictions together; fold summaries give equal weight to the five fold scores.

### Per-stage results and trade-offs

| True stage | Precision | Recall | F1 | Support |
|---|---:|---:|---:|---:|
| W | 0.980 | 0.820 | 0.893 | 248,341 |
| N1 | 0.181 | 0.456 | 0.259 | 17,877 |
| N2 | 0.781 | 0.650 | 0.710 | 60,494 |
| N3 | 0.418 | 0.901 | 0.571 | 11,610 |
| REM | 0.482 | 0.699 | 0.570 | 22,299 |
| Macro average | 0.568 | 0.705 | 0.600 | 360,621 |
| Weighted average | 0.858 | 0.768 | 0.800 | 360,621 |

| Stage | F2 recall | LR1 recall | F2 F1 | LR1 F1 | F1 difference, as printed |
|---|---:|---:|---:|---:|---:|
| W | 0.980 | 0.820 | 0.959 | 0.893 | -0.066 |
| N1 | 0.135 | 0.456 | 0.195 | 0.259 | +0.064 |
| N2 | 0.813 | 0.650 | 0.786 | 0.710 | -0.077 |
| N3 | 0.681 | 0.901 | 0.751 | 0.571 | -0.180 |
| REM | 0.581 | 0.699 | 0.605 | 0.570 | -0.034 |

Differences were calculated before rounding; preserve the supplied difference column rather than recalculating it from the rounded F1 columns.

LR1 recognizes more true N1, N3 and REM epochs but also assigns these labels incorrectly more often. N1 precision falls from **0.351 to 0.181**, despite its F1 improving. N3 precision falls from **0.838 to 0.418**, and its F1 declines substantially even though its recall rises to 0.901. W and N2 recall both fall. N1 is the only stage with improved F1.

Balanced accuracy is the mean of class recalls: the gains in N1/N3/REM recall outweigh the W/N2 recall losses under equal class weighting. Macro-F1 also accounts for false positives through each class's precision, so it can decline while balanced accuracy rises. Accuracy additionally reflects the large Wake support. The panel demonstrates a trade-off, not an overall improvement established by one metric.

### Confusion inspection

Source: `image(20261031-175721).png`, supplied by Vicente and visually inspected. The side-by-side plots use the same stage order and 0–1 colour scale. Rows are true stages and columns predictions, normalized within each true stage. These are the displayed three-decimal rates, not exact integer counts.

| True stage | Predicted W | Predicted N1 | Predicted N2 | Predicted N3 | Predicted REM |
|---|---:|---:|---:|---:|---:|
| W | 0.820 | 0.117 | 0.018 | 0.025 | 0.021 |
| N1 | 0.079 | 0.456 | 0.219 | 0.030 | 0.216 |
| N2 | 0.030 | 0.070 | 0.650 | 0.122 | 0.127 |
| N3 | 0.028 | 0.002 | 0.064 | 0.901 | 0.005 |
| REM | 0.027 | 0.166 | 0.087 | 0.021 | 0.699 |

Rounded rows need not sum to exactly one. Do not derive exact error counts from these rounded rates.

- N1-to-W falls **0.412 → 0.079**, and correct N1 rises **0.135 → 0.456**.
- W-to-N1 rises **0.007 → 0.117**. With Wake's large support, this is an important source of false N1 predictions and helps explain the low N1 precision.
- Correct N3 rises **0.681 → 0.901**, but N2-to-N3 rises **0.022 → 0.122**. W-to-N3 also rises **0.001 → 0.025**.
- Correct REM rises **0.581 → 0.699**; N2-to-REM rises **0.064 → 0.127**, and N1-to-REM rises **0.149 → 0.216**.
- Correct Wake falls **0.980 → 0.820**, and correct N2 falls **0.813 → 0.650**.

These results do not isolate class weighting as the cause: both compared classifiers use the same balanced-weight policy. Nor do they prove that every logistic-regression configuration is inferior. They describe the stated LR1/F2 comparison.

### Paired participant comparison

Vicente supplied the following counts computed **before rounding**:

| Change in participant kappa, LR1 versus F2 | Participants |
|---|---:|
| Increased | 5 |
| Decreased | 63 |
| Exactly equal | 0 |
| Total | 68 |

These are subject-level results pooling each participant's available recordings. The count does not quantify individual effect sizes or identify the five improved participants; no such identities are inferred. Full per-participant differences are included by the supplied consolidated-export cell, but the 68 numerical rows have not been supplied in chat.

### Decision and confirmed exports

**Keep F2_68 with Random Forest as the working reference.** LR1 is much faster in these runs and improves balanced accuracy and N1 F1, but lowers primary kappa in all five folds, pooled kappa, macro-F1, accuracy and F1 for the other four stages. Kappa declines in 63/68 participants.

This is useful evidence from a completed model-family comparison, rather than a reason to hide an unsuccessful primary-metric result. The declared primary metric is not changed after seeing LR1's balanced-accuracy gain. No further LR settings or combined strategies were tested in this experiment.

Artifacts under `/content/drive/MyDrive/CM2013_data/experiments`:

| Artifact | Evidence/status |
|---|---|
| `LR1_68_fixed_AE_fold_A.json` through `LR1_68_fixed_AE_fold_E.json` | Explicit successful save messages supplied for all five folds. |
| `LR1_68_fixed_AE.json` | Explicit successful consolidated-report save message supplied on 2026-10-31. |
| `LR1_68_fixed_AE_confusion.png` | Explicit successful standalone image save message supplied on 2026-10-31; side-by-side F2/LR1 figure also inspected. |

The supplied consolidated-export cell stores feature/model/runtime provenance, fold metrics and mean/sample SD for the full panel, fit/prediction times, per-fold solver iterations and convergence status, pooled predictions/report, classification report, paired fold/global/stage/participant comparisons and the decision. Each per-fold report retains exact training/test indices. The standalone confusion image is saved separately.

The exported JSON/PNG bytes have not been uploaded and independently inspected here; save status is based on the supplied Colab messages. LR1's evaluation, review, decision and export are complete. Saving the executed notebook/log and recording the team's experiment commit remain outstanding. These are five cross-validation fits on 54/55 training subjects per fold, not a final fit on all 68. The ten reserved subjects remain unused.

### Agreed continuation after LR1 — historical specification, now completed

At the 2026-10-31 checkpoint, the agreed next individual experiment was signal-derived current/previous-epoch context, with recording-boundary/gap handling specified before fitting, the same A–E folds and no true test-stage labels as inputs. Selected combinations were to follow that comparison rather than automatically stacking every change.

**Update:** TC1 was subsequently evaluated, followed by TC1 + training-only Wake crop. Filtering was also revisited through a larger signal-only diagnostic and SEL40, which uses F2 rather than TC1. These completed experiments are recorded below. No final all-68 fit or holdout prediction is part of this continuation.

## Session restoration and original epoch times — 2026-11-02

Colab runtime memory was reset between work sessions. Executing the former setup section mounted Drive and made files available, but did not by itself recreate the later feature arrays, saved F2 reference, exact A–E indices or original epoch onsets. The notebook's daily setup was reorganised to restore these dependencies before new experiment cells. Historical work and new training were separated from session preparation.

The supplied restoration output confirms **133/133 original feature caches**, B0 **(360621, 11)**, F2 **(360621, 16)**, 68 subjects, 133 recordings and folds A–E. Labels, participants and original row order were checked against all five F2 fold reports. This restores prepared inputs; it does not fit another model or download duplicate EDFs.

A later attempt to read an annotation file for original timing failed with `ConnectionAbortedError` on Drive. This is an I/O failure, not a classifier result. The timing workflow was revised to use local session copies with source signatures and retry handling, while retaining the persistent source files. The completed setup then enabled the context experiment. Drive caches/files persist across sessions; Python variables must still be recreated after a runtime reset. A versioned cache is reused only when its inputs/settings and alignment checks match.

Original onsets are necessary because retained rows are not necessarily consecutive in elapsed time after Movement/Unknown exclusion. The context rule below uses original timestamps, not just adjacent array rows.

## Iteration 12 (TC1_68) — previous-epoch signal features with Random Forest

**Executed, reviewed and exported in the 2026-11-02 session.** Experiment ID: `TC1_68_fixed_AE`. This is a new five-fold evaluation with new fitted models; it does not reuse F2's fitted trees or add LP40/Wake cropping.

### Question and fixed feature construction

Question: does access to the immediately previous 30-second epoch's signal features improve staging compared with viewing the current epoch alone?

| Item | TC1 specification |
|---|---|
| Input features | F2 version 1: original 11 descriptors plus five relative EEG band powers |
| Current epoch | All 16 F2 features |
| Previous epoch | The same 16 features from the immediately preceding retained epoch, only when it belongs to the same recording and its original onset is exactly one 30-second epoch earlier, within the configured tolerance |
| Direction | Past only; no future epoch or stage prediction/label is an input |
| Missing predecessor | At recording starts or gaps, copy the current feature vector into the previous-feature positions and set the availability flag to 0 |
| Valid predecessor | Use the real previous feature vector and set availability to 1 |
| Total | **16 current + 16 previous + 1 flag = 33 features** |
| Version | `TC1_FEATURE_VERSION = 1` |
| Additional processing | No added EEG filter, Wake crop, feature selection or synthetic examples |
| Classifier | Same fold-fitted StandardScaler and 200-tree balanced Random Forest, seed 0, `n_jobs=-1` |
| Evaluation | Same exact A–E subject memberships and complete 360,621 test epochs |

The matrix is **`X_tc1_68.shape == (360621, 33)`**. Its first 16 columns equal F2. Checks require finite values, matching label/record order, same-recording context and consecutive original onsets. Feature names retain the F2 list, add a `previous_` copy of each name and end with `previous_epoch_available`.

This is a fixed per-recording feature construction, with no parameter learned across subjects. Each subject's recordings stay wholly in one fold, and the scaler/classifier are fitted only on training subjects. True previous sleep-stage labels are never used as features. The existing physical-time gap rule prevents crossing excluded epochs or recording boundaries.

### Five-fold results and comparison

| Fold | Cohen's kappa | Macro-F1 | Accuracy | Balanced accuracy | Fit time (min) |
|---|---|---|---|---|---|
| A | 0.774 | 0.701 | 0.895 | 0.693 | 7.103 |
| B | 0.732 | 0.664 | 0.869 | 0.650 | 6.951 |
| C | 0.749 | 0.663 | 0.882 | 0.631 | 7.442 |
| D | 0.731 | 0.657 | 0.881 | 0.614 | 7.266 |
| E | 0.770 | 0.697 | 0.888 | 0.677 | 7.117 |

**Mean fold kappa: 0.751 ± 0.020**, sample SD (`ddof=1`) across five folds. **Total fitting time: 35.9 minutes.** These prepared-feature fitting times are not an end-to-end timing or a controlled comparison of Colab hardware/session speed.

| Fold | F2 kappa | TC1 kappa | TC1 − F2, calculated from rounded values |
|---|---|---|---|
| A | 0.753 | 0.774 | +0.021 |
| B | 0.718 | 0.732 | +0.014 |
| C | 0.739 | 0.749 | +0.010 |
| D | 0.717 | 0.731 | +0.014 |
| E | 0.748 | 0.770 | +0.022 |

Kappa increases in **all five folds**. Before rounding, participant kappa increases in **62/68**, decreases in **6/68**, with no ties. These counts do not describe effect sizes or a statistical-significance test.

### Pooled metrics and per-stage report

| Pooled metric | F2 | TC1 | Difference, as printed |
|---|---|---|---|
| Cohen's kappa | 0.735 | 0.751 | +0.016 |
| Macro-F1 | 0.659 | 0.677 | +0.018 |
| Accuracy | 0.876 | 0.883 | +0.007 |
| Balanced accuracy | 0.638 | 0.654 | +0.016 |

| True stage / aggregate | Precision | Recall | F1 | Support |
|---|---|---|---|---|
| W | 0.942 | 0.981 | 0.961 | 248,341 |
| N1 | 0.406 | 0.153 | 0.223 | 17,877 |
| N2 | 0.772 | 0.832 | 0.801 | 60,494 |
| N3 | 0.849 | 0.689 | 0.761 | 11,610 |
| REM | 0.671 | 0.615 | 0.642 | 22,299 |
| Macro average | 0.728 | 0.654 | 0.677 | 360,621 |
| Weighted average | 0.867 | 0.883 | 0.871 | 360,621 |

All five pooled stage F1 values improve versus F2: W 0.959 → 0.961, N1 0.195 → 0.223, N2 0.786 → 0.801, N3 0.751 → 0.761 and REM 0.605 → 0.642. N1 remains difficult: only 15.3% of its true epochs are recognized despite the gain.

### Confusion inspection

Vicente supplied the side-by-side F2/TC1 confusion figure. Rows are true stages and columns predicted stages, normalized within each true stage. These are the displayed rounded rates; they are not exact integer counts.

| True stage | Predicted W | Predicted N1 | Predicted N2 | Predicted N3 | Predicted REM |
|---|---|---|---|---|---|
| W | 0.981 | 0.007 | 0.009 | 0.001 | 0.003 |
| N1 | 0.417 | 0.153 | 0.291 | 0.002 | 0.137 |
| N2 | 0.070 | 0.019 | 0.832 | 0.021 | 0.058 |
| N3 | 0.059 | 0.000 | 0.249 | 0.689 | 0.003 |
| REM | 0.122 | 0.053 | 0.209 | 0.001 | 0.615 |

Compared with F2, correct N2 rises 0.813 → 0.832 and correct REM 0.581 → 0.615. N1 recall rises 0.135 → 0.153, but N1-to-W also changes 0.412 → 0.417; context does not resolve that dominant error. N1-to-N2 and N1-to-REM decrease. Rounded rows may not sum exactly to one.

### Decision and confirmed exports

**Adopt TC1_68 as Vicente's primary-kappa working reference.** This is the strongest and most consistent observed gain in the current controlled comparisons. F2 remains the simpler 16-feature reference for isolating changes. The final team pipeline has not been selected.

Five fold completion logs were supplied. The evaluator writes individual fold reports; explicit consolidated save messages confirm:

- `/content/drive/MyDrive/CM2013_data/experiments/TC1_68_fixed_AE.json`
- `/content/drive/MyDrive/CM2013_data/experiments/TC1_68_fixed_AE_confusion.png`

The report records recipe/model/runtime provenance, fold results, pooled predictions, class scores and paired participant comparison. The uploaded TC1 JSON was subsequently checked in the 2026-11-10 paired review. No final all-68 fit or reserved-subject evaluation is claimed.

## Iteration 13 (TC1_C1_68) — temporal context plus training-only Wake crop

**Executed, reviewed and exported in the 2026-11-02 session.** Experiment ID: `TC1_C1_68_crop30_fixed_AE`. This deliberately revisits the earlier training-selection decision using the new TC1 feature reference.

### Combination and controls specified before fitting

- Start from the **same TC1 33-feature matrix**, with no added EEG filter and the same balanced Random Forest/scaler settings.
- Build temporal context on the complete retained sequence **before** selecting training epochs. Cropping must not create artificial adjacency between formerly separated epochs or change the predecessor definition.
- In each recording, retain sleep epochs and Wake within **30 minutes before the first sleep epoch through 30 minutes after the last sleep epoch** in original elapsed time. Only Wake outside this window is removed from training. Wake between sleep epochs remains. Recordings without sleep retain all their epochs.
- Apply this label-based window only to the current fold's **training recordings**. Test recordings keep all original valid epochs, including endpoint Wake. True test-stage labels do not determine test cropping or context.
- Use the exact A–E test sets, new fold-fitted scalers/RFs and unchanged class-weight policy. No oversampling or synthetic epochs are introduced.

| Fold | Train epochs before | Train epochs after | Wake removed | Complete test epochs |
|---|---|---|---|---|
| A | 286,790 | 138,071 | 148,719 | 73,831 |
| B | 285,309 | 131,053 | 154,256 | 75,312 |
| C | 290,405 | 135,556 | 154,849 | 70,216 |
| D | 290,337 | 137,710 | 152,627 | 70,284 |
| E | 289,643 | 132,394 | 157,249 | 70,978 |

These match the earlier C1_68 quantities. Relative class frequencies and the resulting training-fold balanced class weights change because only training Wake is removed.

### Five-fold results and timing

| Fold | Cohen's kappa | Macro-F1 | Accuracy | Balanced accuracy | Fit time (min) |
|---|---|---|---|---|---|
| A | 0.778 | 0.713 | 0.894 | 0.716 | 3.009 |
| B | 0.711 | 0.663 | 0.854 | 0.657 | 2.786 |
| C | 0.747 | 0.676 | 0.877 | 0.654 | 2.923 |
| D | 0.747 | 0.671 | 0.885 | 0.633 | 3.009 |
| E | 0.768 | 0.712 | 0.885 | 0.697 | 2.821 |

**Mean fold kappa: 0.750 ± 0.026**, sample SD across the five folds. **Total fitting time: 14.5 minutes**, versus the earlier TC1 run's 35.9 minutes. Fewer training rows were used; the timings remain observations rather than a controlled hardware benchmark.

| Fold | TC1 kappa | TC1 + crop kappa | Difference, as printed |
|---|---|---|---|
| A | 0.774 | 0.778 | +0.004 |
| B | 0.732 | 0.711 | -0.021 |
| C | 0.749 | 0.747 | -0.002 |
| D | 0.731 | 0.747 | +0.016 |
| E | 0.770 | 0.768 | -0.002 |

Two folds improve and three worsen; fold B has the largest loss. Before rounding, participant kappa increases in **39/68**, decreases in **29/68**, with no ties. This participant comparison is **versus TC1**, not F2.

### Pooled metrics and per-stage report

| Pooled metric | TC1 | TC1 + crop | Difference, as printed |
|---|---|---|---|
| Cohen's kappa | 0.751 | 0.750 | -0.001 |
| Macro-F1 | 0.677 | 0.688 | +0.011 |
| Accuracy | 0.883 | 0.879 | -0.004 |
| Balanced accuracy | 0.654 | 0.672 | +0.018 |

| True stage / aggregate | Precision | Recall | F1 | Support |
|---|---|---|---|---|
| W | 0.958 | 0.964 | 0.961 | 248,341 |
| N1 | 0.377 | 0.226 | 0.282 | 17,877 |
| N2 | 0.740 | 0.851 | 0.792 | 60,494 |
| N3 | 0.844 | 0.703 | 0.767 | 11,610 |
| REM | 0.661 | 0.617 | 0.638 | 22,299 |
| Macro average | 0.716 | 0.672 | 0.688 | 360,621 |
| Weighted average | 0.871 | 0.879 | 0.873 | 360,621 |

| Stage | TC1 recall | TC1 + crop recall | TC1 F1 | TC1 + crop F1 | F1 difference, as printed |
|---|---|---|---|---|---|
| W | 0.981 | 0.964 | 0.961 | 0.961 | 0.000 |
| N1 | 0.153 | 0.226 | 0.223 | 0.282 | +0.060 |
| N2 | 0.832 | 0.851 | 0.801 | 0.792 | -0.009 |
| N3 | 0.689 | 0.703 | 0.761 | 0.767 | +0.006 |
| REM | 0.615 | 0.617 | 0.642 | 0.638 | -0.003 |

The supplied differences were computed before rounding: preserve the printed N1 F1 gain **+0.060**, although subtraction of the displayed 0.282 and 0.223 gives 0.059. N1 recall rises **15.3% → 22.6%**, while N1 precision falls **0.406 → 0.377**. N2 recall improves but its precision/F1 decline. Wake recall falls, and N3 F1 rises slightly.

### Confusion inspection

The supplied side-by-side TC1/TC1 + crop figure shows the same stage order and complete test coverage. The following decimal rates transcribe its percentages.

| True stage | Predicted W | Predicted N1 | Predicted N2 | Predicted N3 | Predicted REM |
|---|---|---|---|---|---|
| W | 0.964 | 0.013 | 0.017 | 0.001 | 0.004 |
| N1 | 0.313 | 0.226 | 0.320 | 0.002 | 0.140 |
| N2 | 0.042 | 0.028 | 0.851 | 0.021 | 0.058 |
| N3 | 0.035 | 0.000 | 0.259 | 0.703 | 0.003 |
| REM | 0.084 | 0.073 | 0.225 | 0.001 | 0.617 |

N1-to-W falls **41.7% → 31.3%**, while correct N1 rises **15.3% → 22.6%**. However, N1-to-N2 rises **29.1% → 32.0%**, and Wake-to-N1/ N2 rise. Correct Wake falls **98.1% → 96.4%**. N2-to-W and REM-to-W decrease. These patterns show a redistribution of errors, not elimination of class imbalance or a uniformly better classifier.

### Decision and confirmed exports

**Keep TC1 without cropping as the primary-kappa reference; retain TC1 + crop as the Macro-F1/N1 alternative.** The 0.001 observed kappa difference is small, while spread is larger with cropping and the class trade-offs are explicit. The declared primary metric is not replaced after observing the secondary gains.

Five fold completions were supplied. Explicit consolidated save messages confirm:

- `/content/drive/MyDrive/CM2013_data/experiments/TC1_C1_68_crop30_fixed_AE.json`
- `/content/drive/MyDrive/CM2013_data/experiments/TC1_C1_68_crop30_fixed_AE_confusion.png`

This is the first completed combination after the individual comparisons: temporal features plus training selection, without LP40 or SEL40. The uploaded JSON was subsequently checked and used to recompute all 68 paired subject changes in the 2026-11-10 review.

## LP40 revisited — targeted checks and full-cohort signal-ratio audit, 2026-11-02

After TC1 + crop, the question of filtering was revisited rather than treating the earlier small global LP40 gain as proof that filtering was unnecessary. The same three previously inspected development nights were used to verify what the filter changes; the signal-only power-ratio measurement was then extended to all 133 nights.

### Before/after checks in three recordings

Plots show an N1 30-second trace, a one-second zoom, median N1 Welch PSD and a near-50-Hz PSD zoom, before and after the same per-epoch LP40 recipe. Stage summaries below give medians of each epoch's high-frequency fraction and of the ratio of post-/pre-filter 0.5–30-Hz integrated power.

| Recording | Stage | Epochs | 48–50 fraction before (%) | 48–50 fraction after (%) | 0.5–30 power retained (%) |
|---|---|---|---|---|---|
| SC4611E0 | W | 1707 | 1.055 | 0.000 | 99.998 |
| SC4611E0 | N1 | 123 | 48.469 | 0.000 | 100.000 |
| SC4611E0 | N2 | 276 | 44.608 | 0.000 | 100.000 |
| SC4611E0 | N3 | 139 | 29.539 | 0.000 | 100.000 |
| SC4611E0 | REM | 399 | 49.452 | 0.000 | 100.000 |
| SC4531E0 | W | 1748 | 1.692 | 0.000 | 99.995 |
| SC4531E0 | N1 | 124 | 2.565 | 0.000 | 99.999 |
| SC4531E0 | N2 | 465 | 1.054 | 0.000 | 100.000 |
| SC4531E0 | N3 | 85 | 1.557 | 0.000 | 100.000 |
| SC4531E0 | REM | 180 | 1.591 | 0.000 | 100.000 |
| SC4141E0 | W | 1939 | 0.873 | 0.000 | 99.997 |
| SC4141E0 | N1 | 29 | 0.504 | 0.000 | 99.999 |
| SC4141E0 | N2 | 404 | 0.111 | 0.000 | 100.000 |
| SC4141E0 | N3 | 151 | 0.044 | 0.000 | 100.000 |
| SC4141E0 | REM | 233 | 0.266 | 0.000 | 99.999 |

In these examples the near-50-Hz component is strongly attenuated while integrated 0.5–30-Hz power changes little. A displayed 0.000% is rounded, not exactly zero residual power; 100.000% is a rounded integrated-power result, not proof that every sample or feature is unchanged. The plots do not establish artifact-free EEG or prove the cause of the original component.

N1 examples include retained epoch **882** in SC4531E0, at **441.0 minutes** after recording start, and epoch **1250** in SC4141E0, at **625.0 minutes**. These are diagnostic examples rather than representative samples. The earlier SC461 diagnosis was based on a participant's pooled kappa, not a single-night score.

### Label-free selection rule specified before SEL40 training

For each retained EEG epoch, compute:

`high_fraction_percent = 100 * integral(PSD, 48–50 Hz) / integral(PSD, 0.5–50 Hz)`

Diagnostic PSD settings: **100-Hz sampling**, **30-second epochs**, Welch with **Hann window**, **800 samples per segment**, **400-sample overlap**, constant detrending and density scaling; trapezoidal integration. Ratio/selection versions are **1**. The threshold is **>= 10.0%**, chosen before SEL40 classification results. It is a heuristic signal criterion, not a validated artifact label, a stage rule or a tuned holdout threshold.

The same signal-only decision applies independently to training and test epochs. No target-stage label, cross-recording fitted transform or classifier prediction determines whether filtering is applied. These diagnostic PSD settings are distinct from the existing **256-sample Welch model-feature estimator**. The selection denominator covers **0.5–50 Hz**, whereas F2's five relative model powers use the sum of its five **0.5–30-Hz** band-power features.

In the initial three-night check, SC4611E0 selected **1,037/2,644 epochs (39.2%)**, SC4531E0 **56/2,602 (2.2%)**, and SC4141E0 **36/2,756 (1.3%)**. SC4611E0 selected 121/123 N1, 276/276 N2, 139/139 N3 and 398/399 REM epochs; SC4141E0 selected only Wake. The criterion is therefore not equivalent to selecting one stage, and its distribution can be associated with stage/recording without being a stage label.

### Audit of all 133 development recordings

The ratio-preparation loop completed **133/133 recordings in 5.9 minutes** using versioned per-recording `viggy_highfreq_ratio` caches. All **360,621** rows were aligned with the existing labels, groups and recording IDs. **25,446 epochs (7.06%)** met the criterion; **335,175** did not.

| Stage | All epochs | Selected epochs | Selected within stage (%) |
|---|---|---|---|
| W | 248,341 | 14,640 | 5.895 |
| N1 | 17,877 | 2,213 | 12.379 |
| N2 | 60,494 | 4,746 | 7.845 |
| N3 | 11,610 | 410 | 3.531 |
| REM | 22,299 | 3,437 | 15.413 |

The full-recording proportions range widely; the ten largest are reproduced with their prediction results in iteration 14. These counts extend the automated ratio audit beyond the initial three nights; they do not mean that every raw recording was manually inspected or that every artifact type was assessed.

Explicit save confirmation: `/content/drive/MyDrive/CM2013_data/experiments/SEL40_68_quality_summary_v1.json`. This diagnostic step produced no new classifier fit.

## Iteration 14 (SEL40_68) — selective LP40 with the original F2 feature recipe

**Executed, reviewed and exported in the 2026-11-02 session; subsequent subset/night diagnostics supplied before this 2026-11-04 log update.** Experiment ID: `SEL40_68_fixed_AE`.

### Controlled construction and cache recovery

Start with F2's **360,621 × 16** matrix. For epochs meeting the fixed >=10% rule, replace the row with the corresponding **LP40-derived 16-feature vector**. All other rows remain exactly F2. The filter is the existing **EEG-only 40-Hz Butterworth**, order **4 per pass**, forward/backward SOS per epoch with odd padding. Recompute all EEG-dependent descriptors and relative powers consistently; EOG/EMG descriptors remain unchanged.

Because the cached LP40 recipe filters and extracts features independently per epoch, reusing a selected row is equivalent to applying that recipe to that selected epoch. It does not require refiltering entire recordings. There is **no temporal context, no Wake crop and no epoch rejection** in SEL40. All fold-fitted scalers and balanced Random Forests are trained anew on the complete original A–E training indices.

An initial expected-key lookup stopped at **SC4152E0** before training. A read-only inventory found **133 readable LP40 recording caches, no missing recordings and no duplicate recording entries**. The candidate for SC4152E0 had **2,859 × 16** features and matched feature names, labels, groups and EOG/EMG columns. The failed exact-key lookup was therefore not evidence that the recording's feature table had never been created. After cache-key recovery, the supplied final assembly completed all **133/133** recordings and reused a matching SC4152E0 cache.

Final preparation output:

- **25,446 rows** use LP40-derived features; **335,175** keep original F2 features.
- **74 LP40 recording caches** were used because only those recordings contained selected epochs.
- Labels, groups, record/row order, feature names, feature finiteness, relative-power construction and unchanged EOG/EMG columns were checked.
- Unselected rows were checked against F2; full row coverage and the fixed mask were checked before any fit.
- The recipe records the threshold/settings, versions, original LP40 provenance/runtime and a fingerprint of the selection mask/record IDs. No new classifier was trained during the diagnostic/cache-recovery step.

### Five-fold results and three-way comparison

| Fold | Cohen's kappa | Macro-F1 | Accuracy | Balanced accuracy | Fit time (min) |
|---|---|---|---|---|---|
| A | 0.752 | 0.677 | 0.885 | 0.673 | 5.151 |
| B | 0.718 | 0.649 | 0.862 | 0.638 | 5.146 |
| C | 0.737 | 0.652 | 0.877 | 0.623 | 5.306 |
| D | 0.720 | 0.639 | 0.876 | 0.602 | 5.371 |
| E | 0.752 | 0.678 | 0.880 | 0.660 | 5.303 |

**Mean fold kappa: 0.736 ± 0.017**, sample SD across five folds. **Total fitting time: 26.3 minutes.** The lower observed time than earlier F2/LP40 runs cannot be assigned to selective filtering: feature count, training-row count and classifier settings were unchanged, and Colab sessions were not controlled hardware benchmarks.

| Fold | F2 kappa | LP40 kappa | SEL40 kappa | SEL40 − F2, as printed | SEL40 − LP40, as printed |
|---|---|---|---|---|---|
| A | 0.753 | 0.756 | 0.752 | -0.001 | -0.004 |
| B | 0.718 | 0.719 | 0.718 | 0.000 | -0.001 |
| C | 0.739 | 0.736 | 0.737 | -0.002 | +0.001 |
| D | 0.717 | 0.716 | 0.720 | +0.003 | +0.004 |
| E | 0.748 | 0.751 | 0.752 | +0.004 | +0.001 |

The displayed fold-B SEL40/F2 difference is 0.000; it is not a claim of exact equality before rounding. Before rounding, participant kappa increases in **37/68**, decreases in **31/68**, with no exact ties, versus F2.

### Pooled metrics and per-stage report

| Pooled metric | F2 | LP40 | SEL40 |
|---|---|---|---|
| Cohen's kappa | 0.735 | 0.736 | 0.736 |
| Macro-F1 | 0.659 | 0.661 | 0.660 |
| Accuracy | 0.876 | 0.876 | 0.876 |
| Balanced accuracy | 0.638 | 0.641 | 0.640 |

| True stage / aggregate | Precision | Recall | F1 | Support |
|---|---|---|---|---|
| W | 0.939 | 0.979 | 0.958 | 248,341 |
| N1 | 0.342 | 0.135 | 0.193 | 17,877 |
| N2 | 0.766 | 0.814 | 0.790 | 60,494 |
| N3 | 0.833 | 0.686 | 0.752 | 11,610 |
| REM | 0.628 | 0.589 | 0.608 | 22,299 |
| Macro average | 0.702 | 0.640 | 0.660 | 360,621 |
| Weighted average | 0.858 | 0.876 | 0.864 | 360,621 |

Relative to F2, pooled N1 recall remains **0.135** and F1 is **0.193 versus 0.195**. N2/N3/REM F1 values are 0.790/0.752/0.608 versus F2's 0.786/0.751/0.605. The global gains are small and do not demonstrate that selective filtering resolves the main N1 problem.

### Confusion inspection

Source: Vicente's supplied F2/SEL40 side-by-side figure, `image(20261102-212551).png`. Rows are true stages and columns predicted stages, normalized within each true stage.

| True stage | Predicted W | Predicted N1 | Predicted N2 | Predicted N3 | Predicted REM |
|---|---|---|---|---|---|
| W | 0.979 | 0.007 | 0.010 | 0.001 | 0.004 |
| N1 | 0.408 | 0.135 | 0.301 | 0.002 | 0.155 |
| N2 | 0.076 | 0.023 | 0.814 | 0.023 | 0.064 |
| N3 | 0.063 | 0.000 | 0.247 | 0.686 | 0.004 |
| REM | 0.144 | 0.071 | 0.193 | 0.002 | 0.589 |

N1-to-W changes only **0.412 → 0.408**, with correct N1 unchanged at the displayed 0.135 and N1-to-REM higher at 0.155. Correct REM increases **0.581 → 0.589**, while REM-to-W also increases **0.138 → 0.144**. As in the other matrices, rounded rates are not exact counts and need not sum to precisely one.

### Supplementary diagnosis: the same predictions, split by selection

The follow-up cell loaded the saved F2, LP40 and SEL40 predictions and verified experiment IDs, A–E assignment, true labels, subject order and lengths against the common arrays. It then recomputed metrics within two fixed sets of test epochs; **no new fit or threshold change** was performed.

| Test-epoch subset | Model | Epochs | Kappa | Macro-F1 | Accuracy | Balanced accuracy |
|---|---|---|---|---|---|---|
| Meets >=10% signal criterion | F2 | 25,446 | 0.524 | 0.469 | 0.739 | 0.446 |
| Meets >=10% signal criterion | LP40 | 25,446 | 0.533 | 0.513 | 0.744 | 0.478 |
| Meets >=10% signal criterion | SEL40 | 25,446 | 0.538 | 0.515 | 0.743 | 0.479 |
| Remaining epochs | F2 | 335,175 | 0.754 | 0.672 | 0.886 | 0.654 |
| Remaining epochs | LP40 | 335,175 | 0.754 | 0.670 | 0.886 | 0.655 |
| Remaining epochs | SEL40 | 335,175 | 0.753 | 0.670 | 0.886 | 0.654 |

Compare models **within the same subset**. In selected epochs, SEL40 versus F2 improves kappa by about **0.014**, macro-F1 by **0.046**, balanced accuracy by **0.033** and accuracy by **0.004**, using the rounded values. Remaining-epoch metrics change little. Differences between the two subsets can also reflect different subject/stage distributions; they do not establish that high-frequency activity caused their errors. Kappa and Macro-F1 are recomputed within each subset, not additive contributions to the global metrics.

Unselected rows retain F2 features but need not retain F2 predictions: changing part of the training matrix changes the fitted trees and potentially predictions for every epoch. This is not an alignment failure.

### Supplementary diagnosis: ten recordings with the largest selected fractions

These recordings were ranked by the signal-only selected fraction, with recording ID breaking ties. Scores pool each **single recording's** out-of-fold predictions, rather than both nights of a participant. Differences below are transcribed as printed and may differ from subtraction of rounded columns.

| Recording | Selected (%) | F2 kappa | LP40 kappa | SEL40 kappa | SEL40 − F2 | SEL40 − LP40 |
|---|---|---|---|---|---|---|
| SC4232E0 | 81.025 | 0.520 | 0.529 | 0.531 | +0.011 | +0.003 |
| SC4202E0 | 72.247 | 0.464 | 0.381 | 0.466 | +0.002 | +0.085 |
| SC4272F0 | 59.443 | 0.777 | 0.779 | 0.772 | -0.006 | -0.007 |
| SC4762E0 | 46.243 | 0.511 | 0.492 | 0.463 | -0.048 | -0.029 |
| SC4111E0 | 43.733 | 0.511 | 0.494 | 0.487 | -0.025 | -0.007 |
| SC4512E0 | 43.418 | 0.727 | 0.723 | 0.741 | +0.015 | +0.018 |
| SC4382F0 | 41.877 | 0.797 | 0.806 | 0.790 | -0.007 | -0.016 |
| SC4591G0 | 40.050 | 0.614 | 0.589 | 0.566 | -0.047 | -0.023 |
| SC4611E0 | 39.221 | 0.303 | 0.339 | 0.355 | +0.052 | +0.016 |
| SC4612E0 | 38.645 | 0.161 | 0.179 | 0.243 | +0.082 | +0.064 |

**Five nights improve and five worsen versus F2.** SC461's two nights improve appreciably, but SC4762E0 and SC4591G0 decline. These are ten selected development examples, not the full 133-night distribution or an independent validation set. The single-night F2 kappas for SC4611E0/SC4612E0 differ from SC461's earlier **pooled subject kappa 0.241**; those quantities must not be interchanged.

### Decision and confirmed exports

**Do not adopt SEL40 as the working reference.** It shows an observed benefit within the selected epochs and some recordings, but global gains versus F2 are small and recording-level effects are mixed. This closes the stated 16-feature selective-filter experiment without declaring all filtering ineffective or predicting how it would interact with temporal context.

TC1 remains the primary-kappa reference; TC1 + crop remains the Macro-F1/N1 alternative. The later **TC1 + LP40** run used full EEG filtering (iteration 15), so it does not establish the effect of selective filtering with TC1. **TC1 + SEL40 and TC1 + filter + crop have not been run.**

Confirmed artifacts under `/content/drive/MyDrive/CM2013_data/experiments`:

| Artifact | Evidence/status |
|---|---|
| `SEL40_68_quality_summary_v1.json` | Successful save message in the all-133-record ratio-preparation output |
| `SEL40_68_fixed_AE.json` | Explicit successful consolidated save message supplied |
| `SEL40_68_fixed_AE_confusion.png` | Explicit successful image save message supplied; paired figure also inspected |
| `SEL40_68_fixed_AE.json`, later diagnostic update | Explicit message confirms subset and top-recording diagnostics were added to the existing report |

Five A–E fold completion logs were supplied; the evaluator writes one report per fold. The consolidated report retains recipe/model/runtime information, fold results and pooled/participant/class diagnostics. Its later supplementary fields are `diagnostics_by_selection` and `diagnostics_top_recordings`. These new model-report JSON bytes have not been independently uploaded and inspected here.

## Post-SEL40 signal inspection — 2026-11-10

To check for slow variations beyond the near-50-Hz diagnosis, three development EEG Fpz-Cz recordings were inspected using consecutive two-minute windows of retained epochs and Welch spectra. The ratio was power at 0.05–0.30 Hz divided by power at 0.05–4 Hz. One window near each recording's 95th percentile was plotted.

| Recording | Windows | Median slow-power ratio | 95th percentile | Example start (min) |
|---|---:|---:|---:|---:|
| SC4351F0 | 677 | 6.86% | 15.58% | 84.0 |
| SC4611E0 | 659 | 5.23% | 25.26% | 768.0 |
| SC4141E0 | 689 | 4.74% | 10.95% | 206.0 |

The SC4351F0 excursion at 85.117 min occurred during Wake and was inspected in Fpz-Cz, Pz-Oz and horizontal EOG. These examples show slow variation and transient deflections, but do not establish their causes or justify removing the whole slow band. This was signal inspection only; no high-pass candidate was fitted.

## Iteration 15 (TC1_LP40_68) — full EEG low-pass with temporal context

**Question:** does the previously tested LP40 improve performance once the model can also use the preceding epoch?

- Restored the **133 original LP40 feature caches**; duplicate cache files were excluded. Used the same EEG-only 40-Hz Butterworth low-pass as iteration 9 (order 4 per pass, forward-backward SOS, odd padding, applied per epoch). EOG and EMG features were retained.
- Replaced the EEG features in both the current and previous-epoch blocks of TC1. The feature matrix remained **360,621 × 33**, with **360,357** valid preceding epochs. The recording-boundary/gap rule, fallback and availability flag were unchanged. There was no selective mask or Wake crop.
- Kept the TC1 scaler and balanced 200-tree Random Forest, seed 0, fitted independently inside each of the same five subject folds. The test epochs and reference stages were unchanged.

| Fold | TC1 kappa | TC1 + LP40 kappa | Paired kappa change | Macro-F1 | Accuracy | Balanced accuracy | Fit (min) |
|---|---:|---:|---:|---:|---:|---:|---:|
| A | 0.774 | 0.774 | ≈0.000 | 0.698 | 0.895 | 0.691 | 12.970 |
| B | 0.732 | 0.731 | -0.002 | 0.663 | 0.869 | 0.650 | 12.635 |
| C | 0.749 | 0.751 | +0.001 | 0.668 | 0.883 | 0.638 | 13.618 |
| D | 0.731 | 0.729 | -0.002 | 0.653 | 0.880 | 0.614 | 13.334 |
| E | 0.770 | 0.773 | +0.003 | 0.700 | 0.889 | 0.683 | 12.969 |

Macro-F1, accuracy, balanced accuracy and fit time in the fold table are for TC1 + LP40. Paired deltas were computed before rounding. Across five folds, mean kappa was **0.751 ± 0.022** versus **0.751 ± 0.020** for TC1; total fit time was **65.5 min** versus **35.9 min**. Pooled kappa/accuracy/Macro-F1/balanced accuracy were **0.752 / 0.883 / 0.678 / 0.656** for TC1 + LP40 versus **0.751 / 0.883 / 0.677 / 0.654** for TC1. The pooled kappa difference itself rounds to **0.000**.

| Stage | Test epochs | TC1 recall | +LP40 recall | TC1 F1 | +LP40 F1 |
|---|---:|---:|---:|---:|---:|
| W | 248,341 | 0.981 | 0.980 | 0.961 | 0.960 |
| N1 | 17,877 | 0.153 | 0.148 | 0.223 | 0.217 |
| N2 | 60,494 | 0.832 | 0.834 | 0.801 | 0.804 |
| N3 | 11,610 | 0.689 | 0.700 | 0.761 | 0.767 |
| REM | 22,299 | 0.615 | 0.619 | 0.642 | 0.641 |

**Decision:** keep TC1 without the added filter. The row-normalized matrices show that N1 is still most often predicted as Wake or N2. The small N3 improvement does not translate to a clear primary-metric gain; N1 recall and F1 both fall. The extra fit time was observed in these Colab runs, so it cannot be attributed entirely to the filter.

**Saved under `CM2013_data/experiments/`:** five `TC1_LP40_68_fixed_AE_fold_<A–E>.json` checkpoints, the consolidated `TC1_LP40_68_fixed_AE.json` and the side-by-side `TC1_LP40_68_fixed_AE_confusion_vs_TC1.png`. The notebook outputs confirm all five completions and the consolidated JSON/PNG saves. The exact TC1 + LP40 report bytes were not inspected in this update.

## Paired review of the TC1 shortlist — 2026-11-10

Recomputed metrics from the saved F2, TC1 and TC1 + crop out-of-fold JSON predictions, without new fits. The three reports have identical reference labels, subject and fold order, and the same test-epoch counts; the same scaler and classifier parameters were verified. TC1 and TC1 + crop also have the same feature-matrix hash. Subject deltas give one weight to each subject and are distinct from the mean of the five fold kappas.

| Paired comparison | Subjects with higher / lower kappa | Mean subject Δkappa ± sample SD | Range of subject Δkappa | Subjects with higher N1 F1 |
|---|---:|---:|---:|---:|
| TC1 − F2 | 62 / 6 | +0.016 ± 0.013 | -0.016 to +0.049 | 49/68 |
| TC1 + crop − TC1 | 39 / 29 | +0.002 ± 0.035 | -0.116 to +0.149 | 59/68 |

The context gain is consistent across all five fold comparisons. The crop gives gains in N1 F1 in most subjects but much more variable changes in kappa (e.g. +0.149 for SC461 and -0.116 for SC435). Its small positive mean subject delta does not contradict the slightly lower mean fold kappa: the summaries aggregate different units. These are descriptive comparisons on the development set. The figure `SleepEDF_paired_kappa_68.png` shows the subject-level changes.

## Iterations 16–17 — short sigma activity and alternative band-power estimation

**TC1 + sigma (`TC1_SIGMA_68_fixed_AE`).** One column was added to TC1's 33 features. On the current 30-second Fpz-Cz epoch, a Hann STFT (1 s windows, 0.25 s step) estimated 11–16 Hz power. The feature is the largest sum over four consecutive time windows divided by total sigma power over the epoch's windows. It is a concentration measure, without event labels or a validated spindle detector. The pilot on one recording showed medians of 11.4% for N1 and 18.0% for N2; those values are exploratory. The same Random Forest and complete training/test epochs were used. All five fold kappas improved by about 0.001–0.009. N1 F1 rose 0.223 → 0.230, with N1 → Wake falling 41.69% → 40.92% and N1 → N2 rising 29.12% → 29.55%. The result therefore does not support the original hypothesis of reduced N1 → N2 confusion.

**TC1 + AR16 (`TC1_AR16_68_fixed_AE`).** Used a fixed Burg autoregressive model of order 16 (PSD evaluated with a 1,024-point FFT grid) to recalculate the same five absolute and relative powers in both the current and previous epochs. Other features, including spectral entropy, and the availability flag were unchanged; the model still uses 33 columns. The pilot compared the AR and Welch curves in N1 and N2. Across the cohort, pooled kappa rose 0.7514 → 0.7532 and N1 F1 0.2227 → 0.2330. N1 → N2 fell 29.12% → 28.75%; N1 → Wake fell 41.69% → 41.03%; N3 F1 declined by 0.0029. Fold D lost kappa. Neither the small aggregate gain nor the observed fit times justify replacing Welch in the reference.

| Fold | TC1 | TC1 + sigma | TC1 + AR16 |
|---|---:|---:|---:|
| A | 0.774 | 0.775 | 0.776 |
| B | 0.732 | 0.741 | 0.733 |
| C | 0.749 | 0.753 | 0.751 |
| D | 0.731 | 0.734 | 0.729 |
| E | 0.770 | 0.773 | 0.776 |

Fold scores are displayed as printed. Differences computed before rounding can differ from subtraction of these cells. The completed JSON and confusion PNG for each model are listed below; per-recording feature caches are in `CM2013_data/cache/viggy/sigma_stft_v1` and `CM2013_data/cache/viggy/ar_burg16_v1`.

## Iteration 18 — single-epoch CNN on Fpz-Cz

One 30-second epoch supplies 3,000 samples of Fpz-Cz at 100 Hz. Input is scaled by a fixed 100 µV, with no extra filter, no crop and no second modality. The model uses three Conv1d blocks with batch normalization and ReLU, temporal pooling and a 64-value embedding followed by a linear classifier. The T4 pilot checked the forward pass and a weight update using training rows only. For each fold: 12 passes, batch size 256, AdamW (learning rate 0.001, weight decay 0.0001), seed 0, and cross-entropy weights derived from training stage counts. The CNN, including batch normalization, was evaluated in inference mode. The EEG cache was checked for row/label alignment across 133 recordings.

Compared with F2, CNN1's balanced accuracy rose 0.638 → 0.768 and N1 F1 rose 0.195 → 0.366. N1 precision was 0.259; N2 → N1 increased from about 2.3% to 17.4% of true N2 epochs. Kappa fell in 42/68 subjects; fold A scored 0.648. These are pipeline results: F2 has engineered EEG, EOG and EMG features, while the CNN receives only EEG.

## Iterations 19–21 — controlled comparison of temporal heads

Each fold reuses its own CNN1 encoder in evaluation mode with frozen weights. It supplies 64 features per epoch. LSTM1 reads the current epoch only; LSTM5 reads it and up to four consecutive earlier epochs from the same recording. The lengths of the 360,621 windows, from one through five valid epochs, were **264 / 262 / 259 / 259 / 359,577**. Short windows were kept and padded on the right. The LSTM uses the state at the last valid epoch. Transformer5 reads the same windows with learned position embeddings relative to the current epoch, masks the padding and uses the current epoch's output. The small Transformer has one encoder layer, four attention heads, model dimension 64, feed-forward dimension 128 and no dropout. A pilot checked that changing the padded values did not change the output. All three heads used the same fixed 12-pass schedule, class weighting, seed and optimizer settings; the reserved subjects were excluded.

| Fold | CNN1 | LSTM1 | LSTM5 | Transformer5 | LSTM5 − LSTM1 | Transformer5 − LSTM5 |
|---|---:|---:|---:|---:|---:|---:|
| A | 0.648 | 0.677 | 0.708 | 0.743 | +0.031 | +0.035 |
| B | 0.698 | 0.743 | 0.772 | 0.777 | +0.029 | +0.005 |
| C | 0.743 | 0.752 | 0.785 | 0.789 | +0.033 | +0.004 |
| D | 0.720 | 0.736 | 0.791 | 0.781 | +0.055 | -0.010 |
| E | 0.707 | 0.739 | 0.776 | 0.781 | +0.037 | +0.005 |

| Pooled N1 diagnostic | LSTM1 | LSTM5 | Transformer5 |
|---|---:|---:|---:|
| Precision | 0.2816 | 0.3432 | 0.3430 |
| Recall | 0.6194 | 0.6738 | 0.6658 |
| F1 | 0.3872 | 0.4548 | 0.4527 |
| W → N1 (% of true W) | 5.1772 | 4.3863 | 4.4721 |
| N2 → N1 (% of true N2) | 17.8332 | 15.1172 | 14.6097 |

The LSTM1 → LSTM5 comparison isolates the addition of past EEG epochs with the same recurrent head design. The Transformer comparison changes the head, so the difference does not isolate an individual attention component. The Transformer led on mean kappa and Macro-F1. Its N1 F1 was slightly lower than LSTM5's, and fold D lost kappa. It improved kappas for **47/68** participants versus **F2**, not versus LSTM5. The reported fold SD and paired deltas describe this development split; no paired inference or repeat-seed run has been reported.

### Completed Colab exports since iteration 15

Paths are relative to `CM2013_data/experiments/`. Each experiment has the corresponding `_fold_A.json` through `_fold_E.json` reports. The CNN runs also saved per-fold `.pt` weights for the trained CNN or sequence head; the heads require the matching CNN1 checkpoint.

| Experiment | Consolidated report | Confusion matrix |
|---|---|---|
| TC1 + sigma | `TC1_SIGMA_68_fixed_AE.json` | `TC1_SIGMA_68_fixed_AE_confusion.png` |
| TC1 + AR16 | `TC1_AR16_68_fixed_AE.json` | `TC1_AR16_68_fixed_AE_confusion.png` |
| CNN1 | `CNN1_68_fixed_AE.json` | `CNN1_68_fixed_AE_confusion.png` |
| CNN + LSTM1 | `CNN1_LSTM1_68_fixed_AE.json` | `CNN1_LSTM1_68_fixed_AE_confusion.png` |
| CNN + LSTM5 | `CNN1_LSTM5_68_fixed_AE.json` | `CNN1_LSTM5_68_fixed_AE_confusion.png` |
| CNN + Transformer5 | `CNN1_TRANSFORMER5_68_fixed_AE.json` | `CNN1_TRANSFORMER5_68_fixed_AE_confusion.png` |

## Iteration 22 — frozen CBraMod representations with logistic regression

CBraMod's official generic checkpoint was used as a frozen EEG feature extractor. [The CBraMod paper](https://proceedings.iclr.cc/paper_files/paper/2025/file/bbbd6d915cb90be21c1254a82d45cedd-Paper-Conference.pdf) documents TUEG as the pretraining corpus and ISRUC as its downstream sleep experiment; the generic checkpoint was selected to avoid known Sleep-EDF overlap. We rely on this documented corpus provenance rather than a subject-identity audit. The [code revision](https://github.com/wjq-learning/CBraMod/tree/b9e961003214326972c567eff390e75b0287e32a) and [released checkpoint revision](https://huggingface.co/weighting666/CBraMod/commit/6d032ec37de981d90d6c37fb6539ac37a3325550) are pinned in the notebook.

Fpz-Cz at 100 Hz was resampled to 200 Hz with a polyphase FIR so each 30-second epoch could be passed as 30 one-second patches. This does not recover frequencies absent from the original recording. After fixed amplitude scaling (100 µV), the frozen encoder gives one 200-dimensional vector per patch. Averaging the 30 vectors yields 200 features per epoch. The eight-epoch pilot passed and extraction completed for all 133 recordings in **3.9 min**. The resulting matrix is `(360621, 200)`, float32, in `CM2013_data/cache/viggy/cbramod_mean_v1/8aa24a7069eada8d0a9e`.

Cell 5.21 fitted a StandardScaler and L2 multinomial logistic regression (lbfgs, C=1, balanced class weights, max_iter=2000, tol=1e-4) using only the training participants in each A–E fold. No previous-epoch context or Wake crop was used. CNN1 is the direct pipeline comparator: it uses the same Fpz-Cz channel, current 30-second epoch and subject folds.

| Fold | CNN1 kappa | CBraMod + LR kappa | Δkappa vs CNN1 | CBraMod + LR Macro-F1 | Accuracy | Balanced accuracy | LR fit (min) |
|---|---:|---:|---:|---:|---:|---:|---:|
| A | 0.648 | 0.622 | −0.026 | 0.594 | 0.799 | 0.690 | 9.875 |
| B | 0.698 | 0.602 | −0.096 | 0.607 | 0.773 | 0.690 | 10.102 |
| C | 0.743 | 0.654 | −0.089 | 0.637 | 0.813 | 0.711 | 10.426 |
| D | 0.720 | 0.651 | −0.069 | 0.634 | 0.818 | 0.691 | 10.281 |
| E | 0.707 | 0.659 | −0.048 | 0.643 | 0.812 | 0.729 | 9.897 |

| Metric | CNN1 | CBraMod + LR |
|---|---:|---:|
| Mean fold kappa ± sample SD | 0.7032 ± 0.0352 | 0.6376 ± 0.0246 |
| Pooled kappa | 0.703 | 0.637 |
| Pooled Macro-F1 | 0.687 | 0.622 |
| Pooled accuracy | 0.841 | 0.803 |
| Pooled balanced accuracy | 0.768 | 0.702 |
| Pooled N1 precision | 0.2587 | 0.2095 |
| Pooled N1 recall | 0.6273 | 0.4618 |
| Pooled N1 F1 | 0.3664 | 0.2882 |

The mean kappa fell by **0.0656** versus CNN1, with lower kappa in all five folds. Compared separately with F2, N1 recall was higher (0.462 vs 0.135) and balanced accuracy rose (0.702 vs 0.638), but pooled kappa fell by 0.098 and 57 of 68 subject kappas decreased. The matrix shows that 7.5% of true Wake and 24.9% of true REM epochs were predicted as N1, compared with 0.7% and 6.1% for F2. Against the earlier engineered-feature logistic regression (LR1, mean fold kappa 0.592 ± 0.024), this linear pipeline had a higher observed mean kappa. That comparison changes the input representation and modalities and does not isolate pretraining. The five CPU fits took **50.6 min**, in addition to the **3.9 min** spent extracting frozen features on the GPU.

**Decision:** do not shortlist this CBraMod + LR configuration. The result applies to averaged embeddings and a linear classifier on Fpz-Cz. It does not determine whether a nonlinear head, retaining the sequence of patch embeddings or fine-tuning would help. Iteration 23 tests a nonlinear classifier on the same cached features and folds. Isolating pretraining itself would require matched encoders with and without pretrained weights.

**Exports:** Colab reported saving the fold results and consolidated `CBRAMOD_LR_68_fixed_AE.json` and `CBRAMOD_LR_68_fixed_AE_confusion.png` under `CM2013_data/experiments/`. Scores above are from the supplied output; the new JSON predictions were not independently inspected.

## Iteration 23 — frozen CBraMod representations with a small MLP

At the 2026-11-15 checkpoint, the last then-planned development experiment tested whether a nonlinear classifier could improve on the CBraMod logistic regression (LR). The cache was restored for the 133 recordings and checked against the LR report's data checksum. Both variants used the same 200 mean patch embeddings from the current 30-second Fpz-Cz epoch, the same retained epochs and subject folds A–E, and identical StandardScaler settings. The scaler and balanced class weights were fitted on each fold's training participants. No holdout data, previous epochs or additional filtering were introduced.

The classifier is a **200 → 64 → 5 MLP** with ReLU, trained using weighted cross-entropy and AdamW (learning rate 0.001, weight decay 0.0001, batch size 1,024, seed 0). It used 20 fixed passes without early stopping. The encoder was frozen and no embeddings were recomputed. The comparison changes the classifier and its optimisation, so it does not isolate either effect separately.

| Fold | LR kappa | MLP kappa | Δkappa (MLP − LR) | MLP Macro-F1 | Accuracy | Balanced accuracy | MLP fit (min) |
|---|---:|---:|---:|---:|---:|---:|---:|
| A | 0.622 | 0.592 | −0.030 | 0.576 | 0.782 | 0.675 | 0.334 |
| B | 0.602 | 0.615 | +0.013 | 0.629 | 0.784 | 0.691 | 0.171 |
| C | 0.654 | 0.661 | +0.007 | 0.642 | 0.817 | 0.713 | 0.177 |
| D | 0.651 | 0.662 | +0.011 | 0.639 | 0.826 | 0.694 | 0.187 |
| E | 0.659 | 0.653 | −0.006 | 0.647 | 0.810 | 0.720 | 0.181 |

| Metric | CBraMod + LR | CBraMod + MLP64 |
|---|---:|---:|
| Mean fold kappa ± sample SD | 0.6376 ± 0.0246 | 0.6366 ± 0.0315 |
| Pooled kappa | 0.637 | 0.636 |
| Pooled Macro-F1 | 0.622 | 0.626 |
| Pooled accuracy | 0.803 | 0.803 |
| Pooled balanced accuracy | 0.702 | 0.698 |
| Pooled N1 precision | 0.2095 | 0.2141 |
| Pooled N1 recall | 0.4618 | 0.4962 |
| Pooled N1 F1 | 0.2882 | 0.2991 |

The MLP improved kappa in three folds, but the decreases in A (−0.030) and E (−0.006) outweighed those gains. Its pooled N1 recall rose **3.44 percentage points** and N1 F1 rose **0.0109**. The confusion matrices also show more true N2 and REM epochs called N1 than with LR (11.6% → 13.8% and 24.9% → 26.5%, respectively, from the rounded matrix cells). The reported subject counts (10 higher, 58 lower) are relative to **F2**, not to CBraMod + LR. MLP fitting took approximately **1.0 min on GPU**; LR took **50.6 min on CPU**. The measured times cover classifier fitting only and do not constitute a controlled speed comparison.

**Decision at the 2026-11-15 checkpoint:** the small MLP did not improve the primary metric on the pooled CBraMod features. Neither foundation-model variant reaches CNN1's mean fold kappa (0.7032). The then-planned exploration was closed with CNN + Transformer5 leading (0.7742 ± 0.0180), pending team selection. No conclusion was drawn about other CBraMod representations, sequence models or fine-tuning. The later reopening and iterations 24–25 are recorded below.

**Exports:** Colab reported all five fold completions and saved `CBRAMOD_MLP64_68_fixed_AE.json` and `CBRAMOD_MLP64_68_fixed_AE_confusion.png` under `CM2013_data/experiments/`. Results are transcribed from the supplied outputs; the new JSON predictions have not been independently inspected.

## Iteration 24 — CNN64 + F2 features with Transformer5

**Recorded:** 2026-11-19. **Experiment ID:** `CNN1_F2_TRANSFORMER5_68_fixed_AE`. This implements the fusion direction suggested by Dalya and compares it with `CNN1_TRANSFORMER5_68_fixed_AE` on the same 68 participants, 133 recordings, fixed A–E folds and all 360,621 retained test epochs.

### Recipe, controls and the choice of F2 rather than TC1

For each epoch, the matching fold's frozen CNN1 encoder supplies 64 features from Fpz-Cz. The 16 F2 features are standardized using **only that fold's training epochs**, then concatenated with the CNN features. The 80 values are projected to 64 by a trainable linear layer and passed to the same Transformer design: one encoder layer, four heads, model dimension 64, feed-forward dimension 128, no dropout, relative-to-current positions and a padding mask. Context remains the current epoch plus up to four consecutive preceding epochs from the same recording, resetting at starts and gaps.

TC1's 33 columns contain **16 current F2 values + 16 previous F2 values + one availability flag**. Giving those 33 values to every step of a five-epoch Transformer would repeat neighbouring manual features and, where available, extend their history to a sixth epoch. Using each step's 16 F2 values keeps manual and CNN inputs on the same five-epoch window. The Transformer still receives manual information from the preceding four epochs. **The 64 + 33 = 97-feature fusion was not run, and this design choice does not establish that it would perform worse.**

The pilot used only fold-A training rows, fitted the F2 scaler on **286,790 training epochs**, and verified `(32, 5, 80) → (32, 5)`, padding invariance and finite gradients while the CNN stayed frozen. All five final fits reused the original fold-specific CNN checkpoints, checking their saved hashes. Training kept **12 passes, batch 256, AdamW, learning rate 0.001, weight decay 0.0001, seed 0 and training-derived balanced cross-entropy weights**. Training and test sets were not cropped. Test features were prepared after fitting the new head.

This adds handcrafted EEG descriptors, the EOG/EMG descriptors present in F2 and a trainable projection. The comparison therefore measures the combined pipeline change; it does not isolate handcrafted EEG, extra modalities or extra parameters separately.

### Fold results and direct comparison with Transformer5

| Fold | Transformer5 kappa | Fusion kappa | Printed Δkappa | Fusion Macro-F1 | Accuracy | Balanced accuracy | Projection + head fit (min) |
|---|---:|---:|---:|---:|---:|---:|---:|
| A | 0.743 | 0.748 | +0.005 | 0.720 | 0.871 | 0.801 | 1.028 |
| B | 0.777 | 0.789 | +0.012 | 0.767 | 0.892 | 0.813 | 1.032 |
| C | 0.789 | 0.786 | −0.003 | 0.762 | 0.888 | 0.819 | 1.045 |
| D | 0.781 | 0.783 | +0.002 | 0.747 | 0.892 | 0.797 | 1.033 |
| E | 0.781 | 0.787 | +0.006 | 0.773 | 0.889 | 0.827 | 1.040 |

| Metric | Transformer5 | CNN64 + F2 → Transformer5 | Printed difference |
|---|---:|---:|---:|
| Mean fold kappa ± sample SD | 0.7742 ± 0.0180 | 0.779 ± 0.017 | — |
| Pooled kappa | 0.774 | 0.779 | +0.005 |
| Pooled Macro-F1 | 0.748 | 0.754 | +0.006 |
| Pooled accuracy | 0.883 | 0.886 | +0.003 |
| Pooled balanced accuracy | 0.806 | 0.811 | +0.005 |

Reported precision is retained; do not infer extra decimal places from the printed fold cells or confuse pooled and mean-fold differences.

| Stage | Support | Fusion precision | Fusion recall | Fusion F1 |
|---|---:|---:|---:|---:|
| W | 248,341 | 0.993 | 0.951 | 0.972 |
| N1 | 17,877 | 0.348 | 0.695 | 0.464 |
| N2 | 60,494 | 0.901 | 0.703 | 0.790 |
| N3 | 11,610 | 0.683 | 0.900 | 0.776 |
| REM | 22,299 | 0.735 | 0.807 | 0.770 |

N1 recall rose about **66.6% → 69.5%** and F1 **0.453 → 0.464** versus Transformer5. N2 recall fell about **71.6% → 70.3%** and F1 **0.796 → 0.790**. REM F1 rose **0.753 → 0.770**, despite a slightly lower recall. The global gain is not a gain in every stage measure.

The displayed participant count, **50 higher / 18 lower / 0 equal**, compares fusion with **F2**, not with Transformer5. A direct participant-level fusion/Transformer5 comparison has not yet been supplied. The modest gain in 4/5 folds is a development observation, not a significance claim. Additional head seeds, conditional on the same frozen CNNs, are proposed but have not run.

**Timing:** the five new fits total **5.2 min**, covering the projection and Transformer only. The original CNN1 training (12.2 min) is reused; feature extraction and F2 scaler fitting are excluded and recorded separately by the supplied code.

**Exports:** Colab reported `CNN1_F2_TRANSFORMER5_68_fixed_AE.json` and `CNN1_F2_TRANSFORMER5_68_fixed_AE_confusion.png` in `CM2013_data/experiments/`, plus five `_fold_A`–`_fold_E` JSON reports and `.pt` head checkpoints. The code saves each fold's F2 mean, scale, variance and sample count, with feature order in metadata, and records CNN/head checkpoint hashes. Inference requires the matching CNN1 encoder, fusion head and F2 normalization. The direct global/fold comparison with Transformer5 was appended to the consolidated report. These are output/save confirmations; the new export bytes were not independently inspected for this log update.

**Decision:** carry fusion forward as the highest observed candidate, retaining Transformer5 as its direct comparator. Stability checks, final team selection and final-model freezing remain pending.

## Iteration 25 — single-epoch CNN2D on log-power spectrograms

**Recorded:** 2026-11-19. **Experiment ID:** `CNN2D_68_fixed_AE`. This tests Helena's suggestion to transform the signal into an image-like representation. The primary comparison is **single-epoch CNN2D versus single-epoch CNN1D**, with the same Fpz-Cz channel, 30-second epochs, A–E memberships and full test recordings.

### Representation, model and checks

The network receives a numerical spectrogram, not an exported plot. EEG is divided by the same fixed **100 µV** as CNN1D. A periodic Hann STFT uses **200 samples / 2 s**, a **50-sample / 0.5-s hop**, a **200-point FFT**, no centring/padding and no detrending. The one-sided PSD is normalized by sampling rate and window energy, with interior bins doubled and DC/Nyquist retained. Input is **log10(max(PSD, 1e-12)) / 4**, a fixed transform without data-fitted normalization.

Each epoch gives **101 frequencies from 0 to 50 Hz and 57 time positions**, hence `(batch, 1, 101, 57)`. This is the full available digital spectrum, not an added 0–50-Hz band-pass filter. STFT is computed per batch on the GPU from the existing aligned EEG cache.

The CNN2D has three 3×3 convolution blocks with **16 / 32 / 64 channels**, batch normalization and ReLU; the first two have 2×2 max pooling. Adaptive pooling keeps **eight frequency regions and one time summary**, followed by a 512→64 linear/ReLU layer and a 64→5 classifier. It is trained **from scratch per fold**. No CNN1 weights, F2 features or adjacent epochs enter this model.

The pilot used eight fold-A training epochs covering all five classes, checked PSD agreement with SciPy, and verified `(8, 1, 101, 57) → (8, 64) → (8, 5)` with finite loss and gradients. The full run kept CNN1D's **12 passes, batch 256, AdamW learning rate 0.001, weight decay 0.0001, seed 0, float32 and training-derived balanced weights**, with deterministic cuDNN settings. All retained training/test epochs were used; each fold was evaluated after the fixed 12 passes.

This changes representation, architecture and parameter count. It compares the specified pipelines under a matched training schedule, rather than isolating dimensionality or testing every image-based approach.

### Fold and pooled results

| Fold | CNN1D kappa | CNN2D kappa | Printed Δkappa | CNN2D Macro-F1 | Accuracy | Balanced accuracy | STFT + CNN2D fit (min) |
|---|---:|---:|---:|---:|---:|---:|---:|
| A | 0.648 | 0.643 | −0.005 | 0.636 | 0.812 | 0.729 | 9.287 |
| B | 0.698 | 0.678 | −0.020 | 0.671 | 0.824 | 0.748 | 9.202 |
| C | 0.743 | 0.735 | −0.008 | 0.709 | 0.860 | 0.765 | 9.366 |
| D | 0.720 | 0.696 | −0.024 | 0.673 | 0.845 | 0.744 | 9.367 |
| E | 0.707 | 0.708 | +0.001 | 0.697 | 0.845 | 0.752 | 9.349 |

| Metric | CNN1D | CNN2D | Printed difference |
|---|---:|---:|---:|
| Mean fold kappa ± sample SD | 0.703 ± 0.035 | 0.692 ± 0.034 | — |
| Pooled kappa | 0.703 | 0.691 | −0.012 |
| Pooled Macro-F1 | 0.687 | 0.677 | −0.010 |
| Pooled accuracy | 0.841 | 0.837 | −0.004 |
| Pooled balanced accuracy | 0.768 | 0.747 | −0.021 |
| Observed full-model fit time (min) | 12.2 | 46.6 | — |

| Stage | Support | CNN2D precision | CNN2D recall | CNN2D F1 |
|---|---:|---:|---:|---:|
| W | 248,341 | 0.988 | 0.914 | 0.950 |
| N1 | 17,877 | 0.254 | 0.585 | 0.354 |
| N2 | 60,494 | 0.888 | 0.629 | 0.736 |
| N3 | 11,610 | 0.636 | 0.904 | 0.747 |
| REM | 22,299 | 0.517 | 0.704 | 0.596 |

All four pooled aggregate metrics were below CNN1D, with lower kappas in **4/5 folds**. N1 F1 fell about **0.366 → 0.354** and REM F1 **0.631 → 0.596**; N3 F1 rose **0.737 → 0.747**. The reported **22-higher / 46-lower / 0-equal** participant counts compare CNN2D with **F2**, not with CNN1D.

The observed **46.6 min** includes per-batch STFT, data transfer and full CNN2D optimization, versus **12.2 min** for CNN1D, about 3.8 times longer in these Colab runs. It must not be compared with fusion's 5.2-min head-only fit as if both were end-to-end costs. Decreasing training loss alone does not diagnose overfitting, establish better generalization or show that extra passes would reverse the result; no internal validation curve was supplied.

**Exports:** Colab reported `CNN2D_68_fixed_AE.json` and `CNN2D_68_fixed_AE_confusion.png` in `CM2013_data/experiments/`, plus five fold JSON reports and `.pt` checkpoints. The code stores STFT settings, model architecture, class order, split/data-order checksums, checkpoint hashes and runtime, and appends the direct CNN1D comparison. No separate PNG inputs or large spectrogram cache are required. The new output files have not been independently audited.

**Decision:** completed, not adopted for this configuration and 12-pass budget. Keep the negative result in the report. This does not establish that all spectrogram/CNN2D approaches are inferior, and it does not alter the leading fusion/Transformer5 shortlist.

## Current evaluation and holdout protocol — instructor clarification logged 2026-11-19

This records the latest instructor email supplied in the conversation and supersedes the earlier blanket prohibition on self-scoring the holdout. No holdout prediction or score has been produced in this update.

- **Development evaluation:** retain the common A–E subject folds and predictions on complete recordings, including long Wake periods.
- **Literature comparison:** additionally report CV metrics on each recording's expert-defined first-to-last sleep interval plus 30 minutes on each side. Expert test labels define an **evaluation-only mask on already-produced out-of-fold predictions**. They must not become model inputs, change those predictions or crop the holdout. This supplementary evaluation is pending.
- **One final holdout use:** select and freeze the pipeline, its settings and seed policy, complete the development refit and commit `EXPECTED_SCORE.md` with CV mean ± SD, split unit and final model commit before generating holdout predictions.
- **Submission and optional scoring:** generate a prediction for every required holdout epoch, including long Wake periods, with the course helpers. The latest email permits computing/reporting metrics from that single frozen prediction set. Do not use it to compare candidates or change the model, preprocessing, thresholds or seed afterwards.
- **Age interpretation:** the email states that holdout subjects are aged 25–88 while the first 20 dataset subjects are young. Retain the 68-subject development scope and document actual training demographics when verified; do not infer an age-specific result from these logs.

## Earlier team experiments — protocol not confirmed

Vicente supplied the following colleagues' table after the selective-filter review. These are **reported team results**, not additional verified A–E evaluations in Vicente's iteration count. The table did not identify the individual author or provide feature/classifier definitions, fold memberships, exact prediction arrays or full metric spread.

| Reported ID | Reported status | Processing | Subjects / recordings | Reported kappa | Accuracy | Macro-F1 | Fold evidence |
|---|---|---|---|---|---|---|---|
| EXP-00 | Baseline | No added preprocessing; Welch; balanced; seed 0 | 68 / 133 | 0.727 | 0.872 | 0.650 | Table asks to verify LOSO / default five-fold GroupKFold; A–E match not confirmed |
| EXP-01 | Configured | Bandpass 0.5–40 Hz; Welch; balanced; seed 0 | 68 / 133 | 0.728 | 0.872 | 0.650 | Table asks to verify same folds as EXP-00; A–E match not confirmed |
| EXP-02 | Configured | Bandpass 0.3–40 Hz; Welch; balanced; seed 0 | 68 / 133 | 0.728 | 0.872 | 0.654 | Table asks to verify same folds as EXP-00; A–E match not confirmed |
| EXP-03 | Completed | Selective wavelet D1 thresholding only: db4, level 5, soft, 0.5 lambda; Welch; balanced; seed 0 | 4 / 8 | 0.800 | 0.900 | 0.741 | Reported subject-wise LOSO, four folds; different cohort from the 68-subject comparisons |

The reported bandpass scores differ little from their reported baseline, but the unseen code and protocol have not been audited. The wavelet score cannot establish superiority over a 68-subject pipeline because cohort and evaluation differ. The table's kappa aggregation and fold SDs were not supplied; do not invent them.

**Pending confirmation:** retrieve each experiment's actual test-subject list for every fold and compare sets with A–E, allowing only fold-order/name permutations. Sixty-eight subjects, five folds and seed 0 do not guarantee the same membership. The older supplied lists demonstrably differ from A–E, but it is unknown whether the subsequently shared EXP table still uses them or has been updated. Confirm common test epochs and feature/classifier controls as well. Listing saved memberships does not require new fits; only candidates requiring re-evaluation need new A–E fits. Keep these results labelled unconfirmed until then.

## Later team experiments — reported by Helena and Dalya

These are the latest tables relayed by Vicente, recorded separately from his individual iteration series. Unless stated otherwise the tables list 68 subjects and 133 recordings. Actual saved test predictions and team commits were not supplied for this update.

### Helena Fortuny — training selection, filtering and feature removal

Vicente confirmed that Helena's C2–C10 runs use the shared subject folds. Her later supplied table also labels C11, C11b, C12 and C13 as fixed A–E. Saved predictions, complete test coverage, temporal boundary handling and exact settings have not been independently checked here. All rows list Welch features and a 30-minute Wake crop; the later rows explicitly specify training-only cropping. Preserve that restriction and verify full test coverage before a paired team comparison.

| Reported ID | Modification / feature set | Mean fold kappa ± SD | Reported pooled kappa | Accuracy | Macro-F1 | Balanced accuracy |
|---|---|---:|---:|---:|---:|---:|
| C2_68_crop30_fixed_AE | Crop only; 11 original; balanced and seed 0 marked for verification | 0.724 ± 0.022 | 0.724 | 0.866 | 0.657 | 0.643 |
| C3_68_crop30_fixed_AE | Band-pass 0.5–40 Hz + crop; 11 original; balanced | 0.724 ± 0.022 | 0.724 | 0.866 | 0.659 | 0.647 |
| C4_68_crop30_LP40_fixed_AE | LP40 + crop; 11 original; balanced | 0.725 ± 0.022 | 0.724 | 0.866 | 0.660 | 0.649 |
| C5_68_crop30_LP40_balanced_subsample_fixed_AE | C4 setup with balanced_subsample; 11 original | 0.724 ± 0.022 | 0.724 | 0.866 | 0.660 | 0.649 |
| C6_68_crop30_LP40_no_balance_fixed_AE | LP40 + crop; 11 original; no class weighting | 0.726 ± 0.019 | 0.725 | 0.866 | 0.665 | 0.658 |
| C7_68_crop30_LP40_14features_no_balance_fixed_AE | Added SEF95, theta/alpha and delta/theta; 14 features | 0.728 ± 0.024 | 0.727 | 0.867 | 0.665 | 0.658 |
| C8_68_crop30_LP40_relative_only_no_balance_fixed_AE | Replaced absolute powers with relative powers in the 11-feature set | 0.733 ± 0.024 | 0.733 | 0.870 | 0.670 | 0.664 |
| C9_68_crop30_LP40_relative_no_activity_no_balance_fixed_AE | Removed Hjorth activity from C8; 10 features | 0.707 ± 0.030 | 0.706 | 0.857 | 0.627 | 0.619 |
| C10_68_crop30_LP40_relative_no_entropy_no_balance_fixed_AE | Removed spectral entropy from C8; 10 features | 0.729 ± 0.022 | 0.728 | 0.867 | 0.667 | 0.662 |
| C11_68_crop30_SEL40_relative_balanced_fixed_AE | Selective LP40 at ≥10% high-frequency fraction + training crop; 11 relative-power features; balanced | 0.735 ± 0.024 | 0.734 | 0.871 | 0.667 | 0.656 |
| C11b_68_crop30_selectiveLP40_relative_no_balance_fixed_AE | Same 11-feature selective-filter recipe; no class weighting | 0.735 ± 0.023 | 0.735 | 0.871 | 0.670 | 0.663 |
| C12_68_crop30_selectiveLP40_relative_prev1_no_balance_fixed_AE | C11b + previous-epoch features and availability flag; 23 columns | 0.755 ± 0.026 | 0.754 | 0.881 | 0.692 | 0.682 |
| C13_68_crop30_selectiveLP40_relative_prev1next1_no_balance_fixed_AE | C12 + next-epoch features and availability flag; 35 columns; future context | **0.757 ± 0.026** | 0.757 | 0.882 | 0.694 | 0.684 |

C8 was Helena's highest-kappa configuration before the selective-filter/context additions. Removing Hjorth activity or spectral entropy lowers mean kappa in that pipeline; the decline is larger for activity. The result does not establish that either feature has the same effect in TC1 or in a neural model. C13 now has the highest reported mean kappa in her supplied series, but includes one future epoch, whereas C12 and Vicente's Transformer5/fusion use past-only context. The source spreadsheet lists `C1_68_crop30_fixed_AE_confusion.png` for C2 and `C8_68_crop30_LP40_no_balance_fixed_AE_confusion.png` for C6; verify both filenames and the meaning of “AE” in the C3/C4 feature-selection column before reuse.


The later source notes correct C11's original “absolute” description: its five band columns were reported to sum to one, so the recipe uses relative powers. Its supplied image name remains `C11_68_crop30_selectiveLP40_absolute_balanced_fixed_AE_confusion.png`; C11b likewise retains `C11b_68_crop30_selectiveLP40_absolute_no_balance_fixed_AE_confusion.png`. Preserve these reported filenames until reconciled with the saved exports.

C11 changes both filtering and the band representation against C4, so it does not isolate selective filtering. C11b versus C8 is the closer reported filter comparison: pooled kappa **0.733 → 0.735**, with Macro-F1 **0.670 → 0.670**, a small observed difference without a stability check. C12 versus C11b adds previous-epoch features and raises pooled kappa **0.735 → 0.754** and Macro-F1 **0.670 → 0.692**. The source reports positive fold deltas **+0.025 / +0.019 / +0.019 / +0.011 / +0.024**. C13 adds future signal features and gives pooled kappa **0.754 → 0.757** and Macro-F1 **0.692 → 0.694**. These are reported comparisons, not independently audited results. The source says context uses signal features rather than labels and is built before the training crop; confirm recording/gap resets in code. C11–C13 list seed 0; fit times were not supplied. No missing fold result or timing has been inferred.


### Dalya Yousif — signal screening and changes to TC1 + crop

| Reported ID | Modification | Mean fold kappa ± SD | Reported pooled kappa | Accuracy | Macro-F1 | Balanced accuracy |
|---|---|---:|---:|---:|---:|---:|
| WAV-68-01 | EEG-only db4 wavelet soft thresholding; 11 baseline features; rejected | — | 0.6784 | 0.8374 | 0.6467 | — |
| SWF-01 | Exploratory slow-wave fraction (0.5–2 Hz), 3 subjects / 5 recordings | — | — | — | — | — |
| ALPHA-01 | Exploratory alpha occupancy (8–13 Hz); sample count not reported | — | — | — | — | — |
| 01_transition_N1_bridge | Reclassified N1–N2–N1 gaps using a future prediction; 213 predictions changed | 0.750266 ± 0.025928 | 0.749783 | 0.878723 | 0.688705 | 0.672770 |
| 02_relative_temporal_delta | Added five current-minus-previous relative powers to TC1 + crop; 38 features | 0.749594 ± 0.025869 | 0.749107 | 0.878454 | 0.687657 | 0.671909 |
| 04_n1_weight15 | Multiplied N1 sample weights by 1.5 on top of balanced RF | 0.749608 ± 0.026687 | 0.749103 | 0.878468 | 0.686622 | 0.671203 |
| TC1_C1_YASA_Spindles_68_AE | Added four YASA features: count, mean duration, amplitude and frequency; 37 total | 0.749236 ± 0.025973 | 0.748767 | 0.878188 | 0.687821 | 0.672719 |

The table marks A–E for the four TC1 + crop variants. The wavelet row specifies five fixed subject-wise folds without an assignment, so equivalence to A–E has not been checked; its kappa (0.6784) is transcribed as reported because its aggregation was unspecified. The YASA row reports a fit time of 26.3 min. Seed is 0 for the wavelet and YASA rows and is unverified for the three other TC1 + crop variants. The bridge produced only a negligible kappa change against TC1 + crop (recomputed pooled reference about 0.749713), and uses a future epoch. None of the four reported variants shows a clear improvement over the TC1 + crop reference. The slow-wave and alpha rows are diagnostics rather than model evaluations.

## Archived proposal M1 — eight-subject classifier comparison (not executed)

Proposed on 2026-10-27 after completing the P1 review; **not executed or scored**. On 2026-10-29 work moved to the 68-subject phase before this proposal was run. It is retained as a historical specification, not the active next action. Any later model-family comparison should be explicitly specified on the current cohort and shared folds. The historical eight-subject count remains five of twelve.

- Question: with F2's fixed 16 descriptors, how does a regularized linear classifier compare with the current random forest? This compares model families and their class trade-offs without changing signal processing or the cohort.
- Keep X8_comb, all 44,303 epochs, no added LPF, no training crop, the same SC400–SC407 groups and eight LOSO folds. Reuse the computed feature matrix; do not recompute features or use hold-out data.
- Candidate: sklearn Pipeline(StandardScaler(), LogisticRegression(C=1.0, penalty="l2", solver="lbfgs", class_weight="balanced", max_iter=2000)). Other defaults follow the recorded scikit-learn 1.6.1 runtime. With five classes, lbfgs uses multinomial logistic loss. No C sweep or hyperparameter selection is part of this candidate.
- Pass this pipeline as clf to track.evaluate(..., cfg=BASELINE_CONFIG). The evaluator clones it per fold, so scaling, balanced class weights and model coefficients are fitted only using that fold's training subjects. RF's existing class weighting remains balanced as before.
- Retain F2's RF result as the working reference until the complete M1 panel, subject spread and paired/class inspection support a change. Report convergence warnings if any; numerical convergence must be resolved before interpreting the candidate's score.
- Method reference checked against the matching installed version: https://scikit-learn.org/1.6/modules/generated/sklearn.linear_model.LogisticRegression.html.

## Archived decision log — eight-subject checkpoint, 2026-10-27

| Module | Current choice | Rationale | Alternatives tested so far |
|---|---|---|---|
| Loading | Eight fixed development subjects, both nights, persistent data and parsed cache | Establish a common comparison cohort; three-subject pilot retained separately | Cohort expansion only; not a pipeline comparison |
| Preprocessing / filtering | No additional LPF, as in F2 | P1 lowers mean subject kappa from 0.837 to 0.833 and macro-F1 from 0.762 to 0.757; preserve the QC evidence and quality flags | P1: EEG-only 35-Hz Butterworth low-pass, order 4, forward-backward SOS; previewed and evaluated, not adopted |
| Training epoch selection | All retained epochs, as in F2 | C1 improves N1 F1 but lowers the declared primary mean kappa and pooled macro-F1 on the complete evaluation set | C1: first–last sleep plus 30-minute margins in training only; not adopted |
| Features | F2: 11 original features plus 5 relative EEG powers, 16 total | Highest current mean subject kappa and macro-F1; 6/8 subjects improve vs F1; accept the documented N1 loss vs F1 while retaining improvement over B0 | B0, F1 and F2 evaluated and inspected; F2 adopted for development |
| Feature selection / classification | Current reference: supplied scaler and balanced RF, fitted within folds | Keep F2 while preparing a controlled model-family comparison | No alternative classifier evaluated yet; M1 logistic regression is specified above before execution |
| Inference / reporting | Complete-epoch eight-subject LOSO retained for B0/F1/F2/C1/P1; P1 aggregate, class, paired subject and confusion results recorded | Preserve evaluation coverage while comparing strategies and report gains as well as losses; final 16-feature training/inference integration remains pending | B0/F1/F2, C1 and P1 JSON saves confirmed; direct C1 confusion inspection, per-record night reporting and independent JSON inspection pending |

## Archived decision log — 68-subject checkpoint, 2026-10-31

| Module | Current choice | Evidence / next comparison |
|---|---|---|
| Cohort and split | 68 development subjects / 133 recordings; exact A–E assignment | B0, F2, LP40, C1 and LR1 use the same 360,621 complete test epochs. C1 changes training selection only; LR1 uses full F2 training indices. Older cohorts and colleague splits remain separate. |
| Data preparation | Versioned per-recording original-feature and LP40-feature caches | 133 entries prepared for each recipe. F2's extra columns derive from original powers; restored order/labels were checked against all five F2 reports. C1 and LR1 reuse F2 features; C1 additionally reads headers/annotations for original event times. LR1 requires no new EDF/feature calculation. |
| Preprocessing / filtering | No additional filter in the F2_68 reference | LP40 was justified by spectra, evaluated and reviewed; 0.736 ± 0.018 vs 0.735 ± 0.017, mixed subject/class results and lower N1 F1. Preserve the experiment without adopting it. |
| Training epoch selection | Keep all retained training epochs in the F2 reference; Wake remains in every common test set | C1_68 removes only training endpoint Wake outside original-time sleep windows plus 30-minute margins. Mean fold kappa falls to 0.729 ± 0.024 while N1 F1 rises to 0.241; 36 subjects improve and 32 worsen. Preserve C1 without adopting it. |
| Features | F2_68: original 11 plus five relative powers | Five-fold gains vs B0 support the reference. Next: define previous-epoch signal-feature context with Random Forest, preserving recording boundaries/gaps and avoiding true test labels. No temporal-context run yet. |
| Classifier / fitted steps | Keep fold-fitted StandardScaler and 200-tree balanced RF, seed 0, n_jobs=-1 | LR1's balanced logistic regression was evaluated on unchanged features/folds: mean kappa 0.592 ± 0.024 vs F2 0.735 ± 0.017; 63/68 subject kappas decline. Faster fitting and higher balanced accuracy/N1 F1 do not replace the primary-metric decision. |
| Reporting / final evaluation | Fold mean/sample SD, pooled/class panel, paired subject and confusion review | F2/LP40/C1/LR1 consolidated exports confirmed; B0's optional consolidated export unconfirmed. LR1 includes solver/convergence records and paired comparisons. Save notebook/log and record the team commit. No all-68 final fit or holdout predictions yet. |

## Archived decision log — 2026-11-10

| Module | Current choice | Evidence / unresolved question |
|---|---|---|
| Cohort and split | 68 development subjects / 133 recordings, exact A–E | All nine configurations retain identical 360,621-epoch test coverage. Earlier eight-subject and colleagues' unverified splits are separate. |
| Features and classifier | **TC1 v1** + StandardScaler + balanced 200-tree Random Forest, seed 0 | Mean fold kappa 0.751 ± 0.020; all five folds and 62/68 subjects improve vs F2. Context uses past signal features from the same recording, with explicit boundary/gap handling. The fitted steps remain inside each fold. |
| Training selection | Full training epochs in TC1; retain TC1 + Wake crop as an alternative | Crop yields 0.750 ± 0.026 and Macro-F1 0.688 vs TC1's 0.677. N1 recall/F1 increase to 0.226/0.282. The paired subject review shows mixed kappa changes. Test coverage is unchanged. |
| Filtering | No additional filter in the working TC1 pipeline | With F2, LP40 and SEL40 have small global gains and mixed subject/recording effects. With TC1, full LP40 shows no clear gain (0.751 ± 0.022 vs 0.751 ± 0.020) and lower N1 F1. TC1 + SEL40 remains untested. |
| Signal diagnosis | Retain high-frequency and slow-variation checks as diagnostic evidence | High-frequency ratio audited across 133 nights; the mask selected 25,446 epochs. Slow variation was inspected in three nights only; no high-pass model was fitted. Neither diagnostic is artifact ground truth. |
| Team choice | Shortlist TC1 and TC1 + crop; write up results now | Verify fold memberships and test coverage for any colleague candidate that could affect selection. A new run is optional and should answer a specific question on A–E. |
| Reproducibility and submission | Pin final code, refit the chosen pipeline on all 68, commit `EXPECTED_SCORE.md` before holdout predictions | JSON/PNG saves are recorded for the nine development runs; exact F2, TC1 and TC1 + crop reports were checked. Team experiment/final commit, reproducible inference and holdout prediction remain pending. |

## Archived decision log — 2026-11-15

| Decision | Evidence / next action |
|---|---|
| Keep Transformer5 as leading development candidate | Highest observed mean fold kappa (0.7742 ± 0.0180) and pooled Macro-F1 (0.748). Its improvement over LSTM5 is small and concentrated largely in fold A. |
| Retain LSTM5 and the engineered temporal references | LSTM5 demonstrates the clearest controlled context gain and slightly higher N1 F1 than Transformer5. TC1 + sigma has the highest observed kappa in the RF series; TC1 remains the matched reference for the sigma, AR and filtering tests. |
| Isolate what each comparison can show | CNN1 vs F2 changes the input modalities and model. LSTM1 vs LSTM5 holds the EEG encoder, recurrent head design and training recipe fixed. A different sequence head tests a different architecture. Report full test coverage and fold spread alongside pooled metrics. |
| Close the planned exploratory runs with the CBraMod comparison | The nonlinear MLP did not improve mean kappa on the same embeddings. Keep both CBraMod runs for the report. Check saved memberships and test order for any team result considered for final selection. |
| Keep the final holdout separate | Select and reproduce the final pipeline before using any reserved subject. Record the team code commit and commit `EXPECTED_SCORE.md` before predicting the holdout. |

## Current decision log — 2026-11-19

| Decision | Evidence / next action |
|---|---|
| Carry CNN64 + F2 → Transformer5 as the leading observed candidate | Mean fold kappa 0.779 ± 0.017 and pooled Macro-F1 0.754; pooled kappa +0.005 versus Transformer5, with higher kappas in 4/5 folds. Final selection is pending. |
| Retain Transformer5 as the matched fusion comparator | Same frozen fold-specific CNNs, five-epoch past-only context and training schedule. Review paired participant differences and head-seed variability before calling the small gain robust. |
| Keep the CNN2D result without adopting its tested configuration | Lower kappa in 4/5 folds and all four pooled aggregate metrics below CNN1D; observed full fit time 46.6 vs 12.2 min. This concerns the specified representation, architecture and 12-pass budget. |
| Keep interpretation of fusion specific | F2 also adds EOG/EMG descriptors and a trainable projection is introduced. The 97-input CNN64 + TC1 variant is untested; 16 F2 values per step keep the manual history on the same five-epoch window. |
| Use reported team results with their protocol labels | Helena's C13 and Dalya's bridge use future context. Keep context scope visible and confirm saved memberships/test coverage before final team selection. |
| Validate the existing shortlist | Proposed additional seeds repeat the two heads with CNNs frozen and measure conditional head variability. No extra seed run or direct fusion/Transformer5 participant panel has yet been supplied. |
| Add supplementary sleep-window CV evaluation | Use expert test labels only to mask saved predictions for first-to-last sleep ±30 min. Preserve complete-recording primary scores and all holdout epochs. |
| Follow the latest one-use holdout rule | Freeze, refit and commit EXPECTED_SCORE.md before prediction; optional self-scoring is allowed on that single frozen prediction set. Never use it for model selection or adjust the model afterwards. |

## Revisions

On 2026-10-22 the provisional **F1 relative-only band-power choice was revisited and replaced with F2 combined absolute/relative powers** after the predeclared F2 experiment and diagnostic review. Before F2, F1 was preferred to B0 because its mean subject kappa and macro-F1 were slightly higher and its subject spread lower. F2 then raised mean subject kappa from 0.828 (SD 0.054) to 0.837 (SD 0.052), and pooled macro-F1 from 0.758 to 0.762, with paired gains in 6/8 subjects. N1 F1 fell from 0.368 to 0.354, while N2, N3 and REM improved versus F1; the overall gain was judged worth this trade-off for the declared metrics. All numbers refer to the same eight-subject development cohort. This records an actual provisional choice changed after a later result; the team's final choice remains open.

On 2026-10-29 the **development scope and validation protocol were revised**: the first-eight cohort became historical exploration and a new 68-subject baseline was established with explicit A–E memberships. The eight-subject M1 run was postponed rather than reported as completed. The F2 feature strategy was then evaluated anew on the same 68-subject folds and retained as the provisional reference (0.735 ± 0.017 versus B0_68 0.728 ± 0.012 across five folds). This repeats a feature strategy on a larger, overlapping cohort; it is not an independent holdout test or evidence that the eight- and 68-subject absolute scores are directly comparable.


On 2026-10-31 the **LP40 review/export checkpoint was closed** after the targeted spectral inspection and five-fold run. The no-additional-filter F2_68 choice was retained after testing a justified 40-Hz candidate. LP40 attenuated the inspected component and SC461's subject kappa rose by 0.030, but aggregate gains were small and N1 performance declined. This records a tested alternative and its trade-offs, not an independent holdout result.

On 2026-10-31 the **training-only crop was re-evaluated on the 68-subject A–E protocol**, now using original elapsed times rather than retained-row margins. C1_68 improves N1 F1 and macro-F1, unlike the earlier eight-subject macro-F1 result, but again lowers the primary kappa relative to its cohort-matched F2 reference. The larger-cohort result updates the evidence and preserves the trade-off; it does not make the two cohorts or crop implementations identical. F2_68 remains the reference, and C1's report/image saves are confirmed.

On 2026-10-31 the **first classifier-family comparison on A–E was completed**: LR1 replaced Random Forest with balanced logistic regression while keeping F2 features and full training/test epochs. Mean fold kappa fell from 0.735 ± 0.017 to 0.592 ± 0.024, despite faster fits, higher balanced accuracy and better N1 F1. The working classifier remains Random Forest. The eight-subject M1 proposal is still historical and unexecuted; it must not be relabelled as this 68-subject run. At that checkpoint the next agreed comparison was temporal-context features with the F2 Random Forest, followed by selected combinations; neither had run yet. Both were subsequently evaluated as documented in the later revisions below.

On 2026-11-02 the **F2 working-feature decision was revisited after adding past-only temporal context**. TC1 raised mean fold kappa from 0.735 ± 0.017 to 0.751 ± 0.020, improved all five fold kappas and 62/68 participant kappas, and improved pooled Macro-F1 from 0.659 to 0.677. TC1 replaced F2 as Vicente's primary-metric reference; F2 remains the 16-feature reference for isolated changes.

On 2026-11-02 the **earlier decision against adopting Wake cropping was revisited after the context result**. TC1 + crop keeps mean kappa close to TC1 (0.750 versus 0.751), raises Macro-F1 from 0.677 to 0.688 and N1 F1 from 0.223 to 0.282, but increases fold SD and changes false-positive/recall trade-offs. This is evidence of an evaluated combination: the crop's effect was remeasured with the changed feature representation rather than assumed to equal its earlier F2 effect. TC1 remains the primary reference and the cropped variant is retained as a useful alternative.

After that combination, **filtering was revisited rather than discarded universally**. Three before/after checks were followed by the all-133-record signal-ratio audit and SEL40. Its global kappa is 0.736 versus F2's 0.735, while selected-epoch Macro-F1 rises 0.469 → 0.515 and the ten most-selected nights split five better/five worse. The diagnosis updates the earlier broad interpretation to a specific one: the tested selective filter has local benefits and mixed recording effects, without a clear global advantage. It is not adopted. Its selective application with TC1 remains untested; the later iteration 15 instead evaluated full LP40 with TC1.

On 2026-11-04 this log was **consolidated against the supplied November 2 model, confusion, cache and diagnostic outputs**. Current decisions, the comparison panel, contribution entries and remaining work were updated. Colleagues' latest fold usage is explicitly left unconfirmed rather than assuming it matches either A–E or their older lists. No new fit, final score, repository commit or holdout evaluation was produced by editing this log.

On 2026-11-10 **the full LP40 filter was revisited with the temporal model**. The same TC1 context and A–E protocol gave 0.751 ± 0.022 after filtering versus 0.751 ± 0.020 without it. N3 recall rose, but N1 F1 fell from 0.223 to 0.217. Keep the simpler TC1 as the working reference. The exact paired review of F2, TC1 and TC1 + crop helped separate the consistent context gain from the crop's mixed subject-level kappa effects.

The notebook was reorganised into daily setup, saved results, optional training, diagnostics and archive sections. The missing `RUN_TC1_LP40_68 = False` default was added; ordinary setup no longer starts the LP40 combination or rewrites experiment reports. The F2 vs SEL40 matrix can be viewed from saved predictions. This reorganisation and the paired review do not add new training iterations.

On 2026-11-14 the development series was extended to short-time EEG features, Burg AR and learned EEG features. The controlled LSTM comparison confirmed the value of past epochs with a learned representation. Transformer5 then became the leading candidate by mean fold kappa; it has not been selected as the final team model. The CBraMod linear evaluation was completed and fell below CNN1 in all five folds; the result did not change the development shortlist. The newer Helena and Dalya tables are now recorded separately from the earlier unconfirmed EXP table.

On 2026-11-15 the CBraMod embeddings were reused for a 64-unit MLP. Higher N1 F1 did not translate into higher mean kappa: 0.6366 versus 0.6376 for logistic regression. This closes the planned exploratory comparisons; the leading development candidate and the reserved holdout are unchanged.


On 2026-11-19 the exploratory closure was **reopened for two specific team suggestions**. Dalya's fusion direction was implemented as 64 CNN + 16 F2 features at each step of the existing five-epoch Transformer, giving 0.779 ± 0.017 mean fold kappa and pooled Macro-F1 0.754. It becomes the leading observed candidate, subject to stability and paired review; the 33-feature TC1 fusion remains untested. Helena's spectrogram direction was evaluated with a new single-epoch CNN2D, giving 0.692 ± 0.034 versus CNN1D's 0.703 ± 0.035, and was not adopted. Vicente's 68-subject count is now **19 completed configurations**. This records both the reopening and its outcome rather than erasing the earlier closure.

The same update adds Helena's supplied C11–C13 results (including C11b), clarifies future-epoch information in C13, and records the latest instructor email: report supplementary sleep-window CV metrics and permit optional scoring of one frozen holdout prediction set after the required commit. No final model, final-model commit, additional seed result, sleep-window score or holdout score is created by this log update.

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
| 68-subject preparation / protocol | Vicente Soares | Continued the existing download to 68 subjects / 133 pairs, supplied the read-only folder inventory, executed per-recording versioned feature caching and supplied all 133 completion records; assembled the 360,621-row baseline and validated the exact A–E indices. Code, checking, interpretation and log preparation were assisted by ChatGPT. | Shared-protocol discussion occurred; no peer review of the new run code/results is recorded. |
| 7 (B0_68) | Vicente Soares | Timed and saved fold A, reused A while completing B–E, supplied all fold metrics/timings and the pooled class report/confusion figure. Code and log preparation were assisted by ChatGPT. | Peer review not yet recorded. |
| 8 (F2_68) | Vicente Soares | Derived 16 features from the cached baseline, executed five new fixed-fold fits, supplied paired fold gains, full pooled metrics, per-stage comparison and confusion figure; subsequently confirmed consolidated F2 JSON/PNG saves. Code, interpretation and log preparation were assisted by ChatGPT. | Peer review not yet recorded. |
| 9 (LP40_68) / 68-subject QC | Vicente Soares | Executed the three-participant selection, time/PSD inspection, near-50-Hz power audit and LP40 preview; prepared all 133 feature caches; ran five fixed-fold fits; supplied pooled/class/fold/subject results and confusion figure; confirmed consolidated JSON/PNG saves at closure. Code, interpretation and log preparation were assisted by ChatGPT. | Peer review of LP40 results not yet recorded. |
| 10 (C1_68) / session recovery | Vicente Soares | Restored 133 original feature tables in saved F2 order and verified all five report alignments; recovered original event timelines for 133 recordings after a Drive I/O disconnect; inspected training counts/distributions; executed five training-only crop fits; supplied the fold/pooled/class panels, side-by-side confusion matrix, participant counts (36 higher, 32 lower) and explicit per-fold/consolidated JSON/PNG save messages. Code, checking, interpretation and log preparation were assisted by ChatGPT. | Peer review of C1_68 results not yet recorded. |
| 11 (LR1_68) | Vicente Soares | Prepared the predeclared same-feature logistic-regression candidate; corrected the reporting-class import before fitting; executed five A–E fits; supplied explicit per-fold saves, timings/iterations, fold and pooled/class panels, the side-by-side confusion image, participant counts (5 higher, 63 lower) and confirmed consolidated JSON/PNG saves. Code, checking, interpretation and log preparation were assisted by ChatGPT. | Peer review of LR1 results not yet recorded. |
| Daily-session restoration / TC1 preparation | Vicente Soares | Reported missing variables and the annotation-read Drive error; executed restored setup and validated B0/F2 order against five saved reports; used original epoch onsets to build the same-recording past-only 33-feature matrix. Code, checking and notebook reorganisation were assisted by ChatGPT. | No separate peer review of the revised setup is recorded. |
| 12 (TC1_68) | Vicente Soares | Executed five A–E fits; supplied fold/pooled/class metrics, timings, the F2/TC1 confusion figure, 62-higher/6-lower participant counts and consolidated JSON/PNG save confirmations. Code, checking, interpretation and log preparation were assisted by ChatGPT. | Peer review of TC1 results not yet recorded. |
| 13 (TC1_C1_68) | Vicente Soares | Checked unchanged crop counts and full test coverage; ran five TC1 + crop fits; supplied comparisons against TC1, the confusion figure, 39-higher/29-lower participant counts and confirmed JSON/PNG saves. Code, checking, interpretation and log preparation were assisted by ChatGPT. | Peer review of the combined strategy not yet recorded. |
| Post-TC1 filtering diagnosis / 14 (SEL40_68) | Vicente Soares | Supplied three before/after signal/PSD audits; prepared all 133 ratio caches and quality-summary export; diagnosed the SC4152E0 expected-key lookup, completed validated assembly from 74 LP40 caches, ran five A–E fits and supplied all result panels, confusion figure, 37-higher/31-lower participant counts and JSON/PNG saves. Executed the no-fit selected/rest and top-ten-night diagnosis and confirmed it was appended to the report. Code, checking, interpretation and log preparation were assisted by ChatGPT. | No independent peer review of SEL40 or its diagnostic threshold is recorded. |
| 15 (TC1_LP40_68) / slow-signal check | Vicente Soares | Inspected three development EEG recordings and the SC4351F0 transient; recovered the original LP40 caches, prepared the 33-feature context, ran five A–E fits and supplied fold, pooled and stage comparisons plus the paired confusion image and save confirmations. Code, interpretation and log preparation were assisted by ChatGPT. | Team review not yet recorded. |
| Paired review and notebook update | Vicente Soares, assisted by ChatGPT | Supplied the F2/TC1/crop JSON files for alignment checks and the paired subject review. Reorganised the notebook with training off by default and separate read-only matrix display. | No new fitting or independent team review. |
| Later team experiment table | Colleagues not individually identified in the supplied table; relayed by Vicente | Shared EXP-00/01/02 results on 68 subjects and EXP-03 wavelet results on four subjects. Vicente clarified that current fold usage is uncertain. These remain separate reported team results, not additional verified A–E runs in Vicente's count. | Authors, actual memberships, test coverage and feature/classifier controls still to confirm. |
| Earlier team split documentation | Colleague (not identified in the supplied message); relayed by Vicente | Supplied the earlier five-fold train/test subject memberships. The lists were checked and retained separately from A–E; no colleague score is reclassified as an A–E result. | Split-list consistency checked; the unseen colleague pipeline was not audited. |
| 16–17 (sigma and AR) | Vicente Soares | Ran diagnostic and extraction cells, five fixed-fold fits per variant, and supplied metrics, class effects, confusion images and save confirmations. Code, interpretation and log preparation were assisted by ChatGPT. | No independent review of the new export files recorded. |
| 18–21 (CNN, LSTM and Transformer) | Vicente Soares | Ran GPU pilots; verified aligned raw EEG; completed the fixed-fold CNN, LSTM controls and Transformer comparison and supplied results, checkpoint confirmations and confusion images. Code, interpretation and log preparation were assisted by ChatGPT. | Candidate selection with the team is pending. |
| 22 (CBraMod) | Vicente Soares | Confirmed the official checkpoint pilot, extracted features for all 133 recordings, completed five logistic-regression fits and supplied the CNN1 comparison, confusion matrix and save confirmations. Code, verification and log preparation were assisted by ChatGPT. | No independent inspection of the new JSON predictions recorded. |
| 23 (CBraMod + MLP64) | Vicente Soares | Restored the same cached embeddings, ran the five GPU fits and supplied the fold/pooled comparison against LR, the F2 confusion figure and save confirmations. Code, verification and log preparation were assisted by ChatGPT. | No independent inspection of the new JSON predictions recorded. |
| C2–C13 (including C11b) | Helena Fortuny; results relayed by Vicente | Reported training-only Wake cropping, global/selective filtering, class weighting, feature replacement/removal, and previous/next-epoch context. The spectrogram direction was suggested by Helena and executed by Vicente as iteration 25. | Saved memberships, full test coverage and exact configuration/boundary checks remain to be audited; C13 includes future context. |
| Wavelet, screening and TC1 + crop extensions | Dalya Yousif; results relayed by Vicente | Reported wavelet denoising, exploratory signal descriptors, a prediction bridge, temporal deltas, N1 weighting and YASA spindle features. | Fold and evidence limits are recorded above. |
| 24 (CNN64 + F2 + Transformer5) | Vicente Soares; fusion direction suggested by Dalya Yousif | Restored aligned EEG and checked existing CNN1 weights; ran the train-only-scaling/padding/gradient pilot and five fusion-head fits; supplied fold/global/stage metrics, direct Transformer5 comparison, confusion image and save confirmations. Code, verification, interpretation and log preparation were assisted by ChatGPT. | New export bytes, paired participant comparison, repeat-seed stability and independent team review remain pending. |
| 25 (CNN2D) | Vicente Soares; spectrogram direction suggested by Helena Fortuny | Ran the numerical spectrogram/PSD/gradient pilot and five CNN2D fits; supplied fold/global/stage metrics, direct CNN1D comparison, confusion image and save confirmations. Code, verification, interpretation and log preparation were assisted by ChatGPT. | Negative result retained; new export bytes and independent team review not yet audited. |

Further contributions and result reviews from named team members will be added when supplied.

## Next steps and missing evidence — updated 2026-11-19

1. **Review the existing shortlist with the team.** Treat CNN64 + F2 → Transformer5 as the highest observed candidate and Transformer5 as its direct comparator. Preserve LSTM1 → LSTM5 as the clearest matched context demonstration and keep the engineered references. Record both new iterations and the non-adopted CNN2D result; no extra architecture is required to close this two-experiment reopening.
2. **Check paired predictions and the small fusion advantage.** Verify saved fusion/Transformer5 memberships, test order, targets, hashes and full coverage, then compare the same participants. The 50/18 count is relative to F2. Two additional, prespecified seeds for both heads are proposed with the original fold-specific CNNs frozen. Record all seed results and their spread rather than choosing the best seed. This measures head-training variability conditional on those CNNs, not full encoder-training variability. These checks have not run.
3. **Add the instructor's supplementary CV protocol.** Compute complete-recording and expert-defined sleep-period ±30-minute metrics from the same saved out-of-fold predictions. Use expert labels only to define the evaluation window and original epoch times to apply margins. Separate this supplementary literature comparison from the full-recording primary protocol. No retraining is needed for the mask, and no window score is yet available.
4. **Write, review and reproduce the final pipeline.** Update the report with the pilot/68-subject distinction, temporal comparisons, fusion's modality/projection changes, CNN2D's negative result and team contributions. Commit code and this log, record actual team/model revisions, provide a README and locked environment, and verify course-compatible inference on development data. Fusion requires matching CNN weights, F2 features and saved normalization; sequence boundaries, gaps, class order and complete epoch coverage must match CV.
5. **Select, freeze and refit on all 68 development subjects.** Fix pipeline settings and seed policy before the holdout. Complete the development refit and commit `EXPECTED_SCORE.md` with CV mean ± SD, subject split unit and final model commit before generating holdout predictions.
6. **Predict the holdout once and submit.** Use course helpers to write predictions for every required epoch, including long Wake periods. Under the latest instructor email, optional metrics may be computed/reported from that one frozen prediction set. Do not compare models on it or change preprocessing, the model, thresholds or seeds afterwards. Submit the report PDF, repository link and `predictions.csv`.

**Current status:** 19 completed 68-subject configurations in Vicente's series. Both new team-suggested experiments are complete; CNN64 + F2 → Transformer5 leads on the reported development metrics. Paired/stability checks, supplementary sleep-window CV metrics, team selection, development-only inference verification, the final refit/commit and the one-use holdout submission remain pending.
