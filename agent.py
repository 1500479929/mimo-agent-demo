import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com",
    timeout=60.0
)

def simple_agent(prompt: str) -> str:
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "你是一个帮助我处理任务的Agent。请分步骤思考后给出答案。"},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=2000
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    tasks = [
        "分析这段代码的性能瓶颈：\ndef add(a,b):\n    return a+b",
        "将下面这句话总结成三个要点：'人工智能正在改变软件开发的方式，尤其是在代码审查和测试生成方面。'",
        "帮我生成一个 Git commit message，描述本次修改：修复了登录页面的按钮样式问题。"
    ]

    for idx, task in enumerate(tasks, 1):
        print(f"=== 任务 {idx} ===")
        print(f"输入: {task[:80]}...")
        result = simple_agent(task)
        print(f"输出: {result}\n")