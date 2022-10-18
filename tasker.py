from operator import truediv
from art import tprint, text2art
import pandas as pd
import os

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
        global taskDf
        taskDf.drop(index=taskId, inplace=True)
    
    def createTask(self ,taskId ,taskName, taskType, taskDescription):
        taskStatus = "INPROGRESS"
        global taskDf
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
    
    def done(self, taskIndex):
        global taskDf
        if(taskIndex > taskDf["Status"].size):
            print("this task id dont exist!")
            return
        else:
            test = taskDf["Status"]
            test.update(pd.Series(["DONE"], index=[taskIndex]))
            return test
    
    def pending(self, taskIndex):
        global taskDf
        if(taskIndex > taskDf["Status"].size):
            print("this task id dont exist!")
            return
        else:
            test = taskDf["Status"]
            test.update(pd.Series(["PENDING"], index=[taskIndex]))
            return test    

    def finished(self, taskIndex):
        global taskDf
        if(taskIndex > taskDf["Status"].size):
            print("this task id dont exist!")
            return
        else:
            test = taskDf["Status"]
            test.update(pd.Series(["FINISHED"], index=[taskIndex]))
            return test     
    
    
    
    def summary(self):
        taskDataFrame = taskDf
        print("========================================================")
        print(self.getTodayDate())
        print(taskDataFrame)
        print("========================================================")
        
    
    def exportCSV(self):
        filename = str(date.today()) + ".csv"
        try:
            os.mkdir('logs')
        except:
            taskDf.to_csv(os.path.join("logs", filename))
            return