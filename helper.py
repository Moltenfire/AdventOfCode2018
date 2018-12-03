

def load_in_list(file, t=int):
    with open(file, 'r') as f:
        return list(map(lambda x : t(x.strip()), f.readlines()))