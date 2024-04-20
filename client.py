
import socket
import hashlib

HOST = 'localhost'
PORT = 5000

def send_message(message):
    client_socket.send(message.encode('utf-8'))

def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(message)
        except:
            print("Disconnected from server.")
            break
def authenticate(auth_type):
    client_socket.send(auth_type.encode('utf-8'))
    if auth_type == "login":
        username = input("Username: ")
        password = input("Password: ")
        client_socket.send(username.encode('utf-8'))
        client_socket.send(password.encode('utf-8'))
        response = client_socket.recv(1024).decode('utf-8')
        if response == "Login failed!":
            print(response)
            return False
        else:
            print(response)
            return True
    elif auth_type == "register":
        username = input("Desired Username: ")
        password = input("Password: ")
        client_socket.send(username.encode('utf-8'))
        response = client_socket.recv(1024).decode('utf-8')
        print(response)

        if response == "Registration successful!":
            return True
        else:
            return False
    else:
        print("Invalid authentication type!")
        return False
    
def main():
    connect()
    while True:
        auth_choice = input("Login (1) or Register (r): ")
        if auth_choice.lower() in ["1", "login"]:
            if authenticate("login"):
                break
        elif auth_choice.lower() in ["r", "register"]:
            if authenticate("register"):
                break
        else:
            print("Invalid choice!")
    
    message_thread = threading.Thread(target=receive_messages)
    message_thread.start()

    while True:
        message = input()
        if message:
            send_message(message)
        else:
            break
    if __name__ == "__main__":
        main()