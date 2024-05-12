def reward_function(params):
    '''
    Example of penalize steering, which helps mitigate zig-zag behaviors
    '''

    # Read input parameters
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    steering = abs(params['steering_angle']) # Only need the absolute steering angle
    steps = params['steps']
    progress = params['progress']

    # Give higher reward if the car is closer to center line and vice versa using a continuous reward. 
    distance_reward = 1- (distance_from_center/track_width*0.5)**0.4

    # Total num of steps we want the car to finish the lap, it will vary depends on the track length
    TOTAL_NUM_STEPS = 300

    # Initialize the reward with typical value
    reward = 1.0

    # Give additional reward if the car pass every 100 steps faster than expected
    if (steps % 100) == 0 and progress > (steps / TOTAL_NUM_STEPS) * 100 :
        step_reward += 1.0
    
    reward = (distance_reward*2 + step_reward)

    return float(reward)
