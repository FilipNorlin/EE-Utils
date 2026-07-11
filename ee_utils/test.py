from RTD import RTD

pt1000 = RTD(R0=1000)

pt1000.set_temperature(25)
print(pt1000.get_resistance())
# 1097.35 Ω

pt1000.set_resistance(1385.05)
print(pt1000.get_temperature())
# ≈100 °C