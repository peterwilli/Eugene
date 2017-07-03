import random
import csv
import string
random.seed(80085)

cmd_pairs = []

def add_command(natural, cmd):
    cmd_pairs.append((natural, cmd))

def random_string(N):
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(N))

def random_strings(N, amount):
    ret = []
    for i in range(0, amount):
        ret.append(random_string(N))
    return ret

def create_data_1(amount_of_commands):
    def create_script(dirs, rs):
        cmds = []
        for i in range(0, dirs):
            cmds.append('mkdir %s_%d' % (rs, i + 1))
        return " && ".join(cmds)

    for i in range(0, amount_of_commands):
        rs = random_string(random.randint(1, 10))
        for i2 in range(0,10):
            script = create_script(i2 + 1, rs)
            add_command("create %d directories starting with %s" % (i2 + 1, rs), script)

def save_data():
    with open('data.csv', 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=';',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for cmd in cmd_pairs:
            writer.writerow((cmd[0], cmd[1]))

def main():
    create_data_1(10)
    save_data()

main()
