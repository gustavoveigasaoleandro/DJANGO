from rest_framework.throttling import AnonRateThrottle


class MatriculaAnonRateThrottle(AnonRateThrottle):
    rate = '3/day'
