# Installation
`sh -c "$(curl -fsLS chezmoi.io/get)" -- init --apply luigibarbato`

# Usage
I implemented a super easy script named `dots-sync` that tracks my dotfiles, encrypting the information that I consider sensitive with my primary gpg key. You can find it in `~/.local/bin/dots-sync`. This script is triggered every day by cronie so, thanks to `chezmoi.toml` config file, my dotfiles repo is always synced. 
1. give the execute permissions for this script
`$ chmod +x ~/.local/bin/dots-sync`
2. edit the existing user crontab 
`$ crontab -e`
3. append the cron expression
`0 3 * * * /home/<username>/.local/bin/dots-sync`
> This schedules the script to run every day, at 3:00 AM (I go to sleep very late usually).

# Credits
Thanks to @ralgozino for the beautiful `POWERSHELL9K` theme for zsh.