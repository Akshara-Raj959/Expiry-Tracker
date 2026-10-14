from datetime import datetime
from plyer import notification

def days_left(expiry_date):
    today = datetime.now().date()
    exp_date = datetime.strptime(expiry_date, "%Y-%m-%d").date()
    return (exp_date - today).days

def check_expiry(data):
    for item in data:
        remaining = days_left(item["expiry"])
        name = item["name"]

        if remaining < 0:
            print(f"❌ {name} has expired {abs(remaining)} days ago!")
            notify_user(name, "already expired!")
        elif remaining == 0:
            print(f"⚠️ {name} expires today!")
            notify_user(name, "expires today!")
        elif remaining <= 3:
            print(f"⚠️ {name} will expire in {remaining} days.")
            notify_user(name, f"will expire in {remaining} days.")
        else:
            print(f"✅ {name} is safe for {remaining} more days.")

def notify_user(item_name, message):
    notification.notify(
        title="Expiry Tracker Alert 🚨",
        message=f"{item_name} {message}",
        timeout=5
    )
