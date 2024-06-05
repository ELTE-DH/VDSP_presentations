import pandas as pd
from matplotlib import pyplot as plt

class SunspotAnalyzer:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None

    def load_data(self):
        self.data = pd.read_csv(self.file_path)

    def filter_many_observations(self, df, min_observations):
        return df[df['Observations'] > min_observations]

    def filter_std_deviation(self, df, max_std_deviation):
        return df[df['Standard Deviation'] < max_std_deviation * df['Number of Sunspots']]

    def calculate_average_by_year(self, min_observations=5, max_std_deviation_ratio=0.2):
        df = self.data.copy()
        if min_observations is not None:
            df = self.filter_many_observations(df, min_observations)
        if max_std_deviation_ratio is not None:
            df = self.filter_std_deviation(df, max_std_deviation_ratio)
        df = df.groupby('Year').mean()
        return df

    def plot_average_sunspots(self, save_path):
        df_avg = self.calculate_average_by_year()
        plt.plot(df_avg.index, df_avg['Number of Sunspots'])
        plt.savefig(save_path)