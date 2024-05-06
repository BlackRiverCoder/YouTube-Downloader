# YouTube-Downloader
## Installation:
  - ***Git clone or just download the files:***
      ```
      sudo git clone https://github.com/BlackRiverCoder/YouTube-Downloader.git
      ```
      
  - ***Install requirements:***
      ```
      pip3 install -r requirements.txt
      ```
      **or**
      ```
      pip3 install yt-dlp colorama pathlib pyperclip -y
      ```
      
  - ***Install **FFMPEG**:***
    - [**Windows**](https://www.wikihow.com/Install-FFmpeg-on-Windows)
    - **Linux:**
      ```
      sudo apt-get update && sudo apt-get install -y ffmpeg
      ffmpeg -version
      ```

## Usage:
  - ***Main menu:***
    - **1.) Basic Setup - includes 3 basic options**
    - **2.) Advanced Setup - more extended menu than Basic Setup**
    - **3.) Skip to URL - uses default setting, which can be viewed using ***S*** option**
    ![](https://github.com/BlackRiverCoder/YouTube-Downloader/blob/master/Assets/Images/Main%20menu.png)

  - **Generated code for yt-dlp:**
    - **1.) Will close actual terminal, open another terminal and copy the generated code**
    - **2.) Will download the video without closing terminal**
    ![](https://github.com/BlackRiverCoder/YouTube-Downloader/blob/master/Assets/Images/Generated%20code.png)

## Update yt-dlp:
  > [!NOTE]
  > If yt-dlp was't installed using pip, update is automatic.
  - ***For Windows (if yt-dlp was installed using **pip**):***
    ```
    pip3 install --upgrade yt-dlp
    ```
