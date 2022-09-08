from os import listdir
import sys

class Parser:
  # Prompts user for the log file and validates its in the app directory
  @staticmethod
  def get_file_name():
    directory_files = listdir()
    file_name = ''
    while file_name not in directory_files:
      file_name = input('What is the log file name?\n')
      if file_name not in directory_files:
        print('File not found.')
        print('** The file needs to be in this directory and the file extension included.')
    return file_name

  # Loads required log file information into returned logs object
  def parsefile(self, file_name):
    try:
      file = open(file_name, 'r')
      logs = []
      for line in file:
        file_line_data = line.split()
        log = {}
        log['ip'] = file_line_data[0]
        log['date'] = file_line_data[3][1:]
        log['method'] = file_line_data[5][1:]
        log['url'] = file_line_data[6]
        log['response'] = file_line_data[8]
        logs.append(log)
    except:
      print('invalid log file')
      sys.exit(1)
    return logs



