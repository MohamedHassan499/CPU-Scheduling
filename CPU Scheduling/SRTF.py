def pickBestProcess(processes, processes_queue, timePassed):

    bestProcess = None
    leastTime = 2e9
    for process in processes_queue:
        if timePassed >= processes[process]['arrival'] and processes[process]['brust'] < leastTime and processes[process]['brust'] > 0:
            bestProcess = process
            leastTime = processes[process]['brust']
    return bestProcess

def SRTF(processes):

    processes_qeueue, temp = [], []
    waiting_processes = {}
    timePassed, average_waiting, average_turnaround = 0, 0, 0
    prevProcess = None

    for process in processes:
        if len(processes_qeueue) == 0:
            processes_qeueue.append(process)
        waiting_processes[process] = []
        temp.append(processes[process]['brust'])

    while True:
        bestProcess = pickBestProcess(processes, processes_qeueue, timePassed)
        if bestProcess == None:
            break
        if prevProcess != bestProcess:
            if prevProcess != None:
                waiting_processes[prevProcess].append(timePassed)
            waiting_processes[bestProcess].append(timePassed)
        timePassed += 1
        for process in processes:
            if timePassed >= processes[process]['arrival'] and processes[process]['brust'] > 0 and (not processes_qeueue.count(process)):
                processes_qeueue.append(process)
        processes[bestProcess]['brust'] -= 1
        prevProcess = bestProcess

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