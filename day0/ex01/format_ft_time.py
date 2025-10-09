import time

month = {1: "January",
		 2: "February",
		 3: "March",
		 4: "April",
		 5: "May",
		 6: "June",
		 7: "July",
		 8: "August",
		 9: "September",
		 10: "October",
		 11: "November",
		 12: "December"}

start = time.gmtime(0)
date = time.asctime()

print(f'Seconds since {month[start.tm_mon]} {start.tm_mday}, {start.tm_year}: {time.time()} or {time.time():e} in scientific notation')
print(f'{date.split()[1]} {date.split()[2]} {date.split()[4]}')