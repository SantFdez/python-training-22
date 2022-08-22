
def main():
    handleExceptions(success, None, ZeroDivisionError)
   
def success(val):
    print("All good", val)
    pass

def failure(exc):
    print("Failure function: Exception raised")
    print(type(exc))
    # raise
    pass

def handleExceptions(success, failure, *exceptions):
    try:
        result = 9/0
        success(result)
    except Exception as e:
        if failure == None:
            for x in exceptions:
                print(type(e))
                print(type(x))
                if x == type(e):
                    raise
        else:
            failure(e)

if __name__ == "__main__":
    main()