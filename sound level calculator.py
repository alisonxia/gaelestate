soundLevel = 10
soundLevelAround = [20, 100, 10, 22, 11]

average = sum(soundLevelAround) / len(soundLevelAround)
difference = (soundLevel - average)
roundedDiff = round(difference)
def numberCheck(a):
  if a < 0:
    print("The noise level is",abs(roundedDiff),"dB below average compared to similar properties.")
  if a == 0:
    print("The noise level is average compared to similar properties ")
  if a > 0:
    print("The noise level is",roundedDiff,"dB above average compared to similar properties.")

numberCheck(difference)