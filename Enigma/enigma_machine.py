class EnigmaMachine:
    """
    This class is representing the Enigma Machine. Methods for encrypting and decrypting. 
    """

    def __init__(self, rotors, reflector, plugboard):
        """
        Initialize the machine, with rotors, reflectors and plugboard settings

        Args:
        rotors list of reflectors objects
        reflector: object
        plugboard: object
        """

        self.rotors = rotors
        self.reflector = reflector
        self.plugboard = plugboard
        self._validate_components()

#do we need to validate the setup?

def _step_rotors(self):
    """
    Step the rotors to simulate the mechanism of the enigma machine after each key press.
    https://en.wikipedia.org/wiki/Enigma_rotor_details
    """


def _process_character(self, char):
    """
    From the encryption method, processed a single character through the enigma. I think we'll need to step through so we can iterate the rotors at each out.
    Need to flesh out that method

    Args:
        char (str): The character to be processed
    Returns
        str: the processed character... we're adding to a list, and then join() to a string. 
    """
    pass




#Encrypt
def encrypt(self, message):
    """
    Encrypt a message using the Enigma Machine
    Args:
        message(str): message from user input to encrypt
    Returns:
        str: The encrypted message
    """
    encrypted_message = []
    for char in message:
        encrypted_message.append(self._process_character(char))
        self._step_rotors()
    return ''.join(encrypted_message)

#decrypt

def decrypt(Self, message):
    """
    Decrypt a message using the machine
    args:
        (str) of the encrypted message
    Returns
        str: decrypted message using today's settings
 
    """