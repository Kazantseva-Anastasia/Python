soups = ["щи", "борщ", "щавелевый суп", "овсяный суп", "суп по-чабански"]
n = int(input())
for i in range(n):
    if len(soups) > i:
        print(soups[i])
    else:
        soups += soups
        print(soups[i])
