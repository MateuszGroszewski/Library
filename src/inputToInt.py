def convertInputToInt(entryValue: any) -> int | None:
    """
    if possible converts a string input into an integer, otherwise returns None
    :param entryValue: string
    :return:  INT or None
    """
    try:
        return int(entryValue)
    except ValueError:
        return None
