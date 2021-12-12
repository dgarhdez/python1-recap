def distance_xy(point1, point2):
    """
    This function takes 4 arguments representing 2 points in cartesian coordinates
    and returns the Euclidean distance between the points:
        d(point1, point2) = sqrt((point1_x - point2_x)^2 + (point1_y - point2_y)^2)
    : param point1 : pair of values representing horizontal and vertical coordinates (type:tuple)
    : param point2 : pair of values representing horizontal and vertical coordinates (type:tuple)
    : return euclidean_distance: euclidean distance between point1 and point2
    """
    return ((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)**0.5


def print_characters_in_string(string):
    print(list(string))