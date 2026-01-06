## Quick PowerShell vs Bash Reference for You

Since you're on Windows, here's a handy reference for future use:

| Task | Bash (Linux/Mac) | PowerShell (Windows) |
|------|------------------|----------------------|
| Create folder | `mkdir folder-name` | `New-Item -ItemType Directory -Path "folder-name"` or `mkdir folder-name` |
| Create file | `touch file.txt` | `New-Item -ItemType File -Path "file.txt"` |
| List files | `ls` | `Get-ChildItem` or `ls` (alias) |
| Change directory | `cd folder` | `cd folder` (same) |
| Show file content | `cat file.txt` | `Get-Content file.txt` or `cat file.txt` |
| Remove file | `rm file.txt` | `Remove-Item file.txt` or `rm file.txt` |

**Good news:** Many basic commands work the same or have aliases in PowerShell!
