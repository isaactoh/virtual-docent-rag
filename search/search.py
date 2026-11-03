from openai import OpenAI
from database.chroma import search_chunks

client = OpenAI(
    base_url="http://localhost:9931/",
    api_key="no-key-required"
)


def search(query):
    # 1. Retrieve relevant chunks
    relevant_chunks = search_chunks(query)

    # 2. Build context
    context = "\n\n".join(str(chunk) for chunk in relevant_chunks)

    # 3. Send context to llama.cpp
    response = client.chat.completions.create(
        model="local-model",
        messages=[
            {
                "role": "system",
                "content": """
                You are a helpful assistant.
                Answer questions using only the provided context.
                If the answer is not in the context, say you don't know.
                """
            },
            {
                "role": "user",
                "content": f"""
                Context:
                {context}

                Question:
                {query}
                """
            }
        ],
        temperature=0.2
    )

    return response.choices[0].message.content


print(search("When was CU founded?"))