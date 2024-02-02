from llm_agent import LLMAgent
from flask import Flask, request
import re
app = Flask(__name__)
llm_agent = LLMAgent()


@app.route('/ai/ask', methods=['POST'])
def ask():
    if request.method == 'POST':
        question = request.form['question']
        if question:
            answer = llm_agent.ask(question)
            if answer:
                pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
                url = re.search(pattern, answer)
                print(url.group() if url else 'No URLs found')
                if url:
                    pattern = r'http[s]?://[^/]*'
                    result = re.sub(pattern, '', url.group())
                    print(result)
                    return success(result)
        return fail()


def success(data,msg="操作成功"):
    return {
        "success": True,
        "data": data,
        "msg": msg
    }


def fail(msg="异常"):
    return {
        "success": False,
        "msg": msg
    }


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
