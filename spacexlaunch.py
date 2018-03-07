import requests


def next_launch():
    apiurl = 'https://api.spacexdata.com/v2/launches/upcoming'
    spacexdata = requests.get(apiurl).json()
    launch = spacexdata[0]
    launch_date_time_utc = launch['launch_date_utc']
    launch_date_utc = launch_date_time_utc[0:10]
    launch_time_utc = launch_date_time_utc[11:]
    launch_site = launch['launch_site']['site_name']
    payloads = []
    for payload in launch['rocket']['second_stage']['payloads']:
        payloads.append(payload['payload_id'])
    rocket_name = launch['rocket']['rocket_name']
    first_stage_flight_num = launch['rocket']['first_stage']['cores'][0]['flight']
    return launch_date_utc, launch_time_utc, launch_site, payloads, rocket_name, first_stage_flight_num


if __name__ == '__main__':
    print(next_launch())