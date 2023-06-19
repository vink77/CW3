from utils import *
#количество последних операций
NUMBER_OF_LASTOPERATION = 5

data = get_data()
data = last_executed_list(data, NUMBER_OF_LASTOPERATION)
data = sort_list(data)
data = output(data)

