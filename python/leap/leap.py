def is_leap_year(year):

    # if year % 4 == 0:
    #     if year % 100 == 0:
    #         if year % 400 == 0:
    #             return True
    #     else:
    #         return True
    # return False

    # return  (year % 4 == 0) \
    #     and ((year % 100 != 0) \
    #       or (year % 400 == 0))

    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0