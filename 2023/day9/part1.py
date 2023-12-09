# Start 8:32 am
# 8:35 pause for breakfast
# 9:18 am restart
# 20-30 minute break
# 10:09 am done
# NOTE: series == history
with open("input.txt", "r") as file:
    sum = 0
    for line in file:
        numberStr = line.split()
        # 2-D array where row is the series, and column numbers show different series
        series = []
        series.append([int(number) for number in numberStr])

        i = 0
        while i < len(series):
            # Create list of differences between values in list in current sereis and append as another row
            series.append([b-a for a, b in zip(series[i][:-1], series[i][1:])])

            """
            # print debugging
            for j in range(len(series)):
                print(series[j])
            print("---------------------")
            """

            # if the newly appended list only has 0, no need to create more series
            if len([number for number in series[i + 1] if number != 0]) == 0:
                break

            i += 1

        # NEXT VALUE PREDICTION
        # Loop through all series by looping through all possible column indices in REVERSE
        for series_number in range(len(series) - 1, -1, -1):
            if series_number == len(series) - 1:
                series[series_number].append(0)
            else:
                # series_number + 1 becuase we are going bottom to up
                # append to end of series with (current end + last number from series directly under)
                series[series_number].append(series[series_number][-1] + series[series_number + 1][-1])
        
        # The intial series prediction of future is added to sum
        sum += series[0][-1]
    print(sum)
        