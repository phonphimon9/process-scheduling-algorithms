import random

def generate_processes(num_processes):
    processes = []
    for i in range(1, num_processes + 1):
        arrival_time = random.randint(0, 10)
        burst_time = random.randint(1, 10)
        priority = random.randint(1, 5)
        processes.append({
            'pid': i,
            'arrival_time': arrival_time,
            'burst_time': burst_time,
            'remaining_time': burst_time,
            'priority': priority
        })
    return processes

def print_results(processes):
    print("PID\tArrival\tBurst\tCompletion\tTurnaround\tWaiting")
    for process in processes:
        print(f"{process['pid']}\t{process['arrival_time']}\t{process['burst_time']}\t"
              f"{process['completion_time']}\t{process['turnaround_time']}\t{process['waiting_time']}")

    # สรุปผลค่าเฉลี่ย
    avg_turnaround = sum(p['turnaround_time'] for p in processes) / len(processes)
    avg_waiting = sum(p['waiting_time'] for p in processes) / len(processes)
    print(f"\nAverage Turnaround Time: {avg_turnaround:.2f}")
    print(f"Average Waiting Time: {avg_waiting:.2f}")

def main():
    mode = input("เลือกโหมดการทำงาน: (on-demand, simulation): ").strip().lower()
    choice = input("เลือกอัลกอริทึมที่ต้องการ: (FCFS, RR, SJF, SRTF, Priority, HRRN, MLFQ): ").strip().upper()
    
    if mode == "simulation":
        num_processes = int(input("จำนวน process ที่ต้องการจำลอง: "))
        processes = generate_processes(num_processes)
    else:
        processes = []  # ให้ผู้ใช้ป้อนข้อมูลเอง
        num_processes = int(input("จำนวน process ที่ต้องการ: "))
        for i in range(num_processes):
            arrival_time = int(input(f"Arrival time of process {i+1}: "))
            burst_time = int(input(f"Burst time of process {i+1}: "))
            priority = int(input(f"Priority of process {i+1} (1-5): "))
            processes.append({
                'pid': i + 1,
                'arrival_time': arrival_time,
                'burst_time': burst_time,
                'remaining_time': burst_time,
                'priority': priority
            })

    # เลือกอัลกอริทึม
    if choice == "FCFS":
        results = fcfs_scheduling(processes)
    elif choice == "RR":
        time_quantum = int(input("กรอก time quantum: "))
        results = rr_scheduling(processes, time_quantum)
    elif choice == "SJF":
        results = sjf_scheduling(processes)
    elif choice == "SRTF":
        results = srtf_scheduling(processes)
    elif choice == "PRIORITY":
        results = priority_scheduling(processes)
    elif choice == "HRRN":
        results = hrrn_scheduling(processes)
    elif choice == "MLFQ":
        queues = int(input("จำนวน queue levels: "))
        time_quantum = int(input("กรอก time quantum: "))
        results = multilevel_feedback_scheduling(processes, queues, time_quantum)

    print_results(results)

def print_results(results):
    for process in results:
        print(f"Process {process['pid']} - Waiting Time: {process['waiting_time']}, Turnaround Time: {process['turnaround_time']}")

def generate_processes(num_processes):
    processes = []
    for i in range(num_processes):
        process = {
            'pid': i + 1,
            'arrival_time': random.randint(0, 10),
            'burst_time': random.randint(1, 10),
            'remaining_time': random.randint(1, 10),
            'priority': random.randint(1, 5)  # สำหรับ Priority Scheduling
        }
        processes.append(process)
    return processes

def fcfs_scheduling(processes):
    processes.sort(key=lambda x: x['arrival_time'])
    current_time = 0
    for process in processes:
        if current_time < process['arrival_time']:
            current_time = process['arrival_time']
        process['start_time'] = current_time
        process['completion_time'] = current_time + process['burst_time']
        current_time += process['burst_time']
        process['turnaround_time'] = process['completion_time'] - process['arrival_time']
        process['waiting_time'] = process['turnaround_time'] - process['burst_time']
    return processes

def rr_scheduling(processes, time_quantum):
    queue = []
    current_time = 0
    completed_processes = []
    
    while processes or queue:
        while processes and processes[0]['arrival_time'] <= current_time:
            queue.append(processes.pop(0))
        
        if queue:
            process = queue.pop(0)
            if process['remaining_time'] <= time_quantum:
                current_time += process['remaining_time']
                process['completion_time'] = current_time
                process['turnaround_time'] = current_time - process['arrival_time']
                process['waiting_time'] = process['turnaround_time'] - process['burst_time']
                completed_processes.append(process)
            else:
                current_time += time_quantum
                process['remaining_time'] -= time_quantum
                queue.append(process)
        else:
            current_time += 1
    
    return completed_processes

def sjf_scheduling(processes):
    processes.sort(key=lambda x: (x['arrival_time'], x['burst_time']))
    current_time = 0
    completed_processes = []
    
    while processes:
        available_processes = [p for p in processes if p['arrival_time'] <= current_time]
        if available_processes:
            available_processes.sort(key=lambda x: x['burst_time'])
            process = available_processes.pop(0)
            processes.remove(process)
            current_time += process['burst_time']
            process['completion_time'] = current_time
            process['turnaround_time'] = process['completion_time'] - process['arrival_time']
            process['waiting_time'] = process['turnaround_time'] - process['burst_time']
            completed_processes.append(process)
        else:
            current_time += 1
        
    return completed_processes

def srtf_scheduling(processes):
    current_time = 0
    completed_processes = []
    while processes:
        available_processes = [p for p in processes if p['arrival_time'] <= current_time]
        if available_processes:
            available_processes.sort(key=lambda x: x['remaining_time'])
            process = available_processes[0]
            current_time += 1
            process['remaining_time'] -= 1
            if process['remaining_time'] == 0:
                processes.remove(process)
                process['completion_time'] = current_time
                process['turnaround_time'] = process['completion_time'] - process['arrival_time']
                process['waiting_time'] = process['turnaround_time'] - process['burst_time']
                completed_processes.append(process)
        else:
            current_time += 1
    
    return completed_processes

def priority_scheduling(processes):
    processes.sort(key=lambda x: (x['arrival_time'], x['priority']))
    current_time = 0
    completed_processes = []
    
    while processes:
        available_processes = [p for p in processes if p['arrival_time'] <= current_time]
        if available_processes:
            available_processes.sort(key=lambda x: x['priority'])
            process = available_processes.pop(0)
            processes.remove(process)
            current_time += process['burst_time']
            process['completion_time'] = current_time
            process['turnaround_time'] = process['completion_time'] - process['arrival_time']
            process['waiting_time'] = process['turnaround_time'] - process['burst_time']
            completed_processes.append(process)
        else:
            current_time += 1
    
    return completed_processes

def hrrn_scheduling(processes):
    current_time = 0
    completed_processes = []
    
    while processes:
        available_processes = [p for p in processes if p['arrival_time'] <= current_time]
        if available_processes:
            for process in available_processes:
                process['response_ratio'] = ((current_time - process['arrival_time']) + process['burst_time']) / process['burst_time']
            available_processes.sort(key=lambda x: x['response_ratio'], reverse=True)
            process = available_processes.pop(0)
            processes.remove(process)
            current_time += process['burst_time']
            process['completion_time'] = current_time
            process['turnaround_time'] = process['completion_time'] - process['arrival_time']
            process['waiting_time'] = process['turnaround_time'] - process['burst_time']
            completed_processes.append(process)
        else:
            current_time += 1
    
    return completed_processes

def multilevel_feedback_scheduling(processes, queues, time_quantum):
    queue_levels = {i: [] for i in range(queues)}
    current_time = 0
    completed_processes = []
    
    while processes or any(queue_levels.values()):
        while processes and processes[0]['arrival_time'] <= current_time:
            queue_levels[0].append(processes.pop(0))
        
        for i in range(queues):
            if queue_levels[i]:
                process = queue_levels[i].pop(0)
                if process['remaining_time'] <= time_quantum:
                    current_time += process['remaining_time']
                    process['completion_time'] = current_time
                    process['turnaround_time'] = current_time - process['arrival_time']
                    process['waiting_time'] = process['turnaround_time'] - process['burst_time']
                    completed_processes.append(process)
                else:
                    current_time += time_quantum
                    process['remaining_time'] -= time_quantum
                    if i < queues - 1:
                        queue_levels[i + 1].append(process)
                    else:
                        queue_levels[i].append(process)
                break
        else:
            current_time += 1
    
    return completed_processes

# Run the main function
if __name__ == "__main__":
    main()