import subprocess

def procx(args):
    l = ['procx']
    l.extend(args)
    process = subprocess.Popen(l,
                     stdout=subprocess.PIPE, 
                     stdin=subprocess.PIPE,
                     stderr=subprocess.PIPE)
    process.wait()
    out, err = process.communicate()
    if out == b'':
        return None, err
    return out, err