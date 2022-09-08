import pandas as pd
from pycaret.regression import *

delaney_with_descriptors_url = 'https://raw.githubusercontent.com/dataprofessor/data/master/delaney_solubility_with_descriptors.csv'
dataset = pd.read_csv(delaney_with_descriptors_url)

model = setup(data = dataset, target = 'logS', train_size=0.8, silent=True)

compare_models()
