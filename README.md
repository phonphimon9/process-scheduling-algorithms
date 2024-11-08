# Process Scheduling Algorithms

โปรเจกต์นี้เป็นการศึกษาและจำลองการทำงานของ Process Scheduling Algorithms ที่ใช้ในระบบปฏิบัติการ เพื่อจัดสรรเวลาในการประมวลผลของโปรเซสต่างๆ โดยมีการนำเสนอตัวอย่างและการเปรียบเทียบระหว่างอัลกอริทึมแต่ละแบบ

## รายละเอียดของอัลกอริทึม

1. **FCFS (First-Come, First-Served)**  
   อัลกอริทึมนี้จะทำการจัดสรร CPU ตามลำดับของโปรเซสที่มาถึงก่อน โดยไม่คำนึงถึงความยาวของเวลาในการประมวลผล เป็นอัลกอริทึมที่ง่ายที่สุดแต่สามารถเกิดปัญหา *Convoy Effect* ได้

2. **RR (Round Robin)**  
   อัลกอริทึมนี้แบ่งเวลาประมวลผลให้แต่ละโปรเซสตาม *Time Quantum* ซึ่งจะสลับกันประมวลผล ทำให้โปรเซสทั้งหมดมีโอกาสได้ประมวลผลในเวลาที่เท่าเทียม เหมาะกับระบบปฏิบัติการแบบ Time-Sharing

3. **SJF (Shortest Job First)**  
   อัลกอริทึมที่เลือกโปรเซสที่มีเวลาในการประมวลผลสั้นที่สุดก่อน ช่วยลดค่า *Average Waiting Time* แต่มักจะเกิด *Starvation* หากมีโปรเซสที่สั้นกว่าเข้ามาเรื่อยๆ

4. **SRTF (Shortest Remaining Time First)**  
   เป็นรูปแบบ Preemptive ของ SJF ที่จะคอยตรวจสอบและสลับไปประมวลผลโปรเซสที่มีเวลาคงเหลือสั้นที่สุด จึงลดเวลาในการรอคอยและทำงานได้อย่างมีประสิทธิภาพมากขึ้น

5. **Priority Scheduling**  
   อัลกอริทึมที่เลือกโปรเซสตามลำดับความสำคัญ (Priority) หากมีโปรเซสที่มี Priority สูงเข้ามาใหม่ โปรเซสปัจจุบันอาจถูกหยุดและสลับไปยังโปรเซสที่มี Priority สูงกว่า

6. **HRRN (Highest Response Ratio Next)**  
   อัลกอริทึมนี้จะพิจารณา *Response Ratio* ซึ่งคำนวณจาก (เวลาในการรอ + เวลาในการประมวลผล) / เวลาในการประมวลผล เพื่อเลือกโปรเซสที่เหมาะสม ช่วยลดการเกิด Starvation ได้ดี

7. **MLFQ (Multi-Level Feedback Queue)**  
   ใช้หลายคิวในการจัดสรรโปรเซส โดยโปรเซสที่ประมวลผลนานจะถูกย้ายไปยังคิวที่ต่ำกว่า ส่วนโปรเซสใหม่จะเริ่มที่คิวสูงสุด เป็นอัลกอริทึมที่ยืดหยุ่นและเหมาะกับระบบที่ต้องการจัดการหลายรูปแบบ

## การติดตั้ง

1. **Clone โปรเจกต์จาก GitHub**
   ```bash
   git clone https://github.com/username/process-scheduling-algorithms.git
   cd process-scheduling-algorithms
   ```

2. **ติดตั้ง Python (ถ้ายังไม่ได้ติดตั้ง)**  
   ตรวจสอบให้แน่ใจว่าคุณติดตั้ง [Python 3.6+](https://www.python.org/downloads/) และเพิ่ม Python ลงในระบบ PATH เรียบร้อยแล้ว

3. **ติดตั้ง Dependencies (ถ้ามี)**  
   ในกรณีที่มีไฟล์ `requirements.txt` ให้ใช้คำสั่งนี้:
   ```bash
   pip install -r requirements.txt
   ```

## วิธีการใช้งาน

1. **รันโปรแกรมหลัก**
   ```bash
   python main.py
   ```

2. **เลือกโหมดการทำงาน**
   - `on-demand` : ให้ผู้ใช้ป้อนข้อมูลของกระบวนการเอง
   - `simulation` : ให้ระบบสร้างกระบวนการแบบสุ่มตามจำนวนที่ผู้ใช้ระบุ

3. **เลือกอัลกอริทึมที่ต้องการทดสอบ**  
   เมื่อรันโปรแกรม คุณจะถูกถามให้เลือกอัลกอริทึมที่ต้องการทดสอบจากตัวเลือกต่อไปนี้:
   - FCFS (First-Come, First-Served)
   - RR (Round Robin)
   - SJF (Shortest Job First)
   - SRTF (Shortest Remaining Time First)
   - Priority
   - HRRN (Highest Response Ratio Next)
   - MLFQ (Multi-Level Feedback Queue)

4. **กำหนดพารามิเตอร์เพิ่มเติม**
   สำหรับบางอัลกอริทึม คุณจะต้องกรอกข้อมูลเพิ่มเติม:
   - **Round Robin (RR)**: กำหนด `time quantum` สำหรับการแบ่งเวลา
   - **MLFQ**: กำหนดจำนวน `queue levels` และ `time quantum` สำหรับแต่ละคิว

5. **ดูผลลัพธ์**  
   หลังจากที่โปรแกรมทำงานเสร็จสิ้น ผลลัพธ์จะแสดงข้อมูลการจัดสรรกระบวนการและค่าเฉลี่ยของ **Turnaround Time** และ **Waiting Time** ของแต่ละโปรเซสในตาราง ตัวอย่างสำหรับ First-Come, First-Served (FCFS)เช่น:

   ```
   PID     Arrival Burst   Completion  Turnaround  Waiting
   1       0       5       5           5           0
   2       2       3       8           6           3
   3       4       4       12          8           4

   Average Turnaround Time: 6.33
   Average Waiting Time: 2.33
   ```
## Algorithms Included
   - First-Come, First-Served (FCFS)
   - Round-Robin (RR)
   - Shortest-Job-First (SJF)
   - Shortest-Remaining-Time-First (SRTF)
   - Priority Scheduling
   - Highest Response Ratio Next (HRRN)
   - Multilevel Queue with Feedback (MLFQ)

## License
   This project is licensed under the MIT License.