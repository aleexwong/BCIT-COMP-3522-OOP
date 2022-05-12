import des
import argparse
import abc
import enum


class CryptoMode(enum.Enum):
    """
    Lists the various modes that the Crypto application can run in.
    """
    # Encryption mode
    EN = "en"
    # Decryption Mode
    DE = "de"


class Request:
    """
    The request object represents a request to either encrypt or decrypt
    certain data. The request object comes with certain accompanying
    configuration options as well as a field that holds the result. The
    attributes are:
        - encryption_state: 'en' for encrypt, 'de' for decrypt
        - data_input: This is the string data that needs to be encrypted or
        decrypted. This is None if the data is coming in from a file.
        - input_file: The text file that contains the string to be encrypted or
        decrypted. This is None if the data is not coming from a file and is
        provided directly.
        - output: This is the method of output that is requested. At this
        moment the program supports printing to the console or writing to
        another text file.
        - key: The Key value to use for encryption or decryption.
        - result: Placeholder value to hold the result of the encryption or
        decryption. This does not usually come in with the request.

    """

    def __init__(self):
        self.encryption_state = None
        self.data_input = None
        self.input_file = None
        self.output = None
        self.key = None
        self.result = None

    def __str__(self):
        return f"Request: State: {self.encryption_state}, Data: {self.data_input}" \
               f", Input file: {self.input_file}, Output: {self.output}, " \
               f"Key: {self.key}"


def setup_request_commandline() -> Request:
    """
    Implements the argparse module to accept arguments via the command
    line. This function specifies what these arguments are and parses it
    into an object of type Request. If something goes wrong with
    provided arguments then the function prints an error message and
    exits the application.
    :return: The object of type Request with all the arguments provided
    in it.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("key", help="The key to use when encrypting or "
                                    "decrypting. This needs to be of "
                                    "length 8, 16 or 24")
    parser.add_argument("-s", "--string", help="The string that needs to be "
                                               "encrypted or decrypted")
    parser.add_argument("-f", "--file", help="The text file that needs to be"
                                             "encrypted or decrypted")
    parser.add_argument("-o", "--output", default="print",
                        help="The output of the program. This is 'print' by "
                             "default, but can be set to a file name as well.")
    parser.add_argument("-m", "--mode", default="en",
                        help="The mode to run the program in. If 'en' (default)"
                             " then the program will encrypt, 'de' will cause "
                             "the program to decrypt")
    try:
        args = parser.parse_args()
        request = Request()
        request.encryption_state = CryptoMode(args.mode)
        request.data_input = args.string
        request.input_file = args.file
        request.output = args.output
        request.key = args.key
        print(request)
        return request
    except Exception as e:
        print(f"Error! Could not read arguments.\n{e}")
        quit()


class BaseHandler(abc.ABC):
    """
    BaseHandler base for each other handler class
    """

    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    @abc.abstractmethod
    def handler(self, crypto_request):
        """
        Each handler would have a specific implementation of how it
        processes a form.
        :param request: a crypto_request
        :return: a tuple where the first element is a string stating the
        outcome and the reason, and the second a bool indicating
        successful handling of the form or not.
        """
        pass

    def set_handler(self, handler):
        """
        Each handler can invoke another handler at the end of it's
        processing of the form. This handler needs to implement the
        BaseHandler interface.
        :param handler: a BaseHandler
        """
        self.next_handler = handler


class KeyHandler(BaseHandler):
    """
    length of word can only be 8, 16 or 24
    """

    def handler(self, crypto_request):
        if len(crypto_request.data_input) != 8 and len(crypto_request.data_input) != 16 and len(
                crypto_request.data_input) != 24:
            self.next_handler.handler(crypto_request)
        else:
            print("wont work not 8/16/24 char long")


class EncryptionHandler(BaseHandler):
    """
    use des library to encrypt data
    """

    def handler(self, crypto_request):
        encryption_des = des.DesKey(bytes(crypto_request.key, "utf-8"))

        if crypto_request.input_file:
            try:
                with open(crypto_request.input_file, mode='r', encoding="utf-8") as text_file:
                    string_encrypt = text_file.read()
                    text_file.close()
                crypto_request.result = encryption_des.encrypt(bytes(string_encrypt, "utf-8"), padding=True)
                return self.next_handler.handler(crypto_request)
            except FileNotFoundError as e:
                print(e)
            except AssertionError as e:
                print(e)


class DecryptionHandler(BaseHandler):
    """
    Uses the key to restore the encrypted data
    """

    def handler(self, crypto_request):
        decryption_des = des.DesKey(bytes(crypto_request.key, "utf-8"))
        if crypto_request.input_file:
            with open(crypto_request.input_file, mode='r', encoding="utf-8") as text_file:
                string_decrypt = text_file.read()
                text_file.close()
            crypto_request.result = decryption_des.decrypt(bytes(string_decrypt, "utf-8"), padding=True).decode("utf-8")
            return self.next_handler.handler(crypto_request)


class OutputHandler(BaseHandler):
    """
    printing
    """

    def handler(self, crypto_request):
        # this is encrypted?
        if crypto_request.output == "print":
            print(crypto_request.output)
        else:
            with open(crypto_request.output, mode="w", encoding="utf-8") as text_file:
                text_file.write(crypto_request.result)
                text_file.close()


class Crypto:

    def __init__(self):
        self.data_length_start_handler = KeyHandler()
        self.encryption_start_handler = EncryptionHandler()
        self.decryption_start_handler = DecryptionHandler()
        self.output_start_handler = OutputHandler()

    def execute_request(self, request: Request):
        self.data_length_start_handler.set_handler(self.output_start_handler)
        self.encryption_start_handler.set_handler(self.output_start_handler)
        self.decryption_start_handler.set_handler(self.output_start_handler)

        # for readability
        if request.encryption_state == CryptoMode.EN:
            self.encryption_start_handler.handler(request)

        if request.encryption_state == CryptoMode.DE:
            self.decryption_start_handler.handler(request)


def main(request: Request):
    crypto = Crypto()
    crypto.execute_request(request)


if __name__ == '__main__':
    request = setup_request_commandline()
    main(request)
