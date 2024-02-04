kkkkkkkkkkimport time

while True:
    localtime = time.localtime()
    result = time.strftime("%I:%M:%S %p", localtime)
    print(result)
    time.sleep(0.1)  # every execution takes 0.1 sec