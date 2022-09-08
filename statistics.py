class Stats:
  def __init__(self, logs):
    self.logs = logs

  # Calculates the number of times the passed in data type (e.g. 'ip') occurs in the log file.
  # Also returns the unique occurences of passed in datatype
  def __calculate_frequency(self, datatype):
    count = {}
    for log in self.logs:
      if log[datatype] in count:
        count[log[datatype]] += 1
      else:
        count[log[datatype]] = 1
    unique_count = len(count.keys())
    sorted_count = sorted(count.items(), key=lambda x: x[1], reverse=True)
    return {
      'unique_%s_count' % datatype: unique_count, 
      '%s_frequency' % datatype: sorted_count
    }

  #Public wrapper method to return stats for each datatype
  def get_stats(self):
    ip_stats = self.__calculate_frequency('ip')
    url_stats = self.__calculate_frequency('url')
    method_stats = self.__calculate_frequency('method')
    response_stats = self.__calculate_frequency('response')
    return ip_stats | url_stats | method_stats | response_stats



