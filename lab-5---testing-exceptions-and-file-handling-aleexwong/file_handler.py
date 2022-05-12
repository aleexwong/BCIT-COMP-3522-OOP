import enum
import json
import pathlib


class FileExtension(enum.Enum):
    """
    Enum for file extensions
    """
    TXT = '.txt'
    JSON = '.json'


class FileHandler:

    @staticmethod
    def load_data(path, file_extension):
        """
        load the data from the path given.
        :param path: file
        :param file_extension: the .txt or a .json file
        :return: data for the Dictionary key
        """
        if pathlib.Path(path).is_file():
            try:
                if file_extension == FileExtension.JSON.value:
                    print(file_extension)
                    print(FileExtension.JSON.value)
                    with open(path, mode='r', encoding='utf-8') as data_file:
                        data = json.load(data_file)
                        data_file.close()
                        return data
                elif file_extension == FileExtension.TXT.value:
                    with open(path, mode='r', encoding='utf-8') as data_file:
                        data = data_file.read()
                        data_file.close()
                        return data
                else:
                    raise InvalidFileTypeError
            except InvalidFileTypeError as e:
                print(e)
        else:
            raise FileNotFoundError("File is not found!")

    @staticmethod
    def write_lines(path, lines):
        """
        Writes data to a file by opening the file in append mode. In this
        mode, if the file does not exist, it gets created. More importantly,
        if the file has any pre-existing data, opening the append mode will
        not overwrite this data. Any calls to file.write() will add the data
        to the end. (Unless you change the file pointer using file.seek()
        :param lines: lines is the values of the specific key given
        :param path: file to be opened
        """
        try:
            with open(path, mode='a') as my_text_file:
                my_text_file.write(lines)
                my_text_file.close()
        except Exception as e:
            print(e)


class InvalidFileTypeError(Exception):
    """
    Exception for the invalid file types (acceptable are ".txt" and ".json")
    """

    def __init__(self):
        super().__init__("File must be a .txt or .json!!!")
