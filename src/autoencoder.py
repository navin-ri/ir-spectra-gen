# ---
# Name: Autoencoder script
# Version: 0.1.0
# ---

import pandas as pd
import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import DataLoader

# Import spectra dataset
spectra_1 = pd.read_csv('/Users/navin/Library/CloudStorage/Dropbox-AIZOTH/研究/Navin/spectra_gen/ir-spectra-gen/data/IR_spectra/Broadened_IR_Spectra/2C9C_b3lyp_broadened_Gauessview_gamma_5_dx2.csv')

spectra_2 = pd.read_csv('/Users/navin/Library/CloudStorage/Dropbox-AIZOTH/研究/Navin/spectra_gen/ir-spectra-gen/data/IR_spectra/Broadened_IR_Spectra/10C_b3lyp_broadened_Gauessview_gamma_5_dx2.csv')

print(spectra_2.head())
print(spectra_2.describe())
