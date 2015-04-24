import initializer as I
import tables as T
import learning as L

global maxGames
MaximumGames = 30000

#-----------------------------------------------------------------------------
"""
Plays games to learn q values and returns qTable
"""

def gameLearning(maxGames):
    state = I.new_game()
    print state
    games = 0
    table = T.qTable
  
    while (games < maxGames):
        print state[0][0]
        print state[0][1]
        print state[0][2]
        print "----------"
        stateKey = T.makeKey(state)
        if stateKey not in table.keys():
            table = T.addKey(stateKey,table)
        action = L.chooseMove(state,table)
        nextState = I.next_state(state,action)
        nextKey = T.makeKey(nextState)
        reward = L.reinforcement(nextState)
        if nextKey not in table.keys():
            table = T.addKey(nextKey,table)
        if (I.eval(nextState) == 'continue'):
            table = L.updateQvalue(state, action, nextState, reward, table)
            state = nextState
        else:
            print nextState[0][0]
            print nextState[0][1]
            print nextState[0][2]
            print "----------"
            print "NEW GAME:"
            state = I.new_game()
            games += 1
       
    return table
    
gameLearning(1000)
  
