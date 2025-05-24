my_list = [10, 20, 30, 40, 50, 'Cable']

user_input = input("Enter a part number or name: ")

global_search_term = user_input

if user_input in my_list:
    print(f"{user_input} exists in the list.")
    web_search_content_to_execute = open('web_search.py').read()
    exec(open('web_search.py').read())
else:
    print(f"{user_input} does not exist in the list.")