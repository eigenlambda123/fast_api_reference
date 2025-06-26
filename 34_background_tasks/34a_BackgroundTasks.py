from fastapi import BackgroundTasks, FastAPI

app = FastAPI()


def write_notification(email: str, message=""):
    """Write a notification message to a log file"""
    with open("log.txt", mode="w") as email_file:
        content = f"notification for {email}: {message}"
        email_file.write(content)


@app.post("/send-notification/{email}")
async def send_notification(email: str, background_tasks: BackgroundTasks):
    """Send a notification in the background"""

    # The function write_notification will be executed in the background
    background_tasks.add_task(write_notification, email, message="some notification")
    
    return {"message": "Notification sent in the background"}