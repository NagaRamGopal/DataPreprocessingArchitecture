import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
import pandas_profiling 
from pandas_profiling import ProfileReport
import sys

class FSMS:
    def __init__(self):
        self.df = None  # Initialize the instance variable to store the dataset

    def pass_dataset(self):
        try:
            self.df = pd.read_csv(r'C:\Users\ramgo\OneDrive\Desktop\Learn\DiwaliSalesAnalysis\DiwaliSales\Diwali Sales Data.csv', encoding='ISO-8859-1')
            print("...........Data Set Imported Successfully.........")
        except:
            print("Please check the file/path given")
            sys.exit(1)
        finally:
            print("Moving to EDA fsm")
        
    def EDABeforeStandardized(self):
        rpt=ProfileReport(self.df, title="Example")
        print("...........Generating HTML Report for Quick View.................")
        rpt.to_file("FinalData.html")
        print("Moving to statistics fsm")

    def dataset_statistics(self):
        print(".........Generating Statistics.......")
        print(self.df.head())

    def run_all(self):
        self.pass_dataset()
        self.EDABeforeStandardized()
        self.dataset_statistics()
obj=FSMS()
obj.run_all()