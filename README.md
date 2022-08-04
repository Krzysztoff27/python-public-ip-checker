# python-public-ip-checker
This simple script allows you to check your public IP address. 

## prerequisites
This script uses Python `requests` package. You can install it using `pip` by executing `pip install requests`.

## disclaimer
Sometimes this package is installed within OS. For example, fresh installation of Ubuntu Server 22.04 comes with `requests` preinstalled. 

## running script
You can run it manually or automatically. Either way it outputs to the `logs.txt` file. Logs contain of date, time and public IP. 

## scheduling execution
You can schedule a crontab job (Linux) or use task scheduler (Windows) in order to run this script manually. 
