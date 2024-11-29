import re

# อ่านไฟล์ .sql
input_file = 'tambol.sql'  # เปลี่ยนเป็นชื่อไฟล์จริง
output_file = 'outputT.txt'

# สร้าง regex pattern เพื่อค้นหาข้อมูล
pattern = re.compile(
    r"INSERT INTO `tambol`\(`tcode`, `tname`, .+?\) VALUES \('(?P<tcode>\d+)', '(?P<tname>[^']+)',",
    re.DOTALL
)

# เก็บผลลัพธ์
results = []

with open(input_file, 'r', encoding='utf-8') as f:
    for line in f:
        match = pattern.search(line)
        if match:
            tcode = match.group('tcode')
            tname = match.group('tname')
            results.append(f"{tcode} {tname}")

# บันทึกผลลัพธ์ลงไฟล์
with open(output_file, 'w', encoding='utf-8') as f:
    f.write('\n'.join(results))

print("ข้อมูลถูกบันทึกแล้ว")