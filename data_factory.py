import pandas as pd

class DataFactory:
  def __init__(self):
    pass

  def load_df(self, *paths):
    self.dataframes = []
    for path in paths:
      self.dataframes.append(pd.read_csv(path))
    return self.dataframes
  
  def save_csv(self, path):
    i = 0
    for df in self.dataframes:
      df.to_csv(path + '/' + str(i) + '.csv')
      i += 1
  
  def save_hdf(self, path):
    i = 0
    for df in self.dataframes:
      df.to_hdf(path + '/' + str(i) + '.hdf', key='df', mode='w')
      i += 1
