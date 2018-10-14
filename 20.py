from sources import daily, weekly
print("Ежедневный прогноз:", daily.forecast())
print("Еженедельный прогноз:")
for number, outlook in enumerate(weekly.forecast(), 1):
    print(number, outlook)


