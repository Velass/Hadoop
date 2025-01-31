import sys

current_year = None
current_playlist = 0

for line in sys.stdin:
    year, playlist = line.split("\t")
    
    try:
        year = int(year)
        playlist = int(playlist)
    except:
        continue
    
    if current_year == year:
        current_playlist += playlist
    else:
        if current_year:
            print("%s\t%s\t%i" % (current_year, current_playlist, current_playlist/current_year))
        current_year = year
        current_playlist = playlist

if current_year:    
    print("%s\t%s\t%s" % (current_year, current_playlist, current_playlist/current_year))