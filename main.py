# main.py

from fastapi import FastAPI, Request, Response
import httpx, os
from clients import CLIENTS
from bots.law_firm import law_firm_bot
from bots.medical import medical_bot
from bots.dealership import dealership_bot
from bots.funeral import funeral_bot

app = FastAPI()

VERIFY_TOKEN   = os.getenv("VERIFY_TOKEN", "offralebot2026")
WHATSAPP_TOKEN = os.getenv("WHATSAPP_TOKEN")

# Map each niche type to its bot function
BOT_FUNCTIONS = {
    "law_firm":   law_firm_bot,
    "medical":    medical_bot,
    "dealership": dealership_bot,
    "funeral":    funeral_bot,
}

@app.get("/webhook")
async def verify(request: Request):
    p = request.query_params
    if p.get("hub.verify_token") == VERIFY_TOKEN:
        return Response(content=p.get("hub.challenge"), media_type="text/plain")
    return Response(content="Forbidden", status_code=403)

@app.post("/webhook")
async def receive(request: Request):
    body = await request.json()
    try:
        change         = body["entry"][0]["changes"][0]["value"]
        phone_id       = change["metadata"]["phone_number_id"]
        message        = change["messages"][0]
        from_number    = message["from"]

        if message["type"] == "text":
            text          = message["text"]["body"].strip()
            client_config = CLIENTS.get(phone_id)

            if client_config:
                niche       = client_config["type"]
                bot_fn      = BOT_FUNCTIONS.get(niche)
                if bot_fn:
                    reply = bot_fn(text, from_number, client_config)
                    await send_reply(from_number, phone_id, reply)

    except (KeyError, IndexError, TypeError):
        pass

    return {"status": "ok"}

async def send_reply(to: str, phone_id: str, text: str):
    url = f"https://graph.facebook.com/v19.0/{phone_id}/messages"
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
