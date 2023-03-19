import requests
import xmltodict

# Define the OpenAI API endpoint and key
openai_key = "YOUR_API_KEY"
openai_url = "https://api.openai.com/v1/engines/text-davinci-003/completions"

# Read the Beer XML file from a URL
xml_url = "http://www.beerxml.com/recipes.xml"
xml_response = requests.get(xml_url)

# Convert the XML content to a Python dictionary using xmltodict
beer_dict_list = xmltodict.parse(xml_response.content)["RECIPES"]["RECIPE"]

# If the XML file contains multiple recipes, select the first recipe
if isinstance(beer_dict_list, list):
    beer_dict = beer_dict_list[0]
else:
    beer_dict = beer_dict_list

# Extract the name and style of the beer from the dictionary
beer_name = beer_dict["NAME"]
beer_style = beer_dict["STYLE"]["NAME"]
beer_hops = beer_dict["HOPS"]

# Construct the prompt for the OpenAI API
prompt = f"Generate a creative beer name based on this beer style {beer_style}"

# Define the OpenAI API request headers and body
headers = {"Content-Type": "application/json", "Authorization": f"Bearer {openai_key}"}
body = {
    "prompt": prompt,
    "temperature": 1.2,
    "max_tokens": 2000,
    "top_p": 1,
    "frequency_penalty": 0,
    "presence_penalty": 0,
}

# Call the OpenAI API to prompt whether the beer conforms to BJCP
response = requests.post(openai_url, headers=headers, json=body)

# Print the result of the OpenAI API call to the terminal output window
print(response.json()["choices"][0]["text"].strip())
