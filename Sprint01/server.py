import socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 5000))
server.listen(1)
print("Waiting for friend to connect...")
conn, address = server.accept()
print("Connected by:", address)
while True:
    message = conn.recv(1024).decode()
    if message.lower() == "exit":
        print("Your friend ended the chat.")
        break
    print("Friend:", message)
    reply = input("You: ")
    conn.send(reply.encode())
    if reply.lower() == "exit":
        break
conn.close()
server.close()

