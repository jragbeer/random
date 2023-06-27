from nicehash import *
import dagster

def sendemail_(TEXT, HTML, SUBJECT = 'Error in Nicehash Scheduler!'):
    """

    This function sends emails to the email list depending on the para

    :param TEXT: text to send in an email
    :param HTML: text to send in an email, but in HTML (default)
    :param week_start: integer that indicates if this is the email sent weekly (start of the week, monday at 7am)
    :param error_email: if this is an error email, send an alert with a different message
    :return:
    """
    # This is a temporary fix. Be careful of malicious links
    context = ssl._create_unverified_context()

    my_email = 'jragbeer@ryerson.ca'
    senders_email = 'julienwork369@gmail.com'  # senders email
    senders_pswd = 'cmyoikyctdywpuhf'  # senders password

    # current date, and a date 5 days away
    curtime = datetime.datetime.now().date()
    week_from_today = curtime + datetime.timedelta(days=5)

    TO = [my_email,
          ]

    # Gmail Sign In
    gmail_sender = senders_email
    gmail_passwd = senders_pswd

    msg = MIMEMultipart('alternative')  # tell the package we'd prefer HTML emails
    msg['Subject'] = SUBJECT  # set the SUBJECT of the email
    msg['From'] = gmail_sender  # set the FROM field of the email
    msg['To'] = ', '.join(TO)  # set the TO field of the email

    # add the 2 parts of the email (one plain text, one html)
    part1 = MIMEText(TEXT, 'plain')
    part2 = MIMEText(HTML, 'html')
    # It will default to the plain text verison if the HTML doesn't work, plain must go first
    msg.attach(part1)
    msg.attach(part2)

    # connect to the GMAIL server
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    # login to the GMAIL server
    server.login(gmail_sender, gmail_passwd)

    try:
        # send email and confirm email is sent / time it is sent
        server.sendmail(gmail_sender, TO, msg.as_string())
        logging.info(str(curtime) + ' email sent')
    except Exception as e:
        # print error if not sent, and confirm it wasn't sent
        logging.info(str(e))
        logging.info(error_handling())
        logging.info(str(curtime) + ' error sending mail')

    server.quit()
def wrap_in_paragraphs(txt, colour="DarkSlateBlue", size=4):
    """

    This function wraps text in paragraph, bold and font tags - according to the colour and size given.

    :param text: text to wrap in tags
    :param colour: colour of the font
    :param size: size of the font
    :return: string wrapped in html tags
    """
    return f"""<p><b><font color={colour} size={size}>{txt}</font></b></p>"""
@dagster.success_hook(name= 'success_hook')
def action_on_success(context):
    now = datetime.datetime.now()
    TEXT = f"{context.op.name} finished successfully | {now}"
    HTML = wrap_in_paragraphs(TEXT)
    sendemail_(TEXT, HTML, )
@dagster.failure_hook(name= 'failure_hook')
def action_on_fail(context):
    now = datetime.datetime.now()
    TEXT = f"{context.job_name} ( {context.op.name} ) failed | {now} | " + f"{context.op_exception}"
    HTML = wrap_in_paragraphs(TEXT)
    sendemail_(TEXT, HTML, )

# OPS / TASKS

@dagster.op
def five_min_func():
    get_data_5mins()

@dagster.op
def check_running():
    are_gpus_runnning()

@dagster.op
def long_term_nicehash_public():
    get_public_data_long_term()

@dagster.op
def four_hour_func():
    get_data_4hr()


@dagster.op
def one_hour_func():
    get_data_1hr()

@dagster.op
def make_easy_sql_func(context, cereals = None):
    add_most_recent_rig_device_stats_table()

# JOBS

@dagster.job(hooks={action_on_fail, })
def one_hour_job():
    one_hour_func()
    check_running()

@dagster.job(hooks={action_on_fail, })
def four_hour_job():
    four_hour_func()

@dagster.job
def five_min_job():
    make_easy_sql_func(five_min_func())

@dagster.job
def long_term_job():
    long_term_nicehash_public()

# SET SCHEDULES FOR EACH JOB

nicehash_longterm_schedule = dagster.ScheduleDefinition(cron_schedule="0 10 * * 4", job=long_term_job, execution_timezone="US/Eastern", )

nicehash_4hr_schedule = dagster.ScheduleDefinition(cron_schedule="0 */4 * * *", job=four_hour_job, execution_timezone="US/Eastern", )

nicehash_1hr_schedule = dagster.ScheduleDefinition(cron_schedule="0 */1 * * *", job=one_hour_job, execution_timezone="US/Eastern", )

nicehash_5min_schedule = dagster.ScheduleDefinition(cron_schedule="*/5 * * * *", job=five_min_job, execution_timezone="US/Eastern", )

# WHATS IS VISIBLE IN REPOSITORY
@dagster.repository
def nicehash_repository():
    return [one_hour_job, four_hour_job, five_min_job, long_term_job, nicehash_longterm_schedule, nicehash_1hr_schedule, nicehash_4hr_schedule, nicehash_5min_schedule]
