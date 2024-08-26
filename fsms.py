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
        print("Shape of DataSet before cleaning",self.df.shape)
        print("..........Dropping Columns............")

    
    def DroppingColumns(self, threshold=40):
        missing_count=self.df.isna().sum()
        missing_count_bypercentage=(missing_count/len(self.df))*100
        columns_to_drop = missing_count_bypercentage[missing_count_bypercentage > threshold].index
        self.df.drop(columns=columns_to_drop, inplace=True)
        print("...........Dropping Rows..........")
    
    def DroppingRows(self, threshold=50):
        missing_counts_by_row = self.df.isnull().sum(axis=1)
        missing_percentage_by_row = (missing_counts_by_row / len(self.df.columns)) * 100
        rows_to_drop = missing_percentage_by_row[missing_percentage_by_row > 50].index
        self.df.drop(index=rows_to_drop, inplace=True)
        print("Shape of DataSet after cleaning",self.df.shape)
    
    
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
        self.DroppingColumns()
        self.DroppingRows()
        self.AfterBasicCLeaning()
        self.StoreReqData()
    



obj=BasicCleaning()
obj.run_all()

