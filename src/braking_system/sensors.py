def get_brake_signal(brake_applied, disc_temp=25.0):
    """Return brake signal voltage.
    
    Args:
        brake_applied (bool): True if brakes are applied.
        disc_temp (float): Disc temperature in Celsius.
        
    Returns:
        float: Voltage signal.
    """
    if brake_applied:
        return 1.0
    else:
        return 0.0