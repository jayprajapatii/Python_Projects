# EMPLOYEE RECORD DEMO – Using All Python Built-in Data Types

# Numeric Types
employee_id = 1086          # int
hourly_rate = 550.75        # float
signal_phase = 2 + 3j       # complex (for hardware simulation)

# Text Type
employee_name = "PATEL SMIT RAKESHBHAI"  # str

# Boolean Type
is_active = True  # bool – is employee currently active?

# Sequence Types
skills = ["Python", "Data Science", "ML"]  # list
location = ("Mehsana", "India")          # tuple
work_hours = range(9, 18)                  # range – work hours from 9 AM to 5 PM

# Mapping Type
employee_record = {
    "id": employee_id,
    "name": employee_name,
    "rate": hourly_rate,
    "active": is_active,
    "skills": skills,
    "location": location,
}

# Set Types
unique_skills = set(skills)  # set – automatically removes duplicates
core_skills = frozenset(["Python", "ML"])  # frozenset – immutable

# Binary Types (simulating image or fingerprint data in bytes)
fingerprint_scan = bytes([120, 3, 255, 0, 100])  # bytes – fixed image data
editable_scan = bytearray(fingerprint_scan)     # bytearray – can be modified
scan_view = memoryview(fingerprint_scan)        # memoryview – efficient slicing

# Display Information
print("🧾 EMPLOYEE PROFILE")
print(f"ID: {employee_record['id']}")
print(f"Name: {employee_record['name']}")
print(f"Hourly Rate: ₹{employee_record['rate']}")
print(f"Active: {employee_record['active']}")
print(f"Skills: {employee_record['skills']}")
print(f"Location: {employee_record['location'][0]}, {employee_record['location'][1]}")
print(f"Work Hours: {list(work_hours)}")
print(f"Unique Skills: {unique_skills}")
print(f"Core Skills (Frozen): {core_skills}")
print(f"Complex Number (Signal Phase): {signal_phase}")

print("\n🔐 Binary Data Handling")
print(f"Fingerprint (bytes): {fingerprint_scan}")
print(f"Editable Scan (bytearray): {editable_scan}")
print(f"Memoryview Slice (first 3 bytes): {scan_view[:3].tolist()}")

