from email import parser
import string
from venv import create
from tasker import tasker
from art import tprint, text2art
import argparse



<<<<<<< HEAD

app = typer.Typer()


@app.command()
def create():
    taskName = input("task name\n")
    taskId = input("task Id\n")
    taskDesc = input("description of your task\n")
    taskType = input("type of task!\n")
    taskObj = tasker()
    taskObj.createTask(taskId, taskName,taskType,taskDesc)
    print(f"new task: {taskName}\nsucessfully added!")
    taskObj.summary()
    


@app.command()
def done():
    tasker().summary()
    task = input("which task to mark done?! \n")
    tasker().done(task)
    tasker().summary()

@app.command()
def pending():
    tasker().summary()
    task = input("which task to mark pending?! \n")
    tasker().pending(task)
    tasker().summary()

@app.command()
def custom():
    index = input("task index\n")
    status = input("custom status\n")
    tasker().customStatus(index, status)

    
@app.command()
def viewlog():
    date = input("enter date of task log \n")
    tasker().viewLog(date)


@app.command()
def summary():
    tasker().summary()

@app.command()
def delete():
    tasker().summary()
    task = input("which task to delete? \n press enter to cancel deletion")
    if(task != int):
        print("deletion cancelled")
        return
    else:
        tasker().deleteTask(task)
        print(f"deleted task{task}")
        tasker().summary()
    
    
=======
>>>>>>> ece872fe663020a69849d305b7bb00c0f34911b7
def main():

    print(text2art("bpt"), "lazy tasker for lazy people")
    
    parser = argparse.ArgumentParser()

    
    parser.add_argument("-c",  help="creates a new task, example: create [TaskId]")
    parser.add_argument('-d', help="deletes a task , example: delete [TaskId]")
    parser.add_argument('-s', help="summary of all tasks")
    parser = parser.parse_args()
 
    
    print(parser)
    
    
    
        
if __name__ == "__main__":  
   main()
    
