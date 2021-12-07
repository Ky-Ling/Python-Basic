'''
Date: 2021-08-22 14:36:18
LastEditors: GC
LastEditTime: 2021-08-22 15:39:07
FilePath: \Mosh Course 1\Python_Package_Index.py
'''

# Pip:

# import requests
# response = requests.get("http://baidu.com")
# print(response)




# Pipenv:

# Install it with the command : pip3 install pipenv
# Then: pipenv install requests
# When the steps are done, this pipenv tool will create a couple of files(Pipfile and Pipfile.lock)
# Then: pipenv --venv
# Then: pip3 uninstall requests
# Then: python3 Python_Package_Index.py
# We will get an error, because we have removed the request package from the list of the global packages, and here Python does
# know where to locate this package, it has no knowledge of this new virtual environment, so we need to activate it.
# Then: Pipenv shell
# Then: python3 Python_Package_Index.py
# From the result, we got a response, so Python successfully locate the request package. So here we are currently in the virtual
# environment for this project. If you wanna deactivate it, just type "exit"








# Virtual Environments in VSCode:
import requests
response = requests.get("http://baidu.com")
print(response)

# Run this program, we also will get an error. --> Because coderunner is running this program using the Python interpreter that 
# is installed globally, and that Python interpreter can not find the requests module. So we have to tell codeuser to use the 
# Python interpreter in a virtual environment.