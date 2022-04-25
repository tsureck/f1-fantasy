from matplotlib import pyplot as plt
import fastf1
import fastf1.plotting
from numpy import full

fastf1.Cache.enable_cache('cache/')

fastf1.plotting.setup_mpl()

race = fastf1.get_session(2022, 'Imola', 'R')

race.load()
fullnames = race.results['FullName']
gridposition = race.results['GridPosition']
for i in range(len(fullnames)):
    print(fullnames[i] + " Started from " + str(gridposition[i]) + " Position")

# fast_leclerc = session.laps.pick_driver('LEC').pick_fastest()
# lec_car_data = fast_leclerc.get_car_data()
# t = lec_car_data['Time']
# vCar = lec_car_data['Speed']

# # The rest is just plotting
# fig, ax = plt.subplots()
# ax.plot(t, vCar, label='Fast')
# ax.set_xlabel('Time')
# ax.set_ylabel('Speed [Km/h]')
# ax.set_title('Leclerc is')
# ax.legend()
# plt.show()