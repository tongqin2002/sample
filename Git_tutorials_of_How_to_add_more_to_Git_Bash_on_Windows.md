# How to add more to Git Bash on Windows 

[Git for Windows](https://git-for-windows.github.io/) comes bundled with the "Git Bash" terminal which is incredibly handy for unix-like commands on a windows machine.
It is missing a few standard linux utilities, but it is easy to add ones that have a windows binary available.

The basic idea is that `C:\Program Files\Git\mingw64\` is your `/` directory according to Git Bash (*note:* depending on how you installed it, the directory might be different. from the start menu, right click on the Git Bash icon and open file location. It might be something like `C:\Users\name\AppData\Local\Programs\Git`, the `mingw64` in this directory is your root. Find it by using `pwd -W`).
If you go to that directory, you will find the typical linux root folder structure (`bin`, `etc`, `lib` and so on). 

If you are missing a utility, such as wget, track down a binary for windows and copy the files to the corresponding directories. 
Sometimes the windows binary have funny prefixes, so you should **rename** the `.exe` file to the standard name.
Since `bin` is on the PATH, it will be automatically available to Git Bash.

*Note:* Many interactive utilities, such as `python`, `ipython` or `nano`, will not display properly with Git Bash's mintty terminal. 
Try invoking them with `winpty` instead, for example `winpty ipython` will work nicely.
The Git-for-Windows team is focused on supporting Git, not a full UNIX shell environment.
If you are interested in more complete package with build tools, check my notes on [Cygwin](https://evanwill.github.io/_drafts/notes/cygwin.html) or [Cmder](https://evanwill.github.io/_drafts/notes/cmdr.html)--or install [Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/install-win10) or [WSL2](https://docs.microsoft.com/en-us/windows/wsl/wsl2-about).

Here are some utilities to add:

## Wget 

- Download the lastest wget binary for windows from [eternallybored](https://eternallybored.org/misc/wget/) (they are available as a zip with documentation, or just an exe)
- If you downloaded the zip, extract all (if windows built in zip utility gives an error, use [7-zip](http://www.7-zip.org/)).
- Rename the file `wget64.exe` to `wget.exe` if necessary. 
- Move `wget.exe` to your `Git\mingw64\bin\`.

*Note: I have noticed some bugs when using Wget on Git Bash to create WARC files. For more complex use of Wget, consider [Cygwin](https://evanwill.github.io/_drafts/notes/cygwin.html) instead.*

## Hugo 

[Hugo](http://gohugo.io/) static site generator can be downloaded as a binary and does not have a installer.
Dropping it into your `bin` easily adds it to your Git Bash path.
Grab the Windows 64-bit version from the [releases page](https://github.com/gohugoio/hugo/releases).
Unzip the download, then copy `hugo.exe` into your `Git\mingw64\bin` directory.

## Xpdf

[Xpdf](http://www.xpdfreader.com/index.html) is a handy utility for manipulating PDF files. 

- Download the [windows version "Xpdf tools"](http://www.xpdfreader.com/download.html).
- Extract zip.
- Copy the contents of `xpdf-tools-win-4.00\bin64\` into your `Git\mingw64\bin\`.
- Check the [docs](http://www.xpdfreader.com/support.html) to get started with tools such as `pdftotext` and `pdftopng`.

## ExifTool

- Download the "stand-alone Windows Executable" from the [ExifTool](https://exiftool.org/) page (this will be a `.zip` file e.g. "exiftool-11.99.zip").
- Unzip the downloaded file.
- Inside you will find a file named `exiftool(-k).exe`. Rename it to `exiftool.exe`.
- Move `exiftool.exe` to your `Git\mingw64\bin\`.

## Other possibilities

Most utilities that provide binary releases for Windows can be added to GitBash following the same pattern. 
Here are some more handy examples:

- [jq](https://github.com/stedolan/jq/releases)
- [htmlq](https://github.com/mgdm/htmlq/releases)

## make

> Keep in mind you can easy add `make`, but it doesn't come packaged with all the standard UNIX build toolchain--so you will have to ensure those are installed *and* on your PATH, or you will encounter endless error messages.

- Go to [ezwinports](https://sourceforge.net/projects/ezwinports/files/).
- Download `make-4.1-2-without-guile-w32-bin.zip` (get the version without guile).
- Extract zip.
- Copy the contents to your `Git\mingw64\` merging the folders, but do NOT overwrite/replace any existing files. 

## Nano

> As of 2018, recent versions of Git Bash include Nano, so this is unnecessary! Just be sure to choose Nano as your default editor when installing Git for Windows.

- Download the Nano binary from Nano [win32-support](https://www.nano-editor.org/dist/win32-support/) page. You just need the `.exe` file, which is named `nano-git-0d9a7347243.exe` (as of this writing).
- Rename the file to `nano.exe`, and copy to the `mingw64\bin` directory.
- This version of Nano will not work with Git Bash alone, but can be invoked using `winpty`, for example, `winpty nano test.txt`.
