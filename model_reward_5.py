def reward_function(params):
    '''
    Example of penalize steering, which helps mitigate zig-zag behaviors
    '''
    
    reward = 1e-3

    # Read input parameters
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    steering = params['steering_angle']
    steps = params['steps']
    progress = params['progress']
    speed = params['speed']

    # Give higher reward if the car is closer to center line and vice versa using a continuous reward. 
    distance_reward = 1- (distance_from_center/track_width*0.5)**0.4

    # Total num of steps we want the car to finish the lap, it will vary depends on the track length
    TOTAL_NUM_STEPS = 300

    # Initialize the reward with typical value
    step_reward = 0
    speed_reward = 0

    # Give additional reward if the car pass every 100 steps faster than expected
    if (steps % 100) == 0 and progress > (steps / TOTAL_NUM_STEPS) * 100 :
        step_reward = 1.0

    if -5 < steering_angle < 5:
        if speed > 2.5:
            speed_reward = 2.0
        elif speed > 2:
            speed_reward = 1.0
    elif steering_angle < -15 or steering_angle > 15:
        if speed < 1.8:
            speed_reward = 1.0
        elif speed_reward > 2.2:
            speed_reward = 0.5
    
    reward = (distance_reward*3 + step_reward + speed_reward*2)

    return float(reward)
