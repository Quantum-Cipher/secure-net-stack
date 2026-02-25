from src.node import NetworkNode

node = NetworkNode("DEMO_NODE")
node.start()
token = node.send_message(b"Hello World")
node.receive_message(token)
