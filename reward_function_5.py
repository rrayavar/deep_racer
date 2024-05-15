def reward_function(params):
    '''
    Example of rewarding the agent to follow center line
    '''

    # Read input parameters
    all_wheels_on_track = params['all_wheels_on_track']
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']

    # Give higher reward if the car is closer to center line and vice versa
    distance_reward = 1- (distance_from_center/track_width*0.5)**0.4

    # Penalize the good buddy when it steps off the track. Note: 2s loss for every step off. Significant issue. 
    if all_wheels_on_track and (0.5*track_width - distance_from_center) >= 0.05:
        wheel_reward = 1.0
    else:
        wheel_reward = 1e-3

    # Steering penality threshold, change the number based on your action space setting
    abs_steering = abs(params['steering_angle'])
    ABS_STEERING_THRESHOLD = 15
      
    # Penalize reward if the car is steering too much
    if abs_steering > ABS_STEERING_THRESHOLD:
        wobble_reward = 0.7
    else:
        wobble_reward = 1.0

    if all_wheels_on_track and (0.5*track_width - distance_from_center) >= 0.45:
        mid_reward = 10.0
    elif all_wheels_on_track and (0.5*track_width - distance_from_center) >= 0.3:
        mid_reward = 7.0
    elif all_wheels_on_track and (0.5*track_width - distance_from_center) >= 0.2:
        mid_reward = 5.0
    elif all_wheels_on_track and (0.5*track_width - distance_from_center) >= 0.05:
        mid_reward = 1.0
    else:
        mid_reward = 1e-3

    reward = (distance_reward*mid_reward + wheel_reward + wobble_reward)

    return float(reward)
