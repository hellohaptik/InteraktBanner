#!/usr/bin/env python3

import json
import sys
from datetime import datetime, timedelta
import pytz

action = sys.argv[1]
json_file = sys.argv[2]

with open(json_file) as f:
    data = json.load(f)

now = datetime.now()

if action == "add":

    ribbon_text = sys.argv[3].strip().rstrip(",")
    expiry_input = sys.argv[4].strip().rstrip(",")

    expiry_dt = datetime.strptime(expiry_input, "%Y-%m-%d %H")

    if expiry_dt <= now:
        raise ValueError("Expiry must be in the future")

    # Expire live ribbons
    for r in data:
        exp = r.get("expireOn")
        if not exp:
            continue

        year = exp["year"]
        month = exp["month"]
        day = exp["date"]
        hour = exp["hour"]

        if hour == 24:
            exp_dt = datetime(year, month, day, 0) + timedelta(days=1)
        else:
            exp_dt = datetime(year, month, day, hour)

        if exp_dt > now:
            r["expireOn"] = {
                "year": now.year,
                "month": now.month,
                "date": now.day,
                "hour": now.hour
            }

    # IST timestamp
    ist = pytz.timezone("Asia/Kolkata")
    ts = datetime.now(ist).strftime("%H%M%S")

    ribbon_id = f"ribbon-{expiry_dt.strftime('%d-%b-%Y').lower()}-{ts}"

    new_ribbon = {
        "closeLimit": 1,
        "id": ribbon_id,
        "text": ribbon_text,
        "position": "top",
        "theme": {
          "bg": "#BE364E",
          "color": "#ffffff",
          "variant": "alert"
        },
        "icon": {
          "iconName": "campaignBlack",
          "iconSize": "small",
          "color": "#ffffff"
        },
        "pages": [
            "^/(?!signup(?:/|$)).*"
        ],
        "expireOn": {
            "year": expiry_dt.year,
            "month": expiry_dt.month,
            "date": expiry_dt.day,
            "hour": expiry_dt.hour
        }
    }

    data.insert(0, new_ribbon)

    print(f"RIBBON_ID: {ribbon_id}")

elif action == "remove":

    ribbon_id = sys.argv[3].strip().rstrip(",")

    new_data = [r for r in data if r.get("id") != ribbon_id]

    if len(new_data) == len(data):
        print(f"Ribbon ID {ribbon_id} not found")
        sys.exit(1)

    data = new_data

    print(f"Ribbon removed: {ribbon_id}")

with open(json_file, "w") as f:
    json.dump(data, f, indent=2)
