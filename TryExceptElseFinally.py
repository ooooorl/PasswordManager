#FileNotFound
#KeyError
"""
    These are the keyword to be used in handling exception error
    try:
    except:
    else:
    finally:
"""
try:
    # this block of codes will execute and try to open if it exist
    file = open("dataaa.txt")
    x = {"xy":"ss"}
    print(x["xy"])

except FileNotFoundError:
    # then the moment try block get executed and it found out that files doesn't exist then except block will
    # executed immediately
    with open("dataaa.txt", "w") as datas:
        datas.write("Errors thrown catched!")

except KeyError as error_message:
    print(f"The key {error_message} you're trying to find out doesn't exist")

else:
    # This will trigger when except doesn't thrown any error
    content = file.read()
    print(content)

finally:
    # this will executed no matter what try and except block of code does
    file.close()
    print("File was close")