def safe_read_log(filename):

    try:
        with open(filename, "r") as file:
            content = file.read()
            if content == "":
                print("Log file is empty.")
                return ""
            else:
                return content
    except FileNotFoundError:
        print("No log file found. Run a diagnostic first.")
        return ""
    finally:
        print("Log read attempt completed.")