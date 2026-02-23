
#  *** TASK 1 ***

from datetime import datetime
def write_to_log(filename, entry):

    with open(filename, "a") as file:
        file.write(entry + "\n")


def read_log(filename):

    with open(filename, "r") as file:
        return file.read()



def log_command_result(command_name, target, output, filename):

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = "[" + timestamp + "] " + command_name + " " + target + "\n"
    entry = entry + output
    entry = entry + "-" * 40
    write_to_log(filename, entry)