# bots/funeral.py
# Handles ALL funeral parlour clients.
# Never edit this file to add a new client — edit clients.py only.
# This niche requires a softer, more compassionate tone throughout.

user_states = {}


def funeral_bot(text: str, phone: str, config: dict) -> str:

    # Pull client details from config
    name      = config["name"]
    number    = config["phone"]
    address   = config.get("address", "")
    hours     = config.get("hours", "24 hours, 7 days a week")
    # emergency falls back to the main number if not separately defined
    emergency = config.get("emergency", number)

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
            f"Thank you for reaching out to *{name}*. 🙏\n\n"
            "We understand this may be a difficult time, "
            "and we are here to assist you with care and compassion.\n\n"
            "How can we help you today?\n\n"
            "1️⃣  Urgent Assistance (bereavement)\n"
            "2️⃣  Pre-Planning Arrangements\n"
            "3️⃣  Our Services & Pricing\n"
            "4️⃣  Speak to a Consultant\n\n"
            "_Reply with a number_"
        )

    # ── Main menu selections ────────────────────────────────────
    if state == "menu":

        if text == "1":
            user_states[phone] = "urgent"
            return (
                "We are so sorry for your loss. 🙏\n\n"
                "To assist you as quickly as possible, "
                "please share:\n\n"
                "• Your *full name*\n"
                "• Your *contact number*\n"
                "• *Location* of the deceased\n"
                "• Your *relationship* to the deceased\n\n"
                "A consultant will call you back within *15 minutes*.\n\n"
                f"📞 For immediate assistance: {emergency}"
            )

        elif text == "2":
            user_states[phone] = "pre_planning"
            return (
                "Pre-Planning Arrangements 📋\n\n"
                "Planning ahead is one of the most meaningful gifts "
                "you can give your loved ones. "
                "Our consultants will guide you through every option "
                "with no pressure whatsoever.\n\n"
                "Please share your *full name* and "
                "*preferred time for a call* and we will arrange "
                "a comfortable, private consultation."
            )

        elif text == "3":
            addr_line = f"📍 {address}\n" if address else ""
            return (
                f"🕊️ *{name} — Our Services:*\n\n"
                "• Full burial services\n"
                "• Cremation services\n"
                "• Repatriation (local & international)\n"
                "• Tombstone services\n"
                "• Pre-planning & funeral cover consultation\n\n"
                "We work with all major funeral policies.\n\n"
                f"{addr_line}"
                f"📞 {number}\n"
                f"⏰ {hours}\n\n"
                "For pricing, please call us directly — "
                "we tailor arrangements to every family's needs.\n\n"
                "Reply *menu* to go back."
            )

        elif text == "4":
            user_states[phone] = "menu"
            return (
                f"A consultant will contact you shortly. 🙏\n\n"
                f"📞 24-Hour Line: {emergency}\n\n"
                "We are available day and night, "
                "every day of the year."
            )

        else:
            return (
                "I didn't quite catch that. "
                "Please reply with a number:\n\n"
                + _menu(name)
            )

    # ── Urgent bereavement — acknowledge immediately ─────────────
    if state == "urgent":
        user_states[phone] = "menu"
        return (
            "Thank you. 🙏 Your message has been received.\n\n"
            "A consultant will contact you "
            "within *15 minutes*.\n\n"
            f"📞 24-Hour Direct Line: {emergency}\n\n"
            "We are with you every step of the way."
        )

    # ── Pre-planning — acknowledge and book callback ─────────────
    if state == "pre_planning":
        user_states[phone] = "menu"
        return (
            "Thank you for reaching out. 🙏\n\n"
            "A consultant will be in touch to arrange "
            "a comfortable, pressure-free consultation "
            "at a time that suits you.\n\n"
            f"📞 {number}\n"
            f"⏰ {hours}"
        )

    # ── Fallback ────────────────────────────────────────────────
    return (
        f"Reply *menu* to see options or call us 24 hours "
        f"on 📞 {emergency}."
    )


def _menu(name: str) -> str:
    return (
        f"*{name}* — How can we help?\n\n"
        "1️⃣  Urgent Assistance\n"
        "2️⃣  Pre-Planning\n"
        "3️⃣  Services & Pricing\n"
        "4️⃣  Speak to a Consultant"
    )
