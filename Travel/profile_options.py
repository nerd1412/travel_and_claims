from .models import ProfileModel

def get_profile_options():
    profile_dict = {}
    profiles = ProfileModel.objects.all()
    for profile in profiles:
        employee_names = profile.TPFCMANID.first_name
        if profile.TPFCNAME not in profile_dict:
            profile_dict[profile.TPFCNAME] = employee_names
        else:
            profile_dict[profile.TPFCNAME] += f" / {employee_names}"

    profile_options = [(profile_name, profile_name) for profile_name, _ in profile_dict.items()]
    return profile_options

profile_options = get_profile_options()