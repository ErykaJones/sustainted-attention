from psychopy import visual, core, clock, event,data
import random
import pandas as pd

win =  visual.Window([1536, 864], fullscr=False)
# Surprise Recognition Task
memfileName = f"data/practice_Mem"
memExp = data.ExperimentHandler(name = 'Memory Task', version = '1.0', dataFileName = memfileName) 

stimList = pd.read_csv('mem_CB1.csv')

practiceList = pd.read_csv('mem_practice.csv')

idx_row = 0
pr_idx_row = 0


def StimRandom (stimList, idx_row): 
     global stimType 
     img_row = stimList.iloc[idx_row]
     img = stimList.iloc[idx_row, 3]
     stimType = stimList.iloc[idx_row, 5]
     stim = visual.ImageStim(win, pos = [0,0])
     stim.setImage(img)
     stim.draw()
     memExp.addData('stim', img) 
     memExp.addData('stimType', stimType) 


def mem_resp (trialDuration = 1.5, rt = None, resp = None,): 
    start_time = core.getTime() 

    keys = event.waitKeys(maxWait = 1.5, keyList=['j', 'l'], timeStamped=True) 

    key = None 
    rt = None
    corr = 0 
    if keys: 
        key, press_time = keys[0] 
        rt = press_time - start_time 
            
        if key == 'j': 
            resp = 'j'
        elif key == 'l': 
            resp = 'l'
            
        if resp == 'j' and stimType == 'New': 
            corr = 1 
        elif resp == 'l' and stimType == 'Old':
            corr = 1 
        else:
            corr = 0 
        memExp.addData('keyPress', key) 
        memExp.addData('rt', rt) 
        memExp.addData('corr', corr)
        return key, rt 
        
        return None, None 

for i in range(1):
    mem_instructions = visual.TextStim(win, text = ''' Surprise Recognition Task:
    You will now be shown another series of objects presented to you in the middle of the screen. Your job is to identify whether or not you recognize the object from the attention task you just completed.
    
    If the object is one you saw in the memory task, it is OLD and press 'j'
    If the object is new to you, it's NEW and press 'l'
    
    Try to respond as fast as possible. 
    Press 'space' to begin the task''', pos = [0,0])
    mem_instructions.draw()
    win.flip()
    event.waitKeys(keyList = 'space')
    win.flip()
    for i in range(len(practiceList)):
        StimRandom(practiceList, pr_idx_row)
        screenText1 = visual.TextStim(win, text = 'New', pos = (-0.4, -0.4), units = "norm", color = 'white') 
        screenText2 = visual.TextStim (win, text = 'Old', pos = (0.4, -0.4), units = "norm", color = 'white')
        screenText1.draw()
        screenText2.draw()
        win.flip()
        fixCross = visual.TextStim(win, text = '+', color = 'white')
        fixCross.draw()
        core.wait(1.5)
        mem_resp()
        pr_idx_row += 1 
        win.flip()
        jittered = random.randrange(350, 750)
        jittered_ITI = jittered/1000
        memExp.addData('ITI', jittered_ITI)
        core.wait(jittered_ITI)
    mem_instructions = visual.TextStim(win, text = ''' Surprise Recognition Task:
    You will now be shown another series of objects presented to you in the middle of the screen. Your job is to identify whether or not you recognize the object from the attention task you just completed.
    
    If the object is one you saw in the memory task, it is OLD and press 'j'
    If the object is new to you, it's NEW and press 'l'
    
    Try to respond as fast as possible. 
    Press 'space' to begin the task''', pos = [0,0])
    mem_instructions.draw()
    win.flip()
    event.waitKeys(keyList = 'space')
    win.flip()
    for i in range(len(stimList)):
        StimRandom(stimList, idx_row)
        screenText1 = visual.TextStim(win, text = 'New', pos = (-0.4, -0.4), units = "norm", color = 'white') 
        screenText2 = visual.TextStim (win, text = 'Old', pos = (0.4, -0.4), units = "norm", color = 'white')
        screenText1.draw()
        screenText2.draw()
        win.flip()
        core.wait(2.0)
        fixCross = visual.TextStim(win, text = '+', color = 'white')
        fixCross.draw()
        mem_resp()
        idx_row += 1
        win.flip()
        jittered = random.randrange(350, 750)
        jittered_ITI = jittered/1000
        memExp.addData('ITI', jittered_ITI)
        core.wait(jittered_ITI)
        memExp.nextEntry()
    

