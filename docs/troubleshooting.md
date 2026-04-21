# Troubleshooting

## Flask module not found
Cause:
- Flask was not installed in the Python environment used to run the app

Fix:
- create a virtual environment
- install Flask inside the venv
- run the app from that environment

## Virtual environment creation failed
Cause:
- `python3-venv` was missing on the Raspberry Pi system

Fix:
- install `python3-venv`
- recreate the virtual environment
- install dependencies again

## systemd service failed to start
Cause:
- app configuration was not suitable for that startup mode
- debug mode caused issues in the service workflow

Fix:
- remove debug mode
- verify the correct interpreter path
- restart and confirm service status

## Nginx returned Not Found for /ruoat/
Cause:
- requests were not reaching the expected backend route
- routing and proxy path handling needed correction

Fix:
- verify the active Nginx server block
- confirm backend app is listening on the expected port
- update reverse proxy routing accordingly
