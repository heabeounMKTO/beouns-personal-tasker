
from multiprocessing.sharedctypes import Value
import numbers
from operator import truediv
from art import tprint, text2art
import pandas as pd
import os
from commonUtils import df_to_table

from rich.table import Table
from rich.console import Console

from pathlib import Path
from datetime import date




taskIdList = []
taskNameList = []
taskTypeList = []
taskStatusList = []
taskDescList = []
taskDf = pd.DataFrame


class tasker():
    def getTodayDate(self):
        return date.today()
    
    def deleteTask(self,taskId):
        taskId = int(taskId)
        try:
            if(os.path.exists(os.path.join("logs", str(date.today()) + ".csv"))):
                taskDf = pd.read_csv(os.path.join("logs", str(date.today()) + ".csv"))
                taskDf.drop(index=taskId, axis=0, inplace=True)
                taskDf.to_csv(os.path.join("logs", str(date.today()) + ".csv"), index=False)
            else:
                print("something went wrong when deleting")
                return;
        except ValueError:
            print(ValueError)
            
            
    def checkFile(self):
        if(os.path.exists(os.path.join("logs", str(date.today()) + ".csv"))):
            print("exist")
        else:
            print("creating file")
            
    
    def createTask(self ,taskId ,taskName, taskType, taskDescription):
        global taskDf
        if(os.path.exists(os.path.join("logs", str(date.today()) + ".csv"))):
            
            taskDf = pd.read_csv(os.path.join("logs", str(date.today()) + ".csv"))
            taskStatus = "INPROGRESS"
            
            taskNameList.append(taskName)
            taskTypeList.append(taskType)
            taskStatusList.append(taskStatus)
            taskIdList.append(taskId)
            taskDescList.append(taskDescription)

            taskNameSeries = pd.Series(taskNameList, name = "Task Name")
            taskTypeSeries = pd.Series(taskTypeList, name = "Type")
            taskStatusSeries = pd.Series(taskStatusList, name = "Status")
            taskIdSeries = pd.Series(taskIdList, name="Id")   
            taskDescSeries = pd.Series(taskDescList, name="Description")          
                    
            taskDf = pd.concat([taskIdSeries, taskNameSeries, taskTypeSeries, taskDescSeries, taskStatusSeries], axis=1)
            taskDf.to_csv(os.path.join(os.path.join("logs", str(date.today()) + ".csv")), mode="a", header=False)
            return taskDf
        else:
            taskStatus = "INPROGRESS"
            
            taskNameList.append(taskName)
            taskTypeList.append(taskType)
            taskStatusList.append(taskStatus)
            taskIdList.append(taskId)
            taskDescList.append(taskDescription)

            taskNameSeries = pd.Series(taskNameList, name = "Task Name")
            taskTypeSeries = pd.Series(taskTypeList, name = "Type")
            taskStatusSeries = pd.Series(taskStatusList, name = "Status")
            taskIdSeries = pd.Series(taskIdList, name="Id")   
            taskDescSeries = pd.Series(taskDescList, name="Description")          
                    
            taskDf = pd.concat([taskIdSeries, taskNameSeries, taskTypeSeries, taskDescSeries, taskStatusSeries], axis=1)
            taskDf.to_csv(os.path.join(os.path.join("logs", str(date.today()) + ".csv")))
            return taskDf
    
    def done(self,taskId):
        taskId = int(taskId)
        try:
            
            taskCSV = pd.read_csv(os.path.join("logs", str(date.today()) + ".csv"))
    #        print(taskCSV["Status"])       
            taskCSV.loc[taskId, "Status"] = "DONE"
            taskCSV.to_csv(os.path.join("logs", str(date.today()) + ".csv"), index=False)
            #taskCSV.to_csv((os.path.join("logs", str(date.today()) + ".csv")), index=False)
            print("tasks updated!")
        except:
            print(f'the task {taskId} does not exist!')       
    
    def customStatus(self, taskId, customStatus):
        taskId = int(taskId)
        customStatus = str(customStatus)
        
        try:
            
            taskCSV = pd.read_csv(os.path.join("logs", str(date.today()) + ".csv"))
    #        print(taskCSV["Status"])       
            taskCSV.loc[taskId, "Status"] = customStatus
            taskCSV.to_csv(os.path.join("logs", str(date.today()) + ".csv"), index=False)
            #taskCSV.to_csv((os.path.join("logs", str(date.today()) + ".csv")), index=False)
            print("tasks updated with custom status!")
        except ValueError:
            print(ValueError)          
        
    
    def pending(self, taskId):
        taskId = int(taskId)
        try:
            
            taskCSV = pd.read_csv(os.path.join("logs", str(date.today()) + ".csv"))
    #        print(taskCSV["Status"])       
            taskCSV.loc[taskId, "Status"] = "PENDING"
            taskCSV.to_csv(os.path.join("logs", str(date.today()) + ".csv"), index=False)
            #taskCSV.to_csv((os.path.join("logs", str(date.today()) + ".csv")), index=False)
            print("tasks updated!")
        except:
            print(f'the task {taskId} does not exist!')     

    def finished(self, taskIndex):
        global taskDf
        if(taskIndex > taskDf["Status"].size):
            print("this task id dont exist!")
            return
        else:
            test = taskDf["Status"]
            test.update(pd.Series(["FINISHED"], index=[taskIndex]))
            return test     
    
    def viewLog(self, date):
        if(os.path.exists(os.path.join("logs", str(date) + ".csv"))):
            taskCSV = pd.read_csv(os.path.join("logs", str(date) + ".csv"))   
            table = df_to_table(taskCSV, table)
            console = Console()
            console.print(table)
        else:
            print("========================================================")
            print(f"sorry , there are no logs for the date {date}")
            print("========================================================")
    

    
    def summary(self):
        taskCSV = pd.read_csv(os.path.join("logs", str(date.today()) + ".csv"))
        taskCSV.drop(columns=["Unnamed: 0"])
        
        table = Table(title=f"tasks summary for {self.getTodayDate()}")
        table = df_to_table(taskCSV, table)
        console = Console()
        console.print(table)
       
        
    
    def exportCSV(self):
        filename = str(date.today()) + ".csv"
        try:
            os.mkdir('logs')
        except:
            taskDf.to_csv(os.path.join("logs", filename), mode="a", index=False, header=False)
            return