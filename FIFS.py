process = ["P1", "P2", "P3", "P4", "P5"]
arrival_time = []
burst_time = []

print("Enter Arrival Time and Burst Time for 5 Processes")

for i in range(5):
    print(f"\nEnter details for {process[i]}")
    at = int(input("Arrival Time: "))
    bt = int(input("Burst Time: "))
    arrival_time.append(at)
    burst_time.append(bt)

# Sorting according to Arrival Time
for i in range(5):
    for j in range(i+1, 5):
        if arrival_time[i] > arrival_time[j]:
            arrival_time[i], arrival_time[j] = arrival_time[j], arrival_time[i]
            burst_time[i], burst_time[j] = burst_time[j], burst_time[i]
            process[i], process[j] = process[j], process[i]

completion_time = []
turnaround_time = []
waiting_time = []

time = 0

for i in range(5):
    if time < arrival_time[i]:
        time = arrival_time[i]

    time += burst_time[i]
    completion_time.append(time)

    tat = completion_time[i] - arrival_time[i]
    turnaround_time.append(tat)

    wt = tat - burst_time[i]
    waiting_time.append(wt)

# Display result
print("\nProcess  AT  BT  CT  TAT  WT")
for i in range(5):
    print(process[i], "   ", arrival_time[i], "  ", burst_time[i], "  ",
          completion_time[i], "  ", turnaround_time[i], "  ", waiting_time[i])

avg_wt = sum(waiting_time) / 5
avg_tat = sum(turnaround_time) / 5

print("\nAverage Waiting Time =", round(avg_wt, 2))
print("Average Turnaround Time =", round(avg_tat, 2))
