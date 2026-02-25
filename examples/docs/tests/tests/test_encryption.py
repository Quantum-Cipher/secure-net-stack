cat > tests/test_encryption.py <<EOF
import unittest
from src.encryption import SecureChannel

class TestEncryption(unittest.TestCase):
    def test_encrypt_decrypt(self):
        channel = SecureChannel()
        message = b"test message"
        token = channel.encrypt(message)
        decrypted = channel.decrypt(token)
        self.assertEqual(message, decrypted)

if __name__ == "__main__":
    unittest.main()
EOF
