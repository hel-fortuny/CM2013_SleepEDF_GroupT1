# Expected hold-out score — Sleep-EDF, Team T1

## Frozen final model

- Model: CNN1_F2_TRANSFORMER5_FINAL68_seed0
- Final model/code commit: c10975593f05ce70442e4ab773df5e93ba4ce673
- Notebook: final_model/capstone_viggy_v2_final.ipynb
- Fixed seed: 0

The model combines 64 CNN features with 16 handcrafted F2 features,
followed by a projection and a Transformer using the current epoch
and up to four consecutive preceding epochs from the same recording.
Context restarts at recording boundaries and gaps.

## Development cross-validation

- Experiment: CNN1_F2_TRANSFORMER5_68_fixed_AE
- Primary metric: Cohen's kappa.
- Mean ± SD across five fixed folds A–E: 0.7787 ± 0.0174.
- Split unit: participant. All recordings from one participant remain
  within the same fold.
- Development cohort: 68 participants, 133 recordings, 360,621 valid epochs.
- Evaluation scope: complete recordings, including long Wake periods.
- Learned preprocessing and models were fitted within training folds only.

The final model was refitted on all development epochs, with 12 passes
for the CNN and 12 passes for the fusion head. The CNN was frozen during
fusion training. F2 standardization was fitted on development data only.

## Hold-out protocol

The ten hold-out participants were excluded from development.
This file is registered before hold-out prediction.

The frozen model will predict every eligible hold-out epoch, including
Wake, without label-based cropping. The hold-out will be used once.
No model, preprocessing, threshold or seed adjustments will be made
after inspecting its results.
