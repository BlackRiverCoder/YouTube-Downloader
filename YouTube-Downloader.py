#Import modules:
import yt_dlp
from colorama import Fore
import os
import sys
import time
import pathlib
import pyperclip
import subprocess

#Get user info:
user_name = os.getenv("USERNAME")

#Get main windows disk letter:
main_disk = pathlib.Path.home().drive

#Startup logo 1:
def startup_logo_1():
    print('          __                .___.__                                 .___      ')
    print(' ___.__._/  |_            __| _/|  | ______          ____  ____   __| _/____  ')
    print('<   |  |\   __\  ______  / __ | |  | \____ \       _/ ___\/  _ \ / __ |/ __ \ ')
    print(' \___  | |  |   /_____/ / /_/ | |  |_|  |_> >      \  \__(  <_> ) /_/ \  ___/ ')
    print(' / ____| |__|           \____ | |____/   __/        \___  >____/\____ |\___  >')
    print(' \/                          \/      |__|               \/           \/    \/ ')
    print('                                                  __                          ')
    print('          ____   ____   ____   ________________ _/  |_  ___________           ')
    print('         / ___\_/ __ \ /    \_/ __ \_  __ \__  \\   __\/  _ \_  __ \          ')
    print('        / /_/  >  ___/|   |  \  ___/|  | \// __ \|  | (  <_> )  | \/          ')
    print('        \___  / \___  >___|  /\___  >__|  (____  /__|  \____/|__|             ')
    print('       /_____/      \/     \/     \/           \/                             ')

#Startup logo 2:
def startup_logo_2():
    print('                      __       ___.                      .___                  .__                    .___            ')
    print(' ___.__. ____  __ ___/  |_ __ _\_ |__   ____           __| _/______  _  ______ |  |   _________     __| _/___________ ')
    print('<   |  |/  _ \|  |  \   __\  |  \ __ \_/ __ \         / __ |/  _ \ \/ \/ /    \|  |  /  _ \__  \   / __ |/ __ \_  __ \ ')
    print(' \___  (  <_> )  |  /|  | |  |  / \_\ \  ___/        / /_/ (  <_> )     /   |  \  |_(  <_> ) __ \_/ /_/ \  ___/|  | \/')
    print(' / ____|\____/|____/ |__| |____/|___  /\___  >       \____ |\____/ \/\_/|___|  /____/\____(____  /\____ |\___  >__|   ')
    print(' \/                                 \/     \/             \/                 \/                \/      \/    \/       ')
    print('                                                                                                                      ')
    print('  By BlackRiver8972')

#Startup loading:
def startup_loading():
    print('Loading:')
    print('▄')
    time.sleep(0.1)
    os.system('cls')

    print('Loading')
    print('▄ ▄')
    time.sleep(0.1)
    os.system('cls')

    print('Loading:')
    print('▄ ▄ ▄')
    time.sleep(0.1)
    os.system('cls')

    print('Loading:')
    print('▄ ▄ ▄ ▄')
    time.sleep(0.1)
    os.system('cls')

    print('Loading:')
    print('▄ ▄ ▄ ▄ ▄')
    time.sleep(0.1)
    os.system('cls')

    print('Loading:')
    print('▄ ▄ ▄ ▄ ▄ ▄')
    time.sleep(0.1)
    os.system('cls')

    print('Loading:')
    print('▄ ▄ ▄ ▄ ▄ ▄ ▄')
    time.sleep(0.1)
    os.system('cls')

    print('Loading:')
    print('▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄')
    time.sleep(0.1)
    os.system('cls')

    print('Loading:')
    print('▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄')
    time.sleep(0.1)
    os.system('cls')

    print('Loading:')
    print('▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄')
    time.sleep(0.1)
    os.system('cls')

    print('Loading:')
    print('▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄')
    time.sleep(0.1)
    os.system('cls')

    print('Loading:')
    print('▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄')
    time.sleep(0.1)
    os.system('cls')

    print('Loading:')
    print('▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄')
    time.sleep(0.1)
    os.system('cls')

    print('Loading:')
    print('▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄')
    time.sleep(0.1)
    os.system('cls')

    print('Loading:')
    print('▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄')
    time.sleep(0.1)
    os.system('cls')

    print('Loading:')
    print('▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄')
    time.sleep(0.1)
    os.system('cls')

    print('Loading:')
    print('▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄')
    time.sleep(0.1)
    os.system('cls')

    print('Loading:')
    print('▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄')
    time.sleep(0.1)
    os.system('cls')

    print('Loading:')
    print('▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄')
    time.sleep(0.1)
    os.system('cls')

    print('Loading:')
    print('▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄ ▄')
    time.sleep(0.1)
    os.system('cls')

    print(Fore.GREEN + 'LOADED SUCCESSFULY')
    print(Fore.RESET)
    time.sleep(0.5)
    os.system('cls')

#Startup loading full:
os.system('cls')
startup_loading()

startup_logo_1()
time.sleep(1)
os.system('cls')

startup_logo_2()
time.sleep(2)
os.system('cls')


#Default settings:
update_yt_dlp = '-U '
abort_on_error = '--abort-on-error '
playlist = '--no-playlist '
restrict_filenames = '--no-restrict-filenames '
windows_filenames = '--no-windows-filenames '
format = '-f "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best" '
time_date = '--no-mtime '
destination_folder = '-o "' + main_disk + '/Users/' + user_name + '/Downloads\%(title)s" '

#option - basic setup or advandced setup:
print('Setup option:')
print(Fore.CYAN + ' 1.) Basic Setup')
print(Fore.CYAN + ' 2.) Advanced setup')
print(Fore.CYAN + ' 3.) Skip to URL (default settings will be used)')
print(Fore.CYAN + '                 (use "S" to show default settings)')
print(Fore.RED + ' e.) Exit')

option_basic_advanced_setup = input(Fore.LIGHTYELLOW_EX + 'Your option: ' + Fore.RESET)


#1.) Basic Setup:
if option_basic_advanced_setup == '1':
    #File format:
    os.system('cls')
    print(Fore.LIGHTBLUE_EX + 'Basic Setup - File format:')
    print(Fore.CYAN + ' 1.) Video (mp4)')
    print(Fore.CYAN + ' 2.) Audio (mp3)')
    print('')
    print(Fore.RED + ' e.) Exit')

    option_basic_file_format = input(Fore.LIGHTYELLOW_EX + 'Your option: ' + Fore.RESET)

    if option_basic_file_format == '1':
        format = '-f "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best" '

    elif option_basic_file_format == '2':
        format = '-x --audio-format mp3 '

    elif option_basic_file_format == 'e' or option_basic_file_format == 'E':
        os.system('cls')
        print('Thanks for using tool: Yt-Dlp Downloader')
        time.sleep(1)
        sys.exit()

    else:
        format = '-f "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best" '
        os.system('cls')
        print(Fore.RED + 'Undefined input. Using default format (mp4).')
        time.sleep(1)


    #Destination folder:
    os.system('cls')
    print(Fore.LIGHTBLUE_EX + 'Basic Setup - Destination folder:')
    print(Fore.CYAN + ' 1.) Downloads')
    print(Fore.CYAN + ' 2.) Documents')
    print(Fore.CYAN + ' 3.) Desktop')
    print(Fore.CYAN + ' 4.) Videos')
    print(Fore.CYAN + ' 5.) Music')
    print('')
    print(Fore.RED + ' e.) Exit')

    option_basic_destination_folder = input(Fore.LIGHTYELLOW_EX + 'Your option: ' + Fore.RESET)

    if option_basic_destination_folder == '1':
        destination_folder = '-o "' + main_disk + '/Users/' + user_name + '/Downloads\%(title)s" '

    elif option_basic_destination_folder == '2':
        destination_folder = '-o "' + main_disk + '/Users/' + user_name + '/Documents\%(title)s" '

    elif option_basic_destination_folder == '3':
        destination_folder = '-o "' + main_disk + '/Users/' + user_name + '/Desktop\%(title)s" '

    elif option_basic_destination_folder == '4':
        destination_folder = '-o "' + main_disk + '/Users/' + user_name + '/Videos\%(title)s" '

    elif option_basic_destination_folder == '5':
        destination_folder = '-o "' + main_disk + '/Users/' + user_name + '/Music\%(title)s" '

    elif option_basic_destination_folder == 'e' or option_basic_destination_folder == 'E':
        os.system('cls')
        print('Thanks for using tool: Yt-Dlp Downloader')
        time.sleep(1)
        sys.exit()

    else:
        destination_folder = '-o "' + main_disk + '/Users/' + user_name + '/Downloads\%(title)s" '
        os.system('cls')
        print(Fore.RED + 'Undefined input. Using default destination (Downloads).')
        time.sleep(1)

    
    #Playlist:
    os.system('cls')
    print(Fore.LIGHTBLUE_EX + 'Basic Setup - Playlist:')
    print(Fore.CYAN + ' 1.) Download only selected video from playlist')
    print(Fore.CYAN + ' 2.) Download full playlist')
    print('')
    print(Fore.RED + ' e.) Exit')

    option_basic_playlist = input(Fore.LIGHTYELLOW_EX + 'Your option: ' + Fore.RESET)

    if option_basic_playlist == '1':
        playlist = '--no-playlist '

    elif option_basic_playlist == '2':
        playlist = '--yes-playlist '

    elif option_basic_playlist == 'e' or option_basic_playlist == 'E':
        os.system('cls')
        print('Thanks for using tool: Yt-Dlp Downloader')
        time.sleep(1)
        sys.exit()

    else:
        playlist = '--no-playlist '
        os.system('cls')
        print(Fore.RED + 'Undefined input. Using default playlist option (1).')
        time.sleep(1)


    #Final Step - URL link:
    os.system('cls')
    video_url = input(Fore.LIGHTYELLOW_EX + 'YouTube URL: ' + Fore.RESET)
    os.system('cls')

    print(Fore.GREEN + 'CODE GENERATED:' + Fore.RESET)
    print('')
    print(Fore.LIGHTMAGENTA_EX + 'yt-dlp ' + update_yt_dlp + abort_on_error + playlist + restrict_filenames + windows_filenames + time_date + format + destination_folder + video_url)
    final_basic_code = ('yt-dlp ' + update_yt_dlp + abort_on_error + playlist + restrict_filenames + windows_filenames + time_date + format + destination_folder + video_url)

    print('')
    print(Fore.CYAN + ' 1.) Open new terminal and copy the generated code')
    print(Fore.CYAN + ' 2.) Download right now')
    basic_decision_code = input(Fore.LIGHTYELLOW_EX + 'Your option: ' + Fore.RESET)

    if basic_decision_code == '1':
        pyperclip.copy(final_basic_code)
        subprocess.Popen('start')

    elif basic_decision_code == '2':
        os.system('cls')
        os.system(final_basic_code)

    else:
        os.system('cls')
        print(Fore.RED + 'Undefined input. Using default option (2).')
        time.sleep(1)
        os.system('cls')
        os.system(final_basic_code)



#2.) Advanced setup:
elif option_basic_advanced_setup == '2':
    #Update:
    os.system('cls')
    print(Fore.LIGHTBLUE_EX + 'Advanced Setup - Perform yt-dlp update?:')
    print(Fore.CYAN + ' 1.) Yes')
    print(Fore.CYAN + ' 2.) No')
    print('')
    print(Fore.RED + ' e.) Exit')

    option_advanced_update = input(Fore.LIGHTYELLOW_EX + 'Your option: ' + Fore.RESET)

    if option_advanced_update == '1':
        update_yt_dlp = '-U '
        update_yt_dlp_summary = 'Update turned on'

    elif option_advanced_update == '2':
        update_yt_dlp = '--no-update '
        update_yt_dlp_summary = 'Update turned off'

    elif option_advanced_update == 'e' or option_advanced_update == 'E':
        os.system('cls')
        print('Thanks for using tool: Yt-Dlp Downloader')
        time.sleep(1)
        sys.exit()

    else:
        update_yt_dlp = '-U '
        update_yt_dlp_summary = 'Update turned on'
        os.system('cls')
        print(Fore.RED + 'Undefined input. Using default update option (Yes).')
        time.sleep(1)

    
    #Keep intermediate video:
    os.system('cls')
    print(Fore.LIGHTBLUE_EX + 'Advanced Setup - Keep intermediate video?:')
    print(Fore.CYAN + ' 1.) Yes')
    print(Fore.CYAN + ' 2.) No')
    print('')
    print(Fore.RED + ' e.) Exit')

    option_advanced_keep_intermediate_video = input(Fore.LIGHTYELLOW_EX + 'Your option: ' + Fore.RESET)

    if option_advanced_keep_intermediate_video == '1':
        keep_intermediate_video = '-k '
        keep_intermediate_video_summary = 'Keep intermediate video'

    elif option_advanced_keep_intermediate_video == '2':
        keep_intermediate_video = '--no-keep-video '
        keep_intermediate_video_summary = "Don't keep intermediate video"

    elif option_advanced_keep_intermediate_video == 'e' or option_advanced_keep_intermediate_video == 'E':
        os.system('cls')
        print('Thanks for using tool: Yt-Dlp Downloader')
        time.sleep(1)
        sys.exit()

    else:
        keep_intermediate_video = '--no-keep-video '
        keep_intermediate_video_summary = "Don't keep intermediate video"
        os.system('cls')
        print(Fore.RED + 'Undefined input. Using default option (No).')
        time.sleep(1)

    
    #Ignore errors:
    os.system('cls')
    print(Fore.LIGHTBLUE_EX + 'Advanced Setup - Ignore errors?:')
    print(Fore.CYAN + ' 1.) Yes')
    print(Fore.CYAN + ' 2.) No')
    print('')
    print(Fore.RED + ' e.) Exit')

    option_advanced_ignore_errors = input(Fore.LIGHTYELLOW_EX + 'Your option: ' + Fore.RESET)

    if option_advanced_ignore_errors == '1':
        ignore_errors = '-i '
        ignore_errors_summary = 'Ignore errors'

    elif option_advanced_ignore_errors == '2':
        ignore_errors = '--no-ignore-errors '
        ignore_errors_summary = "Don't ignore errors"

    elif option_advanced_ignore_errors == 'e' or option_advanced_ignore_errors == 'E':
        os.system('cls')
        print('Thanks for using tool: Yt-Dlp Downloader')
        time.sleep(1)
        sys.exit()

    else:
        ignore_errors = '--no-ignore-errors '
        ignore_errors_summary = "Don't ignore errors"
        os.system('cls')
        print(Fore.RED + 'Undefined input. Using default option (No).')
        time.sleep(1)


    #Abort on error:
    os.system('cls')
    print(Fore.LIGHTBLUE_EX + 'Advanced Setup - Abort on error?:')
    print(Fore.CYAN + ' 1.) Yes')
    print(Fore.CYAN + ' 2.) No')
    print('')
    print(Fore.RED + ' e.) Exit')

    option_advanced_abort_on_error = input(Fore.LIGHTYELLOW_EX + 'Your option: ' + Fore.RESET)

    if option_advanced_abort_on_error == '1':
        abort_on_error = '--abort-on-error '
        abort_on_error_summary = 'Abort on error'

    elif option_advanced_abort_on_error == '2':
        abort_on_error == '--no-abort-on-error '
        abort_on_error_summary = "Don't abort on error"

    elif option_advanced_abort_on_error == 'e' or option_advanced_abort_on_error == 'E':
        os.system('cls')
        print('Thanks for using tool: Yt-Dlp Downloader')
        time.sleep(1)
        sys.exit()

    else:
        abort_on_error = '--abort-on-error '
        abort_on_error_summary = 'Abort on error'
        os.system('cls')
        print(Fore.RED + 'Undefined input. Using default option (Yes).')
        time.sleep(1)


    #Playlist:
    os.system('cls')
    print(Fore.LIGHTBLUE_EX + 'Advanced Setup - Playlist:')
    print(Fore.CYAN + ' 1.) Download only selected video from playlist')
    print(Fore.CYAN + ' 2.) Download full playlist')
    print('')
    print(Fore.RED + ' e.) Exit')

    option_advanced_playlist = input(Fore.LIGHTYELLOW_EX + 'Your option: ' + Fore.RESET)

    if option_advanced_playlist == '1':
        playlist = '--no-playlist '
        playlist_summary = 'Download only one video from playlist'

    elif option_advanced_playlist == '2':
        playlist = '--yes-playlist '
        playlist_summary = 'Download full playlist'

    elif option_advanced_playlist == 'e' or option_advanced_playlist == 'E':
        os.system('cls')
        print('Thanks for using tool: Yt-Dlp Downloader')
        time.sleep(1)
        sys.exit()

    else:
        playlist = '--no-playlist '
        playlist_summary = 'Download only video form playlist'
        os.system('cls')
        print(Fore.RED + 'Undefined input. Using default playlist option (1).')
        time.sleep(1)


    #Restrict filenames:
    os.system('cls')
    print(Fore.LIGHTBLUE_EX + 'Advanced Setup - Restrict filenames:')
    print(Fore.CYAN + ' 1.) Restrict filenames only to ASCII characters')
    print(Fore.CYAN + ' 2.) Allow unicode characters')
    print('')
    print(Fore.RED + ' e.) Exit')

    option_advanced_restrict_filenames = input(Fore.LIGHTYELLOW_EX + 'Your option: ' + Fore.RESET)

    if option_advanced_restrict_filenames == '1':
        restrict_filenames = '--restrict-filenames '
        restrict_filenames_summary = 'Restrict filenames only to ASCII characters'

    elif option_advanced_restrict_filenames == '2':
        restrict_filenames = '--no-restrict-filenames '
        restrict_filenames_summary = 'Allow unicode characters'
    
    elif option_advanced_restrict_filenames == 'e' or option_advanced_restrict_filenames == 'E':
        os.system('cls')
        print('Thanks for using tool: Yt-Dlp Downloader')
        time.sleep(1)
        sys.exit()

    else:
        restrict_filenames = '--no-restrict-filenames '
        restrict_filenames_summary = 'Allow unicode characters'
        os.system('cls')
        print(Fore.RED + 'Undefined input. Using default restrict option (2).')
        time.sleep(1)


    #Windows filenames:
    os.system('cls')
    print(Fore.LIGHTBLUE_EX + 'Advanced Setup - Windows filenames:')
    print(Fore.CYAN + ' 1.) Force filenames to be Windows-compatible')
    print(Fore.CYAN + ' 2.) Make filenames Windows-compatible only if using Windows')
    print('')
    print(Fore.RED + ' e.) Exit')

    option_advanced_windows_filenames = input(Fore.LIGHTYELLOW_EX + 'Your option: ' + Fore.RESET)

    if option_advanced_windows_filenames == '1':
        windows_filenames = '--windows-filenames '
        windows_filenames_summary = 'Force filenames to be Windows-compatible'

    elif option_advanced_windows_filenames == '2':
        windows_filenames = '--no-windows-filenames '
        windows_filenames_summary = 'Make filenames Windows-compatible only if using Windows'

    elif option_advanced_windows_filenames == 'e' or option_advanced_windows_filenames == 'E':
        os.system('cls')
        print('Thanks for using tool: Yt-Dlp Downloader')
        time.sleep(1)
        sys.exit()

    else:
        windows_filenames = '--no-windows-filenames '
        windows_filenames_summary = 'Make filenames Windows-compatible only if using Windows'
        os.system('cls')
        print(Fore.RED + 'Undefined input. Using default restrict option (2).')
        time.sleep(1)


    #Time and date:
    os.system('cls')
    print(Fore.LIGHTBLUE_EX + 'Advanced Setup - Time and date:')
    print(Fore.CYAN + ' 1.) Use the Last-modified header to set file time')
    print(Fore.CYAN + " 2.) Use today's time")
    print('')
    print(Fore.RED + ' e.) Exit')

    option_advanced_time_date = input(Fore.LIGHTYELLOW_EX + 'Your option: ' + Fore.RESET)

    if option_advanced_time_date == '1':
        time_date = '--mtime '
        time_date_summary = 'Use the Last-modified header to set file time'

    elif option_advanced_time_date == '2':
        time_date = '--no-mtime '
        time_date_summary = "Use today's time"

    elif option_advanced_time_date == 'e' or option_advanced_time_date == 'E':
        os.system('cls')
        print('Thanks for using tool: Yt-Dlp Downloader')
        time.sleep(1)
        sys.exit()

    else:
        time_date = '--no-mtime '
        time_date_summary = "Use today's time"
        os.system('cls')
        print(Fore.RED + 'Undefined input. Using default time option (2).')
        time.sleep(1)


    #Description file:
    os.system('cls')
    print(Fore.LIGHTBLUE_EX + 'Advanced Setup - Description file:')
    print(Fore.CYAN + ' 1.) Write description file')
    print(Fore.CYAN + " 2.) Don't write description file")
    print('')
    print(Fore.RED + ' e.) Exit')

    option_advanced_description_file = input(Fore.LIGHTYELLOW_EX + 'Your option: ' + Fore.RESET)

    if option_advanced_description_file == '1':
        description_file = '--write-description '
        description_file_summary = 'Write description file'

    elif option_advanced_description_file == '2':
        description_file = '--no-write-description '
        description_file_summary = "Don't write description file"

    elif option_advanced_description_file == 'e' or option_advanced_description_file == 'E':
        os.system('cls')
        print('Thanks for using tool: Yt-Dlp Downloader')
        time.sleep(1)
        sys.exit()

    else:
        description_file = '--no-write-description '
        description_file_summary = "Don't write description file"
        os.system('cls')
        print(Fore.RED + 'Undefined input. Using default description option (2).')
        time.sleep(1)


    #Automatic subtitles:
    os.system('cls')
    print(Fore.LIGHTBLUE_EX + 'Advanced Setup - Automatic subtitles:')
    print(Fore.CYAN + ' 1.) Auto generate subtitles (default english)')
    print(Fore.CYAN + " 2.) Don't write subtitles")
    print('')
    print(Fore.RED + ' e.) Exit')

    option_advanced_auto_subtitles = input(Fore.LIGHTYELLOW_EX + 'Your option: ' + Fore.RESET)

    if option_advanced_auto_subtitles == '1':
        auto_subtitles = '--write-auto-subs '
        auto_subtitles_summary = 'Auto generate subtitles'

    elif option_advanced_auto_subtitles == '2':
        auto_subtitles = '--no-write-auto-subs '
        auto_subtitles_summary = "Don't generate subtitles"

    elif option_advanced_auto_subtitles == 'e' or option_advanced_auto_subtitles == 'E':
        os.system('cls')
        print('Thanks for using tool: Yt-Dlp Downloader')
        time.sleep(1)
        sys.exit()

    else:
        auto_subtitles = '--no-write-auto-subs '
        auto_subtitles_summary = "Don't generate subtitles"
        os.system('cls')
        print(Fore.RED + 'Undefined input. Using default subtitles option (2).')
        time.sleep(1)


    #Use credentials:
    os.system('cls')
    print(Fore.LIGHTBLUE_EX + 'Advanced Setup - Use credentials for content 18+?:')
    print(Fore.CYAN + ' 1.) Yes')
    print(Fore.CYAN + " 2.) No")
    print('')
    print(Fore.RED + ' e.) Exit')

    option_advanced_use_credentials = input(Fore.LIGHTYELLOW_EX + 'Your option: ' + Fore.RESET)

    if option_advanced_use_credentials == '1':
        os.system('cls')
        username = input(Fore.RED + 'Input your account ID: ')
        password = input(Fore.RED + 'Input your password: ')
        use_credentials = '--username ' + username + '--password ' + password
        use_credentials_summary = 'Use credentials'

    elif option_advanced_use_credentials == '2':
        pass
        use_credentials_summary = "Don't use credentials"

    elif option_advanced_use_credentials == 'e' or option_advanced_use_credentials == 'E':
        os.system('cls')
        print('Thanks for using tool: Yt-Dlp Downloader')
        time.sleep(1)
        sys.exit()

    else:
        use_credentials_summary = "Don't use credentials"
        os.system('cls')
        print(Fore.RED + 'Undefined input. Using default credentials option (No).')
        time.sleep(1)

    
    #File format:
    os.system('cls')
    print(Fore.LIGHTBLUE_EX + 'Advanced Setup - File format:')
    print(Fore.CYAN + ' 1.) Video (mp4)')
    print(Fore.CYAN + ' 2.) Audio (mp3)')
    print('')
    print(Fore.RED + ' e.) Exit')

    option_basic_file_format = input(Fore.LIGHTYELLOW_EX + 'Your option: ' + Fore.RESET)

    if option_basic_file_format == '1':
        format = '-f "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best" '
        format_summary = 'Format mp4'

    elif option_basic_file_format == '2':
        format = '-x --audio-format mp3 '
        format_summary = 'Format mp3'

    elif option_basic_file_format == 'e' or option_basic_file_format == 'E':
        os.system('cls')
        print('Thanks for using tool: Yt-Dlp Downloader')
        time.sleep(1)
        sys.exit()

    else:
        format = '-f "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best" '
        format_summary = 'Format mp4'
        os.system('cls')
        print(Fore.RED + 'Undefined input. Using default format (mp4).')
        time.sleep(1)


    #Destination folder:
    os.system('cls')
    print(Fore.LIGHTBLUE_EX + 'Advanced Setup - Destination folder:')
    print(Fore.CYAN + ' 1.) Downloads')
    print(Fore.CYAN + ' 2.) Documents')
    print(Fore.CYAN + ' 3.) Desktop')
    print(Fore.CYAN + ' 4.) Videos')
    print(Fore.CYAN + ' 5.) Music')
    print('')
    print(Fore.RED + ' e.) Exit')

    option_basic_destination_folder = input(Fore.LIGHTYELLOW_EX + 'Your option: ' + Fore.RESET)

    if option_basic_destination_folder == '1':
        destination_folder = '-o "' + main_disk + '/Users/' + user_name + '/Downloads\%(title)s" '
        destination_folder_summary = 'Destination folder - Downloads'

    elif option_basic_destination_folder == '2':
        destination_folder = '-o "' + main_disk + '/Users/' + user_name + '/Documents\%(title)s" '
        description_file_summary = 'Destination folder - Documents'

    elif option_basic_destination_folder == '3':
        destination_folder = '-o "' + main_disk + '/Users/' + user_name + '/Desktop\%(title)s" '
        destination_folder_summary = 'Destination folder - Desktop'

    elif option_basic_destination_folder == '4':
        destination_folder = '-o "' + main_disk + '/Users/' + user_name + '/Videos\%(title)s" '
        destination_folder_summary = 'Destination folder - Videos'

    elif option_basic_destination_folder == '5':
        destination_folder = '-o "' + main_disk + '/Users/' + user_name + '/Music\%(title)s" '
        destination_folder_summary = 'Destination folder - Music'

    elif option_basic_destination_folder == 'e' or option_basic_destination_folder == 'E':
        os.system('cls')
        print('Thanks for using tool: Yt-Dlp Downloader')
        time.sleep(1)
        sys.exit()

    else:
        destination_folder = '-o "' + main_disk + '/Users/' + user_name + '/Downloads\%(title)s" '
        destination_folder_summary = 'Destination folder - Downloads'
        os.system('cls')
        print(Fore.RED + 'Undefined input. Using default destination (Downloads).')
        time.sleep(1)


    #Summarry:
    os.system('cls')
    print(Fore.LIGHTGREEN_EX + 'Summary:')
    print('')
    print(Fore.LIGHTMAGENTA_EX + ' - ' + update_yt_dlp_summary)
    print(Fore.LIGHTMAGENTA_EX + ' - ' + keep_intermediate_video_summary)
    print(Fore.LIGHTMAGENTA_EX + ' - ' + ignore_errors_summary)
    print(Fore.LIGHTMAGENTA_EX + ' - ' + abort_on_error_summary)
    print(Fore.LIGHTMAGENTA_EX + ' - ' + playlist_summary)
    print(Fore.LIGHTMAGENTA_EX + ' - ' + restrict_filenames_summary)
    print(Fore.LIGHTMAGENTA_EX + ' - ' + windows_filenames_summary)
    print(Fore.LIGHTMAGENTA_EX + ' - ' + time_date_summary)
    print(Fore.LIGHTMAGENTA_EX + ' - ' + description_file_summary)
    print(Fore.LIGHTMAGENTA_EX + ' - ' + auto_subtitles_summary)
    print(Fore.LIGHTMAGENTA_EX + ' - ' + use_credentials_summary)
    print(Fore.LIGHTMAGENTA_EX + ' - ' + format_summary)
    print(Fore.LIGHTMAGENTA_EX + ' - ' + destination_folder_summary)
    print('')
    input(Fore.RESET + 'ENTER to continue...')


    #Final Step - URL link:
    os.system('cls')
    video_url = input(Fore.LIGHTYELLOW_EX + 'YouTube URL: ' + Fore.RESET)
    os.system('cls')

    print(Fore.GREEN + 'CODE GENERATED:' + Fore.RESET)
    print('')
    if option_advanced_use_credentials == '1':
        print(Fore.LIGHTMAGENTA_EX + 'yt-dlp ' + update_yt_dlp + keep_intermediate_video + ignore_errors + abort_on_error + playlist + restrict_filenames + windows_filenames + time_date + description_file + auto_subtitles + use_credentials + format + destination_folder + video_url)  
        final_advanced_code = ('yt-dlp ' + update_yt_dlp + keep_intermediate_video + ignore_errors + abort_on_error + playlist + restrict_filenames + windows_filenames + time_date + description_file + auto_subtitles + use_credentials + format + destination_folder + video_url)
    elif option_advanced_use_credentials == '2':
        print(Fore.LIGHTMAGENTA_EX + 'yt-dlp ' + update_yt_dlp + keep_intermediate_video + ignore_errors + abort_on_error + playlist + restrict_filenames + windows_filenames + time_date + description_file + auto_subtitles + format + destination_folder + video_url)  
        final_advanced_code = ('yt-dlp ' + update_yt_dlp + keep_intermediate_video + ignore_errors + abort_on_error + playlist + restrict_filenames + windows_filenames + time_date + description_file + auto_subtitles + format + destination_folder + video_url)

    else:
        print(Fore.LIGHTMAGENTA_EX + 'yt-dlp ' + update_yt_dlp + keep_intermediate_video + ignore_errors + abort_on_error + playlist + restrict_filenames + windows_filenames + time_date + description_file + auto_subtitles + format + destination_folder + video_url)  
        final_advanced_code = ('yt-dlp ' + update_yt_dlp + keep_intermediate_video + ignore_errors + abort_on_error + playlist + restrict_filenames + windows_filenames + time_date + description_file + auto_subtitles + format + destination_folder + video_url)

    print('')
    print(Fore.CYAN + ' 1.) Open new terminal and copy the generated code')
    print(Fore.CYAN + ' 2.) Download right now')
    advanced_decision_code = input(Fore.LIGHTYELLOW_EX + 'Your option: ' + Fore.RESET)

    if advanced_decision_code == '1':
        pyperclip.copy(final_advanced_code)
        subprocess.Popen('start')

    elif advanced_decision_code == '2':
        os.system('cls')
        os.system(final_advanced_code)

    else:
        os.system('cls')
        print(Fore.RED + 'Undefined input. Using default option (2).')
        time.sleep(1)
        os.system('cls')
        os.system(final_advanced_code)



#Skip to URL (default settings will be used)
elif option_basic_advanced_setup == '3':
    #Final Step - URL link:
    os.system('cls')
    video_url = input(Fore.LIGHTYELLOW_EX + 'YouTube URL: ' + Fore.RESET)
    os.system('cls')

    print(Fore.GREEN + 'CODE GENERATED:' + Fore.RESET)
    print('')
    print(Fore.LIGHTMAGENTA_EX + 'yt-dlp ' + update_yt_dlp + abort_on_error + playlist + restrict_filenames + windows_filenames + format + time_date + destination_folder + video_url)  
    final_default_code = ('yt-dlp ' + update_yt_dlp + abort_on_error + playlist + restrict_filenames + windows_filenames + format + time_date + destination_folder + video_url)

    print('')
    print(Fore.CYAN + ' 1.) Open new terminal and copy the generated code')
    print(Fore.CYAN + ' 2.) Download right now')
    default_decision_code = input(Fore.LIGHTYELLOW_EX + 'Your option: ' + Fore.RESET)

    if default_decision_code == '1':
        pyperclip.copy(final_default_code)
        subprocess.Popen('start')

    elif default_decision_code == '2':
        os.system('cls')
        os.system(final_default_code)

    else:
        os.system('cls')
        print(Fore.RED + 'Undefined input. Using default option (2).')
        time.sleep(1)
        os.system('cls')
        os.system(final_default_code)



#s.) See default options:
elif option_basic_advanced_setup == 's' or option_basic_advanced_setup == 'S':
    os.system('cls')
    print(Fore.LIGHTGREEN_EX + 'Default options:')
    print('')
    print(Fore.LIGHTMAGENTA_EX + ' - Update turned on')
    print(Fore.LIGHTMAGENTA_EX + ' - Abort on error')
    print(Fore.LIGHTMAGENTA_EX + ' - Download only one video from playlist')
    print(Fore.LIGHTMAGENTA_EX + ' - Make filenames Windows-compatible only if using Windows')
    print(Fore.LIGHTMAGENTA_EX + ' - Format mp4')
    print(Fore.LIGHTMAGENTA_EX + " - Use today's date")
    print(Fore.LIGHTMAGENTA_EX + ' - Destination folder - Downloads')
    print('')
    input(Fore.RESET + 'ENTER to continue...')

    os.system('cls')
    print('Download video?:')
    print(Fore.CYAN + ' 1.) Yes (using default settings)')
    print(Fore.CYAN + ' 2.) No')
    print('')
    print(Fore.RED + ' e.) Exit')
    
    option_default_yes_no = input(Fore.LIGHTYELLOW_EX + 'Your option: ' + Fore.RESET)

    if option_default_yes_no == '1':
        os.system('cls')
        video_url = input(Fore.LIGHTYELLOW_EX + 'YouTube URL: ' + Fore.RESET)
        os.system('cls')

        print(Fore.GREEN + 'CODE GENERATED:' + Fore.RESET)
        print('')
        print(Fore.LIGHTMAGENTA_EX + 'yt-dlp ' + update_yt_dlp + abort_on_error + playlist + restrict_filenames + windows_filenames + format + time_date + destination_folder + video_url)  
        final_default_code = ('yt-dlp ' + update_yt_dlp + abort_on_error + playlist + restrict_filenames + windows_filenames + format + time_date + destination_folder + video_url)

        print('')
        print(Fore.CYAN + ' 1.) Open new terminal and copy the generated code')
        print(Fore.CYAN + ' 2.) Download right now')
        default_decision_code = input(Fore.LIGHTYELLOW_EX + 'Your option: ' + Fore.RESET)

        if default_decision_code == '1':
            pyperclip.copy(final_default_code)
            subprocess.Popen('start')

        elif default_decision_code == '2':
            os.system('cls')
            os.system(final_default_code)

        else:
            os.system('cls')
            print(Fore.RED + 'Undefined input. Using default option (2).')
            time.sleep(1)
            os.system('cls')
            os.system(final_default_code)


    elif option_default_yes_no == '2':
        print('Thanks for using tool: Yt-Dlp Downloader')
        time.sleep(2)

    elif option_default_yes_no == 'e' or option_default_yes_no == 'E':
        print('Thanks for using tool: Yt-Dlp Downloader')
        time.sleep(2)

    else:
        os.system('cls')
        print(Fore.RED + 'Undefined input. Using default option (Yes).')
        time.sleep(1)
        os.system('cls')
        video_url = input(Fore.LIGHTYELLOW_EX + 'YouTube URL: ' + Fore.RESET)
        os.system('cls')

        print(Fore.GREEN + 'CODE GENERATED:' + Fore.RESET)
        print('')
        print(Fore.LIGHTMAGENTA_EX + 'yt-dlp ' + update_yt_dlp + abort_on_error + playlist + restrict_filenames + windows_filenames + format + time_date + destination_folder + video_url)  
        final_default_code = ('yt-dlp ' + update_yt_dlp + abort_on_error + playlist + restrict_filenames + windows_filenames + format + time_date + destination_folder + video_url)

        print('')
        print(Fore.CYAN + ' 1.) Open new terminal and copy the generated code')
        print(Fore.CYAN + ' 2.) Download right now')
        default_decision_code = input(Fore.LIGHTYELLOW_EX + 'Your option: ' + Fore.RESET)

        if default_decision_code == '1':
            pyperclip.copy(final_default_code)
            subprocess.Popen('start')

        elif default_decision_code == '2':
            os.system('cls')
            os.system(final_default_code)

        else:
            os.system('cls')
            print(Fore.RED + 'Undefined input. Using default option (2).')
            time.sleep(1)
            os.system('cls')
            os.system(final_default_code)



#Exit
elif option_basic_advanced_setup == 'e' or option_basic_advanced_setup == 'E':
    os.system('cls')
    print('Thanks for using tool: Yt-Dlp Downloader')
    time.sleep(2)



#Else:
else:
    os.system('cls')
    print(Fore.RED + 'Undefined input. Using default option (Skip to URL (Using default settings)).')
    time.sleep(2)
    os.system('cls')

    #Final Step - URL link:
    os.system('cls')
    video_url = input(Fore.LIGHTYELLOW_EX + 'YouTube URL: ' + Fore.RESET)
    os.system('cls')

    print(Fore.GREEN + 'CODE GENERATED:' + Fore.RESET)
    print('')
    print(Fore.LIGHTMAGENTA_EX + 'yt-dlp ' + update_yt_dlp + abort_on_error + playlist + restrict_filenames + windows_filenames + format + time_date + destination_folder + video_url)  
    final_default_code = ('yt-dlp ' + update_yt_dlp + abort_on_error + playlist + restrict_filenames + windows_filenames + format + time_date + destination_folder + video_url)

    print('')
    print(Fore.CYAN + ' 1.) Open new terminal and copy the generated code')
    print(Fore.CYAN + ' 2.) Download right now')
    default_decision_code = input(Fore.LIGHTYELLOW_EX + 'Your option: ' + Fore.RESET)

    if default_decision_code == '1':
        pyperclip.copy(final_default_code)
        subprocess.Popen('start')

    elif default_decision_code == '2':
        os.system('cls')
        os.system(final_default_code)

    else:
        os.system('cls')
        print(Fore.RED + 'Undefined input. Using default option (2).')
        time.sleep(1)
        os.system('cls')
        os.system(final_default_code)