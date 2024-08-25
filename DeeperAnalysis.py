from fsms import ReqData  #ReqData is from fsms.py

class DeeperAnalysis:

    def CheckData(self):
        self.df=ReqData
        if self.df.empty:
            print("Data Not Received")
        else:
            print("Connection Successfull")
            print("Data Received")



    def run_daall(self):
        self.CheckData()


if __name__ == "__main__":
    obj2 = DeeperAnalysis()
    obj2.run_daall()