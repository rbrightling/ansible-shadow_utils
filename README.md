Shadow Utils
============

Manage the shadow utilies package configuration used for managing users and groups accounts on systems.

Best practice security has tried to be applied to the default configurations; however, always ensure sufficiant
scrutiny as this is no guarantee.

Requirements
------------

Ansible 2.8+

Supported OS's
- Debian 10
- CentOS 8

Role Variables
--------------

```yaml
# useradd config options
# #######################

# Default user created shel with useradd
shadow_utils_shell: "{{ shadow_utils__shell }}"

# The GID of the user (100=users), used if no other groups are specified. 
shadow_utils_group: 100

# Number of days after password expires until the accout is permanently disable. -1 to disable.
shadow_utils_inactive: 60

# The default expire date
shadow_utils_expire: null

# The default home directory
shadow_utils_home: "/home"

# The skeletal structure to copy over to the new users home directory.
shadow_utils_skel: "/etc/skel"

# Create a mail spool for new users by default
shadow_utils_create_mail_spool: false

# Login.defs config options
# #########################

# The mail spool directory. This is needed to manipulate the mailbox when its corresponding user account is modified or deleted.
shadow_utils_mail_dir: "{{ shadow_utils__mail_dir }}"

# Defines the location of the users mail spool files relatively to their home directory
shadow_utils_mail_file: null

# Enable logging and display of /var/log/faillog login failure info.         
# This option conflicts with the pam_tally PAM module.
shadow_utils_faillog_enab: true

# Enable display of unknown usernames when login failures are recorded.
shadow_utils_log_unkfail_enab: true
 
# Enable logging of successful logins.
shadow_utils_log_ok_logins: false

# Enable "syslog" logging of su activity - in addition to sulog file logging.
shadow_utils_syslog_su_enab: true

# Enable "syslog" logging of sg activity.
shadow_utils_syslog_sg_enab: true
 
# If defined, all su activity is logged to this file.
shadow_utils_sulog_file: '/var/log/su.log'

shadow_utils_ftmp_file: '/var/log/btmp'

# If defined, file which maps tty line to TERM environment parameter
shadow_utils_ttytype_file: null

# If defined, the command name to display when running "su -".
shadow_utils_su_name: 'su'

# If defined, suppresses login messages. If a full path then hushed is enabled for usernames in the specified file; otherwise,
# hushed is enabled if the file exists in the users directory.
shadow_utils_hushlogin_file: '.hushlogin'

# Sets the PATH varialbe of a superuser on login
shadow_utils_env_supath: 
    - '/usr/local/sbin'
    - '/usr/local/bin'
    - '/usr/sbin'
    - '/usr/bin'
    - '/sbin'
    - '/bin'

# Sets the PATH variable of a regular user on login
shadow_utils_env_path: 
    - '/usr/local/bin'
    - '/usr/bin'
    - '/bin'
    - '/usr/local/games'
    - '/usr/games'

# The terminal permissions.
shadow_utils_ttygroup: 'tty'
shadow_utils_ttyperm: '0600'

# Terminal REASE character (010 = backspace, 0177 = DEL)
shadow_utils_erasechar: '0177'

# Terminal KILL character (025 = CTRL/U)
shadow_utils_killchar: '025'

# The file mode creation mask is initialized to this value.
shadow_utils_umask: '077'
# - 022: files - 640 (rw-rw----), directories - 750 (rwxrwx---)
# - 027: files - 640 (rw-r-----), directories - 750 (rwxr-x---)
# - 077: files - 640 (rw-------), directories - 750 (rwx------)

# The maximum number of days a password may be used. If the password is older than this, a password change will be forced.
shadow_utils_pass_max_days: 366

# he minimum number of days allowed between password changes. Any password changes attempted sooner than this will be rejected.
shadow_utils_pass_min_days: 1

# The number of days warning given before a password expires.
shadow_utils_pass_warn_age: 31

# Range of user IDs used for the creation of regular users
shadow_utils_uid_min: 1000
shadow_utils_uid_max: 60000

# Range of user IDs used for the creation of system users
shadow_utils_sys_uid_min: 201
shadow_utils_sys_uid_max: 999

# Range of group IDs used for the creation of regular groups
shadow_utils_gid_min: 1000
shadow_utils_gid_max: 60000

# Range of group IDs used for the creation of system groups
shadow_utils_sys_gid_min: 201
shadow_utils_sys_gid_max: 999

# Maximum number of login retries in case of bad password.
# This will most likely be overridden by PAM, but can be a safe fallback.
shadow_utils_login_retries: 5

# Max time in seconds for login.
shadow_utils_login_timeout: 60

# Specify the gecos shields a users can change with chfn. 
# f - Full Name, r - Room Number, w - Work phone, h - Home phone
shadow_utils_chfn_restrict: 'rwh'

# Allow users to login if we can't cd to the home directory
shadow_utils_default_home: false

# Create new users home directory by default
shadow_utils_create_home: true

# If defined, this command is run when removing a user
shadow_utils_userdel_cmd: null

# Create default group for new users with the same name, and remove user's group if empty when user is deleted. 
shadow_utils_usergroups_enab: true

# Default encrpyition algorithm for encrypting passwords
shadow_utils_encrypt_method: 'SHA512'

```

Dependencies
------------

None

Example Playbook
----------------

```yaml
- hosts: servers
  tasks:
    - name: "Include shadow_utils"
      include_role:
        name: "shadow_utils"
```

License
-------

LGPLv3

Author Information
------------------

- Robert Brightling | [GitLab](https://gitlab.com/brightling) | [GitHub](https://github.com/rbrightling)
