def reward_function(params):
    '''
    Example of penalize steering, which helps mitigate zig-zag behaviors
    '''

    # Read input parameters
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    steering = abs(params['steering_angle']) # Only need the absolute steering angle

    # Give higher reward if the car is closer to center line and vice versa using a continuous reward. 
    distance_reward = 1- (distance_from_center/track_width*0.5)**0.4

    reward = (distance_reward)

    return float(reward)
