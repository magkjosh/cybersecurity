events = [
    {
        "failed_attempts": 174,
        "recognised_device": False,
        "spent_hours": 40,
        "authorised_account": True
    },
    {
        "failed_attempts": 4,
        "recognised_device": True,
        "spent_hours": 30,
        "authorised_account": True
    },
    {
        "failed_attempts": 20,
        "recognised_device": True,
        "spent_hours": 26,
        "authorised_account": False
    }
]


print('\n =========== SECURITY =========== \n ')



def mrrobot(events):
    risk_level = 0
    for event in events:
    
        if event["failed_attempts"] > 500:
            print(f"CRITICAL: Excessive failed login attempts detected. {event['failed_attempts']} attempts recorded.")
            risk_level += 5
        
        elif event["failed_attempts"] > 100:
            print(f"SERIOUS: High number of failed login attempts detected. {event['failed_attempts']} attempts recorded.")
            risk_level += 4
        
        elif event["failed_attempts"] > 20:
            print(f"WARNING: Suspicious login activity detected. {event['failed_attempts']} attempts recorded.")
            risk_level += 3
        
        elif event["failed_attempts"] > 5:
            print(f"NOTICE: Multiple failed login attempts detected. {event['failed_attempts']} attempts recorded.")
            risk_level += 2
        
        if not event["recognised_device"]:
            print('NOTICE!!! THE DEVICE IS NOT RECOGNISED')
            risk_level += 4
        
        if event["spent_hours"] > 100:
            print(f"CRITICAL: Excessive hours recorded. {event['spent_hours']} hours spent.")
            risk_level += 5
        
        elif event["spent_hours"] > 50:
            print(f"SERIOUS: Unusually high hours recorded. {event['spent_hours']} hours spent.")
            risk_level += 4
        
        elif event["spent_hours"] > 25:
            print(f"WARNING: High hours recorded. {event['spent_hours']} hours spent.")
            risk_level += 3
        
        elif event["spent_hours"] > 15:
            print(f"NOTICE: Above-average hours recorded. {event['spent_hours']} hours spent.")
            risk_level += 2
        
        if not event["authorised_account"] :
            print('NOTICE!!! THIS ACCOUNT IS NOT AUTHORISED')
            risk_level += 4


        if risk_level >= 20:
            print("\n CRITICAL RISK \n")
        elif risk_level >= 10:
            print("\n HIGH RISK \n")
        elif risk_level >= 5:
            print("\n MODERATE RISK \n")
        else:
            print("\n LOW RISK \n")

mrrobot(events)
