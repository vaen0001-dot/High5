import nltk
from nltk.chat.util import Chat, reflections

reflections = {
  "i am"       : "you are",
  "i was"      : "you were",
  "i"          : "you",
  "i'm"        : "you are",
  "i'd"        : "you would",
  "i've"       : "you have",
  "i'll"       : "you will",
  "my"         : "your",
  "you are"    : "I am",
  "you were"   : "I was",
  "you've"     : "I have",
  "you'll"     : "I will",
  "your"       : "my",
  "yours"      : "mine",
  "you"        : "me",
  "me"         : "you"
}

def process_response(process_name, steps, contact):
    response = f"Here’s how the {process_name} process works:\n"
    count = 1
    for i in steps:
        response += f"{count}. {i}\n"
        count += 1
    response += f"\nIf you need help, please contact {contact}.\n"
    return response

processes = {
    "financial claim": process_response(
        "financial claim",
        ["Fill out the Financial Claim Form (link: [URL])",
            "Attach receipts or invoices",
            "Submit for manager approval",
            "Finance reimburses within 10 working days"
        ],
        "finance@company.com"
    ),
    "leave application": process_response(
        "leave application",
        ["Log in to the HR portal (link: [URL])",
            "Choose 'Leave Application' from the menu",
            "Select leave type and dates",
            "Submit for manager approval"
        ],
        "hr@company.com"
    ),
    "travel request": process_response(
        "travel request",
        ["Complete the Travel Request Form (link: [URL])",
            "Attach itinerary or purpose of travel",
            "Submit for manager approval",
            "Finance processes travel allowance"
        ],
        "travel@company.com"
    ),
    "documentation request": process_response(
        "documentation request",
        ["Log in to the Employee Portal (link: [URL])",
            "Select 'Request Documents' from the Services menu",
            "Choose the type of document (e.g., employment letter, payslip, tax form)",
            "Submit the request and track status on the portal"
        ],
        "hr@company.com"
    ),
    "meeting room booking": process_response(
        "meeting room booking",
        ["Go to the Outlook/Calendar system or Room Booking app (link: [URL])",
            "Select the date, time, and preferred meeting room",
            "Check availability and reserve the room",
            "Add attendees and confirm the booking"
        ],
        "hr@company.com"
    ),
    "it equipment request": process_response(
        "IT equipment request",
        ["Log in to the IT Helpdesk portal (link: [URL])",
            "Choose 'Equipment Request' from the options",
            "Select the item you need (laptop, monitor, headset, etc.)",
            "Submit for manager approval and wait for IT to confirm delivery/pickup"
        ],
        "it@company.com"
    )
}

# General Section
general_pairs = [
    (r"(.*)leave(.*)", [f"You have 14 annual leave days per year. {processes["leave application"]}"]),
    (r"(.*)holiday(.*)", [f"We observe all public holidays. If you would like to request for travel. {processes["travel request"]}"]),
    (r"(.*)password(.*)", ["You can reset your password at portal.company.com."]),
    (r"(.*)wifi(.*)", ["The office Wi-Fi is 'CompanyNet', password: Welcome123"]),
    (r"(.*)financial claim(.*)", [f"{processes["financial claim"]}"]),
    (r"book(.*)meeting room(.*)", [f"{processes["meeting room booking"]}"]),
    (r"(.*)onboarding(.*)", ["You need to complete the Get Started course and check in with your manager to complete your onboarding"]),
    (r"(.*)training(.*)", ["Head to the Courses tab for your required training course"]),
    (r"(.*)it equipment(.*)", [f"{processes['it equipment request']}"]),
    (r"(.*)", ["Sorry, I didn't understand that."])
]

# Create bots
general_chat = Chat(general_pairs, reflections)

def chat():
    while True:
        print("Hello! How can I help you?")
        user_input = input("You: ")
        if "quit" in user_input.lower():
            print("Chatbot: Goodbye!")
            break
        else:
            general_chat.converse()

#initiate the conversation
def get_bot_response(user_input):
        return general_chat.respond(user_input)