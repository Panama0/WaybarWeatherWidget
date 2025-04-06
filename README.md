# Waybar Weather Widget
## How to install
1. Download the script
2. Get a free API key from OpenWeatherMaps (from [this](https://home.openweathermap.org/api_keys) page after making an account)
3. Create a file somewhere and paste **only** your API key inside
4. Configure the lat, lon, apiKeyPath, units & icons
5. Add the below to your waybar config (add the path):
    ```json
    "custom/weather": {
		"return-type": "json",
		"exec": "python <path to script>",
		"tooltip": true,
		"restart-interval": 300
	}
    ```
6. Done!

## Notes
- If you are having trouble getting the script to display correctly, try running it in a terminal to see any error messages that may be output.
- It is highly reccomended to use a [nerd font](https://www.nerdfonts.com) for the icons.
- Feel free to copy, change or distribute as you wish!