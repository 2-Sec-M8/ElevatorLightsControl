import io
import unittest
from unittest.mock import patch

import main


class MainTests(unittest.TestCase):
    @patch('main.requests.put')
    @patch('main.API_KEY', 'test-key')
    def test_set_elevator_up_effect_sends_scene_command(self, mock_put):
        mock_put.return_value.status_code = 200

        main.set_elevator_up_effect()

        _, kwargs = mock_put.call_args
        self.assertIn('"name": "scene"', kwargs['data'])
        self.assertIn('"value": "Elevator Up"', kwargs['data'])

    @patch('main.requests.put')
    @patch('main.API_KEY', 'test-key')
    def test_toggle_power_rejects_invalid_state(self, mock_put):
        with patch('sys.stdout', new=io.StringIO()) as stdout:
            main.toggle_govee_power('invalid')

        self.assertIn("Error: State must be 'on' or 'off'", stdout.getvalue())
        mock_put.assert_not_called()


if __name__ == '__main__':
    unittest.main()
