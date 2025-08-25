import sqlite3

class Chat:
    def __init__(self):
        self.chatee = input("Who are you chatting with?\n")
        self.last_message = input("What was your last message?\n")
        self.last_message_time = input("When was the last message sent?\n")

    def __str__(self):
        return f"You are chatting with {self.chatee}"

    def open(self):
        return f"You just opened the chat with {self.chatee} with last message {self.last_message} that was sent at {self.last_message_time}"
    
    def save(self):
        # Connect to database
        connection = sqlite3.connect("database.db")
        # Get access to connection cursor
        cursor = connection.cursor()
        # Create table if not exists
        cursor.execute("CREATE TABLE IF NOT EXISTS chats (id INTEGER PRIMARY KEY AUTOINCREMENT, chatee, last_message, last_message_time);")
        # Save chat to database
        cursor.execute(f"INSERT INTO chats (chatee, last_message, last_message_time) VALUES ('{self.chatee}', '{self.last_message}', '{self.last_message_time}');")
        # Select all chats
        chats = cursor.execute("SELECT * FROM chats;").fetchall()
        # Close connection
        connection.close()
        # Return all chats
        return chats