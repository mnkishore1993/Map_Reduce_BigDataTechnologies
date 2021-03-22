from mrjob.job import MRJob

class MRSalaries(MRJob):

    def mapper(self, _, line):
        (name,jobTitle,agencyID,agency,hireDate,annualSalary,grossPay) = line.split('\t')
        annualSalary = float(annualSalary)      
        
         #Intensionally not keeping lower boundary for the condition
        #Since lower boundary would not pass the first condition
        #having lower bound condition will be a repeat
        
        if(annualSalary<float(49999.99)):        
         yield 'Low', 1         
       
        elif(annualSalary <float(99999.99)):
         yield 'Medium', 1
        else: 
         yield 'High',1

    def combiner(self, jobTitle, counts):
        yield jobTitle, sum(counts)

    def reducer(self, jobTitle, counts):
        yield jobTitle, sum(counts)


if __name__ == '__main__':
    MRSalaries.run()


