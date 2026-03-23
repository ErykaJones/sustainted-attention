from psychopy import visual, core, clock, event,data
import random
import pandas as pd

win =  visual.Window([1536, 864], fullscr=False)

fileName = f"data/practice_Attn" 
thisExp = data.ExperimentHandler(name= 'Sustained Attention', version = '1.0', dataFileName = fileName)

idx_row = 0

#SetUpInfo = {} 
#SetUpInfo['Participant Number'] = ''  
#SetUpInfo['Counterbalance'] = ''
#dlg = gui.DlgFromDict(SetUpInfo) 
#if not dlg.OK: 
    #core.quit()


stimList = pd.read_csv('attn_CB1.csv')

practiceList = pd.read_csv('attn_practice.csv')

idx_row = 0
pr_idx_row = 0

def StimRandom (stimList, idx_row): 
     global stimType 
     img_row = stimList.iloc[idx_row]
     img = stimList.iloc[idx_row, 3]
     stimType = stimList.iloc[idx_row, 2]
     stim = visual.ImageStim(win, pos = [0,0])
     stim.setImage(img)
     stim.draw()
     thisExp.addData('stim', img) 
     thisExp.addData('stimType', stimType) 

def get_responseAttn (trialDuration = 1.5, rt = None, resp = None): 
    start_time = core.getTime() 

    keys = event.getKeys(keyList=['j', 'l'], timeStamped=True)
        
    key = None 
    rt = None
    corr = 0 
    if keys: 
        key, press_time = keys[0]
        rt = start_time - press_time
            
        if key == 'j': 
            resp = 'j'
        elif key == 'l': 
            resp = 'l'
            
        if resp == 'j' and stimType == 'living': 
            corr = 1 
        elif resp == 'l' and stimType == 'nonliving':
            corr = 1 
        else:
            corr = 0 
        thisExp.addData('keyPress', resp) 
        thisExp.addData('rt', rt) 
        thisExp.addData('corr', corr) 
        return key, rt 
        
        return None, None


for i in range(1):
    attn_instructions = visual.TextStim(win, text = '''Sustained Attention Task:
    Practice Trials
    You will see a series of objects presented to you in the middle of the screen. Your job is to identify whether that object is living or nonliving
    
    If the object is LIVING, press j 
    If the object is NONLIVING, press l 
    
    Pay attention and try to respond as fast as you can.
    Press 'space' to begin the task''', pos = [0,0])
    attn_instructions.draw()
    win.flip()
    event.waitKeys(keyList = 'space')
    win.flip()
    for i in range(len(practiceList)):
        StimRandom(practiceList, pr_idx_row)
        screenText1 = visual.TextStim(win, text = 'Living', pos = (-0.4, -0.4), units = "norm", color = 'white') 
        screenText2 = visual.TextStim (win, text = 'Nonliving', pos = (0.4, -0.4), units = "norm", color = 'white')
        screenText1.draw()
        screenText2.draw()
        win.flip()
        fixCross = visual.TextStim(win, text = '+', color = 'white')
        fixCross.draw()
        core.wait(1.5)
        get_responseAttn()
        pr_idx_row += 1 
        win.flip()
        jittered = random.randrange(350, 750)
        jittered_ITI = jittered/1000
        thisExp.addData('ITI', jittered_ITI)
        core.wait(jittered_ITI)
    attn_instructions = visual.TextStim(win, text = '''Sustained Attention Task:
    Test Trials
    You will see a series of objects presented to you in the middle of the screen. Your job is to identify whether that object is living or nonliving
    
    If the object is LIVING, press j 
    If the object is NONLIVING, press l 
    
    Pay attention and try to respond as fast as you can.
    Press 'space' to begin the task''', pos = [0,0])
    attn_instructions.draw()
    win.flip()
    event.waitKeys(keyList = 'space')
    win.flip()
    for i in range(len(stimList)):
        StimRandom(stimList, idx_row)
        screenText1 = visual.TextStim(win, text = 'Living', pos = (-0.4, -0.4), units = "norm", color = 'white') 
        screenText2 = visual.TextStim (win, text = 'Nonliving', pos = (0.4, -0.4), units = "norm", color = 'white')
        screenText1.draw()
        screenText2.draw()
        win.flip()
        core.wait(1.5)
        fixCross = visual.TextStim(win, text = '+', color = 'white')
        fixCross.draw()
        get_responseAttn()
        idx_row += 1
        win.flip()
        jittered = random.randrange(350, 750)
        jittered_ITI = jittered/1000
        thisExp.addData('ITI', jittered_ITI)
        core.wait(jittered_ITI)
        thisExp.nextEntry()

    thank_you = visual.TextStim(win, text = 'Thank you!', pos = [0,0], color = 'white')
    thank_you.draw()
    win.flip()
    core.waitKeys(keyList = ['space'])