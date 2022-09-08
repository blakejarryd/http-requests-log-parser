import parser
import statistics
import report

# Create log file parser instance and load file
log_file_parser =  parser.Parser()
file_name = log_file_parser.get_file_name()
logs = log_file_parser.parsefile(file_name)

# Create log processor instance and calculate statistics
log_processor = statistics.Stats(logs)
stats = log_processor.get_stats()

#Create log report instance and generate log report
log_file_report = report.Report(stats)
log_file_report.print_stats()



