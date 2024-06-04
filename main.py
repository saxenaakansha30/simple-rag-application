import retrieval
import generation

user_input = input("Tell me what are you thinking, i will recommand a song.\n")
relevant_document = retrieval.get_relevant_document(user_input)

#Augment the relavant song to original query.
prompt = f'''
You are a bot that makes recommendations for songs. You answer in very short sentences and do not include extra information.
This is the recommended song: {relevant_document}
The user input is: {user_input}
Compile a recommendation to the user based on the recommended song and the user input. If the user has no interset simple deny.
'''

response = generation.get_response(prompt)

print("I reccomed you to listen: " + response)
