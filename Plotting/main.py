import matplotlib.pyplot as plt

# https://hbr.org/2017/05/linear-thinking-in-a-nonlinear-world

suv_mpg = 10
sedan_mpg = 20

miles_driven_per_year = 10000

gallons_of_gas_used_suv = miles_driven_per_year / suv_mpg
gallons_of_gas_used_sedan = miles_driven_per_year / sedan_mpg


mpg_range = range(10,51)
gallons_used_per_year = [ miles_driven_per_year/mpg for mpg in mpg_range ]


gallons_saved_suvs = [ (gallons_of_gas_used_suv - gallons) for gallons in gallons_used_per_year ]
gallons_saved_sedans = [ (gallons_of_gas_used_sedan - gallons) for gallons in gallons_used_per_year]

plt.plot(mpg_range, gallons_used_per_year, label="gallons used")
plt.plot(mpg_range, gallons_saved_suvs, label="gallons saved in suvs")
plt.plot(mpg_range[10:], gallons_saved_sedans[10:], label="gallons saved in sedans")

plt.xlabel("MPG")
plt.ylabel("gallons")

plt.legend()
plt.show()