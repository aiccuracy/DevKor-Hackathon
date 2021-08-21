
class WebConnect:

    def getWinner(winner, csvList):
        for line in csvList:
            if line[1] == winner:
                return line[0]
                
    def sendRecommend(df, recList):
        output = []
        for rec in recList:
            row = df.loc[df['foodName'] == rec].values.tolist()[0]
            name = row[0]
            imgUrl = row[6]
            output.append([name, imgUrl])
        return output