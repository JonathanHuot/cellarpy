import logging
import os
from os import path


def setwritabledirectory(folders):
    def iswritable(directory):
        if not path.exists(directory):
            try:
                os.makedirs(directory)
            except:
                return False
        return os.access(directory, os.W_OK | os.X_OK | os.R_OK)

    for dir in folders:
        if(iswritable(dir)):
            return dir
    logging.debug("No writable dir was found amongst: " + str(folders))
    raise Exception("No writable dir was found amongst: " + str(folders))


def setreadablefile(folders, filename):
    def isreadable(directory, filename):
        if path.isfile(path.join(directory, filename)):
            return os.access(path.join(directory, filename), os.R_OK)
        return False


    for dir in folders:
        if(isreadable(dir, filename)):
            return path.join(dir, filename)
    logging.debug("No readable conf file was found amongst: " + str(folders))
    raise Exception("No readable conf file was found amongst: " + str(folders))


# Initiate logging
def load_logfile(logfile, dirs=[]):
    log_dir = setwritabledirectory(dirs)
    logging.basicConfig(level=logging.DEBUG,
                        filename=path.join(log_dir, logfile),
                        format='%(asctime)s +%(msecs)d [%(process)d] %(levelname)s %(message)s',
                        datefmt='%d/%b/%Y:%H:%M:%S')
    logging.debug('Log file start')


def load_settings(settingsfile, dirs=[], storage_dirs=[]):
    config_file = setreadablefile(dirs, settingsfile)
    with open(config_file) as fd:
        import json
        settings = json.load(fd)

    if "storage" in settings:
        for name, folder in settings["storage"].iteritems():
            settings["storage"][name] = setwritabledirectory([folder] + [path.join(storage, name) for storage in storage_dirs])
            if name == "database" and settings["sqlite"][name][0] != '/':
                settings["sqlite"][name] = path.join(settings["storage"][name], settings["sqlite"][name])

    logging.debug('Settings loaded')
    return settings
