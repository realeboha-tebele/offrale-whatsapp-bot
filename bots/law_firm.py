# bots/law_firm.py

user_states = {}

def law_firm_bot(text: str, phone: str, config: dict) -> str:

    # Pull client details from the config
    name    = config["name"]
    number  = config["phone"]
    address = config["address"]
    hours   = config["hours"]
    fee     = config["consultation_fee"]
    services = config.get("services", [])

    text = text.lower().strip()
    state = user_states.get(phone, "new")

    if text in ["menu", "main", "back", "0"]:
        user_states[phone] = "menu"
        return _menu(name)

    if state == "new" or text in ["hi", "hello", "hey",
                                   "good morning", "good afternoon"]:
        user_states[phone] = "menu"
        return (
            f"Welcome to *{name}*! 👋\n\n"
            "We are here to assist you with your legal needs.\n\n"
            "Please select an option:\n"
            "1️⃣  Schedule a Consultation\n"
            "2️⃣  Our Practice Areas\n"
            "3️⃣  Office Hours & Location\n"
            "4️⃣  Fees & Billing\n"
            "5️⃣  Speak to a Consultant"
        )

    if state == "menu":
        if text == "1":
            user_states[phone] = "booking"
            return (
                "To schedule a consultation, please reply with:\n\n"
                "• Your *full name*\n"
                "• The *nature of your matter*\n"
                "• Your *preferred date and time*\n\n"
                "We will confirm within 2 hours. ✅"
            )
        elif text == "2":
            service_list = "\n".join(f"⚖️  {s}" for s in services)
            return f"*{name}* specialises in:\n\n{service_list}\n\nReply *menu* to go back."

        elif text == "3":
            return (
                f"📍 *Location:* {address}\n\n"
                f"⏰ *Hours:* {hours}\n\n"
                f"📞 Direct line: {number}\n\n"
                "Reply *menu* to go back."
            )
        elif text == "4":
            return (
                f"💼 *Consultation fee:* {fee}\n\n"
                "We offer flexible payment options for ongoing matters.\n\n"
                "Reply *1* to book or *menu* to go back."
            )
        elif text == "5":
            return (
                f"A consultant will contact you shortly. 📞\n\n"
                f"Direct line: {number}\n"
                f"Hours: {hours}"
            )

    if state == "booking":
        user_states[phone] = "menu"
        return (
            "Thank you! ✅ Your request has been received.\n\n"
            "A team member will contact you within *2 business hours*.\n\n"
            f"📞 Urgent? Call: {number}"
        )

    return f"Reply *menu* to see options or call 📞 {number}."


def _menu(name):
    return (
        f"*{name}* — How can we help?\n\n"
        "1️⃣  Schedule a Consultation\n"
        "2️⃣  Our Practice Areas\n"
        "3️⃣  Office Hours & Location\n"
        "4️⃣  Fees & Billing\n"
        "5️⃣  Speak to a Consultant"
    )
