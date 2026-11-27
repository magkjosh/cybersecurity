file_path = '/home/magkjosh/cyber security/logs'

try:
    with open(file_path,"r") as file:
        failed_attempts = 0
        sucess_attempts = 0
        Warning_attempts = 0
        for x in file:
            if 'FAILED' in x:
                print(x.strip())
                failed_attempts += 1

            if 'SUCCESS' in x:
                sucess_attempts += 1

            if 'WARNING' in x:
                Warning_attempts += 1


except FileNotFoundError:
    print('THAT FILE IS NOT FOUND')


print('\ns================== LOG ANYLIZE ==================\n')
print("Total failed attempts:", failed_attempts)
print("Total sucessfuls attempts:", sucess_attempts)
print("Total warnings:", Warning_attempts)
