from mrjob.job import MRJob

class MRSalaries(MRJob):

    def mapper(self, _, line):
        (UserID,MovieID,Rating,TimeStamp) = line.split(',')
        yield UserID,1

    def combiner(self, UserID, counts):
        yield UserID, sum(counts)

    def reducer(self, UserID, counts):
        yield UserID, sum(counts)


if __name__ == '__main__':
    MRSalaries.run()


