# SenderToMAX

Automated message sender for MAX messenger using pymax library.

## Overview

This project sends daily work status messages to a designated recipient on the MAX messenger platform. It reads exercise themes from a JSON file and generates appropriate messages based on the current date.

## Features

- Automated daily message sending to MAX messenger
- Date-based theme selection from `exercise.json`
- Fallback message for days without specific themes
- Session caching for persistent authentication

## Usage

```bash
python main.py
```

## Configuration

Edit `main.py` to configure:
- `phoneNumber` - Your phone number for authentication
- `NeedId` - Recipient's MAX user ID
- `ua` - User agent settings (device type, app version)

### exercise.json Format

```json
[
    {"date": "DD.MM.YY", "description": "Theme description"}
]
```

Each entry maps a date to a work theme. Dates not in the file receive the default message: "Здравствуйте. Сегодня продолжаю делать прошлую тему."

## Requirements

See `pyproject.toml` for dependencies. Install with:

```bash
pip install -e .
```

## Dependencies

- pymax >= 0.5
- maxapi-python >= 1.2.5
- aiohttp
- SQLAlchemy