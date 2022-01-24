import typing

from .aes import AES128_CTRCipher, AES192_CTRCipher, AES256_CTRCipher
from .common import Cipher
from .none import NoneCipher

_CIPHER_MAPPING = {
    'none': NoneCipher,
    'aes128-ctr': AES128_CTRCipher,
    'aes192-ctr': AES192_CTRCipher,
    'aes256-ctr': AES256_CTRCipher
}


def create_cipher(cipher_type: str) -> typing.Type[Cipher]:
    """Returns the class corresponding to the given cipher type name.

    Args:
        cipher_type
            The name of the OpenSSH private key cipher type.

    Returns:
        The subclass of :py:class:`Cipher` corresponding to the cipher type
        name.

    Raises:
        KeyError: There is no subclass of :py:class:`Cipher` corresponding to
            the given cipher type name.
    """
    return _CIPHER_MAPPING[cipher_type]
