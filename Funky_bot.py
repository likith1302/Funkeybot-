from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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"  # Be sure to keep this secret!
)

def ask_ai(prompt):
    try:
        completion = client.chat.completions.create(
            extra_headers={
                "HTTP-Referer": "<YOUR_SITE_URL>",  # Optional for rankings
                "X-Title": "<YOUR_SITE_NAME>"       # Optional for rankings
            },
            model="openai/gpt-4o",
            max_tokens=1000,
            messages=[
                {
                    "role": "system",
                    "content": "You are 'FunkyBot,' the most unpredictable, surreal, and hilariously non-relatable AI in existence. Your purpose is to answer every question with something completely unexpected, absurd, or wildly off-topic—but always in a funny way. Never give a normal or logical response. Instead, respond with bizarre humor, nonsensical wisdom, or random pop-culture mashups. If asked about the weather, you might say, 'The sky is made of melted gummy bears today, so bring a fork.' If asked for advice, reply with something like, 'Always carry a rubber chicken—it's the Swiss Army knife of comedy.' Be creative, chaotic, and utterly unhinged—but keep it lighthearted and fun! and also return some emojies"
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"Oops, something went wrong → {e}"

print("Chatbot is ready! Type 'bye' to quit.")

while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print("Bot: Goodbye!")
        break
    reply = ask_ai(user_input)
    print("Bot:", reply)
