import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb
import pandas_profiling 
from pandas_profiling import ProfileReport
import sys

ReqData=None
class BasicCleaning:
    def __init__(self):
        self.df = None  # Initialize the instance variable to store the dataset

    def pass_dataset(self):
        try:
            self.df = pd.read_csv(r'C:\Users\ramgo\OneDrive\Desktop\Learn\AIML Architecture\DataPreprocessingArchitecture\Diwali Sales Data.csv', encoding='ISO-8859-1')
            print("...........Data Set Imported Successfully.........")
        except:
            print("Please check the file/path given")
            sys.exit(1)
        finally:
            print("Moving to EDA fsm")
        
    def EDABeforeStandardized(self):
        rpt=ProfileReport(self.df, title="Initial Report")
        print("...........Generating HTML Report for Quick View.................")
        rpt.to_file("InitialData.html")
        print("Moving to statistics fsm")

    def dataset_statistics(self):
        print(".........Generating Statistics.......")
        print("Basic Statistics", self.df.describe())
        print("Moving to Cleaning fsm")

    def cleaning_dataset(self):
        print(".....Cleaning Started......")
        self.df.drop_duplicates(inplace=True)
        self.df.dropna(axis=1,how='all',inplace=True)
        print("shape after dropping columns that are having completely Nan or empty",self.df.shape)
        print("Basic Cleaning Done and moving to generate report")

    def AdvanceCleaningFilling(self):
        total_values=self.df.size
        #print(total_values)
        #print(self.df.isnull().sum())
        missing_percentage=((self.df.isnull().sum().sum())/(total_values))*100
        if (missing_percentage<5):
            self.df.dropna(inplace=True)
    
    def AfterBasicCLeaning(self):
        print(".......Report is being generated.......")
        rpt1=ProfileReport(self.df,title='Report After Cleaning')
        rpt1.to_file("AfterBasicCleaning.html")
        

    def StoreReqData(self):
        self.df.to_csv("ReqData.csv")
        print("Data saved in file for further analysis")
        print("...........Moving to Deeper Analysis.......")
        global ReqData
        ReqData = self.df
        


    def run_all(self):
        self.pass_dataset()
        self.EDABeforeStandardized()
        self.dataset_statistics()
        self.cleaning_dataset()
        self.AdvanceCleaningFilling()
        self.AfterBasicCLeaning()
        self.StoreReqData()
    



obj=BasicCleaning()
obj.run_all()

