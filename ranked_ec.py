
candidates = []
#how to search thru list of objects for an object with an attribute equal to some value
#next((x for x in test_list if x.value == value), None)
#https://stackoverflow.com/questions/7125467/find-object-in-list-that-has-attribute-equal-to-some-value-that-meets-any-condi 


class Candidate:
    candidateName = ""
    percentVote = 0
    secondChoice = ""
    thirdChoice = ""

    def __init__(self, name, percent):
        self.candidateName = name
        self.percentVote = percent

    def setCandidate(self, name):
        self.candidateName = name

    def getCandidate(self):
        return self.candidateName

    def setVotes(self, vote):
        self.percentVote = vote

    def getVotes(self):
        return self.percentVote
    
    def set2ndChoice(self, name):
        self.secondChoice = name

    def get2ndChoice(self):
        return self.secondChoice
    
    def set3rdChoice(self, name):
        self.thirdChoice = name
    
    def get3rdChoice(self):
        return self.thirdChoice

def runRankedElection():

    won = False
    losingCandidate = ""
    winningCandidate = ""
    winningCandidateName = ""

    while won == False:
        minVote = 100

        for candidate in candidates:
            if candidate.getVotes() < minVote:
                losingCandidate = candidate
                minVote = candidate.getVotes()
        
        if losingCandidate.get2ndChoice():
            nextCandidate = getCandidate(losingCandidate.get2ndChoice())
            nextCandidate.setVotes(nextCandidate.getVotes() + losingCandidate.getVotes())
        else if losingCandidate.get3rdChoice():
            nextCandidate = getCandidate(losingCandidate.get3rdChoice())
            nextCandidate.setVotes(nextCandidate.getVotes() + losingCandidate.getVotes())

        candidates.remove(losingCandidate)

        for candidate in candidates:
            if candidate.getVotes() >= 50:
                won = True
                winningCandidate = candidate
                break

    return [winningCandidate.candidateName, winningCandidate, winningCandidate.getVotes()]
    #pass

def runECElection():
    #How AZ Electoral College Elections work:
    #https://www.azcleanelections.gov/how-government-works/electoral-college#:~:text=Arizona%20has%20a%20winner%20take,both%20president%20and%20vice%2Dpresident.
    #Summary: Winner-take-all. Whoever receives the highest number of votes receives all 11 electoral votes.
    maxVote = 0
    maxCandidate = "" #a candidate object
    maxName = ""

    for candidate in candidates:
        if candidate.percentVote > maxVote:
            maxVote = candidate.percentVote
            maxName = candidate.candidateName
            maxCandidate = candidate
    
    return [maxName, maxVote, maxCandidate]




