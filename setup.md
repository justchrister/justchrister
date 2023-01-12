# Mac config

```
# make dock smaller
defaults write com.apple.dock tilesize -int 32; killall Dock

# lock the dock
defaults write com.apple.dock size-immutable -bool yes && killall Dock
```
