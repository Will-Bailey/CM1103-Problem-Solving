import math

def seconds_to_mixed(total_seconds):
	seconds = total_seconds % 60
	total_minutes = total_seconds // 60
	minutes  = total_minutes % 60
	hours = total_minutes // 60
	print(hours, minutes, seconds)


def mixed_to_seconds(hours, minutes, seconds):
    """
    >>> mixed_to_seconds(1,1,1)
    3661
    """
    total_seconds = (hours * (60**2)) + (minutes * 60) + seconds
    return(total_seconds) 

def volume_of_sphere(radius):
	return((4/3) * math.pi * radius ** 3)

def price_of_books(copies):
	return((0.6 * 24.95 * copies) + 3 + (0.75 * (copies - 1)))


print(volume_of_sphere(5))
print(price_of_books(60))