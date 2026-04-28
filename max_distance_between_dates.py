## Find the max distance between signup and logoff
"""
user_signups = {
    "user_signups": [
        { "user_id": 31876, "timestamp": "2024-01-22 11:45:30" },
        { "user_id": 59284, "timestamp": "2024-01-20 08:10:05" },
        { "user_id": 86729, "timestamp": "2024-02-05 17:55:40" },
        { "user_id": 73411, "timestamp": "2023-12-14 21:30:00" },
    ]
}

user_logins = {
    "user_logins": [
        {
            "user_identifier": 31876,
            "login_time": "2024-01-23 09:15:20",
            "logoff_time": "2024-02-23 12:40:10"
        },
        {
            "user_identifier": 31876,
            "login_time": "2024-02-10 16:05:45",
            "logoff_time": "2024-03-10 18:55:30"
        },
        {
            "user_identifier": 31876,
            "login_time": "2024-02-18 07:50:00",
            "logoff_time": "2024-03-18 11:25:15"
        },
        {
            "user_identifier": 59284,
            "login_time": "2024-01-24 13:35:10",
            "logoff_time": "2024-02-24 17:10:50"
        },
    ]
}
"""
## for every user check the signup VS logoff
## signup - logoff = diff_time

user_signups = [
    { "user_id": 31876, "timestamp": "2024-01-22 11:45:30" },
    { "user_id": 59284, "timestamp": "2024-01-20 08:10:05" },
    { "user_id": 86729, "timestamp": "2024-02-05 17:55:40" },
    { "user_id": 73411, "timestamp": "2023-12-14 21:30:00" },
]


def get_user_signup_time(user_signups):
    signups = {}
    for signup in user_signups:
        signups[signup['user_id']] = signup['timestamp']
    return print(f'Check List: {signups}')


def diff_user_time():
    pass