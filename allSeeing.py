import facebook

# Replace ACCESS_TOKEN with your access token
graph = facebook.GraphAPI(access_token="ACCESS_TOKEN")

# Replace USER_ID with the ID of the user whose conversation you want to retrieve
conversations = graph.get_connections(id="USER_ID", connection_name="conversations")

for conversation in conversations['data']:
    # Replace CONVERSATION_ID with the ID of the conversation you want to retrieve messages from
    messages = graph.get_connections(id=conversation['id'], connection_name="messages")
    for message in messages['data']:
        print(message['message'])