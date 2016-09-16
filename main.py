import os
import signal
import time

# Gracefully handle SIGTERM and SIGINT
def handle_signal(signum, stack):
    print 'Received Signal: %s' % signum
    # Raise a KeyboardInterrupt so that the main loop catches this and shuts down
    raise KeyboardInterrupt

signal.signal(signal.SIGTERM, handle_signal)
signal.signal(signal.SIGINT, handle_signal)


if __name__ == '__main__':
    while True:
        try:
            print "Hello World!"
            time.sleep(5)
        except KeyboardInterrupt:
            print "Exiting.."
            break 
        except Exception as ex:
            print "Exiting.."
            break 
