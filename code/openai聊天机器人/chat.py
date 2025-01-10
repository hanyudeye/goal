import openai

# 设置 OpenAI API 密钥
openai.api_key = '你的API密钥'

def chat_with_bot(prompt):
    response = openai.ChatCompletion.create(
          model="gpt-3.5-turbo",  # 或 "gpt-4" （选择对应的模型）
          messages=[
             {"role": "system", "content": "你是一个友善且乐于助人的聊天机器人。"},
             {"role": "user", "content": prompt}
          ],

           max_tokens=150,
           temperature=0.7
    )
    # 获取机器人的回复
    message = response['choices'][0]['message']['content']
    return message

if __name__ == '__main__':
    print("你好！我是 OpenAI 的聊天机器人。你可以问我任何问题，我会尽力回答。")
    while True:
        user_input = input("你：")
        if user_input.lower() == 'exit':
            print("再见！")
            break
        response = chat_with_bot(user_input)
        print