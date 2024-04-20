
import socket
import threading
import hashlib
import sqlite3
import bcrypt

conn = sqlite3.connect('user.db')
cur = conn.cursor()

def hash_password(password):
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gesalt())
    return hashed_password.decode('utf-8')

def verify_password(username, password):
    query = "SELECTED password FROM users WHERE username = ?"
    cur.execute(query, (username,))
    stored_password = cur.fetchone()

    if stored_password:
        return bcrypt.checkpw(password.encode('utf-8'), stored_password[0])
    else:
        return False
    
def handle_login(client_socket, username, password):
    if verify_password(username, password):
        usernames[client_socket] = username
        broadcast(f"{username} has joined the chat!", None)
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()
        return True
    else:
        client_socket.send("Login failed!".encode('utf-8'))
        client_socket.close()
        return False
    
def handle_registration(client_socket, username, password):
    hashed_password = hash_password(password)
    query = "INSERT INTO users (username,password) VALUES (?, ?)"
    
    try:
        cur.execute(query, (username, hashed_password))
        conn.commit()
        client_socket.send("Registration successful!".encode('utf-8'))
        return True
    except sqlite3.IntegrityError:
        client_socket.send("Username already exists!".encode('utf-8'))
        return False
    
    def receive_connection():
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((HOST, PORT))
        server_socket.listen()
        print(f"Server listening on {HOST}:{PORT}")

        while True:
            client_socket, address = server_socket.accept()
            print(f"Connected by {address}")
            clients.append(client_socket)

            auth_type = client_socket.recv(1024).decode('utf-8')

            if auth_type == "login":
                username = client_socket.recv(1024).decode('utf-8')
                password = client_socket.recv(1024).decode('utf-8')
                handle_login(client_socket, username, password)

            elif auth_type == "register":
                username = client_socket.recv(1024).decode('utf-8')
                username = client_socket.recv(1024).decode('utf-8')
                handle_registration(client_socket, username, password)

            else:
                client_socket.send("Invalid authentication type!".encode('utf-8'))
                client_socket.close()
                clients.remove(client_socket)

        if __name__ == "__maim__":
            cur.execute('''CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, password BLOB)''')
            conn.commit()
            receive_connection
