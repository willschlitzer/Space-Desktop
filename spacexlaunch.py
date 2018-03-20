"""Queries the r/spacex API for the upcoming launch information,
and returns the information for the next upcoming launch"""

import requests


def next_launch():
    """Queries the r/spacex API and returns launch info"""
    apiurl = 'https://api.spacexdata.com/v2/launches/upcoming'
    spacexdata = requests.get(apiurl).json()
    # The first entry in spacexdata is the next upcoming launch
    launch = spacexdata[0]
    launch_date_time_utc = launch['launch_date_utc']
    # Slices the date and time as two separate strings
    launch_date_utc = launch_date_time_utc[0:10]
    launch_time_utc = launch_date_time_utc[11:]
    launch_site = launch['launch_site']['site_name']
    # Creates a list of payload IDs in the event of multiple payloads on a single launch
    payloads = []
    for payload in launch['rocket']['second_stage']['payloads']:
        payloads.append(payload['payload_id'])
    rocket_type = launch['rocket']['rocket_name']
    # The number of times the first stage booster has flown
    first_stage_flight_num = launch['rocket']['first_stage']['cores'][0]['flight']
    return {'date': launch_date_utc,
            'time': launch_time_utc,
            'site': launch_site,
            'payloads': payloads,
            'rocket_type': rocket_type,
            'first_stage_flight_num': first_stage_flight_num}


if __name__ == '__main__':
    print(next_launch())