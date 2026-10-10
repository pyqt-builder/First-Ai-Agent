from functions.get_files_info import get_files_info


def test() -> None:
    result = get_files_info("calculator", ".")
    print("Result for current directory:")
    print(result)
    print("")

    result = get_files_info("calculator", "pkg")
    print("Result for 'pkg' directory:")
    print(result)

    result = get_files_info("calculator", "/bin")
    print("Result for '/bin' directory:")
    print(result)

    result = get_files_info("calculator", "../")
    print("Result for '../' directory:")
    print(result)


if __name__ == "__main__":
    test()








if message.tool_calls:
     for tool_call in messages.tool_calls:
             function_args = json.loads(tool_call.function.arguments or "{}")
             print(f"Calling function: {tool_call.function.name}({function_args})")
else:
     print(generated_content = response.choices[0].message.content)
