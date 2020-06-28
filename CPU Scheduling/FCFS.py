def FCFS(processes):

    waitingTime, turnaroundTime = {}, {}
    timePassed = 0
    i = 0
    for process in processes:
        if i == 0:
            timePassed = processes[process]['arrival']
        waitingTime[process] = processes[process]['arrival']
        turnaroundTime[process] = processes[process]['brust']
        i += 1

    average_turnaround, average_waiting = 0, 0

    for process in processes:
        waitingTime[process] = timePassed - waitingTime[process]
        turnaroundTime[process] = waitingTime[process] + turnaroundTime[process]
        average_turnaround += turnaroundTime[process]
        average_waiting += waitingTime[process]
        timePassed += processes[process]['brust']

    average_waiting /= len(processes)
    average_turnaround /= len(processes)

    return [average_waiting, average_turnaround]