import json

lang = "en-US"

# Load translations from JSON file
with open(f"{lang}.json", "r", encoding="utf-8") as f:
    translations = json.load(f)

# Function to handle a specific log message
def handle_message(log_key, **kwargs):
    if "commands" in translations and log_key in translations["commands"]:
        log_data = translations["commands"][log_key]
        message = log_data.format(**kwargs)
        return message
    else:
        return "Log message not found for key: " + log_key

# Example: Handle the "ping" log message
log_key = "ping"
latency = input("Enter value: ")
print(handle_message(log_key, latency=latency))