def get_brake_signal(brake_applied, disc_temp=25.0):
    """Return brake signal voltage.
    
    Args:
        brake_applied (bool): True if brakes are applied.
        disc_temp (float): Disc temperature in Celsius.
        
    Returns:
        float: Voltage signal.
    """
    if not brake_applied:
        return 0.0
    
    # Nominal voltage when brakes fully applied
    nominal_voltage = 5.0
    
    # Temperature compensation: reduce voltage by 0.1V for every 50°C increase
    # Linear reduction relative to disc_temp
    temp_compensation = (disc_temp / 50.0) * 0.1
    voltage = nominal_voltage - temp_compensation
    
    # Ensure voltage does not go below 0
    return max(0.0, voltage)