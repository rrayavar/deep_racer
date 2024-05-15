# -*- coding: utf-8 -*-
"""
Created on Wed May 15 08:24:25 2024

@author: Rama.Rayavarapu
"""

def reward_function(params):
    '''
    Example of rewarding the agent to follow center line
    '''

    # Read input parameters
    all_wheels_on_track = params['all_wheels_on_track']
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    steering = params['steering_angle']
    steps = params['steps']
    progress = params['progress']
    speed = params['speed']

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
        wobble_reward = 0.5
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

    # Total num of steps we want the car to finish the lap, it will vary depends on the track length
    TOTAL_NUM_STEPS = 300

    # Initialize the reward with typical value
    step_reward = 0
    speed_reward = 0
    
    step_reward = 0
    # Give additional reward if the car pass every 100 steps faster than expected
    if (steps % 100) == 0 and progress > (steps / TOTAL_NUM_STEPS) * 100 :
        step_reward = 1.0

    if -5 < steering < 5:
        if speed > 2.5:
            speed_reward = 2.0
        elif speed > 2:
            speed_reward = 1.0
    elif steering < -15 or steering > 15:
        if speed < 1.8:
            speed_reward = 1.0
        elif speed_reward > 2.2:
            speed_reward = 0.5

    reward = (distance_reward*mid_reward + wheel_reward + wobble_reward*step_reward + speed_reward)

    return float(reward)
