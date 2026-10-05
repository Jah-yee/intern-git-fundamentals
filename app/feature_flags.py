FLAGS = {"new_dashboard": False, "beta_calls": True}


def is_enabled(name):
    return FLAGS.get(name, False)