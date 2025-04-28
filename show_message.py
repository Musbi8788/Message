def show_message(text_messages):
    """Display the text message fo peoples"""
    for text_message in text_messages:
        text = f'\n{text_message.title()}'
        # print(text)
        
def send_message(message_lists, send_messages):
    while message_lists:
        current_message = message_lists.pop()
        print(f"\nSending....: '{current_message}'.")
        send_messages.append(current_message)

    """show the sent_message list"""
    for sent_message in sent_messages:
        text = f'\n{sent_message}'
        print(text)

    """print the message list"""
    print(f'The message list is empty: {message_lists}')




    
message_lists = [
                 'python lovers.', 
                 'programmers solve real world problems.',
                 'bug me today and I will come back tommorrow.',
                 'one day you will solve a big real world problem with coding keep it up.'
                 ]

sent_messages = []

show_text = show_message(message_lists)
final_process = send_message(message_lists=message_lists[:], send_messages=sent_messages)
