from datetime import datetime , timedelta
today = datetime.now()
yesterday = datetime.now() - timedelta(1)
tomorrow = datetime.now() + timedelta(1)
print(yesterday)
print(today)
print(tomorrow)