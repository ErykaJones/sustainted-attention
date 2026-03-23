
# Surprise Recognition Task
memfileName = f"data/{SetUpInfo['Participant Number']}_Mem" #create a file name for this specific task and using the participant number collected at the beginning of the experiment
memExp = data.ExperimentHandler(name = 'Memory Task', version = '1.0', extraInfo = SetUpInfo, dataFileName = memfileName) #Open a seperate csv for the memory task
    
def mem_resp (trialDuration = 1.5, rt = None, resp = None,): #create a function to track response, it will look at both the key pressed AND whether or not that was the correct response 
    start_time = core.getTime() #start by getting the time 

    keys = event.waitKeys(maxWait = 1.5, keyList=['j', 'l'], timeStamped=True) #create a list of keys, waitKeys means that it will wait for the key to be pressed then move on but it  also has a max wait which is what our max trial duration will be (1.5 seconds)
        
    key = None #start with no keys pressed
    rt = None #no reaction
    corr = 0 #nothing correct
    if keys: #if a key is pressed
        key, press_time = keys[0] #keys is returned as a tuple of key pressed and the time it was pressed, so here I am assigning key pressed to the variable key and time that the key was pressed to the variable press time
        rt = press_time - start_time #reaction time made up of the time that a key was pressed subtracted from the start time 
            
        if key == 'j': #if the letter 'j' was pressed then the response is j 
            resp = 'j'
        elif key == 'l': #if the letter 'l' was pressed then response is l
            resp = 'l'
            
        if resp == 'j' and stimType == 'New': #this is the loop to track correct responses
            corr = 1 #correct living respone is when the response is j and the stimType is new 
        elif resp == 'l' and stimType == 'Old':
            corr = 1 #correct nonliving response is when the resp is l and the stimType is old
        else:
            corr = 0 #if you press the wrong key in response to the wrong stimType, you get a 0
        memExp.addData('keyPress', key) #add key pressed to csv to make sure I'm tracking that a key has been pressed
        memExp.addData('rt', rt) #add reaction time
        memExp.addData('corr', corr) #add correct response 
        return key, rt #return the values for key pressed and reaction time 
        
        return None, None # if a key is not pressed, return none for key pressed and reaction time 



#Start of memory experiment
PracticeTrials(PracticeMem, memInstructions, NewText, OldText) #call the practice trials, input memory specific practice dataframe, memory task instructions, and the screen text to held constant on screen as arguments 
drawInstructions(memInstructions) #draw instructions for the test trials (using memory specific instructions)
for i in range(21): #trial loop, again all stimuli will be shown to the participant. It's 21 here for the sake of it being easy to code for this assignment/to mark
    currentType = StimRandom(NewStim, OldStim, NewText, OldText) #get the current type of stimulus (old versus new)
    ScreenText(NewText, OldText) #draw the old versus new prompt on the screen
    win.flip() #display to the participant
    mem_resp(currentType)#wait for response, max wait will be 1.5 seconds
    memExp.nextEntry() #move to the next row for the next trial 
    win.flip() #remove the stimuli from screen
    fixation() #draw the fixation cross 
    win.flip() #flip the screen, remove the fixation cross from the screen
    core.wait(0.5) #wait 500ms between each stimulus presentation
    
#The psychopy experiment was based on this paper = https://doi.org/10.1177/0956797623120676  
    

