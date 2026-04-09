from psychopy import visual, core, clock, event,data
import random
import pandas as pd

win =  visual.Window([1536, 864], fullscr=True)
# Surprise Recognition Task
memfileName = f"data/practice_Mem"
memExp = data.ExperimentHandler(name = 'Memory Task', version = '1.0', dataFileName = memfileName) 

stimList = pd.read_csv('mem_CB2.csv')

practiceList = pd.read_csv('mem_practice.csv')

idx_row = 0
pr_idx_row = 0

text_new = visual.TextStim(win, text = 'sure new   maybe new   guess new', pos = (-0.5, -0.4), height = (0.08), units = 'norm', color = 'white')
text_old = visual.TextStim(win, text = 'guess old   maybe old   sure old', pos = (0.5, -0.4), height = (0.08), units = 'norm', color = 'white')
numbers_new = visual.TextStim(win, text = '1           2           3', pos = (-0.5, -0.5), height = (0.1), units = 'norm', color = 'white')
numbers_old = visual.TextStim(win, text = '4           5           6', pos = (0.5, -0.5), height = (0.1), units = 'norm', color = 'white')
keys_new = visual.TextStim(win, text = 'a          s           d', pos = (-0.5, -0.7), height = (0.1), units = 'norm', color = 'white')
keys_old = visual.TextStim(win, text = 'j           k           l', pos = (0.5, -0.7), height = (0.1), units = 'norm', color = 'white')

screenText1 = visual.TextStim(win, text = 'New', pos = (-0.4, -0.4), units = "norm", color = 'white') 
response_new = visual.TextStim(win, text = 'f', pos = (-0.4, -0.5), units = "norm", color = 'white')
screenText2 = visual.TextStim (win, text = 'Old', pos = (0.4, -0.4), units = "norm", color = 'white')
response_old = visual.TextStim(win, text = 'd', pos = (0.4, -0.5), units = "norm", color = 'white')

fixCross = visual.TextStim(win, text = '+', color = 'white')

thank_you = visual.TextStim(win, text = 'Thank You!', pos = (0.0,0.0), units = 'norm', color = 'white')


def StimRandom (stimList, idx_row): 
     global stimType 
     global stim
     img_row = stimList.iloc[idx_row]
     img = stimList.iloc[idx_row, 3]
     stimType = stimList.iloc[idx_row, 5]
     stim = visual.ImageStim(win, pos = [0,0.1], size = [0.5,0.5], units = 'height')
     stim.setImage(img)
     memExp.addData('stim', img) 
     memExp.addData('stimType', stimType) 

def mem_resp (trialDuration = 2.0): 
    start_time = core.getTime() 

    keys = event.waitKeys(maxWait = trialDuration, keyList=['f', 'h', 'escape'], timeStamped=True) 

    key = None 
    rt = None
    corr = 0

    if keys: 
        key, press_time = keys[0] 
        rt = press_time - start_time
        resp = key 

        if key == 'escape':
            core.quit()
    
        if resp == 'f' and stimType == 'new': 
            corr = 1 
        elif resp == 'h' and stimType == 'old':
            corr = 1 
        else:
            corr = 0 

        memExp.addData('keyPress', key) 
        memExp.addData('rt', rt) 
        memExp.addData('corr', corr)
        return key, rt    


def confidenceRating():
    keys = event.waitKeys(keyList=['a', 's', 'd', 'j', 'k', 'l'], timeStamped = True) 

    start_time = core.getTime() 

    key = None
    if keys:
        key, press_time = keys[0]
        rt = start_time - press_time
        if key == 'a':
            resp = 'a'
        elif key == 's':
            resp = 's'
        elif key == 'd':
            resp = 'd'
        elif key == 'j':
            resp = 'j'
        elif key == 'k':
            resp = 'k'
        elif key == 'l':
            resp = 'l'
        else:
            resp = '999'
    memExp.addData('Confidence', resp)
    memExp.addData('RTs', rt)
    return None 
             


mem_instructions = visual.TextStim(win, text = ''' Surprise Recognition Task:
You will now judge if you've seen the objects before.  

If the object is one you saw in the memory task, it is OLD and press H
If the object is new to you, it's NEW and press F

You will then be prompted to rate how sure you are. 
The left side of the screen represents the new objects and how sure you are that they are new. 
The right side of the screen represents the old objects and how sure you are that they are old. 
    
Press 'space' to begin the task''', pos = [0,0], height = (0.06))
mem_instructions.draw()
win.flip()
event.waitKeys(keyList = 'space')
win.flip()
for i in range(440):
    if i >= len(stimList):
        break
    StimRandom(stimList, idx_row)
    stim.draw()
    screenText1.draw()
    response_new.draw()
    screenText2.draw()
    response_old.draw()
    win.flip()
    mem_resp()
    stim.draw()
    text_new.draw()
    text_old.draw()
    numbers_new.draw()
    numbers_old.draw()
    idx_row += 1
    win.flip()
    confidenceRating()
    fixCross.draw()
    win.flip()
    jittered = random.randrange(350, 750)
    jittered_ITI = jittered/1000
    memExp.addData('ITI', jittered_ITI)
    core.wait(jittered_ITI)
    memExp.nextEntry()
thank_you.draw()
win.flip()
event.waitKeys(keyList = 'space')

