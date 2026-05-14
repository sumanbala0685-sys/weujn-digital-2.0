# weujn Digital 2.0 - Digital Will + Kavach 3.0 Security Protocol
# Founder & CEO: Harsh Dixit
# Date: 14 May 2026
# Mission: A Phone That Protects Privacy, Legacy, and Justice - Globally

class WeujnDigitalWill:
    def __init__(self):
        self.owner_name = "Harsh Dixit"
        self.heir_list = []
        self.video_consent = False
        self.death_declared = False
        self.kavach_active = True
        
    def save_legacy_data(self, relation, name, detail):
        if self.video_consent == True:
            print(f"Saved: {relation} - {name}")
            print("Privacy Note: Never asks for Bank/Aadhaar/OTP")
        else:
            print("Error: Owner video consent required first")
    
    def hacker_detected(self):
        print("HACK ALERT: 3 failed biometric attempts detected")
        print("Activating: GPS + Front Camera + Microphone")
        print("Sending: Location + Hacker Photo to Law Enforcement")
        print("Executing: Phone BRICK MODE + Data Wipe")
        self.brick_phone()
    
    def heir_unlock_protocol(self, heir_biometric, death_certificate):
        if self.death_declared == True and heir_biometric == True:
            print("Hello. I am an AI, not your father")
            print("Your father's message: 'My child is a brave soul'")
        else:
            print("Access Denied. Legal authorization required")
    
    def brick_phone(self):
        print("Phone locked. Sensitive data wiped. Evidence sent to police")

# Core Principle: Humanity before Code. Law before Humanity
print("weujn Digital 2.0 Initialized. For Justice. For Everyone.")