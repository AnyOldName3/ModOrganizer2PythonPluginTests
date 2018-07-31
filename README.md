# ModOrganizer2PythonPluginTests
A bunch of stub Python plugins for Mod Organizer 2 used for testing when improving the plugin interface.
They can be used for regression testing or as templates for creating new useful plugins.

## AGame.py
Implements IPluginGame (and also includes a class implementing the GamePlugins game feature).

This implements support for a made up game.
Support for non-GameBryo games is flakey in MO2 right now, so lots of things don't work sensibly.
Once better support is added to the rest of MO2, this is an example of how to add support for arbitrary new games.

## AModPage.py
Implements IPluginModPage.
Based closely on Tannin's TES Alliance mod page plugin.

This plugin interface was created with the intention of eventually moving the entire Nexus integration to a plugin, but it never got anywhere.
Don't expect even the little functionality this plugin interface offers to actually do anything.

## DiagnoseEmptyOverwrite.py
Implements IPluginDiagnose.

Adds a warning to MO's list if you have nothing in your overwrite directory.
This is actually a well-implemented and completely functional plugin, even if its premise is stupid.
It should serve as a solid basis for a range of other diagnosis plugins.

## DiagnoseEmptyOverwriteWithAModPage.py
Implements IPluginDiagnose and IPluginModPage.

This is a combination of DiagnoseEmptyOverwrite and AModPage into a single plugin.
It was created just to test the multiple inheritance system and no one should use it for anything else.

## XMLPreview.py
Implements IPluginPreview.

Allows XML files to be previewed just like other text files.
Doesn't do anything fancy like syntax highlighting, but works as a proof of concept.

## Unimplemented Interfaces
IPluginInstaller and its derivatives haven't been implemented.

IPluginFileMapper must have been implemented at some point, but I can't find the file where I did that, so I can't upload it. It's a really simple interface, though, so there isn't much to figure out when doing it yourself.

IPluginTool has a zillion other plugins implementing it already, so a simplified test plugin was never really needed.
