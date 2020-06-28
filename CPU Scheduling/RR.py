def RR(processes, quantumTime):

    processes_qeueue, temp = [], []
    waiting_processes = {}
    timePassed, average_waiting, average_turnaround = 0, 0, 0

    for process in processes:
        if len(processes_qeueue) == 0:
            processes_qeueue.append(process)
        waiting_processes[process] = []
        temp.append(processes[process]['brust'])

    while len(processes_qeueue) != 0:
        front = processes_qeueue[0]
        waiting_processes[front].append(timePassed)
        timePassed += min(processes[front]['brust'], quantumTime)
        processes[front]['brust'] = max(0, processes[front]['brust'] - quantumTime)
        for process in processes:
            if timePassed >= processes[process]['arrival'] and processes[process]['brust'] > 0 and front != process and (not processes_qeueue.count(process)):
                processes_qeueue.append(process)
        if processes[front]['brust'] > 0:
            processes_qeueue.append(front)
        processes_qeueue.pop(0)
        waiting_processes[front].append(timePassed)

    j = 0
    for process in waiting_processes:
        for i in range(0, len(waiting_processes[process]), 2):
            if i == 0:
                average_waiting += waiting_processes[process][i] - processes[process]['arrival']
            else:
                average_waiting += waiting_processes[process][i] - waiting_processes[process][i - 1]
        average_turnaround += temp[j]
        j += 1
    average_turnaround += average_waiting
    average_turnaround /= len(processes)
    average_waiting /= len(processes)
    return [average_waiting, average_turnaround]