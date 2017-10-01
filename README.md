# ACT Paper Downloader

## Introduction

A self-made simple ACT past papers downloader.

Constructed in Python and packed with py2app to an Mac APP.

## Usage

### Mac Users

Run `ACTPaperDownloader.app` under the `dist/` directory as other macOS applications. 

The downloading process will run in the background without any GUI popups. The downloaded papers are located in your `~/Downloads` folder.

### General Users

Run the python script `ACTPaperDownloader.py`. 

You'll probably need to modify the downloading path in Line 72: 
`download_dir = os.path.expanduser('~/Downloads/ACT_Papers/')`
if you are using Windows.

## Notice
The downloading source is ACTMi but unfortunately the source will be shut down by OCT 10, 2017 so by that time the downloader will become deprecated.