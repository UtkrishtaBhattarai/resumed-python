from time import strptime
from datetime import datetime
date="23-Sep-19"
date_object = datetime.strptime(date, '%d-%b-%y').date()
print(date_object)