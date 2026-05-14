# weujn Digital 2.0 - Digital Vaseeyat + Kavach 3.0
# Founder & CEO: Harsh Dixit
# Date: 14 May 2026, 12:42 PM IST
# Mission: Gareeb ka Phone, Gareeb ki Vaseeyat, Gareeb ka Insaf

class WeujnVaseeyat:
    def __init__(self):
        self.owner_name = "Harsh Dixit"
        self.waris_list = []
        self.consent_video = False
        self.death_declared = False
        self.kavach_active = True
        
    def save_emotional_data(self, relation, name, detail):
        if self.consent_video == True:
            print(f"Save kiya: {relation} - {name}")
            print("Yaad rakhna: Bank/Aadhaar kabhi nahi maangunga")
        else:
            print("Pehle maalik ki video ijazat chahiye")
    
    def hacker_detected(self):
        print("HACK ALERT: 3 galat try detected")
        print("GPS + Camera + Mic ON kar raha hu")
        print("Location + Photo Police ko bhej raha hu")
        print("Phone BRICK MODE me ja raha hai")
        self.brick_phone()
    
    def waris_unlock_protocol(self, waris_biometric, death_certificate):
        if self.death_declared == True and waris_biometric == True:
            print("Namaste Beta. Main AI hu, Papa nahi")
            print("Papa ka sandesh: 'Beta sher ka bachcha hai'")
        else:
            print("Access Denied. Kanoon todna mana hai")
    
    def brick_phone(self):
        print("Phone band. Data wipe. Hacker ki photo thana pahunch gayi")

print("weujn Digital 2.0 Initialized. Jai Hind. Jai Gareeb.")