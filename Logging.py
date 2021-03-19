'''
The 5 security levels there are when it comes to logging include; 
1. DEBUG - Used by developers when they're testing/troubleshooting programs
2. INFO - It gives informational  messages
3. WARNING - Indicates nothing bad happened yet, but something bad could happen
4. ERROR - System is still running, it hasn't crushed but it can't perform a certain task hence produces the error
5. CRITICAL - When a crucial/essential component of the system breaks down. It requires immediate attention.
''' 

import logging

#Make the info visible
logging.basicConfig(level=logging.DEBUG)

logging.info('You have 7 new mails in your inbox!')
logging.critical('All components failed!')

#Create your own loggers
logger = logging.getLogger('User logger')
logger.info('A new logger was created!')
logger.critical('Your local disc C crushed!')
logger.log(logging.WARNING, 'You are running out of storage!')
logger.log(logging.ERROR, 'User not found!')

#Creating log files
logger.setLevel(logging.DEBUG)

handler = logging.FileHandler('mylog.log')
handler.setLevel(logging.INFO)

#Creating a format for the log file
formatter = logging.Formatter('%(levelname)s - %(asctime)s: %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)

logger.debug('Missing parenthesis in line 9!')
logger.info('You have 7 new mails in your inbox!')
logger.warning('You are running out of storage!')
logger.critical('Your local disc C crushed!')
logger.error('User not found!')
