def maxNotes(states, notes, k, length):
    noteTaken = []
    for i in range(length):
        noteTaken.append([notes[i], states[i]])
 
    awakeSum = 0
    for note, state in noteTaken:
        if state:
            awakeSum += note
 
    left = 0
    answer = awakeSum
    for i, given in enumerate(noteTaken):
        note, state = given
        if state == 0:
            awakeSum += note
        if i > k - 1:
            noteLeft, stateLeft = noteTaken[left]
            if stateLeft == 0:
                awakeSum -= noteLeft
            left += 1
        answer = max(answer, awakeSum)
        
    return max(answer, awakeSum)
 
 
size, k = list(map(int, input().split(" ")))
notes = list(map(int, input().split(" ")))
state = list(map(int, input().split(" ")))
print(maxNotes(state, notes, k, size))
