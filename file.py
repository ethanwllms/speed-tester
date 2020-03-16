import datetime, json, os

def write_to(speeds):
    slug = ".json"
    date_time = datetime.datetime.now()
    filename = date_time.strftime("%m-%d-%Y_%I:%M_%p")
    File = filename + slug
    # print(filename)
    file = open(File, "a")
    file.write(json.dumps(speeds, indent=4))
    # test_print(File)
    print("File created..")
    return(File)

def delete_file(filename):
    if os.path.exists(filename):
        os.remove(filename)
    else:
        print(filename + "does not exist in current directory")
    print("File cleaned..")

def test_print(File):
    f = open(File, "r")
    print(f.read())