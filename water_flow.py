#added constants outside the function for EARTH_ACCELERATION, WATER_DYNAMIC_VISCOSITY and WATER_DENSITY

EARTH_ACCELERATION_OF_GRAVITY = 9.8066500
WATER_DENSITY = 998.2000000
WATER_DYNAMIC_VISCOSITY = 0.0010016

def water_column_height(tower_height, tank_height):
    t = float(tower_height)
    w = float(tank_height)
    column_height = t + ( (3 * w) / 4 )
    return column_height

def pressure_gain_from_water_height(height):
    h = float(height)
    pressure_gain = (WATER_DENSITY * EARTH_ACCELERATION_OF_GRAVITY * h) / 1000
    return pressure_gain

def pressure_loss_from_pipe (pipe_diameter,pipe_length, friction_factor, fluid_velocity):
    friction_f = float(friction_factor)
    length_l = float(pipe_length)
    velocity_v = float(fluid_velocity)
    diameter_d = float(pipe_diameter)

    pressure_loss_P = -(friction_f * length_l * WATER_DENSITY * velocity_v**2) / (2000 * diameter_d)
    return pressure_loss_P

def pressure_loss_from_fittings(fluid_velocity, quatity_fittings):
    velocity = float(fluid_velocity)
    fittings = float(quatity_fittings)
    lost_pressure = (-0.04 * WATER_DENSITY * velocity**2 * fittings) / 2000
    return lost_pressure

def reynolds_number(hydraulic_diameter, fluid_velocity):
    diameter = float(hydraulic_diameter)
    velocity = float(fluid_velocity)
    reynolds = (WATER_DENSITY * diameter * velocity) / 0.0010016
    return reynolds

def pressure_loss_from_pipe_reduction(larger_diameter,fluid_velocity, reynolds_number, smaller_diameter):
    reynolds= float(reynolds_number)
    larger_diameter = float(larger_diameter)
    smaller_diameter = float(smaller_diameter)

    k = (0.1 + (50/reynolds)) * ((larger_diameter / smaller_diameter)**4 - 1)
    pressure_loss = (-k * WATER_DENSITY * fluid_velocity**2) / 2000
    return pressure_loss