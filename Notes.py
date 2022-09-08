import math

class Notes:
    TONE = 440
    NOTES = []
    MAJOR = [2,3,3,3,5,5,5,6,6,6]

    def __init__(self,scale):
        self.TONE = self.TONE * 3**(scale/6)
        for x in range(2,6):
            self.NOTES.append(self.TONE * 3**(x/6))

    def getScale(self):
        SCALE = []
        for num in self.MAJOR:
            SCALE.append(self.NOTES[num%4])
        return SCALE

    def normalize(self,note):
        if int(note) == 0:
            return note
        if note < self.TONE:
            return self.normalize(note*2)
        elif note > 2*self.TONE:
            return self.normalize(note/2)
        else:
            return note

    def getStep(self,fold,fnew):
        if int(fold) == 0:
            return fold
        return 6*math.log(fnew/fold,2)
