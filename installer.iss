; Image Format Converter Installer Script
[Setup]
AppName=Image Format Converter
AppVersion=1.0.0
AppPublisher=ApsidD
AppPublisherURL=https://github.com/ApsidD/image-format-converter
DefaultDirName={autopf}\ImageFormatConverter
DefaultGroupName=Image Format Converter
OutputDir=dist
OutputBaseFilename=ImageFormatConverter-Setup
Compression=lzma2
SolidCompression=yes
SetupIconFile=assets\converter_icon_multi.ico
UninstallDisplayIcon={app}\ImageFormatConverter.exe
WizardStyle=modern
ArchitecturesInstallIn64BitMode=x64

[Files]
Source: "dist\ImageFormatConverter.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\Image Format Converter"; Filename: "{app}\ImageFormatConverter.exe"
Name: "{group}\Uninstall Image Format Converter"; Filename: "{uninstallexe}"
Name: "{autodesktop}\Image Format Converter"; Filename: "{app}\ImageFormatConverter.exe"; Tasks: desktopicon

[Tasks]
Name: "desktopicon"; Description: "Create a &desktop shortcut"; GroupDescription: "Additional icons:"

[Run]
Filename: "{app}\ImageFormatConverter.exe"; Description: "Launch Image Format Converter"; Flags: nowait postinstall skipifsilent

