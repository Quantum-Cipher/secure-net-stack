# Secure Net Stack Architecture

Secure Net Stack is structured in a modular way to separate concerns:

- **Networking layer** (`SecureSocket`)  
  Handles connections, addresses, and basic network communication.

- **Encryption layer** (`SecureChannel`)  
  Provides encryption/decryption for secure messaging using `cryptography.fernet`.

- **Node layer** (`NetworkNode`)  
  Integrates networking and encryption, exposing `send_message` and `receive_message`.

This modular design makes it easy to extend or replace components independently.
