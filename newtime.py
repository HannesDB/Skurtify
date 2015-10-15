
    try:
        start_time = json_obj['playlist']['song']['starttimeutc'][6:19]
        start_time = int(json_time)
        start_time = datetime.fromtimestamp(json_time / 1e3)
        start_time = datetime.time(json_time)
        return str(start_time)[0:8]

    except KeyError:
        try:
            start_time = json_obj['playlist']['song']['starttimeutc'][6:19]
            start_time = int(json_time)
            start_time = datetime.fromtimestamp(json_time / 1e3)
            start_time = datetime.time(json_time)
            return str(start_time)[0:8]

        except KeyError:
            try:
                start_time = json_obj['playlist']['song']['starttimeutc'][6:19]
                start_time = int(json_time)
                start_time = datetime.fromtimestamp(json_time / 1e3)
                start_time = datetime.time(json_time)
                return str(start_time)[0:8]
