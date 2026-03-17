#Alternative: Time-Based Log Rotation 
#Use TimedRotatingFileHandler to rotate logs based on time intervals, such as daily or hourly.

from logging.handlers import TimedRotatingFileHandler
# ... setup logger ...
# Rotate daily at midnight, keeping 7 days of backups
handler = TimedRotatingFileHandler('timed_app.log', when='midnight', backupCount=7)


#The when parameter supports intervals like 'h', 'd', or 'midnight' to 
#control rotation timing.
