# from flask import Flask, render_template, request, jsonify
# import requests

# app = Flask(__name__)

# # Replace with your OpenRouter API key
# OPENROUTER_API_KEY = "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"
# OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/chat', methods=['POST'])
# def chat():


#     user_message = request.json.get('message')

#     # Prepare the payload for OpenRouter API
#     headers = {
#         "Authorization": f"Bearer {OPENROUTER_API_KEY}",
#         "Content-Type": "application/json"
#     }
#     payload = {
#         "model": "openai/gpt-3.5-turbo",  # You can change the model as needed
#         "messages": [{"role": "user", "content": user_message}]
#     }

#     # Send request to OpenRouter API
#     response = requests.post(OPENROUTER_API_URL, headers=headers, json=payload)
#     if response.status_code == 200:
#         bot_reply = response.json()['choices'][0]['message']['content']
#     else:
#         bot_reply = "Sorry, I couldn't process your request."

#     return jsonify({"reply": bot_reply})

# @app.route('/chat-history')
# def get_chat_history():
#     return jsonify(load_chat_history())

# if __name__ == '__main__':
#     app.run(debug=True)


# chat history
# from flask import Flask, render_template, request, jsonify
# import requests
# from datetime import datetime
# import json

# app = Flask(__name__)

# # Replace with your OpenRouter API key
# OPENROUTER_API_KEY = "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"
# OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"

# # File to store chat history
# CHAT_HISTORY_FILE = "chat_history.json"

# def load_chat_history():
#     try:
#         with open(CHAT_HISTORY_FILE, 'r') as file:
#             return json.load(file)
#     except FileNotFoundError:
#         return []

# def save_chat_history(history):
#     with open(CHAT_HISTORY_FILE, 'w') as file:
#         json.dump(history, file, indent=4)

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/chat', methods=['POST'])
# def chat():
#     user_message = request.json.get('message')

#     # Load existing chat history
#     chat_history = load_chat_history()

#     # Add user message to history
#     chat_history.append({
#         "role": "user",
#         "content": user_message,
#         "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     })

#     # Prepare the payload for OpenRouter API
#     headers = {
#         "Authorization": f"Bearer {OPENROUTER_API_KEY}",
#         "Content-Type": "application/json"
#     }
#     payload = {
#         "model": "openai/gpt-3.5-turbo",  # You can change the model as needed
#         "messages": chat_history[-10:]  # Send last 10 messages for context
#     }

#     # Send request to OpenRouter API
#     response = requests.post(OPENROUTER_API_URL, headers=headers, json=payload)
#     if response.status_code == 200:
#         bot_reply = response.json()['choices'][0]['message']['content']
#     else:
#         bot_reply = "Sorry, I couldn't process your request."

#     # Add bot reply to history
#     chat_history.append({
#         "role": "assistant",
#         "content": bot_reply,
#         "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     })

#     # Save updated chat history
#     save_chat_history(chat_history)

#     return jsonify({"reply": bot_reply})

# @app.route('/chat-history')
# def get_chat_history():
#     return jsonify(load_chat_history())

# if __name__ == '__main__':
#     app.run(debug=True)




# working code
# from flask import Flask, render_template, request, jsonify
# import requests
# from datetime import datetime
# import json
# import os

# app = Flask(__name__)

# # Replace with your OpenRouter API key
# OPENROUTER_API_KEY = "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"
# OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"

# # Folder to store chat history
# CHAT_HISTORY_FOLDER = "chat_history"

# # Ensure the chat history folder exists
# if not os.path.exists(CHAT_HISTORY_FOLDER):
#     os.makedirs(CHAT_HISTORY_FOLDER)

# # Function to load chat history for a specific session
# def load_chat_history(session_id):
#     file_path = os.path.join(CHAT_HISTORY_FOLDER, f"{session_id}.json")
#     try:
#         with open(file_path, 'r') as file:
#             return json.load(file)
#     except FileNotFoundError:
#         return []

# # Function to save chat history for a specific session
# def save_chat_history(session_id, history):
#     file_path = os.path.join(CHAT_HISTORY_FOLDER, f"{session_id}.json")
#     with open(file_path, 'w') as file:
#         json.dump(history, file, indent=4)



# # Function to list all chat sessions
# def list_chat_sessions():
#     sessions = []
#     for file_name in os.listdir(CHAT_HISTORY_FOLDER):
#         if file_name.endswith(".json"):
#             sessions.append(file_name[:-5])  # Remove .json extension
#     return sessions

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/chat', methods=['POST'])
# def chat():
#     session_id = request.json.get('session_id')
#     user_message = request.json.get('message')

#     # Load existing chat history for the session
#     chat_history = load_chat_history(session_id)

#     # Add user message to history
#     chat_history.append({
#         "role": "user",
#         "content": user_message,
#         "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     })

#     # Prepare the payload for OpenRouter API
#     headers = {
#         "Authorization": f"Bearer {OPENROUTER_API_KEY}",
#         "Content-Type": "application/json"
#     }
#     payload = {
#         "model": "openai/gpt-3.5-turbo",  # You can change the model as needed
#         "messages": chat_history[-10:]  # Send last 10 messages for context
#     }

#     # Send request to OpenRouter API
#     response = requests.post(OPENROUTER_API_URL, headers=headers, json=payload)
#     if response.status_code == 200:
#         bot_reply = response.json()['choices'][0]['message']['content']
#     else:
#         bot_reply = "Sorry, I couldn't process your request."

#     # Add bot reply to history
#     chat_history.append({
#         "role": "assistant",
#         "content": bot_reply,
#         "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     })

#     # Save updated chat history
#     save_chat_history(session_id, chat_history)

#     return jsonify({"reply": bot_reply})

# @app.route('/chat-history')
# def get_chat_history():
#     session_id = request.args.get('session_id')
#     if session_id:
#         return jsonify(load_chat_history(session_id))
#     else:
#         return jsonify([])

# @app.route('/chat-sessions')
# def get_chat_sessions():
#     return jsonify(list_chat_sessions())

# if __name__ == '__main__':
#     app.run(debug=True)



from flask import Flask, render_template, request, jsonify
import requests
from datetime import datetime
import json
import os

app = Flask(__name__)

# Replace with your OpenRouter API key
OPENROUTER_API_KEY = "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"
OPENROUTER_API_URL = "https://openrouter.ai/api/v1/chat/completions"

# Folder to store chat history
CHAT_HISTORY_FOLDER = "chat_history"

# Ensure the chat history folder exists
if not os.path.exists(CHAT_HISTORY_FOLDER):
    os.makedirs(CHAT_HISTORY_FOLDER)

# Function to load chat history for a specific session
def load_chat_history(session_id):
    file_path = os.path.join(CHAT_HISTORY_FOLDER, f"{session_id}.json")
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Function to save chat history for a specific session
def save_chat_history(session_id, history):
    file_path = os.path.join(CHAT_HISTORY_FOLDER, f"{session_id}.json")
    with open(file_path, 'w') as file:
        json.dump(history, file, indent=4)

# Function to list all chat sessions with summaries
def list_chat_sessions():
    sessions = []
    for file_name in os.listdir(CHAT_HISTORY_FOLDER):
        if file_name.endswith(".json"):
            session_id = file_name[:-5]  # Remove .json extension
            chat_history = load_chat_history(session_id)
            summary = chat_history[0]['content'] if chat_history else "New Chat"
            sessions.append({"id": session_id, "summary": summary})
    return sessions

# Function to clear all chat history
def clear_all_chat_history():
    for file_name in os.listdir(CHAT_HISTORY_FOLDER):
        file_path = os.path.join(CHAT_HISTORY_FOLDER, file_name)
        os.remove(file_path)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    session_id = request.json.get('session_id')
    user_message = request.json.get('message')

    # Load existing chat history for the session
    chat_history = load_chat_history(session_id)

    # Add user message to history
    chat_history.append({
        "role": "user",
        "content": user_message,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

    # Prepare the payload for OpenRouter API
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "openai/gpt-3.5-turbo",  # You can change the model as needed
        "messages": chat_history[-10:]  # Send last 10 messages for context
    }

    # Send request to OpenRouter API
    response = requests.post(OPENROUTER_API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        bot_reply = response.json()['choices'][0]['message']['content']
    else:
        bot_reply = "Sorry, I couldn't process your request."

    # Add bot reply to history
    chat_history.append({
        "role": "assistant",
        "content": bot_reply,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

    # Save updated chat history
    save_chat_history(session_id, chat_history)

    return jsonify({"reply": bot_reply})

@app.route('/chat-history')
def get_chat_history():
    session_id = request.args.get('session_id')
    if session_id:
        return jsonify(load_chat_history(session_id))
    else:
        return jsonify([])

@app.route('/chat-sessions')
def get_chat_sessions():
    return jsonify(list_chat_sessions())

@app.route('/clear-all-chats', methods=['POST'])
def clear_all_chats():
    clear_all_chat_history()
    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(debug=True)