import json
import csv

def textfile_read_file(path, encoding="utf-8"):
    try:
        with open(path, encoding=encoding) as file:
            data = file.read()

    except FileNotFoundError as error:
        print(f"Soubor nenalezen:{error}")
        print(error)
        print(type(error))
    except Exception as error:
        return f"Došlo k nějakému problému při otevírání souboru:{error}"
    finally:
        file.close()
    return data

def textfile_write_file(path, data="", encoding="utf-8"):
    try:
        with open(path, mode="w", encoding=encoding) as file:
            file.write(data)

    except FileNotFoundError as error:
        print(f"Soubor nenalezen:{error}")
        return False
        print(type(error))
    except Exception as error:
        print(f"Došlo k nějakému problému při otevírání souboru:{error}")
        return False
    finally:
        file.close()
    return True

# txt = textfile_read_file("./python.txt")

# print(textfile_write_file("./novy.txt", txt))


def jsonfile_read_file(path, encoding="utf-8"):
    try:
        with open(path, encoding=encoding) as file:
            data = json.load(file)
    except FileNotFoundError as error:
        print(f"Soubor nenalezen:{error}")
        print(error)
        print(type(error))
    except Exception as error:
        return f"Došlo k nějakému problému při otevírání souboru:{error}"
    finally:
        file.close()
    return data

def jsonfile_write(path, data="", encoding="utf-8"):
    try:
        with open(path, mode="w", encoding=encoding) as file:
            json.dump(data,file)

    except FileNotFoundError as error:
        print(f"Soubor nenalezen:{error}")
        return False
        print(type(error))
    except Exception as error:
        print(f"Došlo k nějakému problému při otevírání souboru:{error}")
        return False
    finally:
        file.close()
    return True

def csvfile_read(path, encoding="utf-8"):
    try:
        with open(path, encoding=encoding, newline="\n") as file:
            reader = csv.DictReader(file, delimiter=";", quotechar='"')
            dict_list = []
            for row in reader:
                dict_list.append(row)
    except FileNotFoundError as error:
        print(f"Soubor nenalezen:{error}")
        return False
        print(type(error))
    except Exception as error:
        print(f"Došlo k nějakému problému při otevírání souboru:{error}")
        return False
    finally:
        file.close()
    return dict_list

# def csvfile_write(path, data="", encoding="utf-8"):
#     try:
#         with open(path, mode="w", encoding=encoding, newline="\n") as file:
#             reader = csv.DictReader(data, delimiter=";", quotechar='"')
#
#             writer = csv.DictWriter(data, fieldnames= )
#     except FileNotFoundError as error:
#         print(f"Soubor nenalezen:{error}")
#         return False
#         print(type(error))
#     except Exception as error:
#         print(f"Došlo k nějakému problému při otevírání souboru:{error}")
#         return False
#     finally:
#         file.close()
#     return True

csvdata = csvfile_read("./kniha.csv", encoding="windows-1250")
print(type(csvdata))
# print(csvfile_write("./novy.csv", csvdata))

# jsondata = jsonfile_read_file("./pokus.json")
# print(jsonfile_write("./novy.json", jsondata))

# jsondata = jsonfile_read_file("./pokus.json")
# print(jsondata, type(jsondata))