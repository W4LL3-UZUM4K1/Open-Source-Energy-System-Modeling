from main import hydro_power, pv_power, wind_power

# --- Tests für hydro_power ---
def test_hydro_power():
    assert hydro_power(0.9, 10, 50) == 44.5


# --- Tests für pv_power ---
def test_pv_power():
    assert pv_power(300, 800, 35, 0.4) == 23.4


# --- Tests für wind_power ---
def test_wind_power():
    assert wind_power(1.225, 50, 10, 0.4) == 1225