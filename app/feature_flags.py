FLAGS = {"new_dashbord": False, "beta_calls": True}


def is_enabled(name):
    return FLAGS.get(name, False)