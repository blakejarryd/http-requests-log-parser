# -----------------------------------------------------
# Test cases via Pytest. 
# The 'test-data.log' file is used as the test data
# -----------------------------------------------------

import parser
import statistics

#load test-data.log file
log_file_parser =  parser.Parser()
logs = log_file_parser.parsefile('test-data.log')

#generate stats
log_processor = statistics.Stats(logs)
stats = log_processor.get_stats()

# -----------------------------------------------------
# IP Tests
# -----------------------------------------------------
def test_unique_ip():
  unique_ip = stats['unique_ip_count']
  assert unique_ip == 11

def test_top_ip():
  top_ip = stats['ip_frequency'][0][0]
  assert top_ip == '168.41.191.40'

def test_top_ip_count():
  top_ip_count = stats['ip_frequency'][0][1]
  assert top_ip_count == 4

def test_third_ip():
  top_ip = stats['ip_frequency'][2][0]
  assert top_ip == '50.112.00.11'

# -----------------------------------------------------
# URL Tests
# -----------------------------------------------------
def test_unique_url():
  unique_url = stats['unique_url_count']
  assert unique_url == 22

def test_top_url():
  top_url = stats['url_frequency'][0][0]
  assert top_url == '/docs/manage-websites/'

def test_top_url_count():
  top_url_count = stats['url_frequency'][0][1]
  assert top_url_count == 2

# -----------------------------------------------------
# HTTP Method Tests
# -----------------------------------------------------
def test_unique_method():
  unique_method = stats['unique_method_count']
  assert unique_method == 1

def test_top_method():
  top_method = stats['method_frequency'][0][0]
  assert top_method == 'GET'

def test_top_method_count():
  top_method_count = stats['method_frequency'][0][1]
  assert top_method_count == 23

# -----------------------------------------------------
# HTTP Response Tests
# -----------------------------------------------------
def test_unique_response():
  unique_response = stats['unique_response_count']
  assert unique_response == 5

def test_top_response():
  top_response = stats['response_frequency'][0][0]
  assert top_response == '200'

def test_top_response_count():
  top_response_count = stats['response_frequency'][0][1]
  assert top_response_count == 19