from email import parser
import string
from venv import create
from tasker import tasker
from art import tprint, text2art
import argparse



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
    
