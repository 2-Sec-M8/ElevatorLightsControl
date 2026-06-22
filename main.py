import requests
import json

# --- Configuration ---
API_KEY = '7fea9327-e81b-4a3b-a76f-88e5c3c1981b'
MAC_ADDRESS = 'D0:6A:D4:AD:FC:FF:A5:81'  # Format: 'XX:XX:XX:XX:XX:XX:XX:XX'
MODEL = 'H618A'  # Format: 'H61XX'


def toggle_govee_power(state: str):
    """
    Turns a Govee device 'on' or 'off' while preserving its current scene/color.

    :param state: String 'on' or 'off'
    """
    if state.lower() not in ['on', 'off']:
        print("Error: State must be 'on' or 'off'")
        return

    url = 'https://developer-api.govee.com/v1/devices/control'

    headers = {
        'Govee-API-Key': API_KEY,
        'Content-Type': 'application/json'
    }

    payload = {
        "device": MAC_ADDRESS,
        "model": MODEL,
        "cmd": {
            "name": "turn",
            "value": state.lower()
        }
    }

    try:
        response = requests.put(url, headers=headers, data=json.dumps(payload))

        if response.status_code == 200:
            print(f"Success: Light strip turned {state.lower()}.")
        else:
            print(f"Failed with status code {response.status_code}")
            print("Response:", response.json())

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")


# --- Example Usage ---
if __name__ == "__main__":
    # To turn it on:
    toggle_govee_power('off')

    # To turn it off:
    # toggle_govee_power('off')