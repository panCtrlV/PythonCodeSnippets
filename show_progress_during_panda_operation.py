"""
NOT a executable python script. But it shows how to show
progress while applying some function on a Pandas dataframe
(especially helpful when the dataframe is large).

@time: 2017-05-27
"""

fig, ax = plt.subplots( figsize=(10,20) )
m = Basemap(resolution='c',  # c, l, i, h, f or None
            projection='merc',
            lat_0=ctr_lat, lon_0=ctr_lon,  # center
            llcrnrlat=min_lat, llcrnrlon=min_lon,  # lower left cornor
            urcrnrlat=max_lat, urcrnrlon=max_lon)  # upper right cornor

m.drawmapboundary(fill_color='#46bcec')
m.fillcontinents(color='#f2f2f2',lake_color='#46bcec')
m.drawcoastlines()
m.readshapefile('../data/CA_counties/CA_counties', 'areas')

def logged_apply(g, func, *args, **kwargs):
    """
    A reusable fundtion to show progress while apply a function on pandas dataframe.
    Ref: https://stackoverflow.com/questions/18603270/progress-indicator-during-pandas-operations-python
    """
    step_percentage = 100. / len(g)
    import sys
    sys.stdout.write('apply progress:   0%')
    sys.stdout.flush()

    def logging_decorator(func):
        def wrapper(*args, **kwargs):
            progress = wrapper.count * step_percentage
            sys.stdout.write('\033[D \033[D' * 4 + format(progress, '3.0f') + '%')
            sys.stdout.flush()
            # The following two lines are needed in order to enable the progress
            # to update in-place.
            # Ref: https://stackoverflow.com/questions/465348/how-can-i-print-over-the-current-line-in-a-command-line-application
            sys.stdout.write('\r')
            sys.stdout.flush()
            wrapper.count += 1
            return func(*args, **kwargs)
        wrapper.count = 0
        return wrapper

    logged_func = logging_decorator(func)
    res = g.apply(logged_func, *args, **kwargs)
    sys.stdout.write('\033[D \033[D' * 4 + format(100., '3.0f') + '%' + '\n')
    sys.stdout.flush()
    return res

def plotDataOnMap(pos):
    #logerr = train_df[train_df.pos == pos]['logerror']
    #print logerr.values
    x, y = m(pos[0], pos[1])
    #size = np.abs(logerr)*100
    m.plot(x, y, 'o', markersize=1, color='#444444', alpha=0.8)
    
# Plot data points on map
# train_df.pos[:30000].apply(plotDataOnMap)
logged_apply(train_df.pos, plotDataOnMap)