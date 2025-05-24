import webbrowser

try:
	search_term = global_search_term
	print(f"Web Search Script: Received search term: '{search_term}'")

	encoded_search_term = str(search_term).replace(" ", "%20")
	print(f"Web Search Script: Encoded search term: '{encoded_search_term}'")

	websites = [
	f"https://www.mouser.com/Search/Refine?Keyword={encoded_search_term}",
	f"https://www.google.com/search?q={encoded_search_term}"
	]

	for url in websites:
		webbrowser.open(url)

except NameError:
    print("Error: 'global_search_term' not found. This script should be executed by another script that sets this variable.")
except Exception as e:
    print(f"An error occurred in web_search.py: {e}")

