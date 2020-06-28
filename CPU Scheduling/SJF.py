def pickBestProcess(processes, taken, timePassed):

    bestProcess = None
    leastTime = 2e9
    for process in processes:
        if not taken[process] and timePassed >= processes[process]['arrival'] and processes[process]['brust'] <= leastTime:
            bestProcess = process
            leastTime = processes[process]['brust']
    return bestProcess


def SJF(processes):

    waitingTime, turnaroundTime, taken = {}, {}, {}
    i, timePassed = 0, 0
    for process in processes:
        if i == 0:
            timePassed = processes[process]['arrival']
        taken[process] = False
        i += 1

    average_turnaround, average_waiting = 0, 0
    bestProcess = pickBestProcess(processes, taken, timePassed)

    while bestProcess != None:
        taken[bestProcess] = True
        waitingTime[bestProcess] = timePassed - processes[bestProcess]['arrival']
        turnaroundTime[bestProcess] = waitingTime[bestProcess] + processes[bestProcess]['brust']
        average_waiting += waitingTime[bestProcess]
        average_turnaround += turnaroundTime[bestProcess]
        timePassed += processes[bestProcess]['brust']
        bestProcess = pickBestProcess(processes, taken, timePassed)

    average_waiting /= len(processes)
    average_turnaround /= len(processes)


    return [average_waiting, average_turnaround]