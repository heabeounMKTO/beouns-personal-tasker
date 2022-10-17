from art import tprint, text2art
import pandas as pd
import os 
from datetime import date


taskIdList = []
taskNameList = []
taskTypeList = []
taskStatusList = []
taskDescList = []
taskDf = pd.DataFrame


class tasker():
    
    
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
            

    
    def summary(self):
        taskDataFrame = taskDf
        print("========================================================")
        print(taskDataFrame)
        print("========================================================")