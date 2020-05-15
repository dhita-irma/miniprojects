def total_diff(sensorA, sensorB):
    if len(sensorA) == 0:
        return 0
    else:
        last_diff = abs(sensorA[-1] - sensorB[-1])
        return total_diff(sensorA[:-1], sensorB[:-1]) + last_diff


if __name__ == '__main__':
    sensorA = [15, -4, 56, 10, -23]
    sensorB = [14, -9, 56, 14, -23]

    diff = total_diff(sensorA, sensorB)
    print(f"The total difference is: {str(diff)}")
