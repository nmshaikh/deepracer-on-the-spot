def reward_function(params):
    #############################################################################
    '''
    Based off of example at
    https://docs.aws.amazon.com/deepracer/latest/developerguide/deepracer-reward-function-input.html#reward-function-input-steps
    '''
    
    # Read input variable
    steps = params['steps']
    progress = params['progress']
    all_wheels_on_track = params['all_wheels_on_track']
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    is_reversed = params['is_reversed']

    # Total num of steps we want the car to finish the lap, it will vary depends on the track length
    TOTAL_NUM_STEPS = 200

    # Initialize the reward with typical value
    reward = 1.0

    # Give additional reward if the car pass every 100 steps faster than expected
    if (steps % 100) == 0 and progress > (steps / TOTAL_NUM_STEPS) * 100 :
        reward += 10.0

    if not (all_wheels_on_track and (0.5*track_width - distance_from_center) >= 0.05 and not is_reversed):
        reward = 1e-6

    return float(reward)
