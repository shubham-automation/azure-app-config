from flask import Flask, render_template
import os
import yaml

app = Flask(__name__)

@app.route('/')
def index():
    # Default values
    bg_color = "#FFFFFF"
    message = "Welcome to the App!"

    # Try to get config from environment variables
    affiliate_config = os.getenv("INTELLIGENT_TRIAGE_MICROSERVICE1_CONFIG")
    common_config = os.getenv("COMMON_CONFIG")

    # Parse intelligent-traige.microservice1.config if available
    if affiliate_config:
        try:
            affiliate_data = yaml.safe_load(affiliate_config)
            if isinstance(affiliate_data, dict):
                bg_color = affiliate_data.get("background_color", bg_color)
        except yaml.YAMLError as e:
            print(f"Error parsing intelligent-traige.microservice1.config YAML: {e}")

    # Parse common-config if available
    if common_config:
        try:
            common_data = yaml.safe_load(common_config)
            if isinstance(common_data, dict):
                message = common_data.get("message", message)
        except yaml.YAMLError as e:
            print(f"Error parsing common-config YAML: {e}")

    return render_template('index.html', background_color=bg_color, message=message)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
