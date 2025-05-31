# Flipper Network Scanner

Flipper Network Scanner is a tool for analyzing wireless traffic captured from the Flipper Zero via USB/UART.

##  Features
-  Parses Sub-GHz, RFID, and NFC logs and dumps
-  Matches traffic against a known device database
- Displays results in a simple web interface
-  Compatible with Linux, macOS, and Raspberry Pi

##  Requirements

```bash
pip install -r requirements.txt
```

##  How to Run

```bash
python main.py
```

Then open [http://localhost:5000](http://localhost:5000) in your browser.

## Input Logs

Place your Flipper logs in `examples/sample_log.txt` or stream them directly from UART.

