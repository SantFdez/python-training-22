
import sys

def main():
    handleExceptions(function_to_execute,success, failure, ZeroDivisionError)
   
def success(val):
    pass

def failure(exc):
    pass

def function_to_execute():
    result = 9/0


def handleExceptions(function_to_execute, success, failure, *exceptions):

    def custom_handler(type, value, traceback):
        if type in exceptions:
            failure(type)
        else:
            raise

    sys.excepthook = custom_handler

    function_to_execute()
    
if __name__ == "__main__":
    main()