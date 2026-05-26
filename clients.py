# clients.py
# ─────────────────────────────────────────────────────────────────
# This is the ONLY file you edit when adding a new client.
# Step 1: Get the Phone Number ID from Meta Developer Console.
# Step 2: Add the client block below using the correct "type".
# Step 3: Save, push to GitHub, Railway auto-deploys in 90 seconds.
# ─────────────────────────────────────────────────────────────────

CLIENTS = {

    # ════════════════════════════════════════════════════════════
    # LAW FIRMS
    # Required keys: name, phone, address, hours, consultation_fee
    # Optional keys: services (list — shows in practice areas menu)
    # ════════════════════════════════════════════════════════════

    "PASTE_PHONE_ID_HERE": {
        "type": "law_firm",
        "name": "PR Peetja Attorneys Inc",
        "phone": "069 217 3099",
        "address": "88 Jorissen Street, 3rd Floor, Braamfontein, JHB",
        "hours": "Mon–Fri 8AM–5PM | Sat 9AM–12PM",
        "consultation_fee": "R500",
        "services": [
            "Labour Law",
            "Contract Drafting & Review",
            "Commercial Law",
            "Family Law",
            "Property Law",
            "Litigation & Dispute Resolution",
        ],
    },

    "PASTE_PHONE_ID_HERE_2": {
        "type": "law_firm",
        "name": "KO Attorneys Inc",
        "phone": "011 455 7100",
        "address": "Bedfordview, Johannesburg",
        "hours": "Mon–Fri 8AM–5PM",
        "consultation_fee": "R600",
        "services": [
            "Labour Law & CCMA",
            "Commercial Law",
            "Criminal Law",
            "Family Law",
            "Debt Collection",
            "Corporate Compliance",
        ],
    },

    # ════════════════════════════════════════════════════════════
    # MEDICAL PRACTICES
    # Required keys: name, phone, address, hours
    # Optional keys: services (list), emergency (defaults to 10177)
    # ════════════════════════════════════════════════════════════

    "PASTE_PHONE_ID_HERE_3": {
        "type": "medical",
        "name": "Sandton Medical Centre",
        "phone": "011 XXX XXXX",
        "address": "123 Rivonia Road, Sandton, JHB",
        "hours": "Mon–Fri 8AM–5PM | Sat 9AM–1PM",
        "emergency": "10177",
        "services": [
            "General Practitioner",
            "Chronic Disease Management",
            "Child & Maternal Health",
            "Occupational Health Certificates",
            "Minor Procedures",
        ],
    },

    # ════════════════════════════════════════════════════════════
    # CAR DEALERSHIPS
    # Required keys: name, phone, address, hours
    # Optional keys: stock_url (if the client has a website with stock)
    # ════════════════════════════════════════════════════════════

    "PASTE_PHONE_ID_HERE_4": {
        "type": "dealership",
        "name": "Iron Motors",
        "phone": "011 XXX XXXX",
        "address": "456 Main Reef Road, Johannesburg",
        "hours": "Mon–Fri 8AM–6PM | Sat 8AM–4PM",
        "stock_url": "https://ironmotors.co.za/stock",
        # Remove the stock_url line entirely if the client has no website yet
    },

    # ════════════════════════════════════════════════════════════
    # FUNERAL PARLOURS
    # Required keys: name, phone
    # Optional keys: address, hours, emergency
    # emergency falls back to the main phone number if not set
    # ════════════════════════════════════════════════════════════

    "PASTE_PHONE_ID_HERE_5": {
        "type": "funeral",
        "name": "Grace Funeral Services",
        "phone": "011 XXX XXXX",
        "address": "78 Soweto Highway, Soweto",
        "hours": "24 hours, 7 days a week",
        "emergency": "082 XXX XXXX",
        # emergency is a separate 24-hour number if the parlour has one
        # If they only have one number, remove the emergency line
        # and the bot will use the main phone number automatically
    },

}
