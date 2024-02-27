# Discord Message Sender

## Overview

This Python script allows you to send messages to a Discord channel using the Discord API. It reads messages from a file and sends them to the specified channel with customizable delays.

## Prerequisites

Before using the script, make sure you have the following:

- Python 3.x installed
- Required Python packages: `requests`
  ```
  pip install requests
  ```

## Usage

1. Clone the repository or download the script.
2. Open the script in a text editor and configure the following variables:

   - `channel_id`: Replace with the Discord channel ID where you want to send messages.
   - `authorization`: Replace with your Discord bot authentication token.
   - `message_file`: Provide the path to the file containing the messages you want to send.
   - `num_messages`: Set the number of messages to send (use 0 for an infinite loop).
   - `line_delay`: Set the delay between lines (in seconds).
   - `message_interval`: Set the interval between messages (in seconds).
   - `delete_after_send`: Set to `True` if you want sent messages to be automatically deleted, `False` otherwise.
3. Save the script after making the necessary changes.

4. Run the script:

   ```bash
   python discord_message_sender.py
   ```

## Example

```python
python discord_message_sender.py
```

## Notes

- This script uses the `requests` library to interact with the Discord API.
- Ensure your Discord account/bot has the necessary permissions to send messages in the specified channel.
- This script runs 100% on your local computer
- **Never share your authentication token with anyone.** Treat it like a password.

## License

This project is licensed under the [MIT License](LICENSE).
