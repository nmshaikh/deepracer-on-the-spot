import math

def reward_function(params):

    # Read input variables
    waypoints = params['waypoints']
    closest_waypoints = params['closest_waypoints']
    heading = params['heading']

    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    all_wheels_on_track = params['all_wheels_on_track']
    speed = params['speed']
    progress = params['progress']

    # Give a very low reward by default
    reward = 1e-6

    # Make the reward equal to progress if no wheels go off the track and
    # the agent is somewhere in between the track borders
    if all_wheels_on_track and (0.5*track_width - distance_from_center) >= 0.05:
        reward = progress

    # Calculate the direction of the center line based on the closest waypoints
    next_point = waypoints[closest_waypoints[1]]
    prev_point = waypoints[closest_waypoints[0]]

    # Calculate the direction in radius, arctan2(dy, dx), the result is (-pi, pi) in radians
    track_direction = math.atan2(next_point[1] - prev_point[1], next_point[0] - prev_point[0])
    # Convert to degree
    track_direction = math.degrees(track_direction)

    # Calculate the difference between the track direction and the heading direction of the car
    direction_diff = abs(track_direction - heading)
    if direction_diff > 180:
        direction_diff = 360 - direction_diff

    # Function to adjust the reward based on the speed and heading of the car
    DIRECTION_THRESHOLD = 15.0
    DIRECTION_OPTIMUM = 0.0
    MAX_SPEED = 4.0
    MIN_SPEED = 0.1

    if direction_diff > DIRECTION_THRESHOLD:
        direction_diff = DIRECTION_THRESHOLD

    normalised_speed = (speed - MIN_SPEED) / (MAX_SPEED - MIN_SPEED)
    normalised_heading = (direction_diff - DIRECTION_OPTIMUM) / (DIRECTION_THRESHOLD - DIRECTION_OPTIMUM)
    z = normalised_speed - normalised_heading + 1

    return float(reward) * z
