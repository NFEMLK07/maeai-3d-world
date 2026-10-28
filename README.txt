MAE AI 3D WORLD V4.2 — MINIATURE DIORAMA

เปิดเล่นบน Windows:
1. แตก ZIP
2. คัดลอก osm-roads-rivers.geojson ที่ดาวน์โหลดสำเร็จแล้วจาก V4.1 ลงโฟลเดอร์เดียวกับ index.html
   หรือเปิด PowerShell แล้วรัน: python download_osm.py
3. ในโฟลเดอร์นี้รัน: python -m http.server 8000
4. เปิด http://localhost:8000 (Ctrl+Shift+R หากเว็บแคชเดิม)

สิ่งที่อิงข้อมูลจริง: DEM เดิม, GPS จุดเรียนรู้ 75 แห่ง, ถนน/ลำน้ำ OSM เมื่อใส่ GeoJSON
สิ่งที่เป็นแบบจำลองตกแต่ง: บ้านและวัดต้นแบบ ต้นไม้และแปลงเกษตร ไม่ได้เป็นผังบ้านจริง
ถนนหลัก: motorway/trunk/primary/secondary แม่น้ำหลัก: river
สามารถกดปุ่ม 'แสดงทางย่อย' เพื่อดูข้อมูลละเอียดเพิ่มเติมได้
ยังไม่ได้ตรวจสอบความถูกต้องของปริมาณน้ำ/ชื่อสถานที่ทุกแห่ง ณ ภาคสนาม
ใช้อินเทอร์เน็ตสำหรับโหลด Three.js และฟอนต์จาก CDN

© OpenStreetMap contributors. DEM และฐานสถานที่จากไฟล์โครงการที่ผู้ใช้ให้
