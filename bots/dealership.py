# bots/dealership.py
# Handles ALL car dealership clients.
# Never edit this file to add a new client — edit clients.py only.

user_states = {}


def dealership_bot(text: str, phone: str, config: dict) -> str:

    # Pull client details from config
    name      = config["name"]
    number    = config["phone"]
    address   = config["address"]
    hours     = config["hours"]
    stock_url = config.get("stock_url", "")  # optional — not all clients have a website yet

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
            f"Welcome to *{name}*! 🚗\n\n"
            "We have quality pre-owned vehicles waiting for you.\n"
            "How can we help you today?\n\n"
            "1️⃣  Browse Available Stock\n"
            "2️⃣  Book a Test Drive\n"
            "3️⃣  Get a Finance Quote\n"
            "4️⃣  Trade-In Enquiry\n"
            "5️⃣  Service & Parts\n"
            "6️⃣  Speak to a Consultant\n\n"
            "_Reply with a number_"
        )

    # ── Main menu selections ────────────────────────────────────
    if state == "menu":

        if text == "1":
            if stock_url:
                stock_line = f"View our full inventory here:\n{stock_url}\n\n"
            else:
                stock_line = "Contact us and we will send you our latest stock list.\n\n"
            return (
                f"🚗 *Available Stock — {name}*\n\n"
                f"{stock_line}"
                "Reply *2* to book a test drive on any vehicle.\n"
                "Reply *menu* to go back."
            )

        elif text == "2":
            user_states[phone] = "test_drive"
            return (
                "Let's book your test drive! 🚀\n\n"
                "Please reply with:\n\n"
                "• Your *full name*\n"
                "• The *vehicle* you'd like to test\n"
                "  (make, model and year if known)\n"
                "• Your *preferred date and time*\n\n"
                "A consultant will confirm within 1 hour."
            )

        elif text == "3":
            user_states[phone] = "finance"
            return (
                "Let's get you a finance quote! 💳\n\n"
                "Please share:\n\n"
                "• Your *full name*\n"
                "• *Vehicle of interest*\n"
                "• Your *gross monthly income* (approximate)\n"
                "• Your *deposit amount* (if any)\n\n"
                "We work with all major SA banks. "
                "Bad credit considered."
            )

        elif text == "4":
            user_states[phone] = "trade_in"
            return (
                "Trade-In Enquiry 🔄\n\n"
                "Please share:\n\n"
                "• Vehicle *make, model and year*\n"
                "• Current *mileage* (km)\n"
                "• *Condition* — Excellent / Good / Fair\n"
                "• Any *accident history*? Yes / No\n\n"
                "We will provide a valuation within 2 hours."
            )

        elif text == "5":
            return (
                f"🔧 *Service & Parts — {name}*\n\n"
                "Book a service or enquire about parts:\n\n"
                f"📞 {number}\n"
                f"📍 {address}\n"
                f"⏰ {hours}\n\n"
                "Reply *menu* to go back."
            )

        elif text == "6":
            user_states[phone] = "menu"
            return (
                "A consultant will be in touch shortly! 🏎️\n\n"
                f"📞 Call us directly: {number}\n"
                f"📍 {address}\n"
                f"⏰ {hours}\n\n"
                "Reply *menu* to see all options."
            )

        else:
            return (
                "I didn't quite catch that. "
                "Please reply with a number:\n\n"
                + _menu(name)
            )

    # ── Info collected — acknowledge and close the loop ─────────
    if state in ["test_drive", "finance", "trade_in"]:
        user_states[phone] = "menu"
        return (
            "Thank you! ✅ Your request has been received.\n\n"
            "A consultant will contact you within "
            "*1 hour* during business hours.\n\n"
            f"📞 Urgent? Call: {number}\n"
            f"⏰ {hours}\n\n"
            "Reply *menu* to see more options."
        )

    # ── Fallback ────────────────────────────────────────────────
    return f"Reply *menu* to see options or call us on 📞 {number}."


def _menu(name: str) -> str:
    return (
        f"*{name}* — How can we help?\n\n"
        "1️⃣  Browse Stock\n"
        "2️⃣  Book a Test Drive\n"
        "3️⃣  Finance Quote\n"
        "4️⃣  Trade-In Enquiry\n"
        "5️⃣  Service & Parts\n"
        "6️⃣  Speak to a Consultant"
    )
