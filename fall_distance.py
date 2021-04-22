# David Novelo CS 161 Oregon State University
def fall_distance(time_in_seconds: object) -> object:
    """The following formula can be used to determine the distance an object"
           "falls due to gravity in a specific time period
           :type time_in_seconds:"""
    return (1 / 2) * 9.8 * time_in_seconds ** 2


dist = fall_distance(3.2)
print(dist)