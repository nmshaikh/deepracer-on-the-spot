def reward_function(params):
    #############################################################################
    '''
    Based off of examples at
    https://docs.aws.amazon.com/deepracer/latest/developerguide/deepracer-reward-function-input.html#reward-function-input-steps
    and 
    https://docs.aws.amazon.com/deepracer/latest/developerguide/deepracer-reward-function-input.html#reward-function-input-steering_angle
    '''
    
    # Read input variable
    steps = params['steps']
    progress = params['progress']
    all_wheels_on_track = params['all_wheels_on_track']
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    is_reversed = params['is_reversed']
    abs_steering = abs(params['steering_angle']) # We don't care whether it is left or right steering

    # Total num of steps we want the car to finish the lap, it will vary depends on the track length
    TOTAL_NUM_STEPS = 200

    # Initialize the reward with typical value
    reward = 0.5

    # Give additional reward if the car pass every 100 steps faster than expected
    if (steps % 100) == 0 and progress > (steps / TOTAL_NUM_STEPS) * 100 :
        reward += 10.0

    # Penalize if car steer too much to prevent zigzag
    ABS_STEERING_THRESHOLD = 15.0
    if abs_steering > ABS_STEERING_THRESHOLD:
        reward *= 0.8
    
    if not (all_wheels_on_track and (0.5*track_width - distance_from_center) >= 0.05 and not is_reversed):
        reward = 1e-6

    return float(reward)
