def total_diff(sensorA, sensorB):
    diff = 0
    for i in range(len(sensorA)):
        diff += abs(sensorA[i] - sensorB[i])
    return diff


if __name__ == '__main__':
    sensorA = [15, -4, 56, 10, -23]
    sensorB = [14, -9, 56, 14, -23]
    diff = total_diff(sensorA, sensorB)
    print(f"The total difference is: {str(diff)}")
