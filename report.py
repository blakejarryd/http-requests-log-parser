class Report:
  def __init__(self, stats):
    self.stats = stats

  #Prints stats report for provided datatype
  def __print_datatype_stats(self, datatype):
    print('--------------%s stats--------------' % datatype)
    print('Unique:', self.stats['unique_%s_count' % datatype])
    print('Top %ss' % datatype)
    try:
      print(self.stats['%s_frequency' % datatype][0][1], '-', self.stats['%s_frequency' % datatype][0][0])
    except IndexError:
      pass
    try:
      print(self.stats['%s_frequency' % datatype][1][1], '-', self.stats['%s_frequency' % datatype][1][0])
    except IndexError:
      pass
    try:
      print(self.stats['%s_frequency' % datatype][2][1], '-', self.stats['%s_frequency' % datatype][2][0])
    except IndexError:
      pass

  #Public wrapper method to print stats for each datatype
  def print_stats(self):
    print('\nHTTP REQUESTS LOG FILE STATISTICS\n')
    self.__print_datatype_stats('ip')
    self.__print_datatype_stats('url')
    self.__print_datatype_stats('method')
    self.__print_datatype_stats('response')