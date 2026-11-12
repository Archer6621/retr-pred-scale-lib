import pandas as pd
from pathlib import Path

nieman_data = pd.read_csv(Path(__file__).resolve().parent / 'ep_nieman_tudelft_18_10.csv')