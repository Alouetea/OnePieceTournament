import requests
import json

url = "https://api.bandai-tcg-plus.com/api/user/event/list?application_open_flg=0&country_code[]=US&favorite=0&game_title_id=4&limit=20&offset=0&order=1&series_type[]=1&start_date=2024-05-23"
# header - more info about the request itself (json/particular coding format)
def fetch_event_data(url):
    r = requests.get(url)
    data = r.json()
    pretty_json = json.dumps(data, indent=4, sort_keys=True)
    return data
    # print(pretty_json)

def print_event_details(event_list):
    for event in event_list:
        print("ID:", event['id'])
        print("Start Date Time:", event['start_datetime'])
        print("Timezone:", event['timezone'])
        print("Max Join Count:", event['max_join_count'])
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

if __name__ == "__main__":
    data = fetch_event_data(url)
    event_list = data["success"]["event_list"]
    print_event_details(event_list)

