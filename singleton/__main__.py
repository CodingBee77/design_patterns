from logger_base import Logger

logger = Logger('my.log')
logger.write_log('Logging with classic Singleton pattern')

logger2 = Logger('***ignored***')
assert logger is logger2
print('Assertion passed')

logger2.write_log('Another log record')
logger.close_log()

#logger2.close_log() - this will throw an exception because logger and logger 2 are the same instance of the logger class


#Eventhough we've created 2 Logger class, records have been saved in 1 file, as desired
with open('my.log', 'r') as f:
    for line in f:
        print(line, end='')
