import re

# อ่านไฟล์ .sql
input_file = 'amphoe.sql'  # เปลี่ยนเป็นชื่อไฟล์จริง
output_file = 'outputA.txt'

# สร้าง regex pattern เพื่อค้นหาข้อมูล
pattern = re.compile(
    r"INSERT INTO `amphoe`\(`acode`, `aname`, .+?\) VALUES \('(?P<acode>\d+)', '(?P<aname>[^']+)',",
    re.DOTALL
)

# เก็บผลลัพธ์
results = []

with open(input_file, 'r', encoding='utf-8') as f:
    for line in f:
        match = pattern.search(line)
        if match:
            acode = match.group('acode')
            aname = match.group('aname')
            results.append(f"{acode} {aname}")

# บันทึกผลลัพธ์ลงไฟล์
with open(output_file, 'w', encoding='utf-8') as f:
    f.write('\n'.join(results))

print("ข้อมูลถูกบันทึกแล้ว")