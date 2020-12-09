import re

curr_entry = {}
all_entries = []

with open("day04input.txt") as f:
    while True:
        line = f.readline()
        if not line:
            break
        line = line.strip()
        
        if len(line) == 0:
            all_entries.append(curr_entry)
            curr_entry = {}
        else:
            line_entries = line.split(" ")
            for x in line_entries:
                matches = re.match(r"(\w\w\w)\:(.*)", x)
                curr_entry[matches.group(1)] = matches.group(2)

all_entries.append(curr_entry)

valid = 0

#byr (Birth Year) - four digits; at least 1920 and at most 2002.
#iyr (Issue Year) - four digits; at least 2010 and at most 2020.
#eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
#hgt (Height) - a number followed by either cm or in:
#If cm, the number must be at least 150 and at most 193.
#If in, the number must be at least 59 and at most 76.
#hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
#ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
#pid (Passport ID) - a nine-digit number, including leading zeroes.
#cid (Country ID) - ignored, missing or not.

def checkyear(val, min, max):
    if not val:
        return False
    if not re.match(r"^\d\d\d\d$",val):
        print(val)
        return False 
    ival = int(val)
    if ival < min or ival > max:
        return False 
    return True

def checkheight(val):
    if not val:
        return False
    match = re.match(r"^(\d+)([a-z]{2})$", val)
    if not match:
        return False
    if match.group(2) == "cm":
        val = int(match.group(1))
        return val >= 150 and val <= 193
    elif match.group(2) == "in":
        val = int(match.group(1))
        return val >= 59 and val <= 76    
    else:
        return False

def checkhair(val):
    if not val:
        return False 
    return re.match(r"^\#[0-9a-f]{6}$",val)

def checkeye(val):
    if not val:
        return False
    return val in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

def checkid(val):
    if not val:
        return False
    return re.match(r"^\d{9}$", val)

for entry in all_entries:
    if not checkyear(entry.get("byr"), 1920, 2002):
        continue
    if not checkyear(entry.get("iyr"), 2010, 2020):
        continue
    if not checkyear(entry.get("eyr"), 2020, 2030):
        continue
    if not checkheight(entry.get("hgt")):
        continue
    if not checkhair(entry.get("hcl")):
        continue
    if not checkeye(entry.get("ecl")):
        continue
    if not checkid(entry.get("pid")):
        continue
    valid += 1

print(valid)
#print(all_entries)