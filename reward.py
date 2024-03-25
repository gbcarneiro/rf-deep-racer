import math

def reward_function(params):

	all_wheels_on_track = params['all_wheels_on_track']  
	speed = params['speed']  
	steering = params['steering_angle']  
	progress = params['progress']
	track_width = params['track_width']  
	distance_from_center = params['distance_from_center']  
	steps = params['steps']  

	# Constantes
	SPEED_THRESHOLD = 2.0  
	STEERING_THRESHOLD = 15.0  
	MAX_REWARD = 3.0  
	MIN_REWARD = 0.5  
	PENALTY = 1e-3  

	# Calcula marcadores para distância do centro
	marker_1 = 0.1 * track_width
	marker_2 = 0.20 * track_width
	marker_3 = 0.30 * track_width
	marker_4 = 0.40 * track_width
	marker_5 = 0.5 * track_width

	reward = MAX_REWARD if distance_from_center <= marker_1 and all_wheels_on_track else PENALTY

	# Diminui a recompensa gradativamente conforme o carro se afasta do centro
	if distance_from_center <= marker_2:
			reward = 2.5
	elif distance_from_center <= marker_3:
			reward = 1.5
	elif distance_from_center <= marker_4:
			reward = 1.0
	elif distance_from_center <= marker_5:
			reward = MIN_REWARD

	# Penaliza se o carro for muito devagar
	if speed < SPEED_THRESHOLD:
			reward *= 0.8

	if (0.5*track_width - distance_from_center) >= 0.05:
		reward += 1.0

	# Penaliza por volante excessivo para evitar ziguezague
	if abs(steering) > STEERING_THRESHOLD:
			reward *= 0.8

	return float(reward)
