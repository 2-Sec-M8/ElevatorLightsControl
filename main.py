import json
import os

import requests


API_KEY = os.getenv('GOVEE_API_KEY', '')
MAC_ADDRESS = os.getenv('GOVEE_MAC_ADDRESS', 'D0:6A:D4:AD:FC:FF:A5:81')
MODEL = os.getenv('GOVEE_MODEL', 'H618A')



def _send_govee_command(command_name: str, command_value):
    if not API_KEY:
        print('Error: GOVEE_API_KEY is not configured.')
        return False

    url = 'https://developer-api.govee.com/v1/devices/control'
    headers = {
        'Govee-API-Key': API_KEY,
        'Content-Type': 'application/json',
    }
    payload = {
        'device': MAC_ADDRESS,
        'model': MODEL,
        'cmd': {
            'name': command_name,
            'value': command_value,
        },
    }

    try:
        response = requests.put(url, headers=headers, data=json.dumps(payload))
        if response.status_code == 200:
            return True

        print(f'Failed with status code {response.status_code}')
        print('Response:', response.json())
    except requests.exceptions.RequestException as error:
        print(f'An error occurred: {error}')

    return False



def toggle_govee_power(state: str):
    """
    Turns a Govee device 'on' or 'off' while preserving its current scene/color.

    :param state: String 'on' or 'off'
    """
    if state.lower() not in ['on', 'off']:
        print("Error: State must be 'on' or 'off'")
        return

    if _send_govee_command('turn', state.lower()):
        print(f'Success: Light strip turned {state.lower()}.')



def set_elevator_up_effect():
    """Sets the LED strip to the elevator up effect scene."""
    if _send_govee_command('scene', 'Elevator Up'):
        print('Success: Elevator up effect enabled.')


if __name__ == '__main__':
    toggle_govee_power('on')
    set_elevator_up_effect()
