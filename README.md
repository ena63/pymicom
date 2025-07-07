# pymicom
wrapper for MiCom.dll (Midi Ingenierie motor control modules protocol)

<img src="https://www.midi-ingenierie.com/wp-content/uploads/2021/02/cropped-logo_midi_ingenierie2021.png" alt="Logo Midi" style="width:25%;">

AppMiCom_v2025 permet d'appeler MiCom.dll depuis la ligne de commande Windows

*The provided code is for informational purposes only. We are not liable for any malfunctions or issues resulting from its use.*

## Additional resources

[Midi Ingenierie](https://www.midi-ingenierie.com)

[Pyperclip](https://pypi.org/project/pyperclip/))

## Typical usage

```python
import subprocess
import pyperclip

subprocess.run([AppMiCom_2025.exe,"BMAC","COM1","115200","00READ #POSITION"],shell=True)
print(pyperclip.paste())
