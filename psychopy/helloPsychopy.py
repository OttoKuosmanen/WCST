from psychopy import visual, core  # import some libraries from PsychoPy

# create a window
mywin = visual.Window([800,600], monitor="testMonitor", units="deg")

# create some stimuli
message = visual.TextStim(win=mywin, text="Hello, World!", height=2, color=[1,-1,-1])

# draw the stimuli and update the window
message.draw()
mywin.flip()

# pause, so you get a chance to see it!
core.wait(5.0)

# close the window
mywin.close()

# clean up at the end of the experiment.
core.quit()
