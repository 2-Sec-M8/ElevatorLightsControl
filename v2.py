import requests
import uuid
import socket
import json
import time


class GoveeController:
    """
    A Python class to control a Govee Light Strip via Cloud REST API and Local LAN (UDP).
    """

    def __init__(self):
        self.api_key = "7fea9327-e81b-4a3b-a76f-88e5c3c1981b"
        self.device_mac = "D0:6A:D4:AD:FC:FF:A5:81"
        self.sku = "H618A"
        self.lan_ip = "192.168.68.107"

        self.v1_url = "https://developer-api.govee.com/v1/devices/control"
        self.v2_url = "https://openapi.api.govee.com/router/api/v1/device/control"

        self.headers = {
            "Govee-API-Key": self.api_key,
            "Content-Type": "application/json"
        }

    # --- CLOUD API METHODS (From previous script) ---

    def turn_off(self) -> dict:
        """Turns off the light strip via Cloud API."""
        payload = {"device": self.device_mac, "model": self.sku, "cmd": {"name": "turn", "value": "off"}}
        return requests.put(self.v1_url, headers=self.headers, json=payload).json()

    def turn_on(self) -> dict:
        """Turns on the light strip via Cloud API."""
        payload = {"device": self.device_mac, "model": self.sku, "cmd": {"name": "turn", "value": "on"}}
        return requests.put(self.v1_url, headers=self.headers, json=payload).json()

    def set_scene(self, scene_id: str) -> dict:
        """Triggers a scene via Cloud API using a standard Scene ID."""
        payload = {
            "requestId": str(uuid.uuid4()),
            "payload": {
                "sku": self.sku, "device": self.device_mac,
                "capability": {"type": "devices.capabilities.dynamic_scene", "instance": "lightScene",
                               "value": scene_id}
            }
        }
        return requests.post(self.v2_url, headers=self.headers, json=payload).json()

    # --- LOCAL LAN METHODS (Using your discovered payloads) ---

    def trigger_elevator_up(self) -> None:
        """
        Executes the 'elevatorUp' action directly over the local network via UDP.
        Uses the exact ptReal base64 hardware commands discovered from the app dump.
        """
        if not self.lan_ip:
            print("Error: You must provide a lan_ip when initializing GoveeController to use this method.")
            return

        port = 4003
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # 1. Turn the light on via LAN
        turn_payload = {
            "msg": {
                "cmd": "turn",
                "data": {"value": 1}
            }
        }
        sock.sendto(json.dumps(turn_payload).encode('utf-8'), (self.lan_ip, port))

        # Brief pause to ensure the hardware processes the power command
        time.sleep(0.1)

        # 2. Send the custom DIY base64 array (ptReal)
        pt_real_payload = {
            "msg": {
                "cmd": "ptReal",
                "data": {
                    "command": [
                        "owABAgQDBVAP////AQEBAQEBAQM=",
                        "o/8BAQEBAQAAAAAAAAAAAAAAAF0=",
                        "MwUKMQAAAAAAAAAAAAAAAAAAAA0="
                    ]
                }
            }
        }
        sock.sendto(json.dumps(pt_real_payload).encode('utf-8'), (self.lan_ip, port))
        print(f"✅ Successfully fired 'elevatorUp' UDP packets to {self.lan_ip}:{port}")

    def trigger_crash(self) -> None:
        """
        Executes the 'elevatorUp' action directly over the local network via UDP.
        Uses the exact ptReal base64 hardware commands discovered from the app dump.
        """
        if not self.lan_ip:
            print("Error: You must provide a lan_ip when initializing GoveeController to use this method.")
            return

        port = 4003
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # 1. Turn the light on via LAN
        turn_payload = {
            "msg": {
                "cmd": "turn",
                "data": {"value": 1}
            }
        }
        sock.sendto(json.dumps(turn_payload).encode('utf-8'), (self.lan_ip, port))

        # Brief pause to ensure the hardware processes the power command
        time.sleep(0.1)

        # 2. Send the custom DIY base64 array (ptReal)
        pt_real_payload = {
            "msg": {
                "cmd": "ptReal",
                "data": {
                    "command": [
                        "owABAgT/AGAP/wAAAQEBAQEBAco=",
                        "o/8BAQEBAQIDBAAAAAAAAAAAAFg=",
                        "MwUKMQAAAAAAAAAAAAAAAAAAAA0="
                    ]
                }
            }
        }
        sock.sendto(json.dumps(pt_real_payload).encode('utf-8'), (self.lan_ip, port))
        print(f"✅ Successfully fired 'crash' UDP packets to {self.lan_ip}:{port}")

    def trigger_breaking(self) -> None:
        """
        Executes the 'elevatorUp' action directly over the local network via UDP.
        Uses the exact ptReal base64 hardware commands discovered from the app dump.
        """
        if not self.lan_ip:
            print("Error: You must provide a lan_ip when initializing GoveeController to use this method.")
            return

        port = 4003
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # 1. Turn the light on via LAN
        turn_payload = {
            "msg": {
                "cmd": "turn",
                "data": {"value": 1}
            }
        }
        sock.sendto(json.dumps(turn_payload).encode('utf-8'), (self.lan_ip, port))

        # Brief pause to ensure the hardware processes the power command
        time.sleep(0.1)

        # 2. Send the custom DIY base64 array (ptReal)
        pt_real_payload = {
            "msg": {
                "cmd": "ptReal",
                "data": {
                    "command": [
                        "owABBQICIwACBgYAAf8AAfoyMoM=",
                                                "owEC+jIE////////////////AGw=",
                                                "owIAAAAAAAEgAAIGBgAB/zIB+rU=",
                                             "owMUFAL6MgP///////////8AAJY=",
                                             "o/8AAAAAAAAAAAAAAAAAAAAAAFw=",
                                               "MwUE9gEAAAAAAAAAAAAAAAAAAMU="
                    ]
                }
            }
        }
        sock.sendto(json.dumps(pt_real_payload).encode('utf-8'), (self.lan_ip, port))
        print(f"✅ Successfully fired 'breaking' UDP packets to {self.lan_ip}:{port}")


    def trigger_solid(self) -> None:
        """
        Executes the 'elevatorUp' action directly over the local network via UDP.
        Uses the exact ptReal base64 hardware commands discovered from the app dump.
        """
        if not self.lan_ip:
            print("Error: You must provide a lan_ip when initializing GoveeController to use this method.")
            return

        port = 4003
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # 1. Turn the light on via LAN
        turn_payload = {
            "msg": {
                "cmd": "turn",
                "data": {"value": 1}
            }
        }
        sock.sendto(json.dumps(turn_payload).encode('utf-8'), (self.lan_ip, port))

        # Brief pause to ensure the hardware processes the power command
        time.sleep(0.1)

        # 2. Send the custom DIY base64 array (ptReal)
        pt_real_payload = {
            "msg": {
                "cmd": "ptReal",
                "data": {
                    "command": [
                        "MwUVAf///wAAAAAA/38AAAAAAF0="
                    ]
                }
            }
        }
        sock.sendto(json.dumps(pt_real_payload).encode('utf-8'), (self.lan_ip, port))
        print(f"✅ Successfully fired 'solid' UDP packets to {self.lan_ip}:{port}")






# strip = GoveeController()
#
# # Reset
# strip.turn_off()
#
# # when starting the experience:
# strip.trigger_solid()
#
# # when going up (10s):
# strip.trigger_elevator_up()
#
# # After 10s, a.k.a stable on a floor
# strip.trigger_solid()
#
# # Repeat going up
#
# # When the crash sound is started (6s after crash is triggered)
# strip.trigger_breaking()
#
# # During the fall (10s after previous)
# strip.trigger_breaking()
#
# # When reaching the bottom (3s after previous)
# strip.turn_off()