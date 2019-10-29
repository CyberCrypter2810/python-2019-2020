#Section 2.8.2.py

lat = input("Enter lats: ")
lon = input("Enter lons: ")

lat_list = [float(s) for s in lat.split(',')]
lon_list = [float(s) for s in lon.split(',')]

print(lat_list)
print(lon_list)

print("Farthest North = " + str(max(lat_list)))
print("Farthest West = " + str(max(lon_list)))
print("Farthest South = " + str(min(lat_list)))
print("Farthest East = " + str(min(lon_list)))
