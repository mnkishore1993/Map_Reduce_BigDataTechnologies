# Map_Reduce_BigDataTechnologies
 
Connect to AWS:

	ssh hadoop@ec2-34-200-226-56.compute-1.amazonaws.com -i C:/BigDataTechnologies/emr-key-pair.pem

Install Package:

	b)	Enter 	“sudo su”
	c)	Enter	“pip install mrjob[aws]”
	d)	Enter 	“exit”

Upload .config file to Hadoop

	scp -i C:/BigDataTechnologies/emr-key-pair.pem C:/BigDataTechnologies/.mrjob.conf hadoop@ec2-34-200-226-56.compute-1.amazonaws.com:/home/hadoop
	
	instructions:
		Update the file path and hadooop DNS path accordingly
	
Upload Code files to Hadoop
	
	scp -i C:/BigDataTechnologies/emr-key-pair.pem C:/BigDataTechnologies/w.data hadoop@ec2-34-200-226-56.compute-1.amazonaws.com:/home/hadoop
	scp -i C:/BigDataTechnologies/emr-key-pair.pem C:/BigDataTechnologies/WordCount.py hadoop@ec2-34-200-226-56.compute-1.amazonaws.com:/home/hadoop

Move Data File from Local Folder to user/Hadoop Folder
	
	hadoop fs -copyFromLocal w.data /user/hadoop

Execute Python file


	python WordCount.py -r hadoop hdfs:///user/hadoop/w.data
	
	-->Above command deletes the output files after execution. Use below command to not delete the output files
	
	python WordCount.py -r hadoop hdfs:///user/hadoop/w.data- -output-dir /user/hadoop/some-non-existent-directory
	
Upload salaries Data to Hadoop

	scp -i C:/BigDataTechnologies/emr-key-pair.pem C:/BigDataTechnologies/Salaries.tsv hadoop@ec2-34-200-226-56.compute-1.amazonaws.com:/home/hadoop
	scp -i C:/BigDataTechnologies/emr-key-pair.pem C:/BigDataTechnologies/Salaries.py hadoop@ec2-34-200-226-56.compute-1.amazonaws.com:/home/hadoop

Move to Hadoop Folder

	hadoop fs -copyFromLocal Salaries.tsv /user/hadoop
	hadoop fs -copyFromLocal Salaries.py /user/hadoop
	
MovieReview Example :

	Upload Files Code and dataSet
	
		scp -i C:/BigDataTechnologies/emr-key-pair.pem C:/BigDataTechnologies/MovieReview.py hadoop@ec2-34-200-226-56.compute-1.amazonaws.com:/home/hadoop
		scp -i C:/BigDataTechnologies/emr-key-pair.pem C:/BigDataTechnologies/u.data hadoop@ec2-34-200-226-56.compute-1.amazonaws.com:/home/hadoop
		
	Move Data File to Hadoop Folder
		
		hadoop fs -copyFromLocal u.data /user/hadoop
