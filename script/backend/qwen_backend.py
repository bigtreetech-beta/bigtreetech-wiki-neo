import os
from openai import OpenAI

def translate_ai(text:str, src_language:str, target_language:str):
    try:
        client = OpenAI(
            # 若没有配置环境变量，请用阿里云百炼API Key将下行替换为: api_key="sk-xxx",
            api_key=os.getenv("DASHSCOPE_API_KEY"),
            base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
        )

        sys_prompt = f"""你是一个专业的翻译工具，任务是翻译用户输入的内容。
        源语言为{src_language}，目标语言为{target_language}。请确保翻译结果符合目标语言的语法，并保持原文结构不要做任何修改。

        要求：(重要：你返回的内容只能是翻译结果，不需要添加任何注释或代码块符号)
        1. 翻译结果必须符合目标语言的语法。例如，将中文翻译为英文句子，而不是逐字翻译。
        2. 保持原文结构，包括标题、列表、代码块等。
        3. 保持原文语义，确保代码和公式等内容不变。
        4. 原文中的链接、图片、表格、JSX和Markdown代码需保持原样。
        5. 英文关键字、产品名称和型号等内容应保持原样。
        6. 所有缩进必须保持不变。
        7. 翻译结果尾部需保留或添加一个空行。
        8. 文件路径和链接需保持原样。
        9. 原文中的半角字符保持原样。
        10. 返回结果不要添加前缀或后缀，直接给出翻译结果。
        11. 翻译结果开头和结尾不得添加```.
        12. 保持原文中的空行、换行符、空格和制表符等格式不变。
        13. 翻译结果中不能添加原文中不存在的代码、标签或其他内容，包括但不限于<br>。
        14. 不能修改原文中的空格和制表符。不能替换为非断行空格等。
        15. 绝对不能删除原文中的import语句。
        16. 须严格遵循上述要求，否则翻译结果可能会有误。
        17. 翻译后的结果必须行数和翻译前的一致。不然会要求重新翻译。
        """
        user_prompt = text

        completion = client.chat.completions.create(
            model="qwen3-30b-a3b-instruct-2507",  # 模型列表: https://help.aliyun.com/model-studio/getting-started/models
            messages=[
                {'role': 'system', 'content': sys_prompt},
                {'role': 'user', 'content': user_prompt}
            ]
        )

        result = completion.choices[0].message.content
        print(f"[api] [request] {text}")
        print(f"[api] [result] {result}")

        return result

    except Exception as e:
        print(f"[err] {e}")
        print("[err] [ref] https://help.aliyun.com/model-studio/developer-reference/error-code")
