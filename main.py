from fastapi import FastAPI, Request, Response
import httpx
import os
from bots.law_firm import law_firm_bot
from bots.medical import medical_bot
from bots.dealership import dealership_bot
from bots.funeral import funeral_bot

app = FastAPI()

VERIFY_TOKEN = os.getenv("VERIFY_TOKEN", "offralebot2026")
WHATSAPP_TOKEN = os.getenv("WHATSAPP_TOKEN")

# Map each client's Phone Number ID to their bot logic
BOT_ROUTER = {
    "CLIENT_PHONE_ID_1": law_firm_bot,
    "CLIENT_PHONE_ID_2": medical_bot,
    "CLIENT_PHONE_ID_3": dealership_bot,
    "CLIENT_PHONE_ID_4": funeral_bot,
}

# Webhook verification — Meta calls this once during setup
@app.get("/webhook")
async def verify(request: Request):
    params = request.query_params
    if params.get("hub.verify_token") == VERIFY_TOKEN:
        return Response(content=params.get("hub.challenge"), media_type="text/plain")
    return Response(content="Forbidden", status_code=403)

# Incoming messages — Meta calls this every time a user sends a message
@app.post("/webhook")
async def receive(request: Request):
    body = await request.json()
    try:
        change = body["entry"][0]["changes"][0]["value"]
        phone_number_id = change["metadata"]["phone_number_id"]
        message = change["messages"][0]
        from_number = message["from"]

        if message["type"] == "text":
            text = message["text"]["body"].strip()

            # Route to correct bot based on which client number received the message
            bot_handler = BOT_ROUTER.get(phone_number_id)
            if bot_handler:
                reply = bot_handler(text, from_number)
                await send_reply(from_number, phone_number_id, reply)
    except (KeyError, IndexError, TypeError):
        pass

    return {"status": "ok"}

# Send reply via WhatsApp Cloud API
async def send_reply(to: str, phone_number_id: str, text: str):
    url = f"https://graph.facebook.com/v19.0/{phone_number_id}/messages"
    headers = {
        "Authorization": f"Bearer {WHATSAPP_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "messaging_product": "whatsapp",
        "to": to,
        "type": "text",
        "text": {"body": text}
    }
    async with httpx.AsyncClient() as client:
        await client.post(url, json=payload, headers=headers)
