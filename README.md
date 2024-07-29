# shaper-origin-inkscape
Inscape extension to add a Shaper Origin menu to set cut parameters

## Install

First you need to download a copy of the source code. If you're familiar with Git just clone to repo, otherwise click on the green Code menu, and pick Download Zip.

### MacOS

Copy the files in the ext directory to `~/Library/Application Support/org.inkscape.Inkscape/config/inkscape/extensions/`, e.g.

```shell
cp ext/* '~/Library/Application Support/org.inkscape.Inkscape/config/inkscape/extensions/'
```

### Linux / Windows / non-standard Mac installs

Look in the *Preferences | System | User extensions* menu and copy the files in `ext/` to there

## Usage

Create the shape you want to define the cut for, select it, then pick the type of cut from the menu:

![Extensions menu screenshot](docs/screenshot.png?raw=true)

Currently only dpeth in mm is supported, but adding inches would be easy.

By default Inkscape includes with drawn width of the line in the size of the object, which makes it harder to use for Shaper Origin users - you can turn that off - there's an example file in the top level of this repo, `1msq-master.svg`.

## Feedback

If you have any suggestions or feedback, please send them via github.

 - Steve Harris, 2023-11-06
