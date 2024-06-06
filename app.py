import requests
import json

url = "https://api.bandai-tcg-plus.com/api/user/event/list?application_open_flg=0&country_code[]=US&favorite=0&game_title_id=4&limit=20&offset=0&order=1&series_type[]=1&start_date=2024-05-23"
# Function to fetch event data
def fetch_event_data(url):
    r = requests.get(url)
    data = r.json()
    pretty_json = json.dumps(data, indent=4, sort_keys=True)
    return data

#  Function to print event details (including coordinates for Google Geocoding API)
""" def print_event_details(event_list):
    for event in event_list:
        latitude = event['event_place_geo']['x']
        longitude = event['event_place_geo']['y']

        print("ID:", event['id'])
        print("Start Date Time:", event['start_datetime'])
        print("Timezone:", event['timezone'])
        print("Max Join Count:", event['max_join_count'])
        print("Game Format Name: ", event['game_format_name'])
        print("Country Code:", event['country_code'])
        print("Pref Code:", event['pref_code'])
        print("Postcode:", event['postcode'])
        print("City Code:", event['city_code'])
        print("Street Address:", event['street_address'])
        print("Game Title:", event['game_title'])
        print("Organizer Name:", event['organizer_name'])
        print("Phone Number:", event['phone_number'])
        print("Entry Fee:", event['entryFee'])
        print("Currency:", event['entry_fee_currency_code'])
        print()
"""

# Function to generate HTML file with event data
def generate_html(event_list, template_path, output_path):
    with open(template_path, 'r') as file:
        html_template = file.read()

    events_js = []
    for event in event_list:
        event_info = {
            "latitude": event['event_place_geo']['x'],
            "longitude": event['event_place_geo']['y'],
            "start_datetime": event['start_datetime'],
            "timezone": event['timezone'],
            "max_join_count": event['max_join_count'],
            "game_format_name": event['game_format_name'],
            "country_code": event['country_code'],
            "pref_code": event['pref_code'],
            "postcode": event['postcode'],
            "city_code": event['city_code'],
            "street_address": event['street_address'],
            "game_title": event['game_title'],
            "organizer_name": event['organizer_name'],
            "phone_number": event['phone_number'],
            "entry_fee": event['entryFee'],
            "entry_fee_currency_code": event['entry_fee_currency_code']
        }
        events_js.append(event_info)

    events_js_string = json.dumps(events_js, indent=4)

    html_content = html_template.replace("EVENT_DATA", events_js_string)

    with open(output_path, 'w') as file:
        file.write(html_content)

if __name__ == "__main__":
    data = fetch_event_data(url)
    event_list = data["success"]["event_list"]
    
    # paths to the template and output files
    template_path = "template.html"
    output_path = "index.html"

    generate_html(event_list, template_path, output_path)

