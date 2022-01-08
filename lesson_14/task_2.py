class AccessDeniedError(Exception):
    """Raised when you have no access to requested resource"""

    def __init__(self, *args):
        if len(args) == 0:
            args = [ "you have no access to the requested resource" ]
        super().__init__(*args)

def get_restricted_data(login = "guest", password = ""):
    if login == "rgalyant" and password == "pyth0n4ever":
        return "Restriced data"
    else:
        raise AccessDeniedError(f"user {login} has no access to requested data")

def prompt_login():
    login = input("Enter login: ")
    password = input("Enter password: ")
    return login, password

def main():
    login, passwd = prompt_login()

    try:
        result = f"Response: {get_restricted_data(login, passwd)}"
    except AccessDeniedError as error:
        result = f"Error happened during executing request: {error}"

    print(result)

if __name__ == "__main__":
    main()