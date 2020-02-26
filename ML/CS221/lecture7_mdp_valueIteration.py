# 도전시 +4원, 포기 시 +6
class MDP:
    #state : in, out
    def isEnd(self,state):
        return state == 'end'
    def actions(self):
        return ['bet','notBet']
    def succProbReward(self, state, action):
        # return (new state, prob, reward)
        #        (self.state, prob, money)
        result = []
        if state =='in':
            if action == 'bet':
                #실패
                result.append(('end',1/2,4))
                #성공
                result.append(('in',1/2,4))
            else:
                result.append(('end',1,6))
        else :
            result.append(('end',1,0))
        return result
    def discount(self):
        return 1
    def states(self):
        return ['in','end']

def valueIteration(mdp):
    V = {}
    for s in mdp.states():
        V[s] = 0
    def Q(state,action):
        return sum(prob*(reward+mdp.discount()*V[newState]) \
            for newState, prob, reward in mdp.succProbReward(state,action))
    while 1:
        newV = {}
        for state in mdp.states():
            if mdp.isEnd(state):
                newV[state] = 0
            else:
                newV[state] = max(Q(state, action) for action in mdp.actions())
        if max(abs(V[state]-newV[state]) for state in mdp.states()) < 0.001:
            break
        V = newV
        print(V)

mdp = MDP()
valueIteration(mdp)
