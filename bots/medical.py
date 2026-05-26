# bots/medical.py
# Handles ALL medical practice clients.
# Never edit this file to add a new client — edit clients.py only.

# NOTE: user_states stores conversation position in memory.
# States reset if Railway restarts — acceptable behaviour for MVP.

user_states = {}


def medical_bot(text: str, phone: str, config: dict) -> str:

    # Pull client details from config
    name      = config["name"]
    number    = config["phone"]
    address   = config["address"]
    hours     = config["hours"]
    services  = config.get("services", [])
    emergency = config.get("emergency", "10177")

    text  = text.lower().strip()
    state = user_states.get(phone, "new")

    # ── Always allow reset from any state ──────────────────────
    if text in ["menu", "main", "back", "0"]:
        user_states[phone] = "menu"
        return _menu(name)

    # ── First contact / greeting ────────────────────────────────
    if state == "new" or text in ["hi", "hello", "hey",
                                   "good morning", "good afternoon",
                                   "good evening"]:
        user_states[phone] = "menu"
        return (
            f"Hello! Welcome to *{name}*. 👨‍⚕️\n\n"
            "How can we assist you today?\n\n"
            "1️⃣  Book an Appointment\n"
            "2️⃣  Prescription Refill\n"
            "3️⃣  Test Results Enquiry\n"
            "4️⃣  Our Services & Doctors\n"
            "5️⃣  Emergency\n\n"
            "_Reply with a number_"
        )

    # ── Main menu selections ────────────────────────────────────
    if state == "menu":

        if text == "1":
            user_states[phone] = "booking"
            return (
                "To book your appointment, please reply with:\n\n"
                "• Patient *full name*\n"
                "• Patient *date of birth*\n"
                "• *Preferred date and time*\n"
                "• *Reason for visit* (brief description)\n\n"
                "We will confirm your booking via WhatsApp. ✅"
            )

        elif text == "2":
            user_states[phone] = "prescription"
            return (
                "Prescription Refill Request 💊\n\n"
                "Please provide:\n\n"
                "• Patient *full name*\n"
                "• *Medication name(s)*\n"
                "• *Date of last prescription*\n\n"
                "⚠️ Refills require a valid prescription on file. "
                "The doctor may need to see you first."
            )

        elif text == "3":
            user_states[phone] = "results"
            return (
                "Test Results Enquiry 🔬\n\n"
                "Please provide:\n\n"
                "• Patient *full name*\n"
                "• *Date of test*\n"
                "• *Type of test*\n\n"
                "A staff member will assist you within 2 hours.\n"
                "Results are only shared with the patient directly."
            )

        elif text == "4":
            service_list = "\n".join(f"🏥  {s}" for s in services)
            return (
                f"👨‍⚕️ *Our Services at {name}:*\n\n"
                f"{service_list}\n\n"
                f"📞 Reception: {number}\n"
                f"📍 {address}\n"
                f"⏰ {hours}\n\n"
                "Reply *menu* to go back."
            )

        elif text == "5":
            return (
                "🚨 *EMERGENCY*\n\n"
                f"Life-threatening emergency: call *{emergency}* (ambulance)\n"
                "or *10111* (police)\n\n"
                "For urgent but non-life-threatening issues during office hours:\n"
                f"📞 {number}\n\n"
                "⚠️ Do not wait for a WhatsApp reply in an emergency."
            )

        else:
            return (
                "I didn't quite catch that. "
                "Please reply with a number:\n\n"
                + _menu(name)
            )

    # ── Info collected — acknowledge and close the loop ─────────
    if state in ["booking", "prescription", "results"]:
        user_states[phone] = "menu"
        return (
            "Thank you! ✅ Your request has been received.\n\n"
            "A member of our team will respond within "
            "*2 hours* during office hours.\n\n"
            f"📞 Urgent? Call: {number}\n"
            f"⏰ {hours}\n\n"
            "Reply *menu* to see options."
        )

    # ── Fallback ────────────────────────────────────────────────
    return f"Reply *menu* to see options or call us on 📞 {number}."


def _menu(name: str) -> str:
    return (
        f"*{name}* — How can we help?\n\n"
        "1️⃣  Book an Appointment\n"
        "2️⃣  Prescription Refill\n"
        "3️⃣  Test Results Enquiry\n"
        "4️⃣  Our Services & Doctors\n"
        "5️⃣  Emergency"
    )
