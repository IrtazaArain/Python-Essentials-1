hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))
t_min = (hour*60)+(mins+dura)
hour = (t_min//60)%24
mins = t_min % 60
print(hour, ":", mins, sep='')
