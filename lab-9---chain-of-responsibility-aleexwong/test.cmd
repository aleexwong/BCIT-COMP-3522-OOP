ECHO This provides a string to be encrypted with the key abcd1234
python driver.py abcd1234 -s "Test data to be encrypted"

ECHO This provides a text file with the required data that needs to be encrypted with key abcd1234
python driver.py abcd1234 -f "input_file.txt"

ECHO This is the exact same command as the previous one
python driver.py -f "input_file.txt" abcd1234

ECHO This is also the exact same command as the previous one. This uses the long form instead
python driver.py abcd1234 --file "input_file.txt"

ECHO This is also the exact same command, but it explicitly sets the mode to encryption
python driver.py abcd1234 -f "input_file.txt" -m en

ECHO This provides a text file with data that needs to be decrypted with the given key.
python driver.py abcd1234 -f "byte_input_file.bin" -m de

ECHO This is the exact same command as the previous one explicitly stating that the output should be printed to the console.
python driver.py abcd1234 -f "byte_input_file.bin" -m de --output print
