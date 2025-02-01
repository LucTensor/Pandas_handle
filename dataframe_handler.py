import pandas as pd 
import numpy as np

class PandasHandler:
    def __init__(self, data):
        self.df = pd.DataFrame(data)
        self.cols_containing_NaN = self._get_columns_with_nan()

    def _get_columns_with_nan(self):
        return self.df.columns[self.df.isna().any()].tolist()

    def display_col_with_nan(self):
        nan_count = self.df.isnull().sum()
        print('total NaN:' + str(nan_count.sum()))
        print(f'Fields containing NaN:    {nan_count[nan_count>0].sort_values(ascending=False)}')
        return self.cols_containing_NaN


def load_csv(file_path, parse_dates=True):
    df = pd.read_csv(file_path,  parse_dates=parse_dates)
    handler = PandasHandler(df)
    _ = handler.display_col_with_nan()
    return handler
