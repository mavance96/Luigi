from GitCaller import GitCaller
from ProjectCaller import ProjectCaller
from QueueCaller import QueueCaller

queue = QueueCaller()

#print("QUEUE LIST CALL")
#print(queue.get_listOfQueues("SE4330-Mario") + '\n')

git = GitCaller()

print("REPO CALL")
print(git.get_listOfRepos("SE4330-Mario") + '\n')

print("GIT BRANCH LIST CALL")
print(git.get_listOfBranches("SE4330-Mario", "SE4330-Mario") + '\n')

project = ProjectCaller()

print("PROJECT LIST CALL")
print(project.get_listOfProjects() + '\n')