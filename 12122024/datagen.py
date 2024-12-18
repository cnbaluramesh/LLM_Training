from faker import Faker
import random

# Initialize Faker
fake = Faker()

# Generate 1000 realistic employees
employee_list = [
    {
        "Name": fake.name(),
        "Email": fake.email(),
        "EmployeeID": random.randint(10001, 99999),
    }
    for _ in range(1000)
]

# Expanded list of possible requests
possible_requests = [
    "help with resetting my password",
    "software installation",
    "access to the VPN",
    "help with my account credentials",
    "permission for remote desktop access",
    "approval for leave",
    "support for printer setup",
    "a new laptop",
    "access to the shared folder",
    "help with system updates",
    "technical support for my device",
    "upgrade for my software",
    "approval for project tools",
    "help with email configuration",
    "installation of a licensed application",
    "replacement of my damaged laptop",
    "access to the HR portal",
    "upgrading my internet bandwidth",
    "help with setting up a video conference",
    "fixing my system's audio issues",
    "installation of antivirus software",
    "renewal of my software license",
    "troubleshooting email delivery issues",
    "adding a network printer to my system",
    "guidance on data backup procedures",
    "approval for extended working hours",
    "help with integrating third-party tools",
    "request for dual monitors setup",
    "unlocking my account after multiple failed attempts",
    "changing my office phone number in the directory",
    "help with exporting data from internal systems",
    "training for new project management tools",
    "installation of custom scripts for automation",
    "assistance with configuring cloud storage access",
    "approval for external software use",
    "help with creating secure passwords",
    "configuration of mobile device for office emails",
    "recovery of accidentally deleted files",
    "resetting my access token",
    "creating a new user account for a team member",
    "migrating data to a new storage system",
    "request for administrative rights on my device",
    "repairing a broken keyboard or mouse",
    "help with network connectivity issues",
    "approval for attending an external training session",
    "access to restricted internal documentation",
    "request for temporary system access for a visitor",
    "setting up a new phone extension",
    "syncing my local files with the shared drive",
    "help with configuring VPN on my mobile device",
    "updating my desktop hardware configuration",
    "approval for accessing sensitive project data",
    "troubleshooting a software crash issue",
    "help with formatting documents for official use",
    "customizing application settings for my role",
    "request for setting up project-specific folders",
    "extending system login session time",
    "guidance on the use of collaboration tools",
    "unlocking a protected document",
    "configuring access to a specific database",
    "creating automated reports for weekly meetings",
    "help with encrypting sensitive data",
    "enabling multi-factor authentication for my account",
    "request for ergonomic accessories for my desk",
    "fixing issues with remote access to the desktop",
    "setup for office-wide broadcast messaging tools",
]

# Randomized introduction templates
introductions = [
    "Hello, I am",
    "Hi there! This is",
    "Greetings, my name is",
    "Hey! I'm",
    "Good day, this is",
    "Hello, my name is",
    "Hi, this is",
    "Hi, I'm",
    "Greetings from",
    "Hey, it's",
    "Hello! It's",
    "Hi everyone, this is",
    "Warm greetings, I am",
    "Howdy! I'm",
    "Good morning, this is",
    "Good afternoon, I am",
    "Good evening, this is",
    "Pleased to introduce myself, I am",
    "It's a pleasure, I am",
    "Allow me to introduce myself, I am",
    "This is",
    "You're speaking with",
    "Let me introduce myself, I'm",
    "Hi all, this is",
    "Hello everyone, I'm",
    "A quick introduction: I'm",
    "Here's a quick note from",
    "Reaching out as",
    "Checking in, this is",
    "I wanted to say hi, I am",
]
request_phrases = [
    "I need",
    "I am requesting",
    "I would like to request",
    "Can you please help me with",
    "I require",
    "I’m reaching out for",
    "Could you assist me with",
    "I’m looking for help with",
    "Can I get assistance with",
    "I’d appreciate help with",
    "I’d like to request support for",
    "I’m in need of",
    "Could you provide support for",
    "I’d like your assistance with",
    "I’d like to ask for",
    "I’m writing to request",
    "I hope you can help me with",
    "I’m reaching out to ask for",
    "Would you assist me with",
    "I’d like some help regarding",
    "I want to request",
    "May I request assistance for",
    "I’m reaching out to request",
    "Please help me with",
    "I’d be grateful for help with",
    "I’m contacting you regarding",
    "I’d like some support for",
    "I am looking for help with",
    "Could you guide me on",
    "Can you please assist with",
]


# Generate 10,000+ end-user requests with randomized introductions
requests_10k = [
    f"{random.choice(introductions)} {employee['Name']} "
    f"{'emp id ' + str(employee['EmployeeID']) if random.choice([True, False]) else 'email ' + employee['Email']}, "
    f"{random.choice(request_phrases)} {random.choice(possible_requests)}."
    for _ in range(10000)
    for employee in random.choices(employee_list, k=1)
]

# Write to a text file
file_path = "data.txt"
with open(file_path, "w") as file:
    file.write("\n".join(requests_10k))

print(f"Requests generated and saved to {file_path}")
