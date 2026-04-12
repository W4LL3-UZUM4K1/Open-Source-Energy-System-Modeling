def hydro_power(n, q, h):
    """Function to calculate the possible power of a hydroelectric power plant depending on the inputs efficiency (n), the flow rate (q), and the drop height(h)"""
    g = 9.81 #Gravity in m/S
    P = g * n * q * h #Calculates Power in W
    return P

def pv_power(P_STC, G, T_module, beta):
    """
    Function to calculate the PV power under real-world conditions depending
    on the nominal power of the module under standard test conditions (P_STC),
    current solar irradiance (G), module temperature (T_module) and
    the temperature coefficient (beta)."""
    G_STC = 1000  # Standard-Sonneneinstrahlung [W/m²]
    beta_decimal = beta / 100.0 #Temperature coeficient in decimal
    P = P_STC * (G / G_STC) * (1 - beta_decimal * (T_module - 25)) # Calculates Power in W
    P = round(P, 1) #Rounds Power
    return P

def wind_power(rho, A, v, Cp):
    """
    Function to calculate the possible power of a wind turbine depending
    on the inputs air density (rho), rotor swept area (A),
    wind speed (v), and power coefficient (Cp)."""
    P = 0.5 * rho * A * v**3 * Cp  # Calculates Power in W
    P = round(P, 1) #Rounds Power
    return P



