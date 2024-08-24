import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
import pandas_profiling 
from pandas_profiling import ProfileReport

class FSMS:
    def __init__(self):
        self.df = None  # Initialize the instance variable to store the dataset

    def pass_dataset(self):
        try:
            self.df = pd.read_csv(r"C:\Users\ramgo\OneDrive\Desktop\Learn\DiwaliSalesAnalysis\DiwaliSales\CleanedData.csv", encoding='utf-8')
        except:
            print("Please check the file/path given")
            exit()
        finally:
            print("Script executed successfully")
        
    def EDABeforeStandardized(self):
        rpt=ProfileReport(self.df, title="Example")
        rpt.to_file("FinalData.html")

    def dataset_statistics(self):
        print(self.df.head())

    def run_all(self):
        self.pass_dataset()
        self.dataset_statistics()
        self.EDABeforeStandardized()
obj=FSMS()
obj.run_all()