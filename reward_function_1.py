def reward_function(params):
    '''
    Example of penalize steering, which helps mitigate zig-zag behaviors
    '''

    # Read input parameters
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    steering = abs(params['steering_angle']) # Only need the absolute steering angle

    # Calculate 3 marks that are farther and father away from the center line
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width

    # Give higher reward if the car is closer to center line and vice versa
    distance_reward = 1- (distance_from_center/track_width*0.5)**0.4

    # Wheels on Track Penalty
    SPEED_THRESHOLD = 1.0
    if not all_wheels_on_track:
           track_reward = 1e-3
       elif speed < SPEED_THRESHOLD:
           track_reward = 0.1
       else:
           track_reward = 10.0

    #Continuous Speed Reward
    speed_reward = 1-(speed_diff/max_speed_diff)**).5

    # Steering penality threshold, change the number based on your action space setting    ABS_STEERING_THRESHOLD = 15

    # Penalize reward if the car is steering too much
    if steering > ABS_STEERING_THRESHOLD:
        abs_reward *= 0.8

    reward =  distance_reward + track_reward + speed_reward + abs_reward


    steps = params['steps']
    progress = params['progress']
    TOTAL_NUM_STEPS = 300

    if (steps % 100) == 0 and progress > (steps / TOTAL_NUM_STEPS) * 100:
         steps_reward +=10.0

    return float(reward)
