import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


class Visualizer:
    """
  The department reads the data after processing and creates
   hist & pie 2 Feature

    """

    def __init__(self, data: str):
        """
        param dataset: The dataset CSV file path.
        """
        self.data = data

    def dataset(self, x: str, y: str, z: str):
        """
        param x: The x-axis.
        param y: Feature1.
        param z: Feature2.
        """
        df = pd.read_csv(self.data)

        fig, axes = plt.subplots(1, 2)

        overal_qual = df[y].to_numpy()
        overal_qual_values, overal_qual_counts = np.unique(overal_qual, return_counts=True)
        axes[0].pie(overal_qual_counts, labels=overal_qual_values, autopct='%1.1f%%')

        axes[1].hist(df[y], bins=20, color="green")
        axes[1].hist(df[z], bins=20, color="blue", alpha=0.5)

        axes[0].set_title('pie')

        axes[1].set_title('hist')

        plt.tight_layout()

        plt.show()
